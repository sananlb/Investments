# 5Y FY-norm collection plan — remaining sectors

Source of tickers: `data/market_quotes/sector_quote_tickers.json` (key `instruments`).
SEC verification: `https://www.sec.gov/files/company_tickers.json` (ticker→CIK map) +
spot-checked `us-gaap/NetIncomeLoss` annual facts via
`https://data.sec.gov/api/xbrl/companyconcept/...` (1–2 probes per sector, 0.3–0.35 s pauses).
No Twelve Data / FMP calls were made.

Already collected (excluded here): Banks, Energy, Mining, Semiconductors, Technology,
Drugs, Food & Staples, Utilities.

## Key mechanics that drive the plan

- `build_fy_norm.py` keys the SEC ticker→CIK map by the **exact** uppercased ticker with
  **no normalization** (`load_ticker_cik_map`). A ticker that is not present verbatim in
  the SEC map gets "no CIK -> missing" and contributes no fundamentals. This bites two
  symbols from the config:
  - **`MMC` (Marsh & McLennan)**: SEC lists it as **`MRSH`** (CIK 62709, active filer —
    recent 8-K/Form 4). `MMC` is absent from the map → use `MRSH` in the command.
  - **`BRK.B`**: SEC map has **`BRK-B`** (dash), not `BRK.B` (dot). Use `BRK-B`.
- Slug default = `sector.lower().replace(' ','_').replace('/','_')`, except `semi*` → `semis`.
  For "&" sectors the default keeps the ampersand (e.g. `telecom_&_streaming`), which is
  awkward/risky in filenames + shell. The already-collected run used a short clean slug
  ("Food & Staples" → `food`). The commands below pass explicit short slugs to match that
  convention; the raw default is noted in the Notes column.
- IFRS 20-F filers (BHP, RIO) report under `ifrs-full/ProfitLoss`, not `us-gaap/NetIncomeLoss`
  (us-gaap NI annual facts = 0). The script has an `ifrs-full/ProfitLoss` fallback for
  net income only; most other metrics are us-gaap-only tags, so these come back sparse →
  excluded from launch baskets as probable skip.
- Foreign local listings (`*.HK`, `*.SS`) and the Glencore ADR (`GLNCY`) are absent from
  the SEC map entirely → skip.

## Plan

