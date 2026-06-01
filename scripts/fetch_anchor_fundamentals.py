#!/usr/bin/env python3
"""
Fetch point-in-time trailing fundamentals for sector-dashboard anchor dates.

Goal: build real historical valuation multiples on each 10/20/30 anchor date
without paid data. The only free, official, point-in-time fundamental source for
US/ADR companies is SEC EDGAR XBRL Company Facts.

Method (matches 02_MARKET_DASHBOARD.md):
- prices come from data/market_quotes/anchor_quotes.csv (already fetched);
- fundamentals come from SEC EDGAR companyconcept XBRL facts;
- for every anchor date we use ONLY facts with `filed` <= anchor_date
  (point-in-time, no look-ahead bias);
- TTM aggregates are built from the four most recent NON-OVERLAPPING quarters
  available on that date (XBRL ships duplicate/comparative periods, so we
  deduplicate by period and then walk back four contiguous quarters);
- multiples computed: P/E, P/S, P/B, EV/EBITDA, FCF yield.

Forward P/E and EPS revisions are analyst estimates and are NOT available for
past dates for free anywhere. They are replaced by SEC-derivable growth signals
that carry the same "account for future growth" meaning from actual filings:
- revenue_growth_yoy  = TTM revenue / TTM revenue one year earlier
- earnings_growth_yoy = TTM net income / TTM net income one year earlier

These are emitted as raw fundamentals; the sector_score weighting that turns
them into coefficients vs the 5-year norm is a separate step.

This script writes no API keys. SEC requires a descriptive User-Agent only.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUOTES = PROJECT_ROOT / "data" / "market_quotes" / "anchor_quotes.csv"
DEFAULT_OUT_CSV = PROJECT_ROOT / "data" / "market_quotes" / "anchor_fundamentals.csv"
DEFAULT_OUT_JSON = PROJECT_ROOT / "data" / "market_quotes" / "anchor_fundamentals.json"

SEC_TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"
SEC_CONCEPT_URL = "https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/{taxonomy}/{tag}.json"
USER_AGENT = "Investment Library research nalbantovfml@gmail.com"

# SEC asks for <=10 requests/second; we stay far below that.
REQUEST_PAUSE_SECONDS = 0.25

# XBRL tags vary by filer; try them in order until one returns data.
TAGS: Dict[str, List[Tuple[str, str]]] = {
    "net_income": [
        ("us-gaap", "NetIncomeLoss"),
        ("us-gaap", "ProfitLoss"),
        ("us-gaap", "NetIncomeLossAvailableToCommonStockholdersBasic"),
    ],
    "revenue": [
        ("us-gaap", "RevenueFromContractWithCustomerExcludingAssessedTax"),
        ("us-gaap", "Revenues"),
        ("us-gaap", "RevenueFromContractWithCustomerIncludingAssessedTax"),
        ("us-gaap", "SalesRevenueNet"),
    ],
    "gross_profit": [
        ("us-gaap", "GrossProfit"),
    ],
    "operating_income": [
        ("us-gaap", "OperatingIncomeLoss"),
    ],
    "dep_amort": [
        ("us-gaap", "DepreciationDepletionAndAmortization"),
        ("us-gaap", "DepreciationAmortizationAndAccretionNet"),
        ("us-gaap", "DepreciationAndAmortization"),
    ],
    # Some filers (e.g. MSFT) only report D&A as separate components; summed as fallback.
    "depreciation_only": [
        ("us-gaap", "Depreciation"),
    ],
    "amortization_only": [
        ("us-gaap", "AmortizationOfIntangibleAssets"),
    ],
    "op_cash_flow": [
        ("us-gaap", "NetCashProvidedByUsedInOperatingActivities"),
        ("us-gaap", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"),
    ],
    "capex": [
        ("us-gaap", "PaymentsToAcquirePropertyPlantAndEquipment"),
        ("us-gaap", "PaymentsToAcquireProductiveAssets"),
    ],
    # Instantaneous (balance-sheet) facts: single value at a point in time.
    "equity": [
        ("us-gaap", "StockholdersEquity"),
        ("us-gaap", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"),
    ],
    "debt": [
        ("us-gaap", "LongTermDebtAndCapitalLeaseObligations"),
        ("us-gaap", "LongTermDebt"),
        ("us-gaap", "DebtLongtermAndShorttermCombinedAmount"),
    ],
    "cash": [
        ("us-gaap", "CashAndCashEquivalentsAtCarryingValue"),
        ("us-gaap", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"),
    ],
    "shares": [
        ("dei", "EntityCommonStockSharesOutstanding"),
        ("us-gaap", "CommonStockSharesOutstanding"),
        ("us-gaap", "WeightedAverageNumberOfDilutedSharesOutstanding"),
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build point-in-time trailing multiples from SEC EDGAR.")
    parser.add_argument("--quotes", type=Path, default=DEFAULT_QUOTES)
    parser.add_argument("--out-csv", type=Path, default=DEFAULT_OUT_CSV)
    parser.add_argument("--out-json", type=Path, default=DEFAULT_OUT_JSON)
    parser.add_argument("--sector", default="Technology", help="Sector name as used in anchor_quotes.csv.")
    return parser.parse_args()


def http_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def load_ticker_cik_map() -> Dict[str, int]:
    data = http_json(SEC_TICKER_MAP_URL)
    return {row["ticker"].upper(): int(row["cik_str"]) for row in data.values()}


def fetch_concept(cik: int, taxonomy: str, tag: str) -> Optional[List[Dict[str, Any]]]:
    url = SEC_CONCEPT_URL.format(cik=cik, taxonomy=taxonomy, tag=tag)
    try:
        data = http_json(url)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise
    time.sleep(REQUEST_PAUSE_SECONDS)
    units = data.get("units", {})
    key = "USD" if "USD" in units else ("shares" if "shares" in units else None)
    if key is None and units:
        key = next(iter(units))
    return units.get(key, []) if key else None


def latest_filed(points: List[Dict[str, Any]], on_or_before: dt.date) -> Optional[str]:
    """Most recent `end` among points filed on/before the cutoff date."""
    best_end: Optional[str] = None
    for point in points:
        filed = point.get("filed")
        end = point.get("end")
        if not filed or not end or point.get("val") is None:
            continue
        if dt.date.fromisoformat(filed) > on_or_before:
            continue
        if best_end is None or end > best_end:
            best_end = end
    return best_end


def fetch_best_series(cik: int, candidates: List[Tuple[str, str]], as_of: dt.date) -> List[Dict[str, Any]]:
    """Pick the XBRL tag whose data is still current as of `as_of`.

    Some issuers migrate between tags (e.g. NVDA dropped
    RevenueFromContractWithCustomerExcludingAssessedTax for Revenues). Taking the
    first non-empty tag can return a series frozen years ago. Instead we fetch all
    candidate tags and keep the one with the most recent period end available on the
    anchor date; ties break toward the earlier (more standard) tag in the list.
    """
    best_points: List[Dict[str, Any]] = []
    best_end: Optional[str] = None
    for taxonomy, tag in candidates:
        points = fetch_concept(cik, taxonomy, tag)
        if not points:
            continue
        end = latest_filed(points, as_of)
        if end is None:
            continue
        if best_end is None or end > best_end:
            best_end = end
            best_points = points
    return best_points


def duration_days(point: Dict[str, Any]) -> Optional[int]:
    start, end = point.get("start"), point.get("end")
    if not start or not end:
        return None
    return (dt.date.fromisoformat(end) - dt.date.fromisoformat(start)).days


def is_quarterly(point: Dict[str, Any]) -> bool:
    days = duration_days(point)
    return days is not None and 80 <= days <= 100


def is_annual(point: Dict[str, Any]) -> bool:
    days = duration_days(point)
    return days is not None and 350 <= days <= 380


def latest_versions_by_end(
    points: List[Dict[str, Any]],
    anchor: dt.date,
    predicate=None,
) -> Dict[str, Dict[str, Any]]:
    """Keep the most recently filed value for each period end, filed on/before anchor.

    `predicate(point)` optionally filters which points qualify (e.g. quarterly).
    """
    chosen: Dict[str, Dict[str, Any]] = {}
    for point in points:
        filed = point.get("filed")
        end = point.get("end")
        if not filed or not end or point.get("val") is None:
            continue
        if dt.date.fromisoformat(filed) > anchor:
            continue
        if predicate is not None and not predicate(point):
            continue
        prev = chosen.get(end)
        if prev is None or point["filed"] > prev["filed"]:
            chosen[end] = point
    return chosen


def nearest_quarter(quarters: Dict[str, Dict[str, Any]], target_end: dt.date, tolerance: int = 14) -> Optional[Dict[str, Any]]:
    candidates = [e for e in quarters if abs((dt.date.fromisoformat(e) - target_end).days) <= tolerance]
    if not candidates:
        return None
    best = min(candidates, key=lambda e: abs((dt.date.fromisoformat(e) - target_end).days))
    return quarters[best]


def ttm_ending(points: List[Dict[str, Any]], anchor: dt.date, fy_end_str: str) -> Tuple[Optional[float], Optional[str]]:
    """Trailing-twelve-months value for the period ending at the given fiscal-year end,
    rolled forward by any quarters filed after that fiscal year.

    TTM = annual(FY) + sum(quarters after FY end) - sum(matching quarters one year earlier).

    This bridges the common gap where annual filers (10-K) omit a standalone Q4
    quarterly fact: we anchor on the full-year number and only add deltas.

    Returns (value, latest_period_end) or (None, None) if it cannot be built.
    """
    annuals = latest_versions_by_end(points, anchor, is_annual)
    quarters = latest_versions_by_end(points, anchor, is_quarterly)
    fy = annuals.get(fy_end_str)
    if fy is None:
        return None, None

    fy_end = dt.date.fromisoformat(fy_end_str)
    total = fy["val"]
    latest_end = fy_end_str

    new_quarters = sorted(
        (quarters[e] for e in quarters if dt.date.fromisoformat(e) > fy_end),
        key=lambda q: q["end"],
    )
    for q in new_quarters:
        q_end = dt.date.fromisoformat(q["end"])
        prior_target = dt.date(q_end.year - 1, q_end.month, min(q_end.day, 28))
        prior = nearest_quarter(quarters, prior_target)
        if prior is None:
            # Cannot net out the matching prior-year quarter -> abort to avoid a wrong TTM.
            return None, None
        total += q["val"] - prior["val"]
        if q["end"] > latest_end:
            latest_end = q["end"]
    return total, latest_end


def latest_fy_end(points: List[Dict[str, Any]], anchor: dt.date, year_offset: int = 0) -> Optional[str]:
    """The fiscal-year end string for the most recent FY available on `anchor`,
    optionally stepped back `year_offset` fiscal years."""
    annuals = latest_versions_by_end(points, anchor, is_annual)
    if not annuals:
        return None
    ends = sorted(annuals, reverse=True)
    if year_offset >= len(ends):
        return None
    return ends[year_offset]


def ttm_sum(points: List[Dict[str, Any]], anchor: dt.date) -> Tuple[Optional[float], Optional[str], Optional[str]]:
    """Current TTM as known on `anchor`. Returns (value, latest_end, None)."""
    fy_end = latest_fy_end(points, anchor, 0)
    if fy_end is None:
        return None, None, None
    value, latest_end = ttm_ending(points, anchor, fy_end)
    return value, latest_end, None


def ttm_at_offset(points: List[Dict[str, Any]], anchor: dt.date, year_offset: int) -> Optional[float]:
    """TTM for the period one `year_offset` fiscal years before the latest,
    using only data filed on/before `anchor` (point-in-time)."""
    fy_end = latest_fy_end(points, anchor, year_offset)
    if fy_end is None:
        return None
    value, _ = ttm_ending(points, anchor, fy_end)
    return value


def latest_instant(points: List[Dict[str, Any]], anchor: dt.date) -> Tuple[Optional[float], Optional[str]]:
    """Most recent balance-sheet value filed on/before anchor (any period type)."""
    by_end = latest_versions_by_end(points, anchor)
    if not by_end:
        return None, None
    end = max(by_end)
    return by_end[end]["val"], end


def load_quotes(path: Path, sector: str) -> Tuple[List[str], Dict[Tuple[str, str], Dict[str, Any]]]:
    """Return anchor dates and {(symbol, anchor_date): row} for the sector."""
    anchors: List[str] = []
    by_key: Dict[Tuple[str, str], Dict[str, Any]] = {}
    with path.open(encoding="utf-8") as file:
        for row in csv.DictReader(file):
            if row["sector"] != sector:
                continue
            anchors.append(row["anchor_date"])
            by_key[(row["symbol"], row["anchor_date"])] = row
    return sorted(set(anchors)), by_key


def safe_div(numerator: Optional[float], denominator: Optional[float]) -> Optional[float]:
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator


def build_company_rows(
    symbol: str,
    cik: int,
    sector: str,
    anchors: List[str],
    quotes: Dict[Tuple[str, str], Dict[str, Any]],
) -> List[Dict[str, Any]]:
    # Choose tags based on the most recent anchor so migrated tags (e.g. NVDA's
    # Revenues vs the retired RevenueFromContractWithCustomer) resolve to current data.
    latest_anchor = max(dt.date.fromisoformat(a) for a in anchors)
    facts = {name: fetch_best_series(cik, candidates, latest_anchor) for name, candidates in TAGS.items()}
    rows: List[Dict[str, Any]] = []

    for anchor_str in anchors:
        anchor = dt.date.fromisoformat(anchor_str)
        quote = quotes.get((symbol, anchor_str))
        close = None
        actual_date = ""
        if quote and quote.get("status") == "ok" and quote.get("close"):
            try:
                close = float(quote["close"])
            except ValueError:
                close = None
            actual_date = quote.get("actual_trading_date", "")

        ttm_ni, ni_end, _ = ttm_sum(facts["net_income"], anchor)
        ttm_rev, _, _ = ttm_sum(facts["revenue"], anchor)
        ttm_gp, _, _ = ttm_sum(facts["gross_profit"], anchor)
        ttm_oi, _, _ = ttm_sum(facts["operating_income"], anchor)
        ttm_da, _, _ = ttm_sum(facts["dep_amort"], anchor)
        if ttm_da is None:
            # Fallback: some filers split D&A into separate components.
            dep, _, _ = ttm_sum(facts["depreciation_only"], anchor)
            amort, _, _ = ttm_sum(facts["amortization_only"], anchor)
            if dep is not None or amort is not None:
                ttm_da = (dep or 0) + (amort or 0)
        ttm_ocf, _, _ = ttm_sum(facts["op_cash_flow"], anchor)
        ttm_capex, _, _ = ttm_sum(facts["capex"], anchor)

        rev_prior = ttm_at_offset(facts["revenue"], anchor, 1)
        ni_prior = ttm_at_offset(facts["net_income"], anchor, 1)

        equity, eq_end = latest_instant(facts["equity"], anchor)
        debt, _ = latest_instant(facts["debt"], anchor)
        cash, _ = latest_instant(facts["cash"], anchor)
        shares, sh_end = latest_instant(facts["shares"], anchor)

        market_cap = (close * shares) if (close is not None and shares) else None
        ebitda = (ttm_oi + ttm_da) if (ttm_oi is not None and ttm_da is not None) else None
        ev = None
        if market_cap is not None:
            ev = market_cap + (debt or 0) - (cash or 0)
        fcf = (ttm_ocf - ttm_capex) if (ttm_ocf is not None and ttm_capex is not None) else None

        pe = safe_div(market_cap, ttm_ni)
        ps = safe_div(market_cap, ttm_rev)
        pb = safe_div(market_cap, equity)
        ev_ebitda = safe_div(ev, ebitda)
        fcf_yield = safe_div(fcf, market_cap)
        gross_margin = safe_div(ttm_gp, ttm_rev)
        rev_growth = safe_div(ttm_rev, rev_prior)
        earn_growth = safe_div(ttm_ni, ni_prior)

        status = "ok" if (close is not None and market_cap is not None and ttm_ni is not None) else "incomplete"
        notes: List[str] = []
        if close is None:
            notes.append("no ok price in anchor_quotes")
        if shares is None:
            notes.append("no shares outstanding")
        if ttm_ni is None:
            notes.append("no clean TTM net income window")
        if pe is not None and pe < 0:
            notes.append("negative P/E (loss-making TTM)")

        rows.append(
            {
                "anchor_date": anchor_str,
                "actual_trading_date": actual_date,
                "sector": sector,
                "symbol": symbol,
                "cik": f"{cik:010d}",
                "close": close if close is not None else "",
                "shares_outstanding": shares if shares is not None else "",
                "shares_asof": sh_end or "",
                "ttm_net_income": ttm_ni if ttm_ni is not None else "",
                "ttm_revenue": ttm_rev if ttm_rev is not None else "",
                "ttm_ni_end": ni_end or "",
                "equity": equity if equity is not None else "",
                "equity_asof": eq_end or "",
                "market_cap": market_cap if market_cap is not None else "",
                "enterprise_value": ev if ev is not None else "",
                "ebitda_ttm": ebitda if ebitda is not None else "",
                "fcf_ttm": fcf if fcf is not None else "",
                "pe": round(pe, 4) if pe is not None else "",
                "ps": round(ps, 4) if ps is not None else "",
                "pb": round(pb, 4) if pb is not None else "",
                "ev_ebitda": round(ev_ebitda, 4) if ev_ebitda is not None else "",
                "fcf_yield": round(fcf_yield, 6) if fcf_yield is not None else "",
                "gross_margin": round(gross_margin, 4) if gross_margin is not None else "",
                "revenue_growth_yoy": round(rev_growth, 4) if rev_growth is not None else "",
                "earnings_growth_yoy": round(earn_growth, 4) if earn_growth is not None else "",
                "source": "SEC EDGAR XBRL companyconcept (point-in-time, filed<=anchor); price from anchor_quotes",
                "status": status,
                "comment": "; ".join(notes),
            }
        )
    return rows


FIELDNAMES = [
    "anchor_date", "actual_trading_date", "sector", "symbol", "cik",
    "close", "shares_outstanding", "shares_asof",
    "ttm_net_income", "ttm_revenue", "ttm_ni_end",
    "equity", "equity_asof", "market_cap", "enterprise_value", "ebitda_ttm", "fcf_ttm",
    "pe", "ps", "pb", "ev_ebitda", "fcf_yield", "gross_margin",
    "revenue_growth_yoy", "earnings_growth_yoy",
    "source", "status", "comment",
]


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, rows: List[Dict[str, Any]], metadata: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"metadata": metadata, "rows": rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    anchors, quotes = load_quotes(args.quotes, args.sector)
    if not anchors:
        print(f"No rows for sector '{args.sector}' in {args.quotes}")
        return 1

    symbols = sorted({symbol for (symbol, _anchor) in quotes})
    print(f"Sector: {args.sector} | symbols: {', '.join(symbols)}")
    print(f"Anchors: {', '.join(anchors)}")

    ticker_map = load_ticker_cik_map()
    time.sleep(REQUEST_PAUSE_SECONDS)

    all_rows: List[Dict[str, Any]] = []
    unmapped: List[str] = []
    for symbol in symbols:
        cik = ticker_map.get(symbol.upper())
        if cik is None:
            unmapped.append(symbol)
            print(f"  {symbol}: no CIK in SEC map (foreign/local listing) -> skipped")
            continue
        print(f"  {symbol}: CIK{cik:010d} ... fetching facts")
        all_rows.extend(build_company_rows(symbol, cik, args.sector, anchors, quotes))

    ok = sum(1 for r in all_rows if r["status"] == "ok")
    metadata = {
        "generated_at": dt.datetime.now().replace(microsecond=0).isoformat(),
        "sector": args.sector,
        "anchors": anchors,
        "symbols": symbols,
        "unmapped_symbols": unmapped,
        "source": "SEC EDGAR XBRL Company Facts",
        "method": "point-in-time: only facts with filed<=anchor_date; TTM from 4 contiguous quarters",
        "note": "Forward P/E / EPS revisions are not free for past dates; replaced by revenue_growth_yoy and earnings_growth_yoy from filings.",
    }
    write_csv(args.out_csv, all_rows)
    write_json(args.out_json, all_rows, metadata)

    print(f"\nWrote {len(all_rows)} rows: {ok} ok, {len(all_rows) - ok} incomplete")
    print(f"CSV: {args.out_csv}")
    print(f"JSON: {args.out_json}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
