#!/usr/bin/env python3
"""
Backfill historical point-in-time sector_score anchors.

For every selected (sector, date) pair, run build_fy_norm.py --current --as-of
strictly sequentially with Nasdaq historical prices. By default, auto refresh
uses prices only between reporting seasons, refreshes only companies with new
SEC filings, and performs four full audits per year. Completed snapshots are
skipped when their P/E summary has a normal company count.

After collection, rebuild the canonical 17-sector x 10-date dashboard preview
from dated current summaries and the existing five-year norm summaries.
Missing and partially populated points are recorded honestly.

Usage:
    python3 scripts/backfill_history.py
    python3 scripts/backfill_history.py --only banks --dates 2026-05-10
    python3 scripts/backfill_history.py --rebuild-preview-only
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

if __package__:
    from scripts.compute_sector_scores import (
        DASHBOARD_PREVIEW_FIELDNAMES,
        SECTOR_WEIGHTS,
        YIELD_METRICS,
    )
    from scripts.update_all import SECTORS
else:
    from compute_sector_scores import (
        DASHBOARD_PREVIEW_FIELDNAMES,
        SECTOR_WEIGHTS,
        YIELD_METRICS,
    )
    from update_all import SECTORS

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
DATA = REPO_ROOT / "data" / "market_quotes"
DEFAULT_PREVIEW = DATA / "sector_scores_preview_monthly.csv"

DEFAULT_DATES = [
    "2025-09-10",
    "2025-10-10",
    "2025-11-10",
    "2025-12-10",
    "2026-01-10",
    "2026-02-10",
    "2026-03-10",
    "2026-04-10",
    "2026-05-10",
    "2026-06-10",
]


def parse_iso_date(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"invalid date {value!r}; expected YYYY-MM-DD"
        ) from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sequentially backfill historical sector_score anchors."
    )
    parser.add_argument(
        "--dates",
        nargs="+",
        type=parse_iso_date,
        default=[dt.date.fromisoformat(value) for value in DEFAULT_DATES],
        metavar="YYYY-MM-DD",
        help="Anchor dates to collect (default: the canonical 10 monthly dates).",
    )
    parser.add_argument(
        "--only",
        nargs="+",
        default=None,
        metavar="SLUG",
        help="Collect only these sector slugs (default: all 17).",
    )
    parser.add_argument(
        "--rebuild-preview-only",
        action="store_true",
        help="Do not use the network; rebuild preview from existing dated snapshots.",
    )
    parser.add_argument(
        "--pause",
        type=float,
        default=2.0,
        help="Seconds to wait between sequential build_fy_norm calls (default: 2).",
    )
    parser.add_argument(
        "--preview-csv",
        type=Path,
        default=DEFAULT_PREVIEW,
        help=f"Preview output path (default: {DEFAULT_PREVIEW.relative_to(REPO_ROOT)}).",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Pass --no-cache to build_fy_norm.py and force SEC companyconcept requests.",
    )
    parser.add_argument(
        "--refresh-mode",
        choices=("auto", "full", "prices-only"),
        default="auto",
        help=(
            "Fundamentals refresh policy passed to build_fy_norm.py "
            "(default: auto)."
        ),
    )
    return parser.parse_args()


def read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def to_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        parsed = float(str(value).strip())
    except ValueError:
        return None
    return parsed if math.isfinite(parsed) else None


def to_int(value: Any) -> int:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return 0


def rows_by_metric(path: Path) -> Dict[str, Dict[str, str]]:
    return {
        row["metric"].strip(): row
        for row in read_csv_rows(path)
        if row.get("metric", "").strip()
    }


def dated_stem(slug: str, anchor: dt.date) -> str:
    return f"fyn_{slug}_current_{anchor:%Y%m%d}"


def dated_paths(slug: str, anchor: dt.date) -> Tuple[Path, Path, Path]:
    stem = dated_stem(slug, anchor)
    return (
        DATA / f"{stem}.csv",
        DATA / f"{stem}_summary.csv",
        DATA / f"{stem}.json",
    )


def norm_summary_path(slug: str) -> Path:
    return DATA / f"fyn_{slug}_norm_summary.csv"


def expected_pe_companies(slug: str, basket_size: int) -> int:
    """Normal P/E coverage, accounting for structural basket exclusions/losses."""
    reference_paths = [
        norm_summary_path(slug),
        DATA / f"fyn_{slug}_current_summary.csv",
    ]
    counts = []
    for path in reference_paths:
        pe_row = rows_by_metric(path).get("pe", {})
        count = to_int(pe_row.get("n_companies"))
        if pe_row.get("status") == "ok" and count > 0:
            counts.append(count)
    return min(counts) if counts else basket_size


def snapshot_quality(
    slug: str,
    anchor: dt.date,
    basket_size: int,
) -> Tuple[bool, str]:
    _detail_path, summary_path, _json_path = dated_paths(slug, anchor)
    if not summary_path.exists():
        return False, f"missing {summary_path.name}"

    pe_row = rows_by_metric(summary_path).get("pe")
    if pe_row is None:
        return False, "missing pe row"
    if pe_row.get("status") != "ok" or to_float(pe_row.get("value")) is None:
        return False, f"pe.status={pe_row.get('status') or 'missing'}"

    actual = to_int(pe_row.get("n_companies"))
    expected = expected_pe_companies(slug, basket_size)
    if actual < expected:
        return False, f"pe.n_companies={actual}, expected at least {expected}"
    return True, f"pe.status=ok, n_companies={actual} (expected {expected})"


def run_snapshot(
    slug: str,
    name: str,
    tickers: Sequence[str],
    anchor: dt.date,
    no_cache: bool,
    refresh_mode: str,
) -> int:
    cmd = [
        sys.executable,
        str(SCRIPTS / "build_fy_norm.py"),
        "--sector",
        name,
        "--tickers",
        *tickers,
        "--slug",
        slug,
        "--current",
        "--as-of",
        anchor.isoformat(),
        "--price-provider",
        "nasdaq",
        "--refresh-mode",
        refresh_mode,
    ]
    if no_cache:
        cmd.append("--no-cache")
    cache_arg = " --no-cache" if no_cache else ""
    print(
        "  $ "
        f"{Path(sys.executable).name} scripts/build_fy_norm.py "
        f"--sector {name!r} --slug {slug} --current "
        f"--as-of {anchor.isoformat()} --price-provider nasdaq "
        f"--refresh-mode {refresh_mode}{cache_arg}"
    )
    return subprocess.run(cmd, cwd=REPO_ROOT).returncode


def load_metadata(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    metadata = data.get("metadata")
    return metadata if isinstance(metadata, dict) else {}


def actual_trading_dates(detail_path: Path) -> List[str]:
    dates = {
        row.get("close_date", "").strip()
        for row in read_csv_rows(detail_path)
        if row.get("symbol") != "BASKET_AVG" and row.get("close_date", "").strip()
    }
    return sorted(dates)


def metric_value(row: Optional[Dict[str, str]], field: str) -> Optional[float]:
    if not row or row.get("status") != "ok":
        return None
    value = to_float(row.get(field))
    if value is None or value <= 0:
        return None
    return value


def missing_preview_row(
    anchor: dt.date,
    sector: str,
    source: str,
    reason: str,
) -> Dict[str, Any]:
    return {
        "date": anchor.isoformat(),
        "sector": sector,
        "coefficient": "",
        "metric": "sector_score",
        "metric_coefficient": "",
        "metric_weight": "",
        "source": source,
        "comment": f"status=missing; {reason}",
    }


def build_preview_point(
    slug: str,
    sector: str,
    tickers: Sequence[str],
    anchor: dt.date,
) -> Dict[str, Any]:
    detail_path, current_path, json_path = dated_paths(slug, anchor)
    norm_path = norm_summary_path(slug)
    metadata = load_metadata(json_path)
    refresh_mode = metadata.get("refresh_mode") or (
        "prices-only" if "price-only" in str(metadata.get("method") or "") else "legacy-full"
    )
    source = (
        f"build_fy_norm.py --current --as-of; refresh_mode={refresh_mode}; "
        f"{current_path.name}; {norm_path.name}"
    )

    if not current_path.exists():
        return missing_preview_row(
            anchor, sector, source, f"snapshot file not found: {current_path.name}"
        )
    if not norm_path.exists():
        return missing_preview_row(
            anchor, sector, source, f"norm file not found: {norm_path.name}"
        )

    current_rows = rows_by_metric(current_path)
    norm_rows = rows_by_metric(norm_path)
    weights = SECTOR_WEIGHTS[sector]
    available: Dict[str, Tuple[float, float, float]] = {}
    missing_metrics: List[str] = []

    for metric, raw_weight in weights.items():
        current = metric_value(current_rows.get(metric), "value")
        norm = metric_value(norm_rows.get(metric), "five_year_average")
        if current is None or norm is None:
            missing_metrics.append(metric)
            continue
        available[metric] = (current, norm, raw_weight)

    if not available:
        return missing_preview_row(
            anchor,
            sector,
            source,
            "no weighted metric has both an ok current value and an ok 5Y norm",
        )

    weight_sum = sum(raw_weight for _current, _norm, raw_weight in available.values())
    score = 0.0
    components: List[str] = []
    for metric, (current, norm, raw_weight) in available.items():
        weight = raw_weight / weight_sum
        coefficient = norm / current if metric in YIELD_METRICS else current / norm
        score += coefficient * weight
        components.append(f"{metric}: {coefficient:.4f} x {weight * 100:.1f}%")

    quality_ok, quality_comment = snapshot_quality(slug, anchor, len(tickers))
    status = "ok" if not missing_metrics and quality_ok else "provisional"
    price_source = metadata.get("price_source")
    if price_source:
        if isinstance(price_source, list):
            price_source = ", ".join(str(item) for item in price_source)
        source += f"; price source: {price_source}"

    comments = [
        f"status={status}",
        f"refresh_mode={refresh_mode}",
        f"actual_trading_date={','.join(actual_trading_dates(detail_path)) or 'missing'}",
        quality_comment,
    ]
    if missing_metrics:
        comments.append(
            "missing weighted metrics "
            f"{', '.join(missing_metrics)}; remaining weights renormalised"
        )
    comments.append(" | ".join(components))

    return {
        "date": anchor.isoformat(),
        "sector": sector,
        "coefficient": round(score, 4),
        "metric": "sector_score",
        "metric_coefficient": "",
        "metric_weight": "",
        "source": source,
        "comment": "; ".join(comments),
    }


def preview_dates(requested_dates: Iterable[dt.date]) -> List[dt.date]:
    dates = {dt.date.fromisoformat(value) for value in DEFAULT_DATES}
    dates.update(requested_dates)
    for path in DATA.glob("fyn_*_current_????????_summary.csv"):
        date_text = path.name.removesuffix("_summary.csv").rsplit("_", 1)[-1]
        try:
            dates.add(dt.datetime.strptime(date_text, "%Y%m%d").date())
        except ValueError:
            continue
    return sorted(dates)


def rebuild_preview(path: Path, requested_dates: Iterable[dt.date]) -> Tuple[int, int]:
    rows: List[Dict[str, Any]] = []
    for anchor in preview_dates(requested_dates):
        for slug, (sector, tickers) in SECTORS.items():
            rows.append(build_preview_point(slug, sector, tickers, anchor))

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=DASHBOARD_PREVIEW_FIELDNAMES,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    missing = sum(1 for row in rows if row["coefficient"] == "")
    print(f"\nPreview: {path} ({len(rows) - missing} scored, {missing} missing)")
    return len(rows) - missing, missing


def selected_slugs(only: Optional[Sequence[str]]) -> List[str]:
    if not only:
        return list(SECTORS)
    unknown = [slug for slug in only if slug not in SECTORS]
    if unknown:
        raise SystemExit(f"unknown sector slugs: {', '.join(unknown)}")
    return list(dict.fromkeys(only))


def main() -> int:
    args = parse_args()
    slugs = selected_slugs(args.only)
    dates = list(dict.fromkeys(args.dates))
    failures = 0
    collected = 0
    skipped = 0
    pending = 0

    if not args.rebuild_preview_only:
        total = len(slugs) * len(dates)
        print(
            f"Backfill: {len(slugs)} sectors x {len(dates)} dates = {total} pairs "
            "(strictly sequential)"
        )
        pair_index = 0
        for slug in slugs:
            sector, tickers = SECTORS[slug]
            for anchor in dates:
                pair_index += 1
                print(f"\n[{pair_index}/{total}] {sector} / {anchor.isoformat()}")
                if anchor > dt.date.today():
                    pending += 1
                    print(
                        "  pending: anchor is in the future; "
                        "left missing until that date"
                    )
                    continue

                ready, reason = snapshot_quality(slug, anchor, len(tickers))
                if ready:
                    skipped += 1
                    print(f"  skip: {reason}")
                    continue

                print(f"  collect: {reason}")
                started_at = time.perf_counter()
                rc = run_snapshot(
                    slug,
                    sector,
                    tickers,
                    anchor,
                    args.no_cache,
                    args.refresh_mode,
                )
                elapsed = time.perf_counter() - started_at
                ready, reason = snapshot_quality(slug, anchor, len(tickers))
                if rc == 0 and ready:
                    collected += 1
                    print(f"  collected: {reason}; elapsed={elapsed:.1f}s")
                else:
                    failures += 1
                    print(
                        f"  incomplete: returncode={rc}; {reason}; "
                        f"elapsed={elapsed:.1f}s"
                    )

                if pair_index < total and args.pause > 0:
                    time.sleep(args.pause)

        print(
            "\nCollection summary: "
            f"collected={collected}, skipped={skipped}, "
            f"pending={pending}, incomplete={failures}"
        )
    else:
        print("Preview-only mode: no network calls.")

    rebuild_preview(args.preview_csv, dates)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
