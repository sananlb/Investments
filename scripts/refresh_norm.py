#!/usr/bin/env python3
"""
Monthly DETECTOR + PLANNER for the rolling 5Y fiscal-year valuation norm.

Problem (see data/market_quotes/pipeline_audit.md, section 1-2): the 5Y norm
window used to be hardcoded (FY2021..FY2025), so over time it went stale, and
nothing decided when to rebuild it. build_fy_norm.py now uses a ROLLING window
(default_fy_years(as_of) -> last 5 completed fiscal years available in SEC), but
something still has to notice "a new fiscal year's 10-Ks are out -> the window
moved -> the norms need rebuilding". That is this script.

What it IS: a cheap, offline detector and planner. It compares the rolling
window for today (or --as-of) against the window the on-disk norms were actually
built on, and:
  - if the window is UNCHANGED: prints 'norm window unchanged, skip' and exits 0.
  - if the window MOVED: prints (a) a reminder to archive the old norms first
    (scripts/archive_history.py) and (b) the exact build_fy_norm.py commands to
    rerun, one per sector, with the new --years window.

What it is NOT: a collector. It NEVER contacts the network (no SEC / Twelve Data
/ FMP / Nasdaq), NEVER runs build_fy_norm.py, archive_history.py, or any other
script. Rebuilding the norm is a paced, rate-limited, internet-costing job, so it
is left to the coordinator / update_all to run the printed commands. This keeps
refresh_norm safe to run on a schedule (e.g. monthly) and safe to run while a
backfill is collecting in the background.

How "the window the norms were built on" is determined, in order:
  1. The marker file data/market_quotes/.norm_window.json, if present
     ({"fiscal_years": [...], "updated_at": "...", "as_of": "..."}). This is the
     fast path and the single source of truth once written.
  2. Else the fiscal_years recorded in each fyn_<slug>_norm.json metadata (which
     build_fy_norm.py already writes). The set of windows found there is reported;
     a unanimous window is used as the current window.
With --write-marker the script (re-)writes the marker from the CURRENT on-disk
norms WITHOUT changing the window, so the first run after this feature lands can
record the baseline. It still performs no network and no rebuild.

Usage:
    python3 scripts/refresh_norm.py                 # detect for today
    python3 scripts/refresh_norm.py --as-of 2027-06-07   # test a future date
    python3 scripts/refresh_norm.py --write-marker  # record current window, no plan
    python3 scripts/refresh_norm.py --only semis energy
"""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
DATA = REPO_ROOT / "data" / "market_quotes"
MARKER_PATH = DATA / ".norm_window.json"

# slug -> display sector name, kept in sync with scripts/update_all.py SECTORS.
# Only the name/slug are needed here (no baskets): build_fy_norm.py resolves the
# basket from --sector for these built-in sectors, and the planner prints the
# command the coordinator runs, which can add --tickers if ever needed.
SECTORS: Dict[str, str] = {
    "banks": "Banks",
    "energy": "Energy",
    "telecom": "Telecom & Streaming",
    "delivery_logistics": "Delivery & Logistics",
    "insurance": "Insurance",
    "utilities": "Utilities",
    "mining": "Mining",
    "drugs": "Drugs",
    "commodities": "Commodities",
    "semis": "Semiconductors",
    "food": "Food & Staples",
    "technology": "Technology",
    "agriculture_chemicals": "Agriculture & Chemicals",
    "consumer_discretionary": "Consumer Discretionary",
    "medical_services": "Medical Services",
    "solar": "Solar",
    "reit": "REIT",
}


def _load_build_module():
    """Import build_fy_norm.py to reuse default_fy_years (no network at import).

    Imported by file path so refresh_norm works regardless of how it is invoked.
    Module import only runs date logic at top level (FY_YEARS = default_fy_years()),
    so it contacts no network.
    """
    spec = importlib.util.spec_from_file_location(
        "build_fy_norm", SCRIPTS / "build_fy_norm.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def parse_iso_date(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"invalid date {value!r}; expected YYYY-MM-DD"
        ) from exc


def read_marker(path: Path) -> Optional[List[int]]:
    """Return the fiscal_years recorded in the marker file, or None."""
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    years = data.get("fiscal_years")
    if isinstance(years, list) and all(isinstance(y, int) for y in years) and years:
        return list(years)
    return None


def read_norm_windows(source_dir: Path, slugs: List[str]) -> Dict[str, Optional[List[int]]]:
    """Per-slug fiscal_years from each fyn_<slug>_norm.json metadata (offline)."""
    windows: Dict[str, Optional[List[int]]] = {}
    for slug in slugs:
        path = source_dir / f"fyn_{slug}_norm.json"
        years: Optional[List[int]] = None
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                candidate = (data.get("metadata") or {}).get("fiscal_years")
                if (
                    isinstance(candidate, list)
                    and candidate
                    and all(isinstance(y, int) for y in candidate)
                ):
                    years = list(candidate)
            except (OSError, json.JSONDecodeError):
                years = None
        windows[slug] = years
    return windows


def current_window_from_norms(
    windows: Dict[str, Optional[List[int]]],
) -> Tuple[Optional[List[int]], List[str], Dict[str, List[int]]]:
    """Collapse per-slug norm windows into one current window if unanimous.

    Returns (unanimous_window_or_None, slugs_missing_a_window, distinct_windows).
    """
    missing = [slug for slug, years in windows.items() if not years]
    present = {slug: years for slug, years in windows.items() if years}
    distinct: Dict[str, List[int]] = {}
    for years in present.values():
        distinct[json.dumps(years)] = years
    if len(distinct) == 1:
        return next(iter(distinct.values())), missing, distinct
    return None, missing, distinct


