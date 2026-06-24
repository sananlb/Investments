#!/usr/bin/env python3
"""
One-command decade update for the sector valuation dashboard.

What it does, in order:
1. For each sector, refresh the CURRENT snapshot of multiples. The default
   auto policy fetches prices every run, checks cheap SEC submissions metadata,
   refreshes XBRL only for companies with new filings, and performs full SEC
   audits on Mar/May/Aug/Nov 20.
2. Roll those current snapshots against the one-time 5Y FY norms into
   sector_scores.csv / .json via compute_sector_scores.py.

The 5Y NORM itself (fyn_<slug>_norm_summary.csv) is NOT refetched here — it is a
once-a-year job (rerun build_fy_norm.py without --current when a new fiscal year
closes in SEC). This script only updates the moving "current point" and the
score, so history accumulates on its own over time.

Sectors run strictly sequentially. Nasdaq is the default current-price provider
to avoid the Twelve Data free-plan limit; Twelve/FMP/auto remain selectable.

Usage:
    python3 scripts/update_all.py                 # all sectors, then score
    python3 scripts/update_all.py --only banks energy
    python3 scripts/update_all.py --skip-current  # only recompute the score
    python3 scripts/update_all.py --sector-pause 12
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
DATA = REPO_ROOT / "data" / "market_quotes"

# Canonical sector -> (display name, US-only basket). Foreign filers (TSM/ASML/
# GOLD/BABA...) are either excluded from price ratios downstream or skipped; the
# baskets here are the ones whose 5Y norms were built. AI Infrastructure and
# China are intentionally absent (user decision: not sectors / not on the chart).
SECTORS: Dict[str, Tuple[str, List[str]]] = {
    "banks": ("Banks", ["JPM", "BAC", "C", "GS", "MS"]),
    "energy": ("Energy", ["XOM", "CVX", "COP", "EOG", "SLB"]),
    "telecom": ("Telecom & Streaming", ["NFLX", "DIS", "CMCSA", "VZ", "T", "TMUS", "SPOT", "CHTR"]),
    "delivery_logistics": ("Delivery & Logistics", ["UPS", "FDX", "UBER", "DASH", "XPO"]),
    "insurance": ("Insurance", ["UNH", "PGR", "CB", "AIG", "ALL", "BRK-B", "MRSH"]),
    "utilities": ("Utilities", ["NEE", "DUK", "SO", "AEP", "D"]),
    "mining": ("Mining", ["FCX", "SCCO", "NEM", "GOLD", "VALE"]),
    "drugs": ("Drugs", ["LLY", "JNJ", "MRK", "ABBV", "PFE"]),
    "commodities": ("Commodities", ["FCX", "SCCO", "ALB", "NEM"]),
    "semis": ("Semiconductors", ["NVDA", "AMD", "AVGO", "TSM", "ASML", "MU", "QCOM", "TXN"]),
    "food": ("Food & Staples", ["WMT", "COST", "KO", "PEP", "MDLZ", "HSY", "MNST"]),
    "technology": ("Technology", ["AAPL", "MSFT", "GOOG", "META", "ADBE", "CRM", "NOW", "ACN", "IBM"]),
    "agriculture_chemicals": ("Agriculture & Chemicals", ["LIN", "APD", "SHW", "ECL", "CTVA", "NTR", "FMC"]),
    "consumer_discretionary": ("Consumer Discretionary", ["AMZN", "HD", "LOW", "NKE", "MCD", "LULU"]),
    "medical_services": ("Medtech & Life Science Tools", ["ABT", "ISRG", "SYK", "MDT", "BSX", "TMO", "ALGN"]),
    "solar": ("Solar", ["FSLR", "NXT", "ENPH", "SEDG", "RUN", "CSIQ", "SHLS"]),
    "reit": ("REIT", ["WELL", "PLD", "EQIX", "AMT", "O", "DLR", "VICI"]),
}

# Fundamentals CSVs passed to compute_sector_scores as the ticker/anchor source.
# (compute_sector_scores prefers fyn_<slug>_current_summary.csv when present.)
SCORE_INPUTS = [
    DATA / "anchor_fundamentals.csv",
    DATA / "fund_banks_new.csv",
    DATA / "fund_semis.csv",
    DATA / "fund_mining_new.csv",
    DATA / "fund_energy_new.csv",
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="One-command decade update of sector scores.")
    p.add_argument("--only", nargs="*", default=None,
                   help="Update only these slugs (default: all).")
    p.add_argument("--skip-current", action="store_true",
                   help="Skip refreshing current snapshots; only recompute the score.")
    p.add_argument("--sector-pause", type=float, default=1.0,
                   help="Seconds to wait between sectors (default: 1).")
    p.add_argument("--retry-wait", type=float, default=60.0,
                   help="Seconds to wait before retrying a sector that hit 429.")
    p.add_argument("--min-ok-fraction", type=float, default=0.5,
                   help="If fewer than this fraction of price rows are ok, retry the sector once.")
    p.add_argument(
        "--refresh-mode",
        choices=("auto", "full", "prices-only"),
        default="auto",
        help="Fundamentals refresh policy (default: auto).",
    )
    p.add_argument(
        "--price-provider",
        choices=("twelve", "fmp", "nasdaq", "auto"),
        default="nasdaq",
        help="Current-price provider (default: nasdaq).",
    )
    return p.parse_args()


def current_price_ok_fraction(slug: str) -> float:
    """Fraction of PRICE metric rows that came back ok in the current snapshot.
    A low value usually means Twelve Data 429 dropped prices -> worth a retry."""
    path = DATA / f"fyn_{slug}_current_summary.csv"
    if not path.exists():
        return 0.0
    price_metrics = {"pe", "ps", "pb", "ev_ebitda", "fcf_yield"}
    total = ok = 0
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("metric") in price_metrics:
                total += 1
                if row.get("status") == "ok":
                    ok += 1
    return (ok / total) if total else 0.0


def run_current(
    slug: str,
    name: str,
    tickers: List[str],
    refresh_mode: str,
    price_provider: str,
) -> int:
    cmd = [sys.executable, str(SCRIPTS / "build_fy_norm.py"),
           "--sector", name, "--tickers", *tickers, "--slug", slug, "--current",
           "--refresh-mode", refresh_mode, "--price-provider", price_provider]
    print(
        f"  $ build_fy_norm --current --slug {slug} "
        f"--refresh-mode {refresh_mode} --price-provider {price_provider}"
    )
    return subprocess.run(cmd, cwd=REPO_ROOT).returncode


def run_score() -> int:
    inputs = [str(p) for p in SCORE_INPUTS if p.exists()]
    cmd = [sys.executable, str(SCRIPTS / "compute_sector_scores.py"), *inputs,
           "--norms-dir", str(DATA),
           "--out-csv", str(DATA / "sector_scores.csv"),
           "--out-json", str(DATA / "sector_scores.json")]
    print(f"\n  $ compute_sector_scores -> sector_scores.csv")
    return subprocess.run(cmd, cwd=REPO_ROOT).returncode


def main() -> int:
    args = parse_args()
    slugs = list(SECTORS) if not args.only else [s for s in args.only if s in SECTORS]
    unknown = [s for s in (args.only or []) if s not in SECTORS]
    if unknown:
        print(f"Unknown slugs ignored: {unknown}")
    if not slugs:
        print("No valid sectors to update.")
        return 1

    if not args.skip_current:
        print(f"Refreshing current snapshots for {len(slugs)} sectors (sequential, rate-limited)...")
        for i, slug in enumerate(slugs):
            name, tickers = SECTORS[slug]
            print(f"[{i+1}/{len(slugs)}] {name}")
            run_current(
                slug, name, tickers, args.refresh_mode, args.price_provider
            )
            frac = current_price_ok_fraction(slug)
            if frac < args.min_ok_fraction:
                print(f"  ! only {frac:.0%} price rows ok (likely 429) -> retry in {args.retry_wait:.0f}s")
                time.sleep(args.retry_wait)
                run_current(
                    slug, name, tickers, args.refresh_mode, args.price_provider
                )
                frac = current_price_ok_fraction(slug)
                print(f"  retry result: {frac:.0%} price rows ok")
            else:
                print(f"  ok: {frac:.0%} price rows")
            if i < len(slugs) - 1:
                time.sleep(args.sector_pause)

    rc = run_score()
    print("\nDone." if rc == 0 else "\nScore step returned non-zero.")
    print(
        "Next decade: rerun this script. Auto mode performs four full SEC audits "
        "per year and incremental filing refreshes between them."
    )
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
