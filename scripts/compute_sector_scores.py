#!/usr/bin/env python3
"""
Compute decade-anchor sector_score points from raw point-in-time fundamentals.

Input: one or more *fundamentals* CSVs produced by fetch_anchor_fundamentals.py
(per company, per anchor date, with raw multiples pe/ps/pb/ev_ebitda/fcf_yield/...).

Output: data/market_quotes/sector_scores.csv / .json with one component row per
(anchor_date, sector, metric) plus the rolled-up sector_score, following the
schema described in 02_MARKET_DASHBOARD.md. It also writes
sector_scores_preview.csv with one direct dashboard point per date/sector.

Method (matches 02_MARKET_DASHBOARD.md):
- For each (sector, anchor_date, metric) aggregate the company-basket value with
  the MEDIAN (robust to one-off extreme or negative multiples). Non-positive or
  missing values are dropped before taking the median.
- metric_coefficient = current_value / norm, where norm is the metric's own
  baseline. For yield-style metrics (fcf_yield) the formula is inverted
  (norm / current_value) so that >1.0 always means "more expensive".
- Apply per-sector metric weights from the "Стартовые веса по секторам" table.
  Metrics with no data for a sector are dropped and the remaining weights are
  renormalised to sum to 1.0.
- sector_score = sum(metric_coefficient * metric_weight).

HONESTY RULE (project requirement, see AGENTS.md / 02_MARKET_DASHBOARD.md):
The real five-year norm is the FY2021-FY2025 average of each multiple. When a
sector has a ready fyn_<slug>_norm_summary.csv file, this script uses that real
5Y FY norm and marks the component row status=ok. When a sector/metric has no
real norm, the script falls back to a self-baseline (the median of the metric
across the available anchor history) and marks that component row
status=provisional with an explicit comment. A sector is also provisional when
one of its configured weighted current metrics is missing and the remaining
weights have to be renormalised.

If fyn_<slug>_current_summary.csv exists, the script adds the current as-of
snapshot from that file as the latest anchor, so current/norm are produced by
the same FY-norm basket/method instead of mixing in fund_*.csv medians.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "market_quotes"
DEFAULT_OUT_CSV = DATA_DIR / "sector_scores.csv"
DEFAULT_OUT_JSON = DATA_DIR / "sector_scores.json"

# Metrics that mean "cheaper when the number is higher" -> invert the coefficient.
YIELD_METRICS = {"fcf_yield"}

# Per-sector metric weights from 02_MARKET_DASHBOARD.md "Стартовые веса по секторам".
# Keys are columns emitted by fetch_anchor_fundamentals.py. Forward P/E, P/TBV,
# dividend yield, NAV etc. are not available from the free SEC pipeline yet, so
# only the columns we actually have are listed; remaining weights are
# renormalised at runtime over the metrics that have data.
SECTOR_WEIGHTS: Dict[str, Dict[str, float]] = {
    "Banks": {"pb": 0.35, "pe": 0.20},
    "Insurance": {"pb": 0.30, "pe": 0.25},
    "REIT": {"pb": 0.25, "ps": 0.20},
    "Energy": {"ev_ebitda": 0.30, "fcf_yield": 0.30, "pe": 0.15, "pb": 0.15},
    "Mining": {"ev_ebitda": 0.25, "fcf_yield": 0.20, "pb": 0.20, "pe": 0.20},
    "Commodities": {"ev_ebitda": 0.25, "fcf_yield": 0.20, "pb": 0.20, "pe": 0.20},
    "Semiconductors": {"ps": 0.20, "pb": 0.15, "ev_ebitda": 0.25, "gross_margin": 0.15},
    "Technology": {"pe": 0.20, "ev_ebitda": 0.20, "ps": 0.20, "fcf_yield": 0.10},
    # AI Infrastructure intentionally NOT a sector/chart: kept only as a research
    # folder. Use Semiconductors for the chip sector. Do not re-add here.
    "Consumer Discretionary": {"pe": 0.30, "ev_ebitda": 0.25, "ps": 0.20, "fcf_yield": 0.15},
    "Food & Staples": {"pe": 0.30, "ev_ebitda": 0.25, "ps": 0.15},
    "Drugs": {"pe": 0.30, "ev_ebitda": 0.20, "ps": 0.10, "fcf_yield": 0.20},
    "Medical Services": {"pe": 0.30, "ev_ebitda": 0.25, "ps": 0.15},
    "Utilities": {"pe": 0.30, "ev_ebitda": 0.25, "pb": 0.15},
    "Telecom & Streaming": {"ev_ebitda": 0.30, "fcf_yield": 0.25, "ps": 0.15},
    "Delivery & Logistics": {"ev_ebitda": 0.30, "pe": 0.25, "ps": 0.20},
    "Agriculture & Chemicals": {"pe": 0.25, "ev_ebitda": 0.25, "ps": 0.20, "fcf_yield": 0.15},
    "Solar": {"ev_ebitda": 0.30, "ps": 0.25, "pb": 0.15},
    # China intentionally NOT a sector/chart (user decision): Chinese ADRs have
    # an ADR-ratio market-cap bug (e.g. BABA P/E ~216 = 8x inflated). Do not re-add.
}

# Generic fallback weights if a sector is not in the table above.
DEFAULT_WEIGHTS = {"pe": 0.35, "ps": 0.25, "pb": 0.20, "ev_ebitda": 0.20}

SECTOR_SLUGS = {
    "Semiconductors": "semis",
    "Telecom & Streaming": "telecom",
    "Delivery & Logistics": "delivery_logistics",
    "Food & Staples": "food",
    "Agriculture & Chemicals": "agriculture_chemicals",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Roll per-company fundamentals into per-sector decade scores."
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        type=Path,
        help="One or more fundamentals CSVs from fetch_anchor_fundamentals.py.",
    )
    parser.add_argument("--out-csv", type=Path, default=DEFAULT_OUT_CSV)
    parser.add_argument("--out-json", type=Path, default=DEFAULT_OUT_JSON)
    parser.add_argument(
        "--preview-csv",
        type=Path,
        default=None,
        help=(
            "Dashboard CSV path. Defaults to sector_scores_preview.csv next to "
            "--out-csv."
        ),
    )
    parser.add_argument(
        "--aggregate",
        choices=["median", "mean"],
        default="median",
        help="Basket aggregation per metric (median is robust to outliers).",
    )
    parser.add_argument(
        "--norms-dir",
        type=Path,
        default=DATA_DIR,
        help="Directory with fyn_<slug>_norm_summary.csv and optional fyn_<slug>_current_summary.csv files.",
    )
    return parser.parse_args()


def to_float(value: str) -> Optional[float]:
    if value is None:
        return None
    value = value.strip()
    if value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def load_rows(paths: List[Path]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for path in paths:
        if not path.exists():
            print(f"  skip (not found): {path}")
            continue
        with path.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
        print(f"  loaded {path}")
    return rows


def sector_slug(sector: str) -> str:
    if sector in SECTOR_SLUGS:
        return SECTOR_SLUGS[sector]
    return sector.lower().replace(" ", "_").replace("/", "_")


def load_real_norms(sectors: List[str], norms_dir: Path) -> Dict[Tuple[str, str], float]:
    norms: Dict[Tuple[str, str], float] = {}
    for sector in sectors:
        slug = sector_slug(sector)
        path = norms_dir / f"fyn_{slug}_norm_summary.csv"
        if not path.exists():
            continue
        with path.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("status") != "ok":
                    continue
                metric = (row.get("metric") or "").strip()
                value = to_float(row.get("five_year_average", "")) or to_float(row.get("value", ""))
                if not metric or value is None:
                    continue
                norms[(sector, metric)] = value
        print(f"  loaded real norms {path}")
    return norms


def current_snapshot_date(norms_dir: Path, slug: str) -> str:
    path = norms_dir / f"fyn_{slug}_current.json"
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            as_of = data.get("metadata", {}).get("as_of")
            if as_of:
                return str(as_of)
        except (json.JSONDecodeError, OSError):
            pass
    return dt.date.today().isoformat()


def current_snapshot_trading_date(norms_dir: Path, slug: str, fallback: str) -> str:
    path = norms_dir / f"fyn_{slug}_current.csv"
    if not path.exists():
        return fallback
    dates: List[str] = []
    try:
        with path.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                close_date = (row.get("close_date") or "").strip()
                if close_date and row.get("symbol") != "BASKET_AVG":
                    dates.append(close_date)
    except OSError:
        return fallback
    return max(dates) if dates else fallback


def current_snapshot_price_source(norms_dir: Path, slug: str) -> str:
    path = norms_dir / f"fyn_{slug}_current.json"
    if not path.exists():
        return "current EOD provider not recorded"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        source = data.get("metadata", {}).get("price_source")
    except (json.JSONDecodeError, OSError):
        return "current EOD provider not recorded"
    if isinstance(source, list):
        return ", ".join(str(item) for item in source)
    return str(source) if source else "current EOD provider not recorded"


def load_real_current_summaries(
    sectors: List[str],
    norms_dir: Path,
) -> Tuple[Dict[Tuple[str, str, str], float], Dict[Tuple[str, str], str], Dict[Tuple[str, str, str], str]]:
    values: Dict[Tuple[str, str, str], float] = {}
    trading_dates: Dict[Tuple[str, str], str] = {}
    sources: Dict[Tuple[str, str, str], str] = {}
    for sector in sectors:
        slug = sector_slug(sector)
        path = norms_dir / f"fyn_{slug}_current_summary.csv"
        if not path.exists():
            continue
        anchor = current_snapshot_date(norms_dir, slug)
        trading_dates[(sector, anchor)] = current_snapshot_trading_date(norms_dir, slug, anchor)
        source_label = (
            f"{path.name}; price source: "
            f"{current_snapshot_price_source(norms_dir, slug)}"
        )
        with path.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("status") != "ok":
                    continue
                metric = (row.get("metric") or "").strip()
                value = to_float(row.get("value", "")) or to_float(row.get("five_year_average", ""))
                if not metric or value is None or value <= 0:
                    continue
                key = (sector, anchor, metric)
                values[key] = value
                sources[key] = source_label
        print(f"  loaded real current snapshot {path}")
    return values, trading_dates, sources


def aggregate(values: List[float], how: str) -> float:
    if how == "mean":
        return statistics.fmean(values)
    return statistics.median(values)


def main() -> int:
    args = parse_args()
    print("Loading fundamentals:")
    rows = load_rows(args.inputs)
    if not rows:
        print("No input rows.")
        return 1

    # Group raw OK rows by (sector, anchor_date, metric) -> list of company values.
    # values[(sector, anchor, metric)] = [v, v, ...]
    values: Dict[Tuple[str, str, str], List[float]] = defaultdict(list)
    trading_date: Dict[Tuple[str, str], str] = {}
    sectors_seen = set()
    metric_cols = ["pe", "ps", "pb", "ev_ebitda", "fcf_yield", "gross_margin"]

    for row in rows:
        if row.get("status") != "ok":
            continue
        sector = row["sector"]
        anchor = row["anchor_date"]
        sectors_seen.add(sector)
        trading_date[(sector, anchor)] = row.get("actual_trading_date", "")
        for metric in metric_cols:
            v = to_float(row.get(metric, ""))
            # Drop non-positive multiples; they are economically meaningless here.
            if v is None or v <= 0:
                continue
            values[(sector, anchor, metric)].append(v)

    # Fundamentals inputs currently cover only a subset of sectors. Include any
    # configured sector that has a ready current summary in norms_dir so the
    # final current map can contain all completed sector baskets.
    for sector in SECTOR_WEIGHTS:
        current_path = args.norms_dir / f"fyn_{sector_slug(sector)}_current_summary.csv"
        if current_path.exists():
            sectors_seen.add(sector)

    # Per (sector, metric): basket value on each anchor, and the self-baseline norm.
    # current[(sector, anchor, metric)] = aggregated basket value
    current: Dict[Tuple[str, str, str], float] = {}
    history: Dict[Tuple[str, str], List[float]] = defaultdict(list)
    for (sector, anchor, metric), vals in values.items():
        agg = aggregate(vals, args.aggregate)
        current[(sector, anchor, metric)] = agg
        history[(sector, metric)].append(agg)

    norm: Dict[Tuple[str, str], float] = {
        key: statistics.median(vals) for key, vals in history.items()
    }
    print("Loading real 5Y norm summaries:")
    real_norms = load_real_norms(sorted(sectors_seen), args.norms_dir)
    print("Loading real current summaries:")
    real_current, real_current_trading_dates, real_current_sources = load_real_current_summaries(
        sorted(sectors_seen), args.norms_dir
    )
    for key, value in real_current.items():
        sector, anchor, metric = key
        current[key] = value
        history[(sector, metric)].append(value)
    trading_date.update(real_current_trading_dates)

    anchors = sorted({a for (_s, a, _m) in current})
    out_rows: List[Dict[str, Any]] = []

    for sector in sorted(sectors_seen):
        weights = SECTOR_WEIGHTS.get(sector, DEFAULT_WEIGHTS)
        for anchor in anchors:
            # Which weighted metrics actually have data on this anchor?
            available = {
                m: w for m, w in weights.items()
                if (sector, anchor, m) in current
            }
            if not available:
                continue
            missing_weighted_metrics = sorted(set(weights) - set(available))
            weight_sum = sum(available.values())
            sector_score = 0.0
            components: List[Dict[str, Any]] = []
            for metric, raw_weight in available.items():
                w = raw_weight / weight_sum  # renormalise over present metrics
                cur = current[(sector, anchor, metric)]
                real_norm_key = (sector, metric)
                if real_norm_key in real_norms:
                    base = real_norms[real_norm_key]
                    status = "ok"
                    current_source = real_current_sources.get((sector, anchor, metric))
                    current_comment = (
                        f"current TTM snapshot from {current_source}; "
                        if current_source else ""
                    )
                    comment = (
                        current_comment +
                        "real 5Y FY median norm from "
                        f"fyn_{sector_slug(sector)}_norm_summary.csv; "
                        f"aggregate={args.aggregate}"
                    )
                else:
                    base = norm.get((sector, metric), cur)
                    status = "provisional"
                    current_source = real_current_sources.get((sector, anchor, metric))
                    current_comment = (
                        f"current TTM snapshot from {current_source}; "
                        if current_source else ""
                    )
                    comment = (
                        current_comment +
                        "PROVISIONAL norm = self-baseline (median of metric across "
                        "available 2026 anchors), NOT a true FY2021-FY2025 5Y average; "
                        f"aggregate={args.aggregate}; replace norm with real 5Y FY history"
                    )
                if missing_weighted_metrics:
                    status = "provisional"
                    comment += (
                        "; PROVISIONAL sector score: missing weighted current "
                        f"metrics {', '.join(missing_weighted_metrics)}; remaining "
                        "weights renormalised"
                    )
                if base <= 0:
                    continue
                if metric in YIELD_METRICS:
                    coef = base / cur
                else:
                    coef = cur / base
                sector_score += coef * w
                components.append({"metric": metric, "cur": cur, "base": base,
                                   "coef": coef, "weight": w,
                                   "status": status, "comment": comment})
            for c in components:
                row_source = (
                    "build_fy_norm.py --current over SEC EDGAR; "
                    + real_current_sources[(sector, anchor, c["metric"])]
                    if (sector, anchor, c["metric"]) in real_current_sources
                    else "compute_sector_scores.py over SEC EDGAR fundamentals"
                )
                out_rows.append({
                    "anchor_date": anchor,
                    "actual_trading_date": trading_date.get((sector, anchor), ""),
                    "sector": sector,
                    "sector_score": round(sector_score, 4),
                    "metric": c["metric"],
                    "current_value": round(c["cur"], 6),
                    "five_year_average": round(c["base"], 6),
                    "metric_coefficient": round(c["coef"], 4),
                    "metric_weight": round(c["weight"], 4),
                    "source": row_source,
                    "comment": c["comment"],
                    "status": c["status"],
                })

    write_csv(args.out_csv, out_rows)
    write_json(args.out_json, out_rows, sorted(sectors_seen), anchors, args.aggregate)
    preview_csv = args.preview_csv or args.out_csv.with_name("sector_scores_preview.csv")
    preview_rows = build_dashboard_preview_rows(out_rows)
    write_dashboard_preview_csv(preview_csv, preview_rows)

    # Console summary: final sector_score on the latest anchor.
    if anchors:
        latest = anchors[-1]
        print(f"\nsector_score on latest anchor {latest}:")
        seen = set()
        for r in out_rows:
            if r["anchor_date"] == latest and r["sector"] not in seen:
                seen.add(r["sector"])
                print(f"  {r['sector']:<26} {r['sector_score']}")
    print(f"\nWrote {len(out_rows)} component rows for {len(sectors_seen)} sectors")
    print(f"CSV:  {args.out_csv}")
    print(f"JSON: {args.out_json}")
    print(f"Dashboard preview: {preview_csv} ({len(preview_rows)} points)")
    print(
        "NOTE: rows are provisional when a real norm or a configured weighted "
        "current metric is missing."
    )
    return 0


SCORE_FIELDNAMES = [
    "anchor_date", "actual_trading_date", "sector", "sector_score",
    "metric", "current_value", "five_year_average",
    "metric_coefficient", "metric_weight", "source", "comment", "status",
]

DASHBOARD_PREVIEW_FIELDNAMES = [
    "date", "sector", "coefficient", "metric",
    "metric_coefficient", "metric_weight", "source", "comment",
]


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=SCORE_FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_dashboard_preview_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Collapse component rows to one direct sector_score point per date/sector."""
    grouped: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["anchor_date"]), str(row["sector"]))].append(row)

    preview_rows: List[Dict[str, Any]] = []
    for (anchor_date, sector), components in sorted(grouped.items()):
        scores = {float(row["sector_score"]) for row in components}
        if len(scores) != 1:
            raise ValueError(
                f"inconsistent sector_score values for {anchor_date} / {sector}: "
                f"{sorted(scores)}"
            )
        sources = sorted({str(row.get("source") or "") for row in components if row.get("source")})
        statuses = sorted({str(row.get("status") or "") for row in components if row.get("status")})
        trading_dates = sorted({
            str(row.get("actual_trading_date") or "")
            for row in components
            if row.get("actual_trading_date")
        })
        component_details = " | ".join(
            f"{row['metric']}: {float(row['metric_coefficient']):.4f} x "
            f"{float(row['metric_weight']) * 100:.1f}%"
            for row in components
        )
        comment_parts = [
            f"actual_trading_date={','.join(trading_dates)}" if trading_dates else "",
            f"status={','.join(statuses)}" if statuses else "",
            component_details,
        ]
        preview_rows.append({
            "date": anchor_date,
            "sector": sector,
            "coefficient": next(iter(scores)),
            "metric": "sector_score",
            "metric_coefficient": "",
            "metric_weight": "",
            "source": "; ".join(sources),
            "comment": "; ".join(part for part in comment_parts if part),
        })
    return preview_rows


def write_dashboard_preview_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=DASHBOARD_PREVIEW_FIELDNAMES,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, rows: List[Dict[str, Any]], sectors: List[str],
               anchors: List[str], aggregate_how: str) -> None:
    statuses = sorted({str(row.get("status", "")) for row in rows if row.get("status")})
    metadata = {
        "generated_at": dt.datetime.now().replace(microsecond=0).isoformat(),
        "sectors": sectors,
        "anchors": anchors,
        "aggregate": aggregate_how,
        "status": statuses[0] if len(statuses) == 1 else "mixed",
        "norm_method": (
            "real fyn_<slug>_norm_summary.csv FY2021-FY2025 norms where available; "
            "fallback self-baseline median across available anchors where missing"
        ),
        "warning": (
            "Rows with status=provisional either use a self-baseline norm or "
            "omit a configured weighted current metric and renormalise the "
            "remaining weights."
        ),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"metadata": metadata, "rows": rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    raise SystemExit(main())
