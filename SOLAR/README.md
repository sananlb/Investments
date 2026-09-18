# Solar

Solar manufacturers, inverters, trackers, installers and renewable energy exposure.

Группа в TradingView: `Solar`.

## Ключевые компании

- [FSLR](FSLR.md) - First Solar: US solar module leader.
- [NXT](NXT.md) - Nextracker: utility-scale solar tracker leader.
- [ENPH](ENPH.md) - Enphase Energy: microinverters and residential solar.
- [SEDG](SEDG.md) - SolarEdge: inverters and residential solar.
- [RUN](RUN.md) - Sunrun: US residential solar installer.
- [CSIQ](CSIQ.md) - Canadian Solar: global solar manufacturing and projects.
- [NEE](NEE.md) - NextEra Energy: renewables and utility-scale power.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `FSLR`, `NXT`, `ENPH`, `SEDG`, `RUN`, `CSIQ`, `SHLS`.

ETF-proxy для декадного масштабирования: `TAN`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Solar sector_score =
0.30 x Forward P/E coefficient
+ 0.25 x EV/EBITDA coefficient
+ 0.20 x P/S coefficient
+ 0.15 x P/FCF coefficient
+ 0.10 x P/B coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| Forward P/E | `1.241` | 30% | 7 |
| EV/EBITDA | `0.918` | 25% | 6 |
| P/S | `1.056` | 20% | 7 |
| P/FCF | `1.246` | 15% | 4 |
| P/B | `1.027` | 10% | 7 |
| Итоговый sector_score | `1.10` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Solar` равна `1.10` относительно собственной 5-летней нормы. Это valuation-only слой; solar pilot skips non-positive or unavailable multiples; policy risk, rates, polysilicon/module cycle and bookings not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | Forward P/E curr / avg / coeff | EV/EBITDA curr / avg / coeff | P/S curr / avg / coeff | P/FCF curr / avg / coeff | P/B curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `FSLR` | 15.96 / 23.64 / `0.68` | 13.70 / 20.20 / `0.68` | 6.08 / 4.94 / `1.23` | 19.77 / 23.61 / `0.84` | 3.34 / 2.47 / `1.35` |
| `NXT` | 34.54 / 20.70 / `1.67` | 30.36 / 18.66 / `1.63` | 6.60 / 2.79 / `2.36` | 45.76 / 19.89 / `2.30` | 10.01 / 6.57 / `1.52` |
| `ENPH` | 33.77 / 38.78 / `0.87` | 48.51 / 54.31 / `0.89` | 6.44 / 10.15 / `0.63` | 62.11 / 45.36 / `1.37` | 8.17 / 26.75 / `0.31` |
| `SEDG` | 128.21 / 41.14 / `3.12` | n/a | 3.64 / 3.36 / `1.08` | 59.68 / 124.98 / `0.48` | 11.31 / 5.22 / `2.17` |
| `RUN` | 30.49 / 30.19 / `1.01` | 26.43 / 32.31 / `0.82` | 1.26 / 2.21 / `0.57` | n/a | 1.18 / 0.98 / `1.20` |
| `CSIQ` | 24.29 / 50.72 / `0.48` | 8.14 / 10.02 / `0.81` | 0.24 / 0.26 / `0.93` | n/a | 0.46 / 0.73 / `0.63` |
| `SHLS` | 27.11 / 31.17 / `0.87` | 24.55 / 36.29 / `0.68` | 3.90 / 6.78 / `0.58` | n/a | 3.47 / 217.42 / `0.02` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `TAN`.

| Якорная дата | Фактическое закрытие | TAN close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 55.00 | `0.7439` |
| 2026-03-10 | 2026-03-10 | 54.90 | `0.7426` |
| 2026-03-20 | 2026-03-20 | 55.15 | `0.7460` |
| 2026-03-30 | 2026-03-30 | 52.89 | `0.7154` |
| 2026-04-10 | 2026-04-10 | 55.23 | `0.7471` |
| 2026-04-20 | 2026-04-20 | 55.55 | `0.7514` |
| 2026-04-30 | 2026-04-30 | 58.41 | `0.7901` |
| 2026-05-10 | 2026-05-08 | 61.94 | `0.8378` |
| 2026-05-20 | 2026-05-20 | 62.92 | `0.8511` |
| 2026-05-30 | 2026-05-29 | 73.93 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: TAN history](https://stockanalysis.com/etf/tan/history/) |
| `FSLR` ratios | [StockAnalysis](https://stockanalysis.com/stocks/fslr/financials/ratios/) |
| `NXT` ratios | [StockAnalysis](https://stockanalysis.com/stocks/nxt/financials/ratios/) |
| `ENPH` ratios | [StockAnalysis](https://stockanalysis.com/stocks/enph/financials/ratios/) |
| `SEDG` ratios | [StockAnalysis](https://stockanalysis.com/stocks/sedg/financials/ratios/) |
| `RUN` ratios | [StockAnalysis](https://stockanalysis.com/stocks/run/financials/ratios/) |
| `CSIQ` ratios | [StockAnalysis](https://stockanalysis.com/stocks/csiq/financials/ratios/) |
| `SHLS` ratios | [StockAnalysis](https://stockanalysis.com/stocks/shls/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `FSLR`, `NXT`, `ENPH`, `SEDG`, `RUN`, `CSIQ`, `SHLS`.
2. Взять текущие `Forward P/E`, `EV/EBITDA`, `P/S`, `P/FCF`, `P/B`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `TAN` на последний торговый день до якоря.

## Компании и инструменты

- [CSIQ](CSIQ.md)
- [DQ](DQ.md)
- [ENPH](ENPH.md)
- [FSLR](FSLR.md)
- [FTCI](FTCI.md)
- [NEE](NEE.md)
- [NXT](NXT.md)
- [RUN](RUN.md)
- [SEDG](SEDG.md)
- [SHLS](SHLS.md)