def write_marker(path: Path, fiscal_years: List[int], as_of: dt.date) -> None:
    payload = {
        "fiscal_years": list(fiscal_years),
        "as_of": as_of.isoformat(),
        "updated_at": dt.datetime.now().replace(microsecond=0).isoformat(),
        "note": (
            "Window the on-disk fyn_*_norm files were built on. Written by "
            "scripts/refresh_norm.py; read by it to detect when the rolling 5Y "
            "window has moved. Updating this file does NOT rebuild the norms."
        ),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def build_command(slug: str, name: str, years: List[int]) -> str:
    years_str = " ".join(str(y) for y in years)
    return (
        f"python3 scripts/build_fy_norm.py --sector \"{name}\" "
        f"--slug {slug} --years {years_str}"
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Detect whether the rolling 5Y norm window has moved and, if so, "
            "print the build_fy_norm.py commands to rebuild it. Offline only; "
            "never contacts the network and never runs a collector."
        )
    )
    p.add_argument(
        "--as-of",
        type=parse_iso_date,
        default=None,
        metavar="YYYY-MM-DD",
        help="Date to evaluate the rolling window for (default today). For testing future dates.",
    )
    p.add_argument(
        "--only",
        nargs="*",
        default=None,
        help="Limit to these sector slugs (default: all built-in sectors).",
    )
    p.add_argument(
        "--write-marker",
        action="store_true",
        help=(
            "Record the CURRENT on-disk norm window into the marker file without "
            "planning a rebuild (use once to set the baseline). No network."
        ),
    )
    p.add_argument(
        "--source-dir",
        type=Path,
        default=DATA,
        help="Where the fyn_*_norm.json files and the marker live (default data/market_quotes).",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    source_dir: Path = args.source_dir
    marker_path = source_dir / MARKER_PATH.name

    slugs = list(SECTORS) if not args.only else [s for s in args.only if s in SECTORS]
    unknown = [s for s in (args.only or []) if s not in SECTORS]
    if unknown:
        print(f"Unknown slugs ignored: {unknown}")
    if not slugs:
        print("No valid sectors selected.")
        return 1

    as_of = args.as_of or dt.date.today()
    build = _load_build_module()
    desired = build.default_fy_years(as_of)

    print(f"As of      : {as_of.isoformat()}")
    print(f"Rolling 5Y : {desired}  (last {build.FY_WINDOW} completed fiscal years)")

    # Determine the window the on-disk norms were actually built on.
    norm_windows = read_norm_windows(source_dir, slugs)
    norm_window, missing, distinct = current_window_from_norms(norm_windows)
    marker_window = read_marker(marker_path)

    source_label: str
    current: Optional[List[int]]
    if marker_window is not None:
        current = marker_window
        source_label = f"marker {marker_path.name}"
    else:
        current = norm_window
        source_label = "fyn_<slug>_norm.json metadata"

    if current is None:
        print("Current    : UNKNOWN")
        if missing:
            print(f"  no fiscal_years window found for: {', '.join(sorted(missing))}")
        if len(distinct) > 1:
            print("  on-disk norms disagree on the window:")
            for _key, years in distinct.items():
                owners = sorted(s for s, y in norm_windows.items() if y == years)
                print(f"    {years} <- {', '.join(owners)}")
    else:
        print(f"Current    : {current}  (from {source_label})")
        if marker_window is None and missing:
            print(f"  note: no window on disk for: {', '.join(sorted(missing))}")

    # --write-marker: record the current on-disk window as baseline, no plan.
    if args.write_marker:
        baseline = norm_window if norm_window is not None else desired
        if norm_window is None:
            print(
                "  no unanimous on-disk window; recording the rolling window for "
                f"as_of instead: {baseline}"
            )
        write_marker(marker_path, baseline, as_of)
        print(f"Wrote marker: {marker_path}  fiscal_years={baseline}")
        return 0

    # Detect.
    if current is not None and current == desired:
        print("\nnorm window unchanged, skip")
        return 0

    if current is None:
        print(
            "\nnorm window could not be determined from disk; cannot confirm a "
            "move. Run with --write-marker once to record the baseline window, or "
            "(re)build the norms. No commands emitted to avoid a blind rebuild."
        )
        return 2

    # Window moved -> plan (but do not execute).
    added = [y for y in desired if y not in current]
    dropped = [y for y in current if y not in desired]
    print("\nNORM WINDOW MOVED:")
    print(f"  was : {current}")
    print(f"  now : {desired}")
    if added:
        print(f"  + new fiscal year(s) now available: {added}")
    if dropped:
        print(f"  - drop oldest fiscal year(s): {dropped}")

    print("\nStep 1 (archive the OLD norms before rebuilding so they are not lost):")
    print("  python3 scripts/archive_history.py")

    print("\nStep 2 (rebuild each sector norm on the new window; run these via the")
    print("        coordinator / update_all so SEC + price rate limits are paced —")
    print("        refresh_norm does NOT run them itself):")
    for slug in slugs:
        print("  " + build_command(slug, SECTORS[slug], desired))

    print("\nStep 3 (after the rebuild succeeds, record the new window):")
    print(f"  python3 scripts/refresh_norm.py --as-of {as_of.isoformat()} --write-marker")

    print(
        f"\nPlanned rebuild of {len(slugs)} sector norm(s). Nothing was fetched or "
        "rebuilt; this is a detector + planner only."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
