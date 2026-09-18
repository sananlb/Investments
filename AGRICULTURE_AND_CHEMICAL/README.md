# Agriculture And Chemical

Агрохимия, промышленные газы, specialty chemicals, удобрения и материалы.

Группа в TradingView: `Agroculture and chemical`.

## Ключевые компании

- [LIN](LIN.md) - Linde: крупнейший global industrial gases player.
- [APD](APD.md) - Air Products: industrial gases, hydrogen, крупный peer Linde.
- [SHW](SHW.md) - Sherwin-Williams: лидер coatings and paints.
- [ECL](ECL.md) - Ecolab: water, hygiene, specialty chemicals для промышленности.
- [CTVA](CTVA.md) - Corteva: семена и crop protection.
- [NTR](NTR.md) - Nutrien: fertilizers, potash, retail agriculture.
- [FMC](FMC.md) - FMC: crop protection, агрохимия.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `LIN`, `APD`, `SHW`, `ECL`, `CTVA`, `NTR`, `FMC`.

ETF-proxy для декадного масштабирования: `XLB`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Agriculture & Chemicals sector_score =
0.25 x P/E coefficient
+ 0.25 x Forward P/E coefficient
+ 0.20 x EV/EBITDA coefficient
+ 0.15 x P/S coefficient
+ 0.15 x P/FCF coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| P/E | `0.953` | 25% | 6 |
| Forward P/E | `0.902` | 25% | 6 |
| EV/EBITDA | `0.959` | 20% | 7 |
| P/S | `0.947` | 15% | 7 |
| P/FCF | `0.867` | 15% | 5 |
| Итоговый sector_score | `0.93` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Agriculture & Chemicals` равна `0.93` относительно собственной 5-летней нормы. Это valuation-only слой; industrial gases, coatings, crop inputs and specialty chemicals; fertilizer cycle and commodity inputs not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | P/E curr / avg / coeff | Forward P/E curr / avg / coeff | EV/EBITDA curr / avg / coeff | P/S curr / avg / coeff | P/FCF curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `LIN` | 33.00 / 35.89 / `0.92` | 27.23 / 26.65 / `1.02` | 18.58 / 18.00 / `1.03` | 6.64 / 5.67 / `1.17` | 45.15 / 33.93 / `1.33` |
| `APD` | 29.36 / 23.75 / `1.24` | 20.23 / 22.39 / `0.90` | 20.51 / 35.71 / `0.57` | 4.98 / 5.01 / `0.99` | n/a |
| `SHW` | 29.16 / 35.74 / `0.82` | 25.59 / 28.63 / `0.89` | 19.50 / 23.33 / `0.84` | 3.11 / 3.58 / `0.87` | 25.65 / 39.74 / `0.65` |
| `ECL` | 34.63 / 41.49 / `0.83` | 29.77 / 33.98 / `0.88` | 19.99 / 22.97 / `0.87` | 4.38 / 4.15 / `1.06` | 38.52 / 39.18 / `0.98` |
| `CTVA` | 42.56 / 37.88 / `1.12` | 21.52 / 18.92 / `1.14` | 12.97 / 12.82 / `1.01` | 2.93 / 2.29 / `1.28` | 25.59 / 48.57 / `0.53` |
| `NTR` | 13.77 / 17.45 / `0.79` | n/a | 8.27 / 7.43 / `1.11` | 1.22 / 1.24 / `0.99` | 13.94 / 16.42 / `0.85` |
| `FMC` | n/a | 7.27 / 12.54 / `0.58` | 17.99 / 14.14 / `1.27` | 0.50 / 1.82 / `0.27` | n/a |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `XLB`.

| Якорная дата | Фактическое закрытие | XLB close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 53.41 | `1.0442` |
| 2026-03-10 | 2026-03-10 | 49.88 | `0.9752` |
| 2026-03-20 | 2026-03-20 | 46.98 | `0.9185` |
| 2026-03-30 | 2026-03-30 | 49.09 | `0.9597` |
| 2026-04-10 | 2026-04-10 | 51.96 | `1.0158` |
| 2026-04-20 | 2026-04-20 | 52.23 | `1.0211` |
| 2026-04-30 | 2026-04-30 | 51.47 | `1.0063` |
| 2026-05-10 | 2026-05-08 | 51.59 | `1.0086` |
| 2026-05-20 | 2026-05-20 | 49.72 | `0.9720` |
| 2026-05-30 | 2026-05-29 | 51.15 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: XLB history](https://stockanalysis.com/etf/xlb/history/) |
| `LIN` ratios | [StockAnalysis](https://stockanalysis.com/stocks/lin/financials/ratios/) |
| `APD` ratios | [StockAnalysis](https://stockanalysis.com/stocks/apd/financials/ratios/) |
| `SHW` ratios | [StockAnalysis](https://stockanalysis.com/stocks/shw/financials/ratios/) |
| `ECL` ratios | [StockAnalysis](https://stockanalysis.com/stocks/ecl/financials/ratios/) |
| `CTVA` ratios | [StockAnalysis](https://stockanalysis.com/stocks/ctva/financials/ratios/) |
| `NTR` ratios | [StockAnalysis](https://stockanalysis.com/stocks/ntr/financials/ratios/) |
| `FMC` ratios | [StockAnalysis](https://stockanalysis.com/stocks/fmc/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `LIN`, `APD`, `SHW`, `ECL`, `CTVA`, `NTR`, `FMC`.
2. Взять текущие `P/E`, `Forward P/E`, `EV/EBITDA`, `P/S`, `P/FCF`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `XLB` на последний торговый день до якоря.

## Компании и инструменты

- [APD](APD.md)
- [CTVA](CTVA.md)
- [ECL](ECL.md)
- [EMN](EMN.md)
- [FMC](FMC.md)
- [LIN](LIN.md)
- [NTR](NTR.md)
- [SHW](SHW.md)
