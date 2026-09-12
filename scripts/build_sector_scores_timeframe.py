#!/usr/bin/env python3
"""
Build dashboard sector_score preview points on an explicit list of anchor dates.

This reuses the exact scoring method from ``compute_sector_scores.py`` (per-metric
coefficient = current_value / norm, inverted for yield metrics; per-sector
SECTOR_WEIGHTS renormalised over the metrics that actually have data; two-level
median already baked into the summary files) but reads the per-date snapshots
straight from the point-in-time summary files instead of re-rolling raw
fundamentals:

- current value per (sector, date, metric):
  ``fyn_<slug>_current_<YYYYMMDD>_summary.csv`` -> column ``value`` (status=ok)
- 5Y FY norm per (sector, metric):
  ``fyn_<slug>_norm_summary.csv`` -> column ``five_year_average`` (status=ok)

A snapshot that does not exist for a given anchor date is simply skipped, so the
preview is honestly ``missing`` for future / uncollected dates (e.g. the
trailing 2026-06-10 point that has no data yet).

Output schema is byte-for-byte the dashboard preview schema:
``date,sector,coefficient,metric,metric_coefficient,metric_weight,source,comment``
with ``coefficient`` = sector_score and ``metric`` = ``sector_score``.

Used to generate the two dashboard timeframes:
- ``--mode year``  -> 12 monthly 10th-of-month anchors (Oct 2025 .. Sep 2026)
- ``--mode 2year`` -> 12 bi-monthly 10th-of-month anchors (Oct 2024 .. Aug 2026)
  plus the latest monthly anchor (Sep 2026) as a trailing point
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Reuse the canonical scoring config so this script never drifts from the engine.
from compute_sector_scores import (
    DATA_DIR,
    DEFAULT_WEIGHTS,
    SECTOR_WEIGHTS,
    YIELD_METRICS,
    sector_slug,
    to_float,
)

DASHBOARD_PREVIEW_FIELDNAMES = [
    "date", "sector", "coefficient", "metric",
    "metric_coefficient", "metric_weight", "source", "comment",
]

# 12 monthly anchors (rolling: Oct 2025 .. Sep 2026). June 2026 was collected
# on the 20th (no 10th snapshot exists), so that anchor is 2026-06-20.
# Roll this list forward each decade update once the new dated snapshot
# (fyn_<slug>_current_<YYYYMMDD>_summary.csv) has been collected.
YEAR_DATES = [
    "2025-10-10", "2025-11-10", "2025-12-10", "2026-01-10",
    "2026-02-10", "2026-03-10", "2026-04-10", "2026-05-10",
    "2026-06-20", "2026-07-10", "2026-08-10", "2026-09-10",
]

# 12 bi-monthly 10th-of-month anchors (even-month grid, which is the grid the
# 2-year history was collected on) plus the latest monthly anchor as a trailing
# point, so the 2-year view ends on the same fresh date as the 1-year view.
TWO_YEAR_DATES = [
    "2024-10-10", "2024-12-10", "2025-02-10", "2025-04-10",
    "2025-06-10", "2025-08-10", "2025-10-10", "2025-12-10",
    "2026-02-10", "2026-04-10", "2026-06-20", "2026-08-10",
    "2026-09-10",
]

MODE_DATES = {"year": YEAR_DATES, "2year": TWO_YEAR_DATES}
DEFAULT_OUT = {
    "year": DATA_DIR / "sector_scores_preview_year.csv",
    "2year": DATA_DIR / "sector_scores_preview_2year.csv",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build dashboard sector_score preview points on an explicit anchor "
            "date list using the compute_sector_scores.py method."
        )
    )
    parser.add_argument(
        "--mode",
        choices=sorted(MODE_DATES),
        help="Preset anchor list ('year' = 12 monthly, '2year' = 12 bi-monthly).",
    )
    parser.add_argument(
        "--dates",
        help="Comma-separated ISO anchor dates (overrides --mode date list).",
    )
    parser.add_argument(
        "--out-csv",
        type=Path,
        default=None,
        help="Output preview CSV path (defaults per --mode).",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DATA_DIR,
        help="Directory with fyn_<slug>_current_<date>_summary.csv and norm files.",
    )
    return parser.parse_args()


def load_norms(slug: str, data_dir: Path) -> Dict[str, float]:
    """metric -> 5Y FY norm (status=ok rows only)."""
    path = data_dir / f"fyn_{slug}_norm_summary.csv"
    norms: Dict[str, float] = {}
    if not path.exists():
        return norms
    with path.open(encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row.get("status") != "ok":
                continue
            metric = (row.get("metric") or "").strip()
            value = to_float(row.get("five_year_average", "")) or to_float(row.get("value", ""))
            if metric and value is not None and value > 0:
                norms[metric] = value
    return norms


def load_current(slug: str, data_dir: Path, date: str) -> Dict[str, float]:
    """metric -> current snapshot value on ``date`` (status=ok, positive)."""
    stamp = date.replace("-", "")
    path = data_dir / f"fyn_{slug}_current_{stamp}_summary.csv"
    values: Dict[str, float] = {}
    if not path.exists():
        return values
    with path.open(encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row.get("status") != "ok":
                continue
            metric = (row.get("metric") or "").strip()
            value = to_float(row.get("value", "")) or to_float(row.get("five_year_average", ""))
            if metric and value is not None and value > 0:
                values[metric] = value
    return values


def score_point(
    sector: str,
    date: str,
    current: Dict[str, float],
    norms: Dict[str, float],
) -> Optional[Dict[str, str]]:
    """Compute one dashboard preview row, or None if no usable metrics."""
    weights = SECTOR_WEIGHTS.get(sector, DEFAULT_WEIGHTS)
    # Metrics that are weighted AND have both a current value and a real norm.
    available = {
        m: w for m, w in weights.items()
        if m in current and m in norms and norms[m] > 0
    }
    if not available:
        return None
    weight_sum = sum(available.values())
    missing_weighted = sorted(set(weights) - set(available))

    sector_score = 0.0
    component_details: List[str] = []
    for metric, raw_weight in available.items():
        w = raw_weight / weight_sum  # renormalise over present metrics
        cur = current[metric]
        base = norms[metric]
        coef = base / cur if metric in YIELD_METRICS else cur / base
        sector_score += coef * w
        component_details.append(f"{metric}: {coef:.4f} x {w * 100:.1f}%")

    status = "ok" if not missing_weighted else "provisional"
    comment_parts = [
        f"status={status}",
        " | ".join(component_details),
    ]
    if missing_weighted:
        comment_parts.append(
            "missing weighted metrics: " + ", ".join(missing_weighted)
            + "; remaining weights renormalised"
        )
    return {
        "date": date,
        "sector": sector,
        "coefficient": f"{round(sector_score, 4)}",
        "metric": "sector_score",
        "metric_coefficient": "",
        "metric_weight": "",
        "source": (
            "build_sector_scores_timeframe.py over SEC EDGAR point-in-time "
            f"fyn_{sector_slug(sector)}_current_{date.replace('-', '')}_summary.csv; "
            f"norm fyn_{sector_slug(sector)}_norm_summary.csv"
        ),
        "comment": "; ".join(part for part in comment_parts if part),
    }


def build_rows(dates: List[str], data_dir: Path) -> Tuple[List[Dict[str, str]], Dict[str, set]]:
    rows: List[Dict[str, str]] = []
    points_per_sector: Dict[str, set] = defaultdict(set)
    for sector in sorted(SECTOR_WEIGHTS):
        slug = sector_slug(sector)
        norms = load_norms(slug, data_dir)
        if not norms:
            continue
        for date in dates:
            current = load_current(slug, data_dir, date)
            if not current:
                continue  # snapshot missing for this date -> honestly skipped
            row = score_point(sector, date, current, norms)
            if row is None:
                continue
            rows.append(row)
            points_per_sector[sector].add(date)
    rows.sort(key=lambda r: (r["sector"], r["date"]))
    return rows, points_per_sector


def write_preview(path: Path, rows: List[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=DASHBOARD_PREVIEW_FIELDNAMES, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    if args.dates:
        dates = [d.strip() for d in args.dates.split(",") if d.strip()]
        out_csv = args.out_csv or (DATA_DIR / "sector_scores_preview_custom.csv")
    elif args.mode:
        dates = MODE_DATES[args.mode]
        out_csv = args.out_csv or DEFAULT_OUT[args.mode]
    else:
        # No args: build both presets.
        for mode in ("year", "2year"):
            rows, pps = build_rows(MODE_DATES[mode], args.data_dir)
            out = DEFAULT_OUT[mode]
            write_preview(out, rows)
            distinct_dates = sorted({r["date"] for r in rows})
            print(
                f"[{mode}] wrote {len(rows)} points for {len(pps)} sectors over "
                f"{len(distinct_dates)} dates -> {out}"
            )
            for sector in sorted(pps):
                print(f"    {sector:<26} {len(pps[sector])} points")
        return 0

    rows, pps = build_rows(dates, args.data_dir)
    write_preview(out_csv, rows)
    distinct_dates = sorted({r["date"] for r in rows})
    print(
        f"Wrote {len(rows)} points for {len(pps)} sectors over "
        f"{len(distinct_dates)} dates -> {out_csv}"
    )
    for sector in sorted(pps):
        print(f"    {sector:<26} {len(pps[sector])} points")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