| Sector | US tickers for launch | Probable skip | Ready command | Notes |
|---|---|---|---|---|
| REIT | WELL PLD EQIX AMT O DLR VICI | — | `python3 scripts/build_fy_norm.py --sector "REIT" --tickers WELL PLD EQIX AMT O DLR VICI --slug reit` | All 7 in SEC with us-gaap NetIncomeLoss (WELL 26, O 57, PLD 45 annual facts). Default slug already `reit`. REIT caveat: P/E and EV/EBITDA are weak for REITs; P/FFO and P/B are the right multiples. We collect what the script produces now; treat earnings multiples with caution downstream. |
| Medical Services | ABT ISRG SYK MDT BSX TMO ALGN | — | `python3 scripts/build_fy_norm.py --sector "Medical Services" --tickers ABT ISRG SYK MDT BSX TMO ALGN --slug medical_services` | All 7 in SEC, us-gaap (ABT 39, ISRG 51 annual facts). Default slug = `medical_services`. |
| Consumer Discretionary | AMZN HD LOW NKE MCD LULU | — | `python3 scripts/build_fy_norm.py --sector "Consumer Discretionary" --tickers AMZN HD LOW NKE MCD LULU --slug consumer_discretionary` | All 6 in SEC, us-gaap (AMZN 158, HD 59 annual facts). Default slug = `consumer_discretionary`. |
| Telecom & Streaming | NFLX DIS CMCSA VZ T TMUS META SPOT CHTR | — | `python3 scripts/build_fy_norm.py --sector "Telecom & Streaming" --tickers NFLX DIS CMCSA VZ T TMUS META SPOT CHTR --slug telecom` | All 9 in SEC, us-gaap (NFLX 59, TMUS 59 annual facts). Default slug would be `telecom_&_streaming` (ampersand) — passing clean `telecom`. SPOT is a 20-F filer but reports us-gaap; expect it to work. |
| AI Infrastructure | NVDA MSFT GOOG AMZN META AVGO TSM AMD ORCL TSLA | (TSM partial) | `python3 scripts/build_fy_norm.py --sector "AI Infrastructure" --tickers NVDA MSFT GOOG AMZN META AVGO TSM AMD ORCL TSLA --slug ai_infrastructure` | All 10 in SEC. NVDA/MSFT/ORCL etc. us-gaap healthy. TSM is IFRS (handled via ifrs-full fallback + PREFERRED_CCY USD in the script, same as Semiconductors run) — keep it. Default slug = `ai_infrastructure`. |
| Agriculture & Chemicals | LIN APD SHW ECL CTVA NTR FMC | — | `python3 scripts/build_fy_norm.py --sector "Agriculture & Chemicals" --tickers LIN APD SHW ECL CTVA NTR FMC --slug agriculture_chemicals` | All 7 in SEC, us-gaap (LIN 29, APD 54, CTVA 20 annual facts). Default slug would be `agriculture_&_chemicals` (ampersand) — passing clean `agriculture_chemicals`. |
| Solar | FSLR NXT ENPH SEDG RUN CSIQ SHLS | — | `python3 scripts/build_fy_norm.py --sector "Solar" --tickers FSLR NXT ENPH SEDG RUN CSIQ SHLS --slug solar` | All 7 in SEC, us-gaap (FSLR 51, ENPH 42, NXT 12 annual facts). Default slug = `solar`. Several names are loss-making in parts of FY21–25, so P/E will be noisy/negative — expected for the sector. |
| Insurance | UNH BRK-B PGR CB AIG MRSH ALL | — | `python3 scripts/build_fy_norm.py --sector "Insurance" --tickers UNH BRK-B PGR CB AIG MRSH ALL --slug insurance` | Config has `BRK.B`→ use `BRK-B`; config has `MMC`→ SEC ticker is `MRSH` (Marsh & McLennan, CIK 62709). Both healthy us-gaap (BRK-B 51, UNH 54). Other 5 in SEC us-gaap. BRK-B is a conglomerate, not a pure insurer — its multiples will skew the basket; treat as a special member. Default slug = `insurance`. |
| China | BABA PDD JD | 700.HK 1810.HK 1398.HK 600519.SS | `python3 scripts/build_fy_norm.py --sector "China" --tickers BABA PDD JD --slug china` | Only 3 of 7 are in SEC (US ADRs, 20-F but file us-gaap: BABA 15, PDD 8, JD 3 annual facts). HK/SS local listings absent from SEC → skip. Thin basket (3 names) — sector norm will be low-confidence. Default slug = `china`. |
| Commodities | FCX SCCO ALB NEM GOLD | BHP RIO GLNCY | `python3 scripts/build_fy_norm.py --sector "Commodities" --tickers FCX SCCO ALB NEM GOLD --slug commodities` | FCX/SCCO/ALB/NEM/GOLD = us-gaap (SCCO 14, NEM 60, ALB 54, GOLD 15). BHP & RIO report IFRS only (us-gaap NI annual=0; ifrs-full ProfitLoss 27/30) → most metrics sparse → skip from basket. GLNCY (Glencore ADR) not in SEC map → skip. Default slug = `commodities`. |
| Delivery & Logistics | UPS FDX UBER DASH XPO AMZN | — | `python3 scripts/build_fy_norm.py --sector "Delivery & Logistics" --tickers UPS FDX UBER DASH XPO AMZN --slug delivery_logistics` | All 6 in SEC, us-gaap (UPS 51, FDX 51 annual facts). DASH/UBER recently IPO'd → fewer/younger annual facts but us-gaap present. Default slug would be `delivery_&_logistics` (ampersand) — passing clean `delivery_logistics`. |

## Summary

- Ready-to-run sectors: 11 of 11 (each has ≥3 usable US/us-gaap tickers).
- Total US tickers across all launch commands: 74 (with duplicates across sectors,
  e.g. AMZN/META/TSM appear in several). Distinct symbols: 71.
- Thin / low-confidence baskets: **China** (only 3 US tickers after dropping HK/SS),
  **Commodities** (5 after dropping BHP/RIO/GLNCY).
- Symbol fixes vs config: `MMC`→`MRSH`, `BRK.B`→`BRK-B`.
- Sector-quality caveats: REIT (earnings multiples weak; P/FFO & P/B preferred),
  Insurance (BRK-B is a conglomerate, not a pure insurer), Solar (loss-making years).
