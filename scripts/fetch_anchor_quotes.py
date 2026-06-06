#!/usr/bin/env python3
"""
Fetch company-basket closes for sector-dashboard anchor dates.

The script mirrors the old investment-site data providers:
- Financial Modeling Prep for US/global tickers.
- MOEX ISS for Russian instruments.

It does not write API keys to output files. FMP keys are read from environment
variables first, then from the old local Django module if it exists.
"""

from __future__ import annotations

import argparse
import calendar
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = PROJECT_ROOT / "data" / "market_quotes" / "sector_quote_tickers.json"
DEFAULT_CSV = PROJECT_ROOT / "data" / "market_quotes" / "anchor_quotes.csv"
DEFAULT_JSON = PROJECT_ROOT / "data" / "market_quotes" / "anchor_quotes.json"
FMP_STABLE_BASE = "https://financialmodelingprep.com/stable"
MOEX_ISS_BASE = "https://iss.moex.com/iss"
FMP_KEY_NAMES = (
    "FMP_API_KEY",
    "FINANCIAL_MODELING_PREP_API_KEY",
    "FINANCIALMODELINGPREP_API_KEY",
)
TWELVE_DATA_BASE = "https://api.twelvedata.com"
TWELVE_DATA_KEY_NAMES = (
    "TWELVE_DATA_API_KEY",
    "TWELVEDATA_API_KEY",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch 10/20/30 anchor-date quote closes.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--out-csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--out-json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--as-of", default=dt.date.today().isoformat())
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--lookback-days", type=int, default=10)
    parser.add_argument("--twelve-data-min-interval", type=float, default=8.0)
    parser.add_argument("--yahoo-min-interval", type=float, default=2.0)
    parser.add_argument(
        "--sector",
        default=None,
        help="If set, only fetch instruments for this sector (faster, avoids burning rate limits).",
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge into existing output instead of overwriting (keeps rows for other sectors).",
    )
    return parser.parse_args()


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        key = key.strip().replace("export ", "")
        value = value.strip().strip("'").strip('"')
        os.environ.setdefault(key, value)


def legacy_fmp_key_path() -> Path:
    explicit = os.environ.get("FMP_LEGACY_MARKETDATA_PATH")
    if explicit:
        return Path(explicit).expanduser()
    return Path.home() / "Desktop" / "Project \u2014 \u043a\u043e\u043f\u0438\u044f" / "leftbar" / "marketdata.py"


def read_legacy_fmp_key(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"^Api\s*=\s*['\"]([^'\"]+)['\"]", text, re.MULTILINE)
    return match.group(1) if match else None


def get_fmp_api_key() -> Tuple[Optional[str], str]:
    for env_path in (PROJECT_ROOT / ".env", Path.home() / "Desktop" / ".env"):
        load_dotenv(env_path)

    for name in FMP_KEY_NAMES:
        if os.environ.get(name):
            return os.environ[name], f"env:{name}"

    path = legacy_fmp_key_path()
    key = read_legacy_fmp_key(path)
    if key:
        return key, f"legacy:{path}"
    return None, "missing"


def get_twelve_data_api_key() -> Tuple[Optional[str], str]:
    for env_path in (PROJECT_ROOT / ".env", Path.home() / "Desktop" / ".env"):
        load_dotenv(env_path)

    for name in TWELVE_DATA_KEY_NAMES:
        if os.environ.get(name):
            return os.environ[name], f"env:{name}"
    return None, "missing"


def sanitize_error(error: BaseException, api_key: Optional[str]) -> str:
    text = str(error)
    if api_key:
        text = text.replace(api_key, "[API_KEY]")
    return text


def anchor_dates(as_of: dt.date, count: int) -> List[dt.date]:
    anchors: List[dt.date] = []
    year, month = as_of.year, as_of.month

    for _ in range(36):
        last_day = calendar.monthrange(year, month)[1]
        for day in (10, 20, min(30, last_day)):
            anchor = dt.date(year, month, day)
            if anchor <= as_of:
                anchors.append(anchor)

        month -= 1
        if month == 0:
            month = 12
            year -= 1

        if len(anchors) >= count + 3:
            break

    return sorted(set(anchors))[-count:]


def request_json(url: str, params: Dict[str, Any], api_key: Optional[str]) -> Any:
    query = urllib.parse.urlencode(params)
    request_url = f"{url}?{query}"
    try:
        with urllib.request.urlopen(request_url, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="ignore")
        if api_key:
            body = body.replace(api_key, "[API_KEY]")
        raise RuntimeError(f"HTTP {error.code}: {body[:300]}") from error


def fetch_fmp_history(symbol: str, start: dt.date, end: dt.date, api_key: str) -> Dict[dt.date, Dict[str, Any]]:
    data = request_json(
        f"{FMP_STABLE_BASE}/historical-price-eod/full",
        {
            "symbol": symbol,
            "from": start.isoformat(),
            "to": end.isoformat(),
            "apikey": api_key,
        },
        api_key,
    )
    if isinstance(data, dict) and data.get("Error Message"):
        raise RuntimeError(str(data.get("Error Message")))
    if not isinstance(data, list):
        raise RuntimeError("Unexpected FMP response format")

    rows: Dict[dt.date, Dict[str, Any]] = {}
    for item in data:
        if not item.get("date"):
            continue
        rows[dt.date.fromisoformat(item["date"])] = item
    return rows


def fetch_twelve_data_history(
    symbol: str,
    start: dt.date,
    end: dt.date,
    api_key: str,
) -> Dict[dt.date, Dict[str, Any]]:
    data = request_json(
        f"{TWELVE_DATA_BASE}/time_series",
        {
            "symbol": symbol,
            "interval": "1day",
            "start_date": start.isoformat(),
            "end_date": (end + dt.timedelta(days=1)).isoformat(),
            "apikey": api_key,
        },
        api_key,
    )
    if isinstance(data, dict) and data.get("status") == "error":
        raise RuntimeError(str(data.get("message") or data))
    values = data.get("values") if isinstance(data, dict) else None
    if not isinstance(values, list):
        raise RuntimeError("Unexpected Twelve Data response format")

    rows: Dict[dt.date, Dict[str, Any]] = {}
    for item in values:
        day = item.get("datetime")
        if not day:
            continue
        rows[dt.date.fromisoformat(day)] = {
            "symbol": symbol,
            "date": day,
            "open": item.get("open"),
            "high": item.get("high"),
            "low": item.get("low"),
            "close": item.get("close"),
            "volume": item.get("volume"),
        }
    return rows


YAHOO_CHART_BASE = "https://query1.finance.yahoo.com/v8/finance/chart"
YAHOO_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


def fetch_yahoo_history(
    symbol: str,
    start: dt.date,
    end: dt.date,
    max_retries: int = 4,
    base_pause: float = 2.0,
) -> Dict[dt.date, Dict[str, Any]]:
    """Keyless fallback via the unofficial Yahoo Finance chart API.

    Returns split-adjusted OHLC. This is acceptable for valuation multiples as long
    as shares outstanding are taken point-in-time for the same date (the fundamentals
    script does this). A realistic browser User-Agent avoids the Too Many Requests
    response seen with the default urllib agent.

    Yahoo rate-limits bursts hard, so on HTTP 429 we back off exponentially and retry.
    Callers should also space out symbols (see YAHOO_MIN_INTERVAL in build_rows).
    """
    period1 = int(dt.datetime(start.year, start.month, start.day).timestamp())
    period2 = int(dt.datetime(end.year, end.month, end.day).timestamp()) + 86400
    url = (
        f"{YAHOO_CHART_BASE}/{urllib.parse.quote(symbol)}"
        f"?period1={period1}&period2={period2}&interval=1d"
    )
    data = None
    for attempt in range(max_retries):
        req = urllib.request.Request(url, headers={"User-Agent": YAHOO_USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as error:
            if error.code == 429 and attempt < max_retries - 1:
                time.sleep(base_pause * (2 ** attempt))
                continue
            raise RuntimeError(f"HTTP {error.code}") from error
    if data is None:
        raise RuntimeError("Yahoo request failed after retries")

    chart = data.get("chart", {})
    if chart.get("error"):
        raise RuntimeError(str(chart["error"]))
    results = chart.get("result")
    if not results:
        raise RuntimeError("Unexpected Yahoo response format")

    result = results[0]
    timestamps = result.get("timestamp", []) or []
    quote = (result.get("indicators", {}).get("quote") or [{}])[0]
    opens = quote.get("open", [])
    highs = quote.get("high", [])
    lows = quote.get("low", [])
    closes = quote.get("close", [])
    volumes = quote.get("volume", [])

    rows: Dict[dt.date, Dict[str, Any]] = {}
    for index, ts in enumerate(timestamps):
        close = closes[index] if index < len(closes) else None
        if close is None:
            continue
        day = dt.datetime.utcfromtimestamp(ts).date()
        rows[day] = {
            "symbol": symbol,
            "date": day.isoformat(),
            "open": opens[index] if index < len(opens) else None,
            "high": highs[index] if index < len(highs) else None,
            "low": lows[index] if index < len(lows) else None,
            "close": close,
            "volume": volumes[index] if index < len(volumes) else None,
        }
    return rows


def fetch_moex_history(
    symbol: str,
    start: dt.date,
    end: dt.date,
    market: str,
    board: str,
) -> Dict[dt.date, Dict[str, Any]]:
    data = request_json(
        f"{MOEX_ISS_BASE}/history/engines/stock/markets/{market}/boards/{board}/securities/{symbol}.json",
        {
            "from": start.isoformat(),
            "till": end.isoformat(),
        },
        None,
    )
    history = data.get("history", {})
    columns = history.get("columns", [])
    records = history.get("data", [])
    rows: Dict[dt.date, Dict[str, Any]] = {}
    if not columns:
        return rows

    for record in records:
        item = dict(zip(columns, record))
        trade_date = item.get("TRADEDATE")
        if not trade_date:
            continue
        close = item.get("LEGALCLOSEPRICE") or item.get("CLOSE") or item.get("WAPRICE")
        if close is None:
            continue
        rows[dt.date.fromisoformat(trade_date)] = {
            "symbol": symbol,
            "date": trade_date,
            "open": item.get("OPEN"),
            "high": item.get("HIGH"),
            "low": item.get("LOW"),
            "close": close,
            "volume": item.get("VOLUME"),
        }
    return rows


def pick_anchor_row(
    history: Dict[dt.date, Dict[str, Any]],
    anchor: dt.date,
    lookback_days: int,
) -> Tuple[Optional[dt.date], Optional[Dict[str, Any]]]:
    floor = anchor - dt.timedelta(days=lookback_days)
    candidates = [day for day in history if floor <= day <= anchor]
    if not candidates:
        return None, None
    actual = max(candidates)
    return actual, history[actual]


def source_label(provider: str) -> str:
    if provider == "fmp":
        return "Financial Modeling Prep stable historical-price-eod/full"
    if provider == "twelve_data":
        return "Twelve Data time_series"
    if provider == "yahoo":
        return "Yahoo Finance chart API (split-adjusted, keyless fallback)"
    if provider == "moex":
        return "MOEX ISS history"
    return provider


def build_rows(
    instruments: Iterable[Dict[str, Any]],
    anchors: List[dt.date],
    lookback_days: int,
    fmp_api_key: Optional[str],
    twelve_data_api_key: Optional[str],
    twelve_data_min_interval: float = 8.0,
    yahoo_min_interval: float = 2.0,
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    start = min(anchors) - dt.timedelta(days=lookback_days)
    end = max(anchors)
    cache: Dict[Tuple[str, str, str, str], Tuple[Optional[Dict[dt.date, Dict[str, Any]]], str, str, str]] = {}
    last_twelve_data_request = 0.0
    last_yahoo_request = 0.0

    for instrument in instruments:
        provider = instrument["provider"]
        symbol = instrument["symbol"]
        market = instrument.get("market", "")
        board = instrument.get("board", "")
        cache_key = (provider, symbol, market, board)

        if cache_key not in cache:
            try:
                if provider == "fmp":
                    if not fmp_api_key:
                        raise RuntimeError("FMP API key not found")
                    history = fetch_fmp_history(symbol, start, end, fmp_api_key)
                    cache[cache_key] = (history, "", "fmp", "")
                elif provider == "moex":
                    history = fetch_moex_history(
                        symbol,
                        start,
                        end,
                        market or "shares",
                        board or "TQBR",
                    )
                    cache[cache_key] = (history, "", "moex", "")
                else:
                    raise RuntimeError(f"Unknown provider: {provider}")
            except Exception as error:
                provider_error = sanitize_error(error, fmp_api_key)
                resolved = False

                # Fallback 1: Twelve Data (only if a key is configured).
                if provider == "fmp" and twelve_data_api_key:
                    try:
                        if last_twelve_data_request and twelve_data_min_interval > 0:
                            elapsed = time.monotonic() - last_twelve_data_request
                            if elapsed < twelve_data_min_interval:
                                time.sleep(twelve_data_min_interval - elapsed)
                        last_twelve_data_request = time.monotonic()
                        history = fetch_twelve_data_history(symbol, start, end, twelve_data_api_key)
                        cache[cache_key] = (
                            history,
                            "",
                            "twelve_data",
                            f"fallback after FMP error: {provider_error}",
                        )
                        resolved = True
                    except Exception as fallback_error:
                        provider_error = (
                            f"{provider_error}; Twelve Data fallback error: "
                            f"{sanitize_error(fallback_error, twelve_data_api_key)}"
                        )

                # Fallback 2: Yahoo chart API (keyless, last resort for US/global).
                if not resolved and provider == "fmp":
                    try:
                        if last_yahoo_request and yahoo_min_interval > 0:
                            elapsed = time.monotonic() - last_yahoo_request
                            if elapsed < yahoo_min_interval:
                                time.sleep(yahoo_min_interval - elapsed)
                        last_yahoo_request = time.monotonic()
                        history = fetch_yahoo_history(symbol, start, end)
                        cache[cache_key] = (
                            history,
                            "",
                            "yahoo",
                            f"keyless fallback after FMP error: {provider_error}",
                        )
                        resolved = True
                    except Exception as yahoo_error:
                        provider_error = (
                            f"{provider_error}; Yahoo fallback error: "
                            f"{sanitize_error(yahoo_error, None)}"
                        )

                if not resolved:
                    cache[cache_key] = (None, provider_error, provider, "")

        history, provider_error, provider_used, fallback_comment = cache[cache_key]
        for anchor in anchors:
            actual, item = pick_anchor_row(history or {}, anchor, lookback_days)
            status = "ok" if item else "missing"
            comment = fallback_comment
            if provider_error:
                status = "provider_error"
                comment = provider_error
            elif actual and actual != anchor:
                suffix = f"previous trading day for anchor {anchor.isoformat()}"
                comment = f"{comment}; {suffix}" if comment else suffix
            elif not item:
                suffix = f"no close found within {lookback_days} days before anchor"
                comment = f"{comment}; {suffix}" if comment else suffix

            rows.append(
                {
                    "anchor_date": anchor.isoformat(),
                    "actual_trading_date": actual.isoformat() if actual else "",
                    "sector": instrument["sector"],
                    "symbol": symbol,
                    "provider": provider_used,
                    "kind": instrument.get("kind", ""),
                    "open": value_or_empty(item, "open"),
                    "high": value_or_empty(item, "high"),
                    "low": value_or_empty(item, "low"),
                    "close": value_or_empty(item, "close"),
                    "volume": value_or_empty(item, "volume"),
                    "source": source_label(provider_used),
                    "status": status,
                    "comment": comment,
                }
            )
    return rows


def value_or_empty(item: Optional[Dict[str, Any]], key: str) -> Any:
    if not item:
        return ""
    value = item.get(key)
    return "" if value is None else value


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "anchor_date",
        "actual_trading_date",
        "sector",
        "symbol",
        "provider",
        "kind",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "source",
        "status",
        "comment",
    ]
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, rows: List[Dict[str, Any]], metadata: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "metadata": metadata,
        "rows": rows,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_existing_rows(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main() -> int:
    args = parse_args()
    as_of = dt.date.fromisoformat(args.as_of)
    config = json.loads(args.config.read_text(encoding="utf-8"))
    anchors = anchor_dates(as_of, args.count)
    fmp_api_key, fmp_key_source = get_fmp_api_key()
    twelve_data_api_key, twelve_data_key_source = get_twelve_data_api_key()

    instruments = config["instruments"]
    if args.sector:
        instruments = [i for i in instruments if i.get("sector") == args.sector]
        if not instruments:
            print(f"No instruments for sector '{args.sector}' in config.")
            return 1

    rows = build_rows(
        instruments,
        anchors,
        args.lookback_days,
        fmp_api_key,
        twelve_data_api_key,
        args.twelve_data_min_interval,
        args.yahoo_min_interval,
    )

    if args.merge:
        # Replace only the rows for the symbols we just fetched; keep everything else.
        fetched_symbols = {(r["sector"], r["symbol"]) for r in rows}
        kept = [
            r for r in load_existing_rows(args.out_csv)
            if (r["sector"], r["symbol"]) not in fetched_symbols
        ]
        rows = kept + rows
        rows.sort(key=lambda r: (r["sector"], r["symbol"], r["anchor_date"]))

    metadata = {
        "generated_at": dt.datetime.now().replace(microsecond=0).isoformat(),
        "as_of": as_of.isoformat(),
        "anchors": [anchor.isoformat() for anchor in anchors],
        "config": str(args.config),
        "sector_filter": args.sector or "all",
        "merged": bool(args.merge),
        "fmp_key_source": fmp_key_source,
        "twelve_data_key_source": twelve_data_key_source,
        "twelve_data_min_interval": args.twelve_data_min_interval,
        "yahoo_min_interval": args.yahoo_min_interval,
        "note": "FMP API key value is intentionally not stored in this file.",
    }
    write_csv(args.out_csv, rows)
    write_json(args.out_json, rows, metadata)

    ok_count = sum(1 for row in rows if row["status"] == "ok")
    missing_count = len(rows) - ok_count
    print(f"Wrote {len(rows)} rows: {ok_count} ok, {missing_count} non-ok")
    print(f"CSV: {args.out_csv}")
    print(f"JSON: {args.out_json}")
    return 0 if ok_count else 1


if __name__ == "__main__":
    sys.exit(main())
