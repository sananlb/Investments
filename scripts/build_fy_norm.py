#!/usr/bin/env python3
"""
Build a ONE-TIME 5-year fiscal-year valuation NORM for the Semiconductors basket.

Goal: produce the historical FY2021..FY2025 norm of valuation multiples for
NVDA, AMD, AVGO, TSM, ASML, MU, QCOM, TXN, so the current snapshot (built
elsewhere) can be compared against this norm. This is NOT a point-in-time
walk: it deliberately uses the latest restated annual fact for each fiscal
year (the best available value for "what FY20xx actually was").

Sources:
- Fundamentals: SEC EDGAR XBRL companyconcept (annual facts only). Reuses the
  tag-fallback + annual-duration approach of fetch_anchor_fundamentals.py.
- Prices: Twelve Data time_series with adjust=none, i.e. the AS-REPORTED close
  on each fiscal-year-end date. adjust=none is required so the price is on the
  SAME split basis as the shares-outstanding count SEC reported at that date;
  otherwise a stock split (e.g. NVDA 10:1) would corrupt market_cap.

Fiscal year definition: a company's "FY20YY" is the annual period whose period
END falls in calendar year 20YY. NVDA's fiscal year ends in late January, so
NVDA FY2025 ends 2025-01-26; most others end 2025-12-31. This keeps the basket
comparable on a calendar-year-of-fiscal-end basis.

Currency: most filers report USD; TSM exposes USD units (used). ASML reports in
EUR. Price-based ratios for ASML mix a USD price with EUR fundamentals, so they
are emitted with a currency_warning and excluded from the basket average for
those metrics. Currency-neutral metrics (margins, growth) are always valid.

Multiples (per 02_MARKET_DASHBOARD.md):
  market_cap   = fy_end_close * shares_outstanding(at FY end, as reported)
  P/E          = market_cap / net_income
  P/S          = market_cap / revenue
  P/B          = market_cap / equity
  EV/EBITDA    = (market_cap + debt - cash) / (operating_income + D&A)
  FCF yield    = (op_cash_flow - capex) / market_cap
Currency-neutral: net_margin, gross_margin, revenue_growth_yoy, earnings_growth_yoy.

No API keys are written to the repo. Twelve Data key is read from .env.
SEC requires only a descriptive User-Agent. Free Twelve Data tier is rate
limited (8 calls/min); the script paces price calls accordingly.

Default output: data/market_quotes/fyn_semis_norm.csv (+ .json), one row per
company-FY plus aggregate basket rows (symbol=BASKET_AVG) carrying the
five_year_average per metric. With --current, writes fyn_<slug>_current.csv /
fyn_<slug>_current_summary.csv from the same basket and formulas, using the
latest available close and SEC facts filed on/before today. With
--current --as-of YYYY-MM-DD, the date is included in the output filenames and
all facts/prices are limited to that date. Missing values use status/comment,
never invented numbers.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, List, Optional, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"
OUT_DIR = PROJECT_ROOT / "data" / "market_quotes"
SEC_CACHE_DIR = OUT_DIR / ".sec_cache"
# These three are rebound in main() once the sector slug is known; defaults keep
# the module importable and match the original Semiconductors output names.
OUT_CSV = OUT_DIR / "fyn_semis_norm.csv"
OUT_SUMMARY_CSV = OUT_DIR / "fyn_semis_norm_summary.csv"
OUT_JSON = OUT_DIR / "fyn_semis_norm.json"

SEC_TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"
SEC_SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"
SEC_CONCEPT_URL = "https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/{taxonomy}/{tag}.json"
USER_AGENT = "Investment Library research nalbantovfml@gmail.com"
SEC_PAUSE = 0.25
SEC_CACHE_MAX_AGE = dt.timedelta(days=7)
SEC_CACHE_ENABLED = True
HTTP_ATTEMPTS = 4
HTTP_RETRY_DELAYS = (2, 4, 8)
NETWORK_EXCEPTIONS = (urllib.error.URLError, socket.gaierror, TimeoutError, ConnectionError)

TWELVE_BASE = "https://api.twelvedata.com/time_series"
# Free tier allows 8 requests/minute. Stay safely under it.
TWELVE_PAUSE = 8.0
FMP_STABLE_BASE = "https://financialmodelingprep.com/stable"
FMP_PAUSE = 0.25
NASDAQ_HISTORY_BASE = "https://api.nasdaq.com/api/quote"
NASDAQ_PAUSE = 1.0
NASDAQ_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 Chrome/124 Safari/537.36"
)
FMP_KEY_NAMES = (
    "FMP_API_KEY",
    "FINANCIAL_MODELING_PREP_API_KEY",
    "FINANCIALMODELINGPREP_API_KEY",
)

# Default basket (the semiconductor norm task). Overridable via --tickers.
SEMIS = ["NVDA", "AMD", "AVGO", "TSM", "ASML", "MU", "QCOM", "TXN"]

# Number of fiscal years in the rolling valuation norm.
FY_WINDOW = 5

# 10-K filing-lag cutoff month. A US annual report (10-K) for a fiscal year that
# ends ~Dec 31 is typically filed within 60-90 days, i.e. by late March (large
# accelerated filers must file within 60 days; the SEC absolute deadline is
# 90 days). So we treat "calendar year minus 1" as a fully-available FY only once
# we are PAST that filing window; before then the most recent fully-filed FY is
# "calendar year minus 2". Set to 4 (April) so the rolling window does not pull a
# fiscal year whose 10-K may not yet be on EDGAR for the whole basket.
FY_FILING_LAG_CUTOFF_MONTH = 4

# Safe default window for 2026 (the window the already-collected fyn_*_norm*
# files were built on). default_fy_years() must reproduce this for any as_of in
# calendar 2026; if the heuristic ever disagrees for 2026 it warns and falls back
# to this list rather than silently rebuilding the existing norms on a new window.
SAFE_2026_FY_YEARS = [2021, 2022, 2023, 2024, 2025]


def default_fy_years(
    as_of: Optional[dt.date] = None,
    window: int = FY_WINDOW,
) -> List[int]:
    """Last `window` COMPLETED fiscal years whose 10-Ks should be on SEC by as_of.

    Rolling-window heuristic (see FY_FILING_LAG_CUTOFF_MONTH):
      - A company's "FY20YY" is the annual period whose period END falls in
        calendar year 20YY (same convention as the rest of this module).
      - The 10-K for FY = (current calendar year - 1) is normally filed within
        60-90 days of fiscal-year end, i.e. by late March for Dec-fiscal filers.
        So once we are at/after FY_FILING_LAG_CUTOFF_MONTH (April), we treat
        (year - 1) as the most-recent fully-available FY; before April we use
        (year - 2), because the just-closed year's 10-K may not yet be filed
        across the whole basket.
      - The window is the `window` consecutive fiscal years ending at that most
        recent available FY.

    Worked examples:
      as_of 2026-06-07 -> month 6 >= 4 -> newest FY = 2025 -> [2021..2025]
      as_of 2027-01-15 -> month 1 <  4 -> newest FY = 2025 -> [2021..2025]
      as_of 2027-06-07 -> month 6 >= 4 -> newest FY = 2026 -> [2022..2026]

    No `as_of` means "today", which keeps the historical no-args behaviour of a
    last-5-fiscal-years norm.
    """
    if as_of is None:
        as_of = dt.date.today()
    newest_fy = as_of.year - 1 if as_of.month >= FY_FILING_LAG_CUTOFF_MONTH else as_of.year - 2
    years = list(range(newest_fy - window + 1, newest_fy + 1))

    # Guardrail: never silently rebuild the already-collected 2026 norms on a
    # different window. If the heuristic disagrees for a 2026 as_of, warn and use
    # the known-good SAFE_2026_FY_YEARS instead (documented in the module).
    if as_of.year == 2026 and window == FY_WINDOW and years != SAFE_2026_FY_YEARS:
        print(
            f"  WARNING: rolling window {years} for as_of {as_of.isoformat()} "
            f"differs from the collected 2026 norm window {SAFE_2026_FY_YEARS}; "
            f"using the safe 2026 default to avoid rebuilding existing norms."
        )
        return list(SAFE_2026_FY_YEARS)
    return years


# Module-level FY_YEARS: the rolling last-5-fiscal-years window for today. Kept
# as a module global (rebound in main()) so existing references continue to work.
# For any 2026 run this resolves to [2021..2025], matching the collected norms.
FY_YEARS = default_fy_years()
SECTOR_NAME = "Semiconductors"
SECTOR_SLUG = "semis"

# Built-in baskets so --sector alone is enough for known sectors.
SECTOR_BASKETS: Dict[str, List[str]] = {
    "Semiconductors": ["NVDA", "AMD", "AVGO", "TSM", "ASML", "MU", "QCOM", "TXN"],
}

# Tag candidates, tried in order. Mix of us-gaap (US filers + ASML) and
# ifrs-full (TSM). The first candidate that yields an annual value for a given
# fiscal year wins.
FLOW_TAGS: Dict[str, List[Tuple[str, str]]] = {
    "net_income": [
        ("us-gaap", "NetIncomeLoss"),
        ("ifrs-full", "ProfitLoss"),
        ("us-gaap", "ProfitLoss"),
    ],
    "revenue": [
        ("us-gaap", "RevenueFromContractWithCustomerExcludingAssessedTax"),
        ("us-gaap", "Revenues"),
        ("ifrs-full", "Revenue"),
        ("us-gaap", "RevenueFromContractWithCustomerIncludingAssessedTax"),
    ],
    "gross_profit": [
        ("us-gaap", "GrossProfit"),
        ("ifrs-full", "GrossProfit"),
    ],
    "operating_income": [
        ("us-gaap", "OperatingIncomeLoss"),
        ("ifrs-full", "ProfitLossFromOperatingActivities"),
    ],
    "dep_amort": [
        ("us-gaap", "DepreciationDepletionAndAmortization"),
        ("us-gaap", "DepreciationAmortizationAndAccretionNet"),
        ("us-gaap", "DepreciationAndAmortization"),
        ("ifrs-full", "DepreciationAndAmortisationExpense"),
    ],
    "op_cash_flow": [
        ("us-gaap", "NetCashProvidedByUsedInOperatingActivities"),
        ("us-gaap", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"),
        ("ifrs-full", "CashFlowsFromUsedInOperatingActivities"),
    ],
    "capex": [
        ("us-gaap", "PaymentsToAcquirePropertyPlantAndEquipment"),
        ("us-gaap", "PaymentsToAcquireProductiveAssets"),
        ("ifrs-full", "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"),
    ],
}

INSTANT_TAGS: Dict[str, List[Tuple[str, str]]] = {
    "equity": [
        ("us-gaap", "StockholdersEquity"),
        ("ifrs-full", "EquityAttributableToOwnersOfParent"),
        ("ifrs-full", "Equity"),
        ("us-gaap", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"),
    ],
    "debt": [
        ("us-gaap", "LongTermDebtAndCapitalLeaseObligations"),
        ("us-gaap", "LongTermDebt"),
        ("us-gaap", "DebtLongtermAndShorttermCombinedAmount"),
    ],
    "cash": [
        ("us-gaap", "CashAndCashEquivalentsAtCarryingValue"),
        ("ifrs-full", "CashAndCashEquivalents"),
        ("us-gaap", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"),
    ],
}

SHARE_TAGS: List[Tuple[str, str, str]] = [
    ("dei", "EntityCommonStockSharesOutstanding", "instant"),
    ("us-gaap", "CommonStockSharesOutstanding", "instant"),
    ("ifrs-full", "NumberOfSharesOutstanding", "instant"),
    ("us-gaap", "WeightedAverageNumberOfDilutedSharesOutstanding", "annual"),
]

CURRENT_SHARE_TAGS: List[Tuple[str, str]] = [
    ("dei", "EntityCommonStockSharesOutstanding"),
    ("us-gaap", "CommonStockSharesOutstanding"),
    ("us-gaap", "WeightedAverageNumberOfDilutedSharesOutstanding"),
    ("us-gaap", "WeightedAverageNumberOfSharesOutstandingBasic"),
]

SHARE_LOOKBACK_DAYS = 14
SHARE_FILING_LAG_DAYS = 120

# Preferred reporting currency per ticker (units key in companyconcept).
PREFERRED_CCY = {"TSM": "USD"}  # ASML -> EUR (only option); rest -> USD


def http_json(url: str, headers: Optional[Dict[str, str]] = None) -> Any:
    for attempt in range(1, HTTP_ATTEMPTS + 1):
        req = urllib.request.Request(url, headers=headers or {"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError:
            raise
        except NETWORK_EXCEPTIONS as exc:
            if attempt == HTTP_ATTEMPTS:
                raise
            delay = HTTP_RETRY_DELAYS[attempt - 1]
            print(
                f"    network error {type(exc).__name__} on attempt "
                f"{attempt}/{HTTP_ATTEMPTS}; retrying in {delay}s: {exc}"
            )
            time.sleep(delay)


def read_twelve_key() -> Optional[str]:
    if not ENV_PATH.exists():
        return None
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("TWELVE_DATA_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def read_fmp_key() -> Optional[str]:
    for name in FMP_KEY_NAMES:
        value = os.environ.get(name)
        if value:
            return value
    for env_path in (ENV_PATH, Path.home() / "Desktop" / ".env"):
        if not env_path.exists():
            continue
        for line in env_path.read_text(encoding="utf-8", errors="ignore").splitlines():
            for name in FMP_KEY_NAMES:
                if line.startswith(f"{name}="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    legacy_path = Path.home() / "Desktop" / "Project — копия" / "leftbar" / "marketdata.py"
    if legacy_path.exists():
        match = re.search(
            r"^Api\s*=\s*['\"]([^'\"]+)['\"]",
            legacy_path.read_text(encoding="utf-8", errors="ignore"),
            re.MULTILINE,
        )
        if match:
            return match.group(1)
    return None


def load_ticker_cik_map() -> Dict[str, int]:
    data = http_json(SEC_TICKER_MAP_URL)
    time.sleep(SEC_PAUSE)
    return {row["ticker"].upper(): int(row["cik_str"]) for row in data.values()}


def fetch_submission_metadata(cik: int) -> Dict[str, Any]:
    data = http_json(SEC_SUBMISSIONS_URL.format(cik=cik))
    time.sleep(SEC_PAUSE)
    return data


def sec_concept_cache_path(cik: int, taxonomy: str, tag: str) -> Path:
    return SEC_CACHE_DIR / f"CIK{cik:010d}_{taxonomy}_{tag}.json"


def read_sec_concept_cache(
    path: Path,
) -> Tuple[bool, Optional[Dict[str, List[Dict[str, Any]]]]]:
    try:
        age = time.time() - path.stat().st_mtime
    except OSError:
        return False, None
    if age >= SEC_CACHE_MAX_AGE.total_seconds():
        return False, None

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False, None
    if not isinstance(data, dict):
        return False, None
    if data.get("_sec_cache_status") == 404:
        return True, None
    units = data.get("units", {})
    return True, units or None


def write_sec_concept_cache(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temp_path.write_text(
            json.dumps(data, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )
        os.replace(temp_path, path)
    finally:
        try:
            temp_path.unlink()
        except FileNotFoundError:
            pass


def fetch_concept_units(cik: int, taxonomy: str, tag: str) -> Optional[Dict[str, List[Dict[str, Any]]]]:
    """Return raw concept units; point-in-time filtering remains in callers."""
    cache_path = sec_concept_cache_path(cik, taxonomy, tag)
    if SEC_CACHE_ENABLED:
        cache_hit, units = read_sec_concept_cache(cache_path)
        if cache_hit:
            return units

    url = SEC_CONCEPT_URL.format(cik=cik, taxonomy=taxonomy, tag=tag)
    try:
        data = http_json(url)
    except urllib.error.HTTPError as error:
        time.sleep(SEC_PAUSE)
        if error.code == 404:
            if SEC_CACHE_ENABLED:
                write_sec_concept_cache(
                    cache_path,
                    {"_sec_cache_status": 404, "url": url},
                )
            return None
        raise
    time.sleep(SEC_PAUSE)
    if SEC_CACHE_ENABLED:
        write_sec_concept_cache(cache_path, data)
    return data.get("units", {}) or None


def pick_unit_points(units: Dict[str, List[Dict[str, Any]]], symbol: str) -> Tuple[Optional[str], List[Dict[str, Any]]]:
    """Choose the currency/unit series. Honour PREFERRED_CCY, else USD, else first."""
    if not units:
        return None, []
    pref = PREFERRED_CCY.get(symbol)
    if pref and pref in units:
        return pref, units[pref]
    if "USD" in units:
        return "USD", units["USD"]
    if "shares" in units:
        return "shares", units["shares"]
    key = next(iter(units))
    return key, units[key]


def duration_days(point: Dict[str, Any]) -> Optional[int]:
    start, end = point.get("start"), point.get("end")
    if not start or not end:
        return None
    return (dt.date.fromisoformat(end) - dt.date.fromisoformat(start)).days


def is_annual(point: Dict[str, Any]) -> bool:
    days = duration_days(point)
    return days is not None and 350 <= days <= 380


def annual_by_end_year(points: List[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    """Latest-filed annual fact keyed by the calendar year of its period END."""
    chosen: Dict[str, Dict[str, Any]] = {}
    for point in points:
        if point.get("val") is None or not point.get("end"):
            continue
        if not is_annual(point):
            continue
        end = point["end"]
        prev = chosen.get(end)
        if prev is None or point["filed"] > prev["filed"]:
            chosen[end] = point
    by_year: Dict[int, Dict[str, Any]] = {}
    for end, point in chosen.items():
        year = dt.date.fromisoformat(end).year
        # If two fiscal periods end in the same calendar year (rare), keep the later end.
        if year not in by_year or end > by_year[year]["end"]:
            by_year[year] = point
    return by_year


def instant_by_end_year(
    points: List[Dict[str, Any]],
    fy_end_by_year: Dict[int, str],
    tolerance: int = 14,
) -> Dict[int, Dict[str, Any]]:
    """For each FY, the balance-sheet value nearest the FY-end date within `tolerance` days.

    Most balance-sheet instants (equity, debt, cash) are dated exactly to the
    fiscal-year end, so the default 14-day window is plenty. The dei share count
    is the exception: it is reported on the 10-K *cover* date, which lands a few
    weeks AFTER the fiscal-year end (e.g. NVDA FY2025 ends 2025-01-26 but the
    cover-page count is dated 2025-02-21). Callers pass a wider tolerance for
    shares so that cover-date count is captured.
    """
    chosen: Dict[str, Dict[str, Any]] = {}
    for point in points:
        if point.get("val") is None or not point.get("end") or point.get("start"):
            continue  # instants have no start
        end = point["end"]
        prev = chosen.get(end)
        if prev is None or point["filed"] > prev["filed"]:
            chosen[end] = point
    result: Dict[int, Dict[str, Any]] = {}
    for year, fy_end in fy_end_by_year.items():
        target = dt.date.fromisoformat(fy_end)
        best = None
        best_gap = tolerance + 1
        for end, point in chosen.items():
            gap = abs((dt.date.fromisoformat(end) - target).days)
            # On a tie, prefer the value dated on/after fy_end (the cover-page count
            # that reflects the just-closed fiscal year, not a stale prior quarter).
            if gap < best_gap or (
                gap == best_gap and best is not None
                and dt.date.fromisoformat(end) >= target
                and dt.date.fromisoformat(best["end"]) < target
            ):
                best_gap = gap
                best = point
        if best is not None:
            result[year] = best
    return result


def fetch_series(symbol: str, cik: int, candidates: List[Tuple[str, str]]) -> Tuple[Optional[str], List[Dict[str, Any]]]:
    """Return (currency, merged points) across all candidate tags sharing a currency.

    Filers migrate between XBRL tags over time. NVDA, for example, reported
    revenue under RevenueFromContractWithCustomerExcludingAssessedTax through
    ~FY2023 and under Revenues thereafter; picking only the first non-empty tag
    would silently drop the newer years. Instead we take the currency of the
    first candidate that has data, then merge every candidate that reports in
    that same currency, keeping the most-recently-filed point per period end.
    This fills tag-migration gaps without mixing currencies.
    """
    chosen_ccy: Optional[str] = None
    merged: Dict[str, Dict[str, Any]] = {}  # keyed by (end, start) so annual vs instant don't collide
    for taxonomy, tag in candidates:
        units = fetch_concept_units(cik, taxonomy, tag)
        if not units:
            continue
        ccy, points = pick_unit_points(units, symbol)
        if not points:
            continue
        if chosen_ccy is None:
            chosen_ccy = ccy
        elif ccy != chosen_ccy:
            continue  # don't mix currencies across migrated tags
        for p in points:
            if p.get("val") is None or not p.get("end"):
                continue
            pkey = f"{p.get('start', '')}|{p['end']}"
            prev = merged.get(pkey)
            if prev is None or p.get("filed", "") > prev.get("filed", ""):
                merged[pkey] = p
    if chosen_ccy is None:
        return None, []
    return chosen_ccy, list(merged.values())


def point_filed_on_or_before(point: Dict[str, Any], as_of: dt.date) -> bool:
    filed = point.get("filed")
    if not filed:
        return False
    try:
        return dt.date.fromisoformat(filed) <= as_of
    except ValueError:
        return False


def point_end_on_or_before(point: Dict[str, Any], as_of: dt.date) -> bool:
    end = point.get("end")
    if not end:
        return False
    try:
        return dt.date.fromisoformat(end) <= as_of
    except ValueError:
        return False


def fetch_series_asof(
    symbol: str,
    cik: int,
    candidates: List[Tuple[str, str]],
    as_of: dt.date,
) -> Tuple[Optional[str], List[Dict[str, Any]]]:
    """Return (currency, merged points), keeping only facts filed by as_of."""
    chosen_ccy: Optional[str] = None
    merged: Dict[str, Dict[str, Any]] = {}
    for taxonomy, tag in candidates:
        units = fetch_concept_units(cik, taxonomy, tag)
        if not units:
            continue
        ccy, points = pick_unit_points(units, symbol)
        if not points:
            continue
        if chosen_ccy is None:
            chosen_ccy = ccy
        elif ccy != chosen_ccy:
            continue
        for p in points:
            if p.get("val") is None or not p.get("end"):
                continue
            if not point_filed_on_or_before(p, as_of) or not point_end_on_or_before(p, as_of):
                continue
            pkey = f"{p.get('start', '')}|{p['end']}"
            prev = merged.get(pkey)
            if prev is None or p.get("filed", "") > prev.get("filed", ""):
                merged[pkey] = p
    if chosen_ccy is None:
        return None, []
    return chosen_ccy, list(merged.values())


def share_point_near_fy_end(
    points: List[Dict[str, Any]],
    fy_end: str,
    point_kind: str,
) -> Optional[Dict[str, Any]]:
    """Closest originally reported share fact around one fiscal-year end."""
    target = dt.date.fromisoformat(fy_end)
    original_by_end: Dict[str, Dict[str, Any]] = {}
    for point in points:
        if point.get("val") is None or not point.get("end"):
            continue
        if point_kind == "instant":
            if point.get("start"):
                continue
        elif point_kind == "annual":
            if not is_annual(point):
                continue
        else:
            raise ValueError(f"unsupported share point kind: {point_kind}")

        end_date = dt.date.fromisoformat(point["end"])
        gap = (end_date - target).days
        if gap < -SHARE_LOOKBACK_DAYS or gap > SHARE_FILING_LAG_DAYS:
            continue

        prev = original_by_end.get(point["end"])
        point_filed = str(point.get("filed") or "9999-12-31")
        prev_filed = str(prev.get("filed") or "9999-12-31") if prev else ""
        if prev is None or point_filed < prev_filed:
            original_by_end[point["end"]] = point

    if not original_by_end:
        return None

    def sort_key(point: Dict[str, Any]) -> Tuple[int, int, str]:
        gap = (dt.date.fromisoformat(point["end"]) - target).days
        return (
            abs(gap),
            0 if gap >= 0 else 1,
            str(point.get("filed") or "9999-12-31"),
        )

    return min(original_by_end.values(), key=sort_key)


def fetch_shares_by_year(
    symbol: str,
    cik: int,
    fy_end_by_year: Dict[int, str],
) -> Dict[int, Dict[str, Any]]:
    """Select FY shares per year, using ordered tag fallbacks.

    Cover-page share facts can be dated as of the 10-K filing rather than the
    fiscal-year end, so instant facts may land up to 120 days after FY-end.
    The final US-GAAP fallback is annual diluted weighted-average shares, whose
    period end normally matches FY-end exactly and is appropriate for annual P/E.

    The earliest-filed fact per period end is retained to stay split-consistent
    with the unadjusted FY-end price.
    """
    result: Dict[int, Dict[str, Any]] = {}
    for taxonomy, tag, point_kind in SHARE_TAGS:
        units = fetch_concept_units(cik, taxonomy, tag)
        if not units:
            continue
        _unit, points = pick_unit_points(units, symbol)
        if not points:
            continue
        for year, fy_end in fy_end_by_year.items():
            if year in result:
                continue
            point = share_point_near_fy_end(points, fy_end, point_kind)
            if point is not None:
                result[year] = point
        if len(result) == len(fy_end_by_year):
            break
    return result


def fetch_fy_close(symbol: str, fy_end: str, key: str) -> Tuple[Optional[float], Optional[str], str]:
    """As-reported (adjust=none) close on/just-before the FY-end date.

    Returns (close, actual_date, note). Looks back up to ~6 days to land on the
    last trading day on/before the fiscal-year end.
    """
    end = dt.date.fromisoformat(fy_end)
    start = end - dt.timedelta(days=8)
    params = {
        "symbol": symbol,
        "interval": "1day",
        "start_date": start.isoformat(),
        "end_date": fy_end,
        "apikey": key,
        "format": "JSON",
        "adjust": "none",
    }
    url = TWELVE_BASE + "?" + urllib.parse.urlencode(params)
    try:
        data = http_json(url, headers={"User-Agent": USER_AGENT})
    except Exception as exc:  # network/HTTP error
        return None, None, f"twelvedata error: {exc}"
    if data.get("status") == "error":
        return None, None, f"twelvedata: {data.get('message')}"
    values = data.get("values") or []
    if not values:
        return None, None, "twelvedata: no values in window"
    # values are newest-first; pick the latest datetime <= fy_end
    for v in values:
        if v["datetime"] <= fy_end:
            try:
                return float(v["close"]), v["datetime"], ""
            except (ValueError, KeyError):
                return None, None, "twelvedata: unparseable close"
    return None, None, "twelvedata: no trading day on/before FY end"


def fetch_latest_close(symbol: str, as_of: dt.date, key: str) -> Tuple[Optional[float], Optional[str], str]:
    """Latest as-reported daily close on/before as_of."""
    start = as_of - dt.timedelta(days=10)
    params = {
        "symbol": symbol,
        "interval": "1day",
        "start_date": start.isoformat(),
        "end_date": as_of.isoformat(),
        "apikey": key,
        "format": "JSON",
        "adjust": "none",
    }
    url = TWELVE_BASE + "?" + urllib.parse.urlencode(params)
    try:
        data = http_json(url, headers={"User-Agent": USER_AGENT})
    except Exception as exc:
        return None, None, f"twelvedata error: {exc}"
    if data.get("status") == "error":
        return None, None, f"twelvedata: {data.get('message')}"
    values = data.get("values") or []
    if not values:
        return None, None, "twelvedata: no values in latest window"
    for v in values:
        try:
            value_date = dt.date.fromisoformat(v["datetime"])
        except (ValueError, KeyError):
            continue
        if value_date <= as_of:
            try:
                return float(v["close"]), v["datetime"], ""
            except (ValueError, KeyError):
                return None, None, "twelvedata: unparseable close"
    return None, None, "twelvedata: no trading day on/before as-of date"


def fetch_latest_fmp_close(
    symbol: str,
    as_of: dt.date,
    key: str,
) -> Tuple[Optional[float], Optional[str], str]:
    """Latest unadjusted FMP EOD close on/before as_of."""
    params = {
        "symbol": symbol,
        "from": (as_of - dt.timedelta(days=10)).isoformat(),
        "to": as_of.isoformat(),
        "apikey": key,
    }
    url = (
        f"{FMP_STABLE_BASE}/historical-price-eod/full?"
        + urllib.parse.urlencode(params)
    )
    try:
        data = http_json(url, headers={"User-Agent": USER_AGENT})
    except Exception as exc:
        return None, None, f"fmp error: {exc}"
    if isinstance(data, dict):
        return None, None, f"fmp: {data.get('Error Message') or data}"
    if not isinstance(data, list):
        return None, None, "fmp: unexpected response format"
    for item in sorted(data, key=lambda row: row.get("date", ""), reverse=True):
        date_value = item.get("date")
        if not date_value or date_value > as_of.isoformat():
            continue
        try:
            return float(item["close"]), date_value, ""
        except (KeyError, TypeError, ValueError):
            return None, None, "fmp: unparseable close"
    return None, None, "fmp: no trading day on/before as-of date"


def fetch_latest_nasdaq_close(
    symbol: str,
    as_of: dt.date,
) -> Tuple[Optional[float], Optional[str], str]:
    """Latest Nasdaq historical API close on/before as_of."""
    params = {
        "assetclass": "stocks",
        "fromdate": (as_of - dt.timedelta(days=10)).isoformat(),
        # Nasdaq returns rows newest-first through today, even when fromdate is
        # historical. Request enough rows for the as-of window, then enforce
        # the point-in-time cutoff below.
        "limit": 5000,
    }
    url = (
        f"{NASDAQ_HISTORY_BASE}/{urllib.parse.quote(symbol)}/historical?"
        + urllib.parse.urlencode(params)
    )
    headers = {
        "User-Agent": NASDAQ_USER_AGENT,
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.nasdaq.com/",
    }
    try:
        data = http_json(url, headers=headers)
    except Exception as exc:
        return None, None, f"nasdaq error: {exc}"
    rows = (
        ((data.get("data") or {}).get("tradesTable") or {}).get("rows")
        if isinstance(data, dict)
        else None
    )
    if not rows:
        return None, None, f"nasdaq: no historical rows ({data.get('status') if isinstance(data, dict) else data})"
    parsed: List[Tuple[dt.date, Dict[str, Any]]] = []
    for item in rows:
        try:
            item_date = dt.datetime.strptime(item["date"], "%m/%d/%Y").date()
        except (KeyError, TypeError, ValueError):
            continue
        if item_date <= as_of:
            parsed.append((item_date, item))
    if not parsed:
        return None, None, "nasdaq: no trading day on/before as-of date"
    item_date, item = max(parsed, key=lambda pair: pair[0])
    try:
        close = float(str(item["close"]).replace("$", "").replace(",", ""))
    except (KeyError, TypeError, ValueError):
        return None, None, "nasdaq: unparseable close"
    return close, item_date.isoformat(), ""


def latest_instant_point(
    points: List[Dict[str, Any]],
    as_of: dt.date,
    max_age_days: int = 550,
) -> Optional[Dict[str, Any]]:
    """Latest instant fact filed by as_of; stale values are treated as missing."""
    best: Optional[Dict[str, Any]] = None
    for point in points:
        if point.get("val") is None or not point.get("end") or point.get("start"):
            continue
        if not point_filed_on_or_before(point, as_of) or not point_end_on_or_before(point, as_of):
            continue
        end_date = dt.date.fromisoformat(point["end"])
        if (as_of - end_date).days > max_age_days:
            continue
        if best is None:
            best = point
            continue
        best_end = dt.date.fromisoformat(best["end"])
        if end_date > best_end or (end_date == best_end and point.get("filed", "") > best.get("filed", "")):
            best = point
    return best


def latest_current_shares_point(
    points: List[Dict[str, Any]],
    as_of: dt.date,
) -> Optional[Dict[str, Any]]:
    """Latest shares fact known by as_of, with no age limit.

    Current snapshots may need an older cover-page instant or a duration-based
    weighted-average fallback. Both the filing and fact end must not be in the
    future. Within one preferred tag, the latest filing/end pair wins.
    """
    candidates = [
        point
        for point in points
        if point.get("val") is not None
        and point.get("end")
        and point_filed_on_or_before(point, as_of)
        and point_end_on_or_before(point, as_of)
    ]
    if not candidates:
        return None
    return max(
        candidates,
        key=lambda point: (str(point.get("filed") or ""), str(point["end"])),
    )


def fetch_current_shares_point(
    symbol: str,
    cik: int,
    as_of: dt.date,
) -> Tuple[Optional[str], Optional[Dict[str, Any]], str]:
    """Latest current shares fact, using tag order to break freshness ties."""
    unavailable_tags: List[str] = []
    candidates: List[Tuple[str, str, Dict[str, Any], int]] = []
    for priority, (taxonomy, tag) in enumerate(CURRENT_SHARE_TAGS):
        units = fetch_concept_units(cik, taxonomy, tag)
        if not units:
            unavailable_tags.append(f"{taxonomy}:{tag} unavailable")
            continue
        ccy, points = pick_unit_points(units, symbol)
        if not points:
            unavailable_tags.append(f"{taxonomy}:{tag} has no shares unit")
            continue
        point = latest_current_shares_point(points, as_of)
        if point is not None:
            candidates.append((ccy or "", f"{taxonomy}:{tag}", point, priority))
            continue
        unavailable_tags.append(f"{taxonomy}:{tag} has no fact filed/end<=as_of")
    if candidates:
        ccy, source, point, _priority = max(
            candidates,
            key=lambda item: (
                str(item[2].get("filed") or ""),
                str(item[2]["end"]),
                -item[3],
            ),
        )
        return ccy or None, point, source
    return (
        None,
        None,
        "no shares fact filed/end<=as_of across current fallbacks"
        + (f" ({'; '.join(unavailable_tags)})" if unavailable_tags else ""),
    )


def make_quarter(
    value: float,
    start: dt.date,
    end: dt.date,
    filed: str,
    source: str,
) -> Dict[str, Any]:
    return {
        "val": value,
        "start": start.isoformat(),
        "end": end.isoformat(),
        "filed": filed,
        "source": source,
    }


def add_quarter(quarters: Dict[str, Dict[str, Any]], quarter: Dict[str, Any]) -> None:
    """Keep one quarter per end date, preferring direct facts over derived ones."""
    end = quarter["end"]
    prev = quarters.get(end)
    if prev is None:
        quarters[end] = quarter
        return
    prev_direct = str(prev.get("source", "")).startswith("direct")
    new_direct = str(quarter.get("source", "")).startswith("direct")
    if new_direct and not prev_direct:
        quarters[end] = quarter
    elif new_direct == prev_direct and quarter.get("filed", "") > prev.get("filed", ""):
        quarters[end] = quarter


def build_quarter_facts(points: List[Dict[str, Any]], as_of: dt.date) -> List[Dict[str, Any]]:
    """Build discrete quarter facts from direct quarterly facts and YTD deltas."""
    quarters: Dict[str, Dict[str, Any]] = {}
    ytd_by_start: Dict[str, Dict[str, Dict[str, Any]]] = {}

    for point in points:
        if point.get("val") is None or not point.get("start") or not point.get("end"):
            continue
        if not point_filed_on_or_before(point, as_of) or not point_end_on_or_before(point, as_of):
            continue
        days = duration_days(point)
        if days is None or days < 60 or days > 390:
            continue
        start = dt.date.fromisoformat(point["start"])
        end = dt.date.fromisoformat(point["end"])
        value = float(point["val"])
        filed = point.get("filed", "")

        if 60 <= days <= 120:
            add_quarter(quarters, make_quarter(value, start, end, filed, "direct_quarter"))

        # Same fiscal-year start periods let us derive Q2/Q3/Q4 by differencing.
        per_start = ytd_by_start.setdefault(point["start"], {})
        prev = per_start.get(point["end"])
        if prev is None or filed > prev.get("filed", ""):
            per_start[point["end"]] = point

    for start_text, by_end in ytd_by_start.items():
        sorted_points = sorted(by_end.values(), key=lambda p: p["end"])
        prev_ytd: Optional[Dict[str, Any]] = None
        for point in sorted_points:
            days = duration_days(point)
            if days is None:
                continue
            end = dt.date.fromisoformat(point["end"])
            filed = point.get("filed", "")
            current_value = float(point["val"])
            if prev_ytd is None:
                if 60 <= days <= 120:
                    start = dt.date.fromisoformat(point["start"])
                    add_quarter(quarters, make_quarter(current_value, start, end, filed, "derived_q1_ytd"))
                prev_ytd = point
                continue
            prev_end = dt.date.fromisoformat(prev_ytd["end"])
            gap_days = (end - prev_end).days
            if 70 <= gap_days <= 120:
                quarter_start = prev_end + dt.timedelta(days=1)
                quarter_value = current_value - float(prev_ytd["val"])
                add_quarter(
                    quarters,
                    make_quarter(quarter_value, quarter_start, end, filed, f"derived_ytd_delta_from_{start_text}"),
                )
            prev_ytd = point

    return sorted(quarters.values(), key=lambda q: q["end"], reverse=True)


def ttm_from_points(
    points: List[Dict[str, Any]],
    as_of: dt.date,
) -> Tuple[Optional[float], Optional[str], int, str, Optional[float]]:
    """Return current TTM, TTM end, quarter count, note, and prior TTM if available."""
    quarters = build_quarter_facts(points, as_of)
    if not quarters:
        return None, None, 0, "no quarterly/YTD facts filed<=as_of", None

    selected: List[Dict[str, Any]] = []
    for quarter in quarters:
        end_date = dt.date.fromisoformat(quarter["end"])
        if selected:
            previous_start = dt.date.fromisoformat(selected[-1]["start"])
            if end_date >= previous_start:
                continue
        selected.append(quarter)
        if len(selected) == 8:
            break

    if len(selected) < 4:
        return None, selected[0]["end"] if selected else None, len(selected), "fewer than four non-overlapping quarters", None
    latest_end = dt.date.fromisoformat(selected[0]["end"])
    if (as_of - latest_end).days > 420:
        return None, selected[0]["end"], len(selected), "latest TTM quarter is stale", None

    current_quarters = selected[:4]
    current_ttm = sum(float(q["val"]) for q in current_quarters)
    prior_ttm = None
    if len(selected) >= 8:
        prior_ttm = sum(float(q["val"]) for q in selected[4:8])
    note = "quarters=" + ",".join(q["end"] for q in reversed(current_quarters))
    return current_ttm, current_quarters[0]["end"], len(current_quarters), note, prior_ttm


def safe_div(num: Optional[float], den: Optional[float]) -> Optional[float]:
    if num is None or den in (None, 0):
        return None
    return num / den


def rnd(value: Optional[float], digits: int) -> Any:
    return round(value, digits) if value is not None else ""


FIELDNAMES = [
    "symbol", "cik", "fiscal_year", "fy_end", "currency",
    "fy_end_close", "close_date", "shares_outstanding", "shares_asof",
    "net_income", "revenue", "gross_profit", "operating_income", "dep_amort",
    "op_cash_flow", "capex", "equity", "debt", "cash",
    "market_cap", "enterprise_value", "ebitda", "fcf",
    "pe", "ps", "pb", "ev_ebitda", "fcf_yield",
    "net_margin", "gross_margin", "revenue_growth_yoy", "earnings_growth_yoy",
    "price_source", "fundamental_source", "status", "comment",
]


def missing_company_rows(symbol: str, cik: Optional[int], comment: str) -> List[Dict[str, Any]]:
    cik_value = f"{cik:010d}" if cik is not None else ""
    return [
        {
            **{f: "" for f in FIELDNAMES},
            "symbol": symbol,
            "cik": cik_value,
            "fiscal_year": year,
            "fundamental_source": "SEC EDGAR XBRL companyconcept",
            "price_source": "missing",
            "status": "missing",
            "comment": comment,
        }
        for year in FY_YEARS
    ]


# Metrics aggregated into the basket five_year_average/current summary.
PRICE_METRICS = ["pe", "ps", "pb", "ev_ebitda", "fcf_yield"]
NEUTRAL_METRICS = ["net_margin", "gross_margin", "revenue_growth_yoy", "earnings_growth_yoy"]

# Foreign 20-F/IFRS filers can report ADR/foreign-share counts that corrupt
# market-cap-based ratios. Until those share ratios are normalized, exclude
# known affected names from PRICE metrics. Their currency-neutral metrics
# (margins, growth) stay valid and are kept.
BASE_PRICE_RATIO_EXCLUDE = frozenset({"TSM", "ASML", "GOLD"})
PRICE_RATIO_EXCLUDE = set(BASE_PRICE_RATIO_EXCLUDE)


def excluded_price_tickers(rows: List[Dict[str, Any]]) -> str:
    """Comma-separated configured exclusions that are present in these rows."""
    symbols = {str(row.get("symbol", "")).upper() for row in rows}
    excluded = sorted(symbols & PRICE_RATIO_EXCLUDE)
    return ", ".join(excluded) if excluded else "none"


def build_company(symbol: str, cik: int, key: Optional[str]) -> List[Dict[str, Any]]:
    print(f"  {symbol}: CIK{cik:010d} fetching SEC annual facts ...")
    flows = {name: fetch_series(symbol, cik, cands) for name, cands in FLOW_TAGS.items()}
    instants = {name: fetch_series(symbol, cik, cands)
                for name, cands in INSTANT_TAGS.items() if name != "shares"}

    ni_ccy, ni_pts = flows["net_income"]
    ni_by_year = annual_by_end_year(ni_pts)
    rev_ccy, rev_pts = flows["revenue"]
    rev_by_year = annual_by_end_year(rev_pts)
    gp_by_year = annual_by_end_year(flows["gross_profit"][1])
    oi_by_year = annual_by_end_year(flows["operating_income"][1])
    da_by_year = annual_by_end_year(flows["dep_amort"][1])
    ocf_by_year = annual_by_end_year(flows["op_cash_flow"][1])
    capex_by_year = annual_by_end_year(flows["capex"][1])

    # Determine the FY-end date for each fiscal year from net_income (most reliable annual flow).
    fy_end_by_year: Dict[int, str] = {y: ni_by_year[y]["end"] for y in ni_by_year}
    # Fill any gaps from revenue annuals.
    for y, p in rev_by_year.items():
        fy_end_by_year.setdefault(y, p["end"])

    eq_ccy, eq_pts = instants["equity"]
    equity_by_year = instant_by_end_year(eq_pts, fy_end_by_year)
    debt_by_year = instant_by_end_year(instants["debt"][1], fy_end_by_year)
    cash_by_year = instant_by_end_year(instants["cash"][1], fy_end_by_year)
    shares_by_year = fetch_shares_by_year(symbol, cik, fy_end_by_year)

    fundamental_ccy = ni_ccy or rev_ccy or "USD"
    rows: List[Dict[str, Any]] = []

    for year in FY_YEARS:
        fy_end = fy_end_by_year.get(year)
        notes: List[str] = []
        if fy_end is None:
            rows.append({
                "symbol": symbol, "cik": f"{cik:010d}", "fiscal_year": year,
                "fy_end": "", "currency": fundamental_ccy, "fy_end_close": "",
                "close_date": "", "shares_outstanding": "", "shares_asof": "",
                "net_income": "", "revenue": "", "gross_profit": "", "operating_income": "",
                "dep_amort": "", "op_cash_flow": "", "capex": "", "equity": "", "debt": "", "cash": "",
                "market_cap": "", "enterprise_value": "", "ebitda": "", "fcf": "",
                "pe": "", "ps": "", "pb": "", "ev_ebitda": "", "fcf_yield": "",
                "net_margin": "", "gross_margin": "", "revenue_growth_yoy": "", "earnings_growth_yoy": "",
                "price_source": "", "fundamental_source": "SEC EDGAR XBRL companyconcept",
                "status": "missing", "comment": "no annual filing for this fiscal year (not yet filed?)",
            })
            continue

        ni = ni_by_year.get(year, {}).get("val")
        rev = rev_by_year.get(year, {}).get("val")
        gp = gp_by_year.get(year, {}).get("val")
        oi = oi_by_year.get(year, {}).get("val")
        da = da_by_year.get(year, {}).get("val")
        ocf = ocf_by_year.get(year, {}).get("val")
        capex = capex_by_year.get(year, {}).get("val")
        equity = equity_by_year.get(year, {}).get("val")
        debt = debt_by_year.get(year, {}).get("val")
        cash = cash_by_year.get(year, {}).get("val")
        shares = shares_by_year.get(year, {}).get("val")
        shares_asof = shares_by_year.get(year, {}).get("end", "")

        # Price (as-reported close) on the FY-end date.
        close, close_date, price_note = (None, None, "no twelvedata key")
        price_source = "missing"
        if key:
            close, close_date, price_note = fetch_fy_close(symbol, fy_end, key)
            time.sleep(TWELVE_PAUSE)
            price_source = "Twelve Data time_series adjust=none" if close is not None else "missing"
        if price_note:
            notes.append(price_note)

        # Currency consistency for price-based ratios: price is USD.
        price_ccy_ok = fundamental_ccy == "USD"
        if not price_ccy_ok:
            notes.append(f"price-based ratios suppressed: fundamentals in {fundamental_ccy}, price in USD (FX not applied)")

        market_cap = (close * shares) if (close is not None and shares) else None
        ebitda = (oi + da) if (oi is not None and da is not None) else None
        ev = (market_cap + (debt or 0) - (cash or 0)) if market_cap is not None else None
        fcf = (ocf - capex) if (ocf is not None and capex is not None) else None

        # Only compute price ratios when currency is consistent.
        pe = safe_div(market_cap, ni) if price_ccy_ok else None
        ps = safe_div(market_cap, rev) if price_ccy_ok else None
        pb = safe_div(market_cap, equity) if price_ccy_ok else None
        ev_ebitda = safe_div(ev, ebitda) if price_ccy_ok else None
        fcf_yield = safe_div(fcf, market_cap) if price_ccy_ok else None

        net_margin = safe_div(ni, rev)
        gross_margin = safe_div(gp, rev)
        rev_prior = rev_by_year.get(year - 1, {}).get("val")
        ni_prior = ni_by_year.get(year - 1, {}).get("val")
        rev_growth = (rev / rev_prior - 1) if (rev is not None and rev_prior) else None
        earn_growth = (ni / ni_prior - 1) if (ni is not None and ni_prior) else None

        have_price_ratio = any(x is not None for x in (pe, ps, pb))
        if have_price_ratio:
            status = "ok"
        elif net_margin is not None or gross_margin is not None:
            status = "partial"
        else:
            status = "missing"

        if shares is None:
            notes.append("no shares outstanding at FY end")
        if ni is None:
            notes.append("no annual net income")
        if rev is None:
            notes.append("no annual revenue")
        if pe is not None and pe < 0:
            notes.append("negative P/E (loss-making FY)")

        rows.append({
            "symbol": symbol, "cik": f"{cik:010d}", "fiscal_year": year,
            "fy_end": fy_end, "currency": fundamental_ccy,
            "fy_end_close": rnd(close, 4), "close_date": close_date or "",
            "shares_outstanding": shares if shares is not None else "",
            "shares_asof": shares_asof,
            "net_income": ni if ni is not None else "",
            "revenue": rev if rev is not None else "",
            "gross_profit": gp if gp is not None else "",
            "operating_income": oi if oi is not None else "",
            "dep_amort": da if da is not None else "",
            "op_cash_flow": ocf if ocf is not None else "",
            "capex": capex if capex is not None else "",
            "equity": equity if equity is not None else "",
            "debt": debt if debt is not None else "",
            "cash": cash if cash is not None else "",
            "market_cap": rnd(market_cap, 0),
            "enterprise_value": rnd(ev, 0),
            "ebitda": ebitda if ebitda is not None else "",
            "fcf": fcf if fcf is not None else "",
            "pe": rnd(pe, 4), "ps": rnd(ps, 4), "pb": rnd(pb, 4),
            "ev_ebitda": rnd(ev_ebitda, 4), "fcf_yield": rnd(fcf_yield, 6),
            "net_margin": rnd(net_margin, 4), "gross_margin": rnd(gross_margin, 4),
            "revenue_growth_yoy": rnd(rev_growth, 4), "earnings_growth_yoy": rnd(earn_growth, 4),
            "price_source": price_source,
            "fundamental_source": "SEC EDGAR XBRL companyconcept (latest restated annual)",
            "status": status, "comment": "; ".join(notes),
        })
    return rows


def current_missing_company_row(symbol: str, cik: Optional[int], as_of: dt.date, comment: str) -> Dict[str, Any]:
    row = {f: "" for f in FIELDNAMES}
    row.update({
        "symbol": symbol,
        "cik": f"{cik:010d}" if cik is not None else "",
        "fiscal_year": "current",
        "fy_end": as_of.isoformat(),
        "currency": "",
        "price_source": "missing",
        "fundamental_source": f"SEC EDGAR XBRL companyconcept TTM filed<={as_of.isoformat()}",
        "status": "missing",
        "comment": comment,
    })
    return row


def build_current_company(
    symbol: str,
    cik: int,
    twelve_key: Optional[str],
    fmp_key: Optional[str],
    price_provider: str,
    as_of: dt.date,
) -> Dict[str, Any]:
    print(f"  {symbol}: CIK{cik:010d} fetching SEC TTM facts filed<={as_of.isoformat()} ...")
    submission_metadata = fetch_submission_metadata(cik)
    entity_type = (submission_metadata.get("entityType") or "").strip().lower()
    flows = {name: fetch_series_asof(symbol, cik, cands, as_of) for name, cands in FLOW_TAGS.items()}
    instants = {name: fetch_series_asof(symbol, cik, cands, as_of)
                for name, cands in INSTANT_TAGS.items() if name != "shares"}
    shares_ccy, shares_point, shares_source = fetch_current_shares_point(symbol, cik, as_of)

    ni_ccy, ni_pts = flows["net_income"]
    rev_ccy, rev_pts = flows["revenue"]
    fundamental_ccy = ni_ccy or rev_ccy or "USD"

    ttm_values: Dict[str, Optional[float]] = {}
    ttm_ends: Dict[str, Optional[str]] = {}
    ttm_notes: Dict[str, str] = {}
    prior_ttm_values: Dict[str, Optional[float]] = {}
    for name, (_ccy, points) in flows.items():
        value, end, count, note, prior = ttm_from_points(points, as_of)
        ttm_values[name] = value
        ttm_ends[name] = end
        ttm_notes[name] = note if value is not None else f"{note} ({count} quarters)"
        prior_ttm_values[name] = prior

    equity_point = latest_instant_point(instants["equity"][1], as_of)
    debt_point = latest_instant_point(instants["debt"][1], as_of)
    cash_point = latest_instant_point(instants["cash"][1], as_of)

    notes: List[str] = []
    close: Optional[float] = None
    close_date: Optional[str] = None
    price_note = ""
    price_source = "missing"
    if price_provider in ("twelve", "auto"):
        if twelve_key:
            close, close_date, price_note = fetch_latest_close(symbol, as_of, twelve_key)
            time.sleep(TWELVE_PAUSE)
            if close is not None:
                price_source = "Twelve Data time_series adjust=none latest close"
        else:
            price_note = "no twelvedata key"
    if close is None and price_provider in ("fmp", "auto"):
        twelve_note = price_note
        if fmp_key:
            close, close_date, price_note = fetch_latest_fmp_close(symbol, as_of, fmp_key)
            time.sleep(FMP_PAUSE)
            if close is not None:
                price_source = "Financial Modeling Prep stable historical-price-eod/full close"
                if twelve_note:
                    notes.append(f"{twelve_note}; FMP fallback used")
        else:
            price_note = "no FMP key"
    if close is None and price_provider in ("nasdaq", "auto"):
        prior_note = price_note
        close, close_date, price_note = fetch_latest_nasdaq_close(symbol, as_of)
        time.sleep(NASDAQ_PAUSE)
        if close is not None:
            price_source = "Nasdaq historical API close"
            if prior_note:
                notes.append(f"{prior_note}; Nasdaq fallback used")
    if close is not None and price_source == "missing":
        price_source = "current EOD close"
    if price_note:
        notes.append(price_note)

    shares = shares_point.get("val") if shares_point else None
    shares_asof = shares_point.get("end", "") if shares_point else ""
    if shares is None:
        notes.append(shares_source)

    ni = ttm_values["net_income"]
    rev = ttm_values["revenue"]
    gp = ttm_values["gross_profit"]
    oi = ttm_values["operating_income"]
    da = ttm_values["dep_amort"]
    ocf = ttm_values["op_cash_flow"]
    capex = ttm_values["capex"]
    equity = equity_point.get("val") if equity_point else None
    debt = debt_point.get("val") if debt_point else None
    cash = cash_point.get("val") if cash_point else None

    if ni is None:
        notes.append(f"no clean TTM net_income: {ttm_notes['net_income']}")
    if rev is None:
        notes.append(f"no clean TTM revenue: {ttm_notes['revenue']}")
    if equity is None:
        notes.append("no non-stale equity instant filed<=as_of")

    foreign_entity = entity_type == "other"
    price_ccy_ok = fundamental_ccy == "USD" and symbol not in PRICE_RATIO_EXCLUDE and not foreign_entity
    if not price_ccy_ok:
        if symbol in PRICE_RATIO_EXCLUDE:
            notes.append("price-based ratios suppressed: ADR/foreign-share ratio not normalized")
        elif foreign_entity:
            notes.append("price-based ratios suppressed: SEC entityType=other (foreign/ADR entity not in US-only price basket)")
        else:
            notes.append(f"price-based ratios suppressed: fundamentals in {fundamental_ccy}, price in USD (FX not applied)")

    market_cap = (close * shares) if (close is not None and shares) else None
    ebitda = (oi + da) if (oi is not None and da is not None) else None
    ev = (market_cap + (debt or 0) - (cash or 0)) if market_cap is not None else None
    fcf = (ocf - capex) if (ocf is not None and capex is not None) else None

    pe = safe_div(market_cap, ni) if price_ccy_ok else None
    ps = safe_div(market_cap, rev) if price_ccy_ok else None
    pb = safe_div(market_cap, equity) if price_ccy_ok else None
    ev_ebitda = safe_div(ev, ebitda) if price_ccy_ok else None
    fcf_yield = safe_div(fcf, market_cap) if price_ccy_ok else None

    net_margin = safe_div(ni, rev)
    gross_margin = safe_div(gp, rev)
    rev_prior = prior_ttm_values.get("revenue")
    ni_prior = prior_ttm_values.get("net_income")
    rev_growth = (rev / rev_prior - 1) if (rev is not None and rev_prior) else None
    earn_growth = (ni / ni_prior - 1) if (ni is not None and ni_prior) else None

    have_price_ratio = any(x is not None for x in (pe, ps, pb, ev_ebitda))
    if have_price_ratio:
        status = "ok"
    elif net_margin is not None or gross_margin is not None:
        status = "partial"
    else:
        status = "missing"

    ttm_end = ttm_ends.get("net_income") or ttm_ends.get("revenue") or ""
    row = {
        "symbol": symbol, "cik": f"{cik:010d}", "fiscal_year": "current",
        "fy_end": ttm_end, "currency": fundamental_ccy,
        "fy_end_close": rnd(close, 4), "close_date": close_date or "",
        "shares_outstanding": shares if shares is not None else "",
        "shares_asof": shares_asof,
        "net_income": ni if ni is not None else "",
        "revenue": rev if rev is not None else "",
        "gross_profit": gp if gp is not None else "",
        "operating_income": oi if oi is not None else "",
        "dep_amort": da if da is not None else "",
        "op_cash_flow": ocf if ocf is not None else "",
        "capex": capex if capex is not None else "",
        "equity": equity if equity is not None else "",
        "debt": debt if debt is not None else "",
        "cash": cash if cash is not None else "",
        "market_cap": rnd(market_cap, 0),
        "enterprise_value": rnd(ev, 0),
        "ebitda": ebitda if ebitda is not None else "",
        "fcf": fcf if fcf is not None else "",
        "pe": rnd(pe, 4), "ps": rnd(ps, 4), "pb": rnd(pb, 4),
        "ev_ebitda": rnd(ev_ebitda, 4), "fcf_yield": rnd(fcf_yield, 6),
        "net_margin": rnd(net_margin, 4), "gross_margin": rnd(gross_margin, 4),
        "revenue_growth_yoy": rnd(rev_growth, 4), "earnings_growth_yoy": rnd(earn_growth, 4),
        "price_source": price_source,
        "fundamental_source": f"SEC EDGAR XBRL companyconcept TTM filed<={as_of.isoformat()}",
        "status": status,
        "comment": "; ".join(notes),
    }
    return row


def to_float(value: Any) -> Optional[float]:
    if value in ("", None):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def build_basket_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """One BASKET_AVG row per fiscal year + an overall five_year_average row.

    Per metric, average across companies that have a valid (non-negative for
    price ratios) value. The final five_year_average row averages each metric
    across all valid company-FY observations.
    """
    metrics = PRICE_METRICS + NEUTRAL_METRICS
    out: List[Dict[str, Any]] = []

    def avg_for(subset: List[Dict[str, Any]], metric: str, drop_negative: bool) -> Optional[float]:
        vals = []
        for r in subset:
            if metric in PRICE_METRICS and r["symbol"] in PRICE_RATIO_EXCLUDE:
                continue
            v = to_float(r.get(metric))
            if v is None:
                continue
            if drop_negative and metric in PRICE_METRICS and v < 0:
                continue
            vals.append(v)
        return mean(vals) if vals else None

    for year in FY_YEARS:
        subset = [r for r in rows if r["fiscal_year"] == year]
        row = {f: "" for f in FIELDNAMES}
        row.update({
            "symbol": "BASKET_AVG", "cik": "", "fiscal_year": year, "fy_end": "",
            "currency": "USD",
            "fundamental_source": "basket average across semis companies for this FY",
            "price_source": "", "status": "aggregate",
            "comment": (
                f"average over {len([r for r in subset if r['status']!='missing'])} companies with data; "
                f"excluded from price metrics: {excluded_price_tickers(subset)}"
            ),
        })
        for m in metrics:
            row[m] = rnd(avg_for(subset, m, drop_negative=True), 4 if m != "fcf_yield" else 6)
        out.append(row)

    # Overall five-year average (all company-FY observations pooled).
    company_rows = [r for r in rows if r["status"] in ("ok", "partial")]
    row = {f: "" for f in FIELDNAMES}
    row.update({
        "symbol": "BASKET_AVG", "cik": "", "fiscal_year": "five_year_average", "fy_end": "",
        "currency": "USD",
        "fundamental_source": (
            f"five-year (FY{FY_YEARS[0]}-FY{FY_YEARS[-1]}) basket norm, "
            "pooled across all company-FY observations"
        ),
        "price_source": "", "status": "aggregate",
        "comment": (
            "USD-fundamental companies only for price ratios; "
            f"excluded from price metrics: {excluded_price_tickers(company_rows)}"
        ),
    })
    for m in metrics:
        row[m] = rnd(avg_for(company_rows, m, drop_negative=True), 4 if m != "fcf_yield" else 6)
    out.append(row)
    return out


def build_current_basket_rows(rows: List[Dict[str, Any]], as_of: dt.date) -> List[Dict[str, Any]]:
    """One current aggregate detail row using the same median logic as the summary."""
    summary = {row["metric"]: row for row in build_current_summary_rows(rows, as_of)}
    row = {f: "" for f in FIELDNAMES}
    row.update({
        "symbol": "BASKET_AVG", "cik": "", "fiscal_year": "current",
        "fy_end": as_of.isoformat(), "currency": "USD",
        "fundamental_source": f"current TTM basket median filed<={as_of.isoformat()}",
        "price_source": "Twelve Data latest close",
        "status": "aggregate",
        "comment": "median over current company observations with valid values",
    })
    for metric, summary_row in summary.items():
        row[metric] = summary_row.get("value", "")
    return [row]


SUMMARY_FIELDNAMES = ["metric", "five_year_average", "n_companies", "n_observations", "status", "comment"]
CURRENT_SUMMARY_FIELDNAMES = ["metric", "value", "n_companies", "n_observations", "status", "comment"]


def build_summary_rows(company_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """One row per metric using a two-level median for five_year_average.

    First take each company's median across its available FY observations, then
    take the median across companies. This gives every company equal weight
    regardless of how many fiscal years are available. Price ratios drop
    non-positive values and only use USD-fundamental companies (the per-company
    builder already suppresses non-USD price ratios).
    """
    metrics = PRICE_METRICS + NEUTRAL_METRICS
    rows = [r for r in company_rows if r.get("status") in ("ok", "partial")]
    out: List[Dict[str, Any]] = []
    for metric in metrics:
        values_by_company: Dict[str, List[float]] = {}
        for r in rows:
            if metric in PRICE_METRICS and r["symbol"] in PRICE_RATIO_EXCLUDE:
                continue
            v = to_float(r.get(metric))
            if v is None:
                continue
            if metric in PRICE_METRICS and v <= 0:
                continue
            values_by_company.setdefault(r["symbol"], []).append(v)
        if values_by_company:
            company_medians = [
                median(values) for values in values_by_company.values()
            ]
            n_observations = sum(len(values) for values in values_by_company.values())
            comment = (
                "two-level median: per-company 5Y median, then median across companies"
            )
            if metric in PRICE_METRICS:
                comment += (
                    "; price ratios exclude non-positive values and non-USD filers; "
                    f"excluded from price metrics: {excluded_price_tickers(company_rows)}"
                )
            out.append({
                "metric": metric,
                "five_year_average": round(median(company_medians), 6),
                "n_companies": len(values_by_company),
                "n_observations": n_observations,
                "status": "ok",
                "comment": comment,
            })
        else:
            comment = "no valid observations across the basket"
            if metric in PRICE_METRICS:
                comment += f"; excluded from price metrics: {excluded_price_tickers(company_rows)}"
            out.append({
                "metric": metric,
                "five_year_average": "",
                "n_companies": 0,
                "n_observations": 0,
                "status": "missing",
                "comment": comment,
            })
    return out


def build_current_summary_rows(company_rows: List[Dict[str, Any]], as_of: dt.date) -> List[Dict[str, Any]]:
    """One row per metric: current median across the basket."""
    metrics = PRICE_METRICS + NEUTRAL_METRICS
    rows = [r for r in company_rows if r.get("status") in ("ok", "partial")]
    out: List[Dict[str, Any]] = []
    for metric in metrics:
        vals: List[float] = []
        companies = set()
        for r in rows:
            if metric in PRICE_METRICS and r["symbol"] in PRICE_RATIO_EXCLUDE:
                continue
            v = to_float(r.get(metric))
            if v is None:
                continue
            if metric in PRICE_METRICS and v < 0:
                continue
            vals.append(v)
            companies.add(r["symbol"])
        if vals:
            comment = f"MEDIAN current TTM snapshot as of {as_of.isoformat()}"
            if metric in PRICE_METRICS:
                comment += (
                    "; price ratios exclude negatives and ADR/foreign-share exceptions; "
                    f"excluded from price metrics: {excluded_price_tickers(company_rows)}"
                )
            out.append({
                "metric": metric,
                "value": round(median(vals), 6),
                "n_companies": len(companies),
                "n_observations": len(vals),
                "status": "ok",
                "comment": comment,
            })
        else:
            comment = "no valid current observations across the basket"
            if metric in PRICE_METRICS:
                comment += f"; excluded from price metrics: {excluded_price_tickers(company_rows)}"
            out.append({
                "metric": metric,
                "value": "",
                "n_companies": 0,
                "n_observations": 0,
                "status": "missing",
                "comment": comment,
            })
    return out


def write_outputs(rows: List[Dict[str, Any]], summary_rows: List[Dict[str, Any]]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    with OUT_SUMMARY_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SUMMARY_FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(summary_rows)
    metadata = {
        "generated_at": dt.datetime.now().replace(microsecond=0).isoformat(),
        "sector": SECTOR_NAME,
        "fiscal_years": FY_YEARS,
        "symbols": SEMIS,
        "fundamental_source": "SEC EDGAR XBRL companyconcept (latest restated annual facts)",
        "price_source": "Twelve Data time_series, adjust=none (as-reported FY-end close)",
        "fy_definition": "FY20YY = annual period whose period END falls in calendar year 20YY",
        "split_handling": "as-reported (unadjusted) close paired with as-reported shares -> split-consistent market_cap",
        "currency_note": "TSM uses USD units; ASML reports EUR -> ASML price ratios suppressed (no FX applied)",
        "is_point_in_time": False,
        "purpose": "one-time 5-year FY norm for comparing the current snapshot against history",
    }
    OUT_JSON.write_text(
        json.dumps({"metadata": metadata, "summary": summary_rows, "rows": rows},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_norm_outputs(company_rows: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    output_rows = company_rows + build_basket_rows(company_rows)
    summary_rows = build_summary_rows(company_rows)
    write_outputs(output_rows, summary_rows)
    return output_rows, summary_rows


def resummarize_from_detail() -> List[Dict[str, Any]]:
    """Rebuild only the norm summary from an existing local detail CSV."""
    if not OUT_CSV.exists():
        raise FileNotFoundError(f"detail CSV not found: {OUT_CSV}")

    with OUT_CSV.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = set(reader.fieldnames or [])
        required = {"symbol", "status", *PRICE_METRICS, *NEUTRAL_METRICS}
        missing = sorted(required - fieldnames)
        if missing:
            raise ValueError(
                f"detail CSV is missing required columns: {', '.join(missing)}"
            )
        company_rows = [
            row for row in reader
            if row.get("symbol") != "BASKET_AVG"
        ]

    summary_rows = build_summary_rows(company_rows)
    OUT_SUMMARY_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_SUMMARY_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SUMMARY_FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(summary_rows)
    return summary_rows


def write_current_outputs(
    company_rows: List[Dict[str, Any]],
    summary_rows: List[Dict[str, Any]],
    as_of: dt.date,
) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    output_rows = company_rows + build_current_basket_rows(company_rows, as_of)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)
    with OUT_SUMMARY_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CURRENT_SUMMARY_FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(summary_rows)
    price_sources = sorted({
        str(row.get("price_source"))
        for row in company_rows
        if row.get("price_source") and row.get("price_source") != "missing"
    })
    metadata = {
        "generated_at": dt.datetime.now().replace(microsecond=0).isoformat(),
        "sector": SECTOR_NAME,
        "as_of": as_of.isoformat(),
        "symbols": SEMIS,
        "fundamental_source": f"SEC EDGAR XBRL companyconcept TTM facts filed<={as_of.isoformat()}",
        "price_source": price_sources[0] if len(price_sources) == 1 else price_sources,
        "is_point_in_time": True,
        "purpose": "current snapshot using the same basket/formulas as the FY norm",
    }
    OUT_JSON.write_text(
        json.dumps({"metadata": metadata, "summary": summary_rows, "rows": output_rows},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def parse_iso_date(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"invalid date {value!r}; expected YYYY-MM-DD"
        ) from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a one-time 5-year FY valuation norm for a sector basket.")
    parser.add_argument("--sector", default="Semiconductors",
                        help="Sector name (used for metadata and to look up a built-in basket).")
    parser.add_argument("--tickers", nargs="+", default=None,
                        help="Override the basket (e.g. --tickers NVDA AMD). Defaults to the sector basket.")
    parser.add_argument("--years", nargs="+", type=int, default=None,
                        help=("Override fiscal years explicitly. When omitted, the "
                              "norm uses the rolling last-5-fiscal-years window for "
                              "--as-of (or today), which is [2021..2025] in 2026."))
    parser.add_argument("--slug", default=None,
                        help="Filename slug; default 'semis' for Semiconductors else the lowercased sector.")
    parser.add_argument("--current", action="store_true",
                        help="Build a current TTM snapshot instead of the FY2021-FY2025 norm.")
    parser.add_argument(
        "--as-of",
        type=parse_iso_date,
        default=None,
        metavar="YYYY-MM-DD",
        help=(
            "Point-in-time date. For --current it is the snapshot date (and is "
            "included in current output filenames). For the norm it selects the "
            "rolling fiscal-year window via default_fy_years(as_of). Defaults to "
            "today. Ignored if --years is given explicitly."
        ),
    )
    parser.add_argument(
        "--price-provider",
        choices=("twelve", "fmp", "nasdaq", "auto"),
        default="twelve",
        help="Current-price provider. 'auto' tries Twelve Data, FMP, then Nasdaq.",
    )
    parser.add_argument(
        "--resummarize-from-detail",
        action="store_true",
        help=(
            "Rebuild only fyn_<slug>_norm_summary.csv from the existing local "
            "fyn_<slug>_norm.csv; performs no network requests."
        ),
    )
    parser.add_argument(
        "--exclude-price",
        nargs="*",
        default=[],
        metavar="TICKER",
        help="Add tickers to the built-in exclusions from price-based metrics.",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Force SEC companyconcept network requests; do not read or write the disk cache.",
    )
    return parser.parse_args()


def main() -> int:
    global SEMIS, FY_YEARS, SECTOR_NAME, SECTOR_SLUG, OUT_CSV, OUT_SUMMARY_CSV, OUT_JSON
    global PRICE_RATIO_EXCLUDE, SEC_CACHE_ENABLED

    args = parse_args()
    SEC_CACHE_ENABLED = not args.no_cache
    if args.current and args.resummarize_from_detail:
        raise SystemExit("--current and --resummarize-from-detail are mutually exclusive")
    # --as-of now applies to the norm too (it selects the rolling FY window). It
    # only affects current OUTPUT FILENAMES, so for the norm it stays metadata.
    PRICE_RATIO_EXCLUDE = set(BASE_PRICE_RATIO_EXCLUDE)
    PRICE_RATIO_EXCLUDE.update(
        ticker.strip().upper() for ticker in args.exclude_price if ticker.strip()
    )
    SECTOR_NAME = args.sector
    if args.tickers:
        SEMIS = [t.upper() for t in args.tickers]
    elif args.sector in SECTOR_BASKETS:
        SEMIS = SECTOR_BASKETS[args.sector]
    # else: keep default basket
    if args.years:
        # Explicit manual override always wins (unchanged behaviour).
        FY_YEARS = args.years
    elif not args.current:
        # Norm mode, no explicit --years: use the rolling last-5-fiscal-years
        # window for --as-of (or today). For any 2026 date this is [2021..2025],
        # so the already-collected norms are not rebuilt on a different window.
        FY_YEARS = default_fy_years(args.as_of)
    # --current mode keeps its own date-driven TTM logic and ignores FY_YEARS.
    if args.slug:
        SECTOR_SLUG = args.slug
    elif args.sector.lower().startswith("semi"):
        SECTOR_SLUG = "semis"
    else:
        SECTOR_SLUG = args.sector.lower().replace(" ", "_").replace("/", "_")

    if args.current and args.as_of is not None:
        suffix = f"current_{args.as_of:%Y%m%d}"
    else:
        suffix = "current" if args.current else "norm"
    OUT_CSV = OUT_DIR / f"fyn_{SECTOR_SLUG}_{suffix}.csv"
    OUT_SUMMARY_CSV = OUT_DIR / f"fyn_{SECTOR_SLUG}_{suffix}_summary.csv"
    OUT_JSON = OUT_DIR / f"fyn_{SECTOR_SLUG}_{suffix}.json"

    if args.resummarize_from_detail:
        summary_rows = resummarize_from_detail()
        print(f"Read detail:    {OUT_CSV}")
        print(f"Wrote summary: {OUT_SUMMARY_CSV}")
        for row in summary_rows:
            print(
                f"  {row['metric']:20s} five_year_average={row['five_year_average']} "
                f"(n_companies={row['n_companies']}, "
                f"n_obs={row['n_observations']}, {row['status']})"
            )
        return 0

    as_of = args.as_of or dt.date.today()
    if args.current:
        print(f"Sector: {SECTOR_NAME} | basket: {', '.join(SEMIS)} | current TTM as of {as_of.isoformat()}")
    else:
        print(f"Sector: {SECTOR_NAME} | basket: {', '.join(SEMIS)} | FY {FY_YEARS[0]}..{FY_YEARS[-1]}")
    twelve_key = read_twelve_key()
    fmp_key = read_fmp_key() if args.current and args.price_provider in ("fmp", "auto") else None
    print(f"Twelve Data key: {'present' if twelve_key else 'ABSENT'}")
    if args.current and args.price_provider in ("fmp", "auto"):
        print(f"FMP key: {'present' if fmp_key else 'ABSENT -> FMP price ratios will be missing'}")
    ticker_map = load_ticker_cik_map()

    all_rows: List[Dict[str, Any]] = []
    output_rows: List[Dict[str, Any]] = []
    summary_rows: List[Dict[str, Any]] = []
    if args.current:
        for symbol in SEMIS:
            cik = ticker_map.get(symbol.upper())
            if cik is None:
                print(f"  {symbol}: no CIK in SEC map -> missing")
                all_rows.append(current_missing_company_row(
                    symbol,
                    None,
                    as_of,
                    "no CIK in SEC ticker map (no SEC companyconcept facts)",
                ))
                summary_rows = build_current_summary_rows(all_rows, as_of)
                write_current_outputs(all_rows, summary_rows, as_of)
                continue
            try:
                all_rows.append(build_current_company(
                    symbol,
                    cik,
                    twelve_key,
                    fmp_key,
                    args.price_provider,
                    as_of,
                ))
            except Exception as exc:
                print(f"  {symbol}: failed -> missing ({type(exc).__name__}: {exc})")
                all_rows.append(current_missing_company_row(
                    symbol,
                    cik,
                    as_of,
                    f"company processing error: {type(exc).__name__}: {exc}",
                ))
            summary_rows = build_current_summary_rows(all_rows, as_of)
            write_current_outputs(all_rows, summary_rows, as_of)

        summary_rows = build_current_summary_rows(all_rows, as_of)
        write_current_outputs(all_rows, summary_rows, as_of)
        output_rows = all_rows + build_current_basket_rows(all_rows, as_of)
        ok = sum(1 for r in all_rows if r.get("status") == "ok")
        partial = sum(1 for r in all_rows if r.get("status") == "partial")
        missing = sum(1 for r in all_rows if r.get("status") == "missing")
        print(f"\nWrote {len(output_rows)} detail rows ({len(all_rows)} current company rows): "
              f"{ok} ok, {partial} partial, {missing} missing")
        print(f"Detail:  {OUT_CSV}")
        print(f"Summary: {OUT_SUMMARY_CSV}")
        print(f"JSON:    {OUT_JSON}")
        for s in summary_rows:
            print(f"  {s['metric']:20s} value={s['value']} "
                  f"(n_companies={s['n_companies']}, n_obs={s['n_observations']}, {s['status']})")
        return 0

    for symbol in SEMIS:
        cik = ticker_map.get(symbol.upper())
        if cik is None:
            print(f"  {symbol}: no CIK in SEC map (foreign 20-F/IFRS filer) -> missing")
            all_rows.extend(missing_company_rows(
                symbol,
                None,
                "no CIK in SEC ticker map (foreign 20-F/IFRS filer; no us-gaap facts)",
            ))
            output_rows, summary_rows = write_norm_outputs(all_rows)
            continue
        try:
            all_rows.extend(build_company(symbol, cik, twelve_key))
        except Exception as exc:
            print(f"  {symbol}: failed -> missing ({type(exc).__name__}: {exc})")
            all_rows.extend(missing_company_rows(
                symbol,
                cik,
                f"company processing error: {type(exc).__name__}: {exc}",
            ))
        output_rows, summary_rows = write_norm_outputs(all_rows)

    output_rows, summary_rows = write_norm_outputs(all_rows)

    ok = sum(1 for r in all_rows if r.get("status") == "ok")
    partial = sum(1 for r in all_rows if r.get("status") == "partial")
    missing = sum(1 for r in all_rows if r.get("status") == "missing")
    print(f"\nWrote {len(output_rows)} detail rows ({len(all_rows)} company-year): "
          f"{ok} ok, {partial} partial, {missing} missing")
    print(f"Detail:  {OUT_CSV}")
    print(f"Summary: {OUT_SUMMARY_CSV}")
    print(f"JSON:    {OUT_JSON}")
    for s in summary_rows:
        print(f"  {s['metric']:20s} five_year_average={s['five_year_average']} "
              f"(n_companies={s['n_companies']}, n_obs={s['n_observations']}, {s['status']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
