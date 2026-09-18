# REIT

Real estate investment trusts: logistics, data centers, towers, healthcare, net lease and retail.

Группа в TradingView: `Reit`.

## Ключевые компании

- [WELL](WELL.md) - Welltower: healthcare/senior housing REIT leader.
- [PLD](PLD.md) - Prologis: logistics real estate leader.
- [EQIX](EQIX.md) - Equinix: data center REIT.
- [AMT](AMT.md) - American Tower: tower REIT.
- [O](O.md) - Realty Income: net lease REIT benchmark.
- [DLR](DLR.md) - Digital Realty: data center REIT peer.
- [VICI](VICI.md) - VICI Properties: gaming and experiential real estate.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `WELL`, `PLD`, `EQIX`, `AMT`, `O`, `DLR`, `VICI`.

ETF-proxy для декадного масштабирования: `VNQ`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
REIT sector_score =
0.36 x Dividend Yield coefficient
+ 0.29 x P/B coefficient
+ 0.21 x EV/EBITDA coefficient
+ 0.14 x P/S coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| Dividend Yield | `1.085` | 36% | 7 |
| P/B | `1.176` | 29% | 6 |
| EV/EBITDA | `0.997` | 21% | 7 |
| P/S | `1.000` | 14% | 7 |
| Итоговый sector_score | `1.08` | 100% |  |

Вывод по первой версии: текущая оценка корзины `REIT` равна `1.08` относительно собственной 5-летней нормы. Это valuation-only слой; P/FFO and NAV discount are not available from this source, so P/FCF, yield and balance-sheet proxies are used.

Ограничение данных: метрики без валидных положительных значений были исключены и веса были нормализованы по доступным метрикам. В этой версии исключены: P/FCF.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | Dividend Yield curr / avg / coeff | P/B curr / avg / coeff | EV/EBITDA curr / avg / coeff | P/S curr / avg / coeff |
|---|---:|---:|---:|---:|
| `WELL` | 1.44 / 2.57 / `1.78` | 3.30 / 2.27 / `1.46` | 53.61 / 35.78 / `1.50` | 12.32 / 8.64 / `1.43` |
| `PLD` | 2.98 / 2.75 / `0.92` | 2.50 / 2.41 / `1.04` | 26.08 / 31.09 / `0.84` | 14.57 / 16.88 / `0.86` |
| `EQIX` | 1.93 / 1.88 / `0.98` | 7.37 / 6.10 / `1.21` | 29.73 / 28.17 / `1.06` | 11.06 / 9.57 / `1.16` |
| `AMT` | 3.83 / 2.95 / `0.77` | 24.73 / 23.14 / `1.07` | 18.69 / 23.83 / `0.78` | 8.05 / 10.14 / `0.79` |
| `O` | 5.30 / 5.09 / `0.96` | 1.46 / 1.41 / `1.04` | 16.67 / 22.29 / `0.75` | 9.67 / 12.33 / `0.78` |
| `DLR` | 2.57 / 3.55 / `1.38` | 2.93 / 2.35 / `1.25` | 29.41 / 21.93 / `1.34` | 10.76 / 8.94 / `1.20` |
| `VICI` | 6.38 / 5.12 / `0.80` | n/a | 12.04 / 16.85 / `0.71` | 7.63 / 9.85 / `0.77` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `VNQ`.

| Якорная дата | Фактическое закрытие | VNQ close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 95.69 | `0.9999` |
| 2026-03-10 | 2026-03-10 | 93.62 | `0.9783` |
| 2026-03-20 | 2026-03-20 | 88.75 | `0.9274` |
| 2026-03-30 | 2026-03-30 | 87.33 | `0.9125` |
| 2026-04-10 | 2026-04-10 | 92.98 | `0.9716` |
| 2026-04-20 | 2026-04-20 | 97.03 | `1.0139` |
| 2026-04-30 | 2026-04-30 | 96.33 | `1.0066` |
| 2026-05-10 | 2026-05-08 | 96.62 | `1.0096` |
| 2026-05-20 | 2026-05-20 | 96.49 | `1.0083` |
| 2026-05-30 | 2026-05-29 | 95.70 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: VNQ history](https://stockanalysis.com/etf/vnq/history/) |
| `WELL` ratios | [StockAnalysis](https://stockanalysis.com/stocks/well/financials/ratios/) |
| `PLD` ratios | [StockAnalysis](https://stockanalysis.com/stocks/pld/financials/ratios/) |
| `EQIX` ratios | [StockAnalysis](https://stockanalysis.com/stocks/eqix/financials/ratios/) |
| `AMT` ratios | [StockAnalysis](https://stockanalysis.com/stocks/amt/financials/ratios/) |
| `O` ratios | [StockAnalysis](https://stockanalysis.com/stocks/o/financials/ratios/) |
| `DLR` ratios | [StockAnalysis](https://stockanalysis.com/stocks/dlr/financials/ratios/) |
| `VICI` ratios | [StockAnalysis](https://stockanalysis.com/stocks/vici/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `WELL`, `PLD`, `EQIX`, `AMT`, `O`, `DLR`, `VICI`.
2. Взять текущие `Dividend Yield`, `P/B`, `EV/EBITDA`, `P/S`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `VNQ` на последний торговый день до якоря.

## Компании и инструменты

- [AMT](AMT.md)
- [DLR](DLR.md)
- [EQIX](EQIX.md)
- [O](O.md)
- [PLD](PLD.md)
- [VICI](VICI.md)
- [WELL](WELL.md)
