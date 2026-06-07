#!/usr/bin/env python3
"""Среднеисторический композит президентского цикла S&P 500.

Берёт месячный ряд S&P 500 (DataHub / Shiller), считает среднюю помесячную
доходность по году президентского цикла с 1950 года и строит кумулятивный
индекс (база 100, старт = декабрь года выборов) на 49 точек.

Результат: data/market_quotes/presidential_cycle_composite.json
Эти 49 значений вшиты в cycleChart() в sector_valuation_dashboard.html.

Источник ряда: https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv
Это price return без дивидендов, поэтому цифры немного отличаются от
total-return исследований (Stock Trader's Almanac и т.п.).
"""
import csv
import json
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

URL = "https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv"
START = 1950
OUT = Path(__file__).resolve().parent.parent / "data/market_quotes/presidential_cycle_composite.json"


def load_rows(path_or_url: str):
    if path_or_url.startswith("http"):
        with urllib.request.urlopen(path_or_url, timeout=30) as r:
            text = r.read().decode("utf-8")
        lines = text.splitlines()
    else:
        lines = Path(path_or_url).read_text().splitlines()
    rows = []
    for d in csv.DictReader(lines):
        y, m, _ = d["Date"].split("-")
        try:
            px = float(d["SP500"])
        except ValueError:
            continue
        if px <= 0:
            continue
        rows.append((int(y), int(m), px))
    rows.sort()
    return rows


def yr_of_cycle(y: int) -> int:
    """1=post-election, 2=midterm, 3=pre-election, 4=election (выборы в год%4==0)."""
    return {1: 1, 2: 2, 3: 3, 0: 4}[y % 4]


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else URL
    rows = load_rows(src)
    px = {(y, m): p for y, m, p in rows}
    months = [(y, m) for y, m, _ in rows]

    ret_by = defaultdict(list)
    for i in range(1, len(months)):
        y, m = months[i]
        py, pm = months[i - 1]
        if y < START:
            continue
        ret_by[(yr_of_cycle(y), m)].append(px[(y, m)] / px[(py, pm)] - 1)

    avg = {k: sum(v) / len(v) for k, v in ret_by.items()}

    seq = [(cy, mo) for cy in (1, 2, 3, 4) for mo in range(1, 13)]
    idx = [100.0]
    for cy, mo in seq:
        idx.append(idx[-1] * (1 + avg[(cy, mo)]))

    names = {1: "post-election", 2: "midterm", 3: "pre-election", 4: "election"}
    year_changes = {
        names[cy]: round((idx[cy * 12] / idx[(cy - 1) * 12] - 1) * 100, 2)
        for cy in (1, 2, 3, 4)
    }
    seg = idx[12:25]
    bottom = 12 + min(range(len(seg)), key=lambda i: seg[i])

    out = {
        "source": src,
        "start_year": START,
        "note": "price return, S&P 500 monthly, composite presidential cycle",
        "index": [round(v, 3) for v in idx],
        "year_changes": year_changes,
        "midterm_bottom_month_index": bottom,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print("Saved", OUT)
    print("Year changes:", year_changes)
    print("Midterm bottom at point index:", bottom)


if __name__ == "__main__":
    main()
