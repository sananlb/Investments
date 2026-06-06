#!/usr/bin/env python3
"""
Build preview sector_score points from already fetched point-in-time fundamentals.

This is an intermediate bridge, not the final 5-year baseline engine.

Method:
- raw company metrics come from data/market_quotes/*fund*.csv;
- 5-year company baselines come from data/market_quotes/sector_metric_baselines.csv
  where available;
- calibration coefficients from sector README summaries are only a fallback for
  metrics that do not yet have a strict baseline/raw data pair;
- each anchor point is built from real point-in-time raw company metrics on that
  date, not by ETF price scaling;
- unavailable metrics are excluded and weights are normalized over available
  metrics, with the output status marked as partial_calibrated.

Final version should remove the remaining README calibration fallback after
estimates/tangible-book metrics are automated.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Optional, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "market_quotes"

DEFAULT_COMPONENTS_CSV = DATA_DIR / "sector_score_components_preview.csv"
DEFAULT_SCORES_CSV = DATA_DIR / "sector_scores_preview.csv"
DEFAULT_JSON = DATA_DIR / "sector_scores_preview.json"
DEFAULT_BASELINES_CSV = DATA_DIR / "sector_metric_baselines.csv"

SOURCE_NOTE = (
    "SEC EDGAR point-in-time raw fundamentals plus sector_metric_baselines.csv "
    "where available; fallback to sector README 2026-05-30 calibration coefficients"
)
METHOD_NOTE = (
    "preview: company_baseline uses raw company metric / 5Y company baseline; "
    "readme_calibration fallback uses calibration_coefficient * raw_metric(date) / "
    "raw_metric(calibration_date); yield inputs are transformed or inverted as needed"
)


SECTOR_CONFIG: Dict[str, Dict[str, Any]] = {
    "Banks": {
        "raw_file": "fund_banks.csv",
        "calibration_date": "2026-05-30",
        "calibration_source": "BANKS_AND_FUNDS/README.md",
        "metrics": {
            "pb": {
                "raw_field": "pb",
                "weight": 0.35,
                "calibration_coefficient": 1.635,
                "direction": "multiple",
            },
            "p_tbv": {
                "raw_field": None,
                "weight": 0.25,
                "calibration_coefficient": 1.491,
                "direction": "multiple",
            },
            "pe": {
                "raw_field": "pe",
                "weight": 0.20,
                "calibration_coefficient": 1.265,
                "direction": "multiple",
            },
            "forward_pe": {
                "raw_field": None,
                "weight": 0.20,
                "calibration_coefficient": 1.159,
                "direction": "multiple",
            },
        },
    },
    "Semiconductors": {
        "raw_file": "fund_semis.csv",
        "calibration_date": "2026-05-30",
        "calibration_source": "SEMICONDUCTORS/README.md",
        "metrics": {
            "forward_pe": {
                "raw_field": None,
                "weight": 0.30,
                "calibration_coefficient": 1.302,
                "direction": "multiple",
            },
            "ps": {
                "raw_field": "ps",
                "weight": 0.25,
                "calibration_coefficient": 2.161,
                "direction": "multiple",
            },
            "pb": {
                "raw_field": "pb",
                "weight": 0.20,
                "calibration_coefficient": 2.243,
                "direction": "multiple",
            },
            "ev_ebitda": {
                "raw_field": "ev_ebitda",
                "weight": 0.25,
                "calibration_coefficient": 1.743,
                "direction": "multiple",
            },
        },
    },
    "Mining": {
        "raw_file": "fund_mining.csv",
        "calibration_date": "2026-05-30",
        "calibration_source": "MINING/README.md",
        "metrics": {
            "ev_ebitda": {
                "raw_field": "ev_ebitda",
                "weight": 0.35,
                "calibration_coefficient": 1.589,
                "direction": "multiple",
            },
            "p_fcf": {
                "raw_field": "fcf_yield",
                "weight": 0.25,
                "calibration_coefficient": 1.415,
                "direction": "inverse_yield",
            },
            "pb": {
                "raw_field": "pb",
                "weight": 0.20,
                "calibration_coefficient": 1.594,
                "direction": "multiple",
            },
            "pe": {
                "raw_field": "pe",
                "weight": 0.20,
                "calibration_coefficient": 1.564,
                "direction": "multiple",
            },
        },
    },
    "Technology": {
        "raw_file": "anchor_fundamentals.csv",
        "calibration_date": "2026-05-30",
        "calibration_source": "TECHNOLOGY/README.md",
        "metrics": {
            "forward_pe": {
                "raw_field": None,
                "weight": 0.30,
                "calibration_coefficient": 0.799,
                "direction": "multiple",
            },
            "pe": {
                "raw_field": "pe",
                "weight": 0.20,
                "calibration_coefficient": 0.694,
                "direction": "multiple",
            },
            "ev_ebitda": {
                "raw_field": "ev_ebitda",
                "weight": 0.20,
                "calibration_coefficient": 0.854,
                "direction": "multiple",
            },
            "ps": {
                "raw_field": "ps",
                "weight": 0.20,
                "calibration_coefficient": 0.927,
                "direction": "multiple",
            },
            "p_fcf": {
                "raw_field": "fcf_yield",
                "weight": 0.10,
                "calibration_coefficient": 1.008,
                "direction": "inverse_yield",
            },
        },
    },
}


COMPONENT_FIELDS = [
    "anchor_date",
    "sector",
    "metric",
    "raw_field",
    "calculation_mode",
    "metric_weight",
    "normalized_weight",
    "raw_average",
    "raw_calibration_average",
    "calibration_date",
    "calibration_coefficient",
    "metric_coefficient",
    "company_count",
    "symbols",
    "baseline_source",
    "status",
    "source",
    "method",
    "comment",
]

SCORE_FIELDS = [
    "anchor_date",
    "sector",
    "sector_score",
    "available_weight",
    "total_weight",
    "covered_company_count",
    "expected_company_count",
    "company_coverage",
    "metrics_used",
    "metrics_missing",
    "status",
    "source",
    "method",
    "comment",
]


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def load_baselines(path: Path) -> Dict[Tuple[str, str, str], Dict[str, str]]:
    if not path.exists():
        return {}
    baselines: Dict[Tuple[str, str, str], Dict[str, str]] = {}
    for row in read_csv(path):
        key = (row["sector"], row["symbol"], row["metric"])
        baselines[key] = row
    return baselines


def as_float(value: str) -> Optional[float]:
    if value is None or value == "":
        return None
    try:
        parsed = float(value)
    except ValueError:
        return None
    if parsed <= 0:
        return None
    return parsed


def metric_values(rows: Iterable[Dict[str, str]], anchor_date: str, raw_field: str) -> List[Tuple[str, float]]:
    values: List[Tuple[str, float]] = []
    for row in rows:
        if row.get("anchor_date") != anchor_date or row.get("status") != "ok":
            continue
        value = as_float(row.get(raw_field, ""))
        if value is None:
            continue
        values.append((row.get("symbol", ""), value))
    return values


def transformed_metric_values(
    rows: Iterable[Dict[str, str]],
    anchor_date: str,
    raw_field: str,
    direction: str,
) -> List[Tuple[str, float]]:
    values: List[Tuple[str, float]] = []
    for row in rows:
        if row.get("anchor_date") != anchor_date or row.get("status") != "ok":
            continue
        raw_value = as_float(row.get(raw_field, ""))
        if raw_value is None:
            continue
        value = (1 / raw_value) if direction == "inverse_yield" else raw_value
        values.append((row.get("symbol", ""), value))
    return values


def rounded(value: Optional[float], digits: int = 6) -> str:
    if value is None:
        return ""
    return str(round(value, digits))


def build_sector(
    sector: str,
    config: Dict[str, Any],
    baselines: Dict[Tuple[str, str, str], Dict[str, str]],
) -> Tuple[List[Dict[str, str]], List[Dict[str, str]]]:
    rows = read_csv(DATA_DIR / config["raw_file"])
    dates = sorted({row["anchor_date"] for row in rows})
    expected_symbols = sorted({row["symbol"] for row in rows if row.get("symbol")})
    total_weight = sum(metric["weight"] for metric in config["metrics"].values())

    component_rows: List[Dict[str, str]] = []
    score_rows: List[Dict[str, str]] = []

    for anchor_date in dates:
        components_for_score: List[Tuple[str, float, float]] = []
        missing_metrics: List[str] = []
        covered_symbols: set[str] = set()

        for metric_name, metric_config in config["metrics"].items():
            raw_field = metric_config["raw_field"]
            weight = float(metric_config["weight"])
            calibration_coefficient = float(metric_config["calibration_coefficient"])
            direction = metric_config["direction"]

            status = "ok"
            comment = ""
            calculation_mode = "readme_calibration"
            baseline_source = ""
            values: List[Tuple[str, float]] = []
            calibration_values: List[Tuple[str, float]] = []
            raw_average: Optional[float] = None
            calibration_average: Optional[float] = None
            metric_coefficient: Optional[float] = None

            if raw_field is None:
                status = "missing_raw_metric"
                comment = "metric is not available in SEC-derived raw fundamentals yet"
            else:
                baseline_company_values: List[Tuple[str, float, float, str]] = []
                transformed_values = transformed_metric_values(rows, anchor_date, raw_field, direction)
                for symbol, value in transformed_values:
                    baseline = baselines.get((sector, symbol, metric_name))
                    if baseline is None:
                        continue
                    baseline_average = as_float(baseline.get("baseline_average", ""))
                    if baseline_average is None:
                        continue
                    baseline_company_values.append(
                        (symbol, value, baseline_average, baseline.get("baseline_source", ""))
                    )

                if baseline_company_values:
                    calculation_mode = "company_baseline"
                    values = [(symbol, value) for symbol, value, _baseline, _source in baseline_company_values]
                    baseline_averages = [baseline for _symbol, _value, baseline, _source in baseline_company_values]
                    raw_average = mean(value for _symbol, value in values)
                    calibration_average = mean(baseline_averages)
                    metric_coefficient = mean(
                        value / baseline for _symbol, value, baseline, _source in baseline_company_values
                    )
                    baseline_source = "; ".join(
                        sorted({source for _symbol, _value, _baseline, source in baseline_company_values if source})
                    )
                    components_for_score.append((metric_name, weight, metric_coefficient))
                    covered_symbols.update(symbol for symbol, _value in values)
                else:
                    values = metric_values(rows, anchor_date, raw_field)
                    calibration_values = metric_values(rows, config["calibration_date"], raw_field)
                    if not values:
                        status = "missing_raw_values"
                        comment = "no positive point-in-time raw values for this anchor date"
                    elif not calibration_values:
                        status = "missing_calibration_values"
                        comment = "no positive raw values for calibration date"
                    else:
                        raw_average = mean(value for _symbol, value in values)
                        calibration_average = mean(value for _symbol, value in calibration_values)
                        if direction == "inverse_yield":
                            metric_coefficient = calibration_coefficient * calibration_average / raw_average
                        else:
                            metric_coefficient = calibration_coefficient * raw_average / calibration_average
                        components_for_score.append((metric_name, weight, metric_coefficient))
                        covered_symbols.update(symbol for symbol, _value in values)

            component_rows.append(
                {
                    "anchor_date": anchor_date,
                    "sector": sector,
                    "metric": metric_name,
                    "raw_field": raw_field or "",
                    "calculation_mode": calculation_mode,
                    "metric_weight": rounded(weight),
                    "normalized_weight": "",
                    "raw_average": rounded(raw_average),
                    "raw_calibration_average": rounded(calibration_average),
                    "calibration_date": config["calibration_date"],
                    "calibration_coefficient": rounded(calibration_coefficient),
                    "metric_coefficient": rounded(metric_coefficient),
                    "company_count": str(len(values)) if values else "0",
                    "symbols": ",".join(symbol for symbol, _value in values),
                    "baseline_source": baseline_source,
                    "status": status,
                    "source": SOURCE_NOTE,
                    "method": METHOD_NOTE,
                    "comment": comment,
                }
            )
            if status != "ok":
                missing_metrics.append(metric_name)

        available_weight = sum(weight for _metric, weight, _coefficient in components_for_score)
        expected_company_count = len(expected_symbols)
        covered_company_count = len(covered_symbols)
        company_coverage = (
            covered_company_count / expected_company_count if expected_company_count else 0
        )
        if available_weight > 0:
            score = sum(coefficient * weight for _metric, weight, coefficient in components_for_score) / available_weight
            metrics_used = [metric for metric, _weight, _coefficient in components_for_score]
            if company_coverage < 0.5:
                status = "low_coverage"
            elif abs(available_weight - total_weight) < 1e-9:
                status = "ok_calibrated"
            else:
                status = "partial_calibrated"
            comment = (
                "weights normalized over available metrics; final version should use "
                "full 5-year point-in-time baselines"
            )
        else:
            score = None
            metrics_used = []
            status = "missing"
            comment = "no usable metrics for this sector/date"

        normalized_by_metric = {
            metric: weight / available_weight
            for metric, weight, _coefficient in components_for_score
            if available_weight > 0
        }
        for row in component_rows:
            if row["sector"] == sector and row["anchor_date"] == anchor_date and row["metric"] in normalized_by_metric:
                row["normalized_weight"] = rounded(normalized_by_metric[row["metric"]])

        score_rows.append(
            {
                "anchor_date": anchor_date,
                "sector": sector,
                "sector_score": rounded(score),
                "available_weight": rounded(available_weight),
                "total_weight": rounded(total_weight),
                "covered_company_count": str(covered_company_count),
                "expected_company_count": str(expected_company_count),
                "company_coverage": rounded(company_coverage),
                "metrics_used": ",".join(metrics_used),
                "metrics_missing": ",".join(missing_metrics),
                "status": status,
                "source": SOURCE_NOTE,
                "method": METHOD_NOTE,
                "comment": comment,
            }
        )

    return component_rows, score_rows


def write_csv(path: Path, rows: List[Dict[str, str]], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    all_components: List[Dict[str, str]] = []
    all_scores: List[Dict[str, str]] = []
    baselines = load_baselines(DEFAULT_BASELINES_CSV)

    for sector, config in SECTOR_CONFIG.items():
        components, scores = build_sector(sector, config, baselines)
        all_components.extend(components)
        all_scores.extend(scores)

    all_components.sort(key=lambda row: (row["sector"], row["anchor_date"], row["metric"]))
    all_scores.sort(key=lambda row: (row["sector"], row["anchor_date"]))

    write_csv(DEFAULT_COMPONENTS_CSV, all_components, COMPONENT_FIELDS)
    write_csv(DEFAULT_SCORES_CSV, all_scores, SCORE_FIELDS)
    DEFAULT_JSON.write_text(
        json.dumps(
            {
                "metadata": {
                    "generated_at": dt.datetime.now().replace(microsecond=0).isoformat(),
                    "status": "preview",
                    "source": SOURCE_NOTE,
                    "method": METHOD_NOTE,
                    "sectors": sorted(SECTOR_CONFIG),
                    "note": (
                        "This preview is calibrated from existing README component "
                        "coefficients. It is not yet the final 5-year point-in-time baseline."
                    ),
                },
                "scores": all_scores,
                "components": all_components,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Wrote {len(all_scores)} sector score rows")
    print(f"Scores: {DEFAULT_SCORES_CSV}")
    print(f"Components: {DEFAULT_COMPONENTS_CSV}")
    print(f"JSON: {DEFAULT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
