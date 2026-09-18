# Food

Food, beverages, restaurants, packaged goods and defensive consumer demand.

Группа в TradingView: `Food`.

## Ключевые компании

- [WMT](WMT.md) - Walmart: largest grocery/retail scale.
- [COST](COST.md) - Costco: membership retail and consumer staples proxy.
- [KO](KO.md) - Coca-Cola: global beverage brand.
- [PEP](PEP.md) - PepsiCo: beverages + snacks.
- [MCD](MCD.md) - McDonald's: global restaurant leader.
- [SBUX](SBUX.md) - Starbucks: global coffee chain.
- [MDLZ](MDLZ.md) - Mondelez: snacks and packaged food.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `WMT`, `COST`, `KO`, `PEP`, `MCD`, `SBUX`, `MDLZ`, `MNST`, `HSY`.

ETF-proxy для декадного масштабирования: `XLP`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Food & Staples sector_score =
0.25 x P/E coefficient
+ 0.25 x Forward P/E coefficient
+ 0.20 x EV/EBITDA coefficient
+ 0.15 x Dividend Yield coefficient
+ 0.15 x P/S coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| P/E | `1.204` | 25% | 9 |
| Forward P/E | `1.035` | 25% | 9 |
| EV/EBITDA | `1.055` | 20% | 9 |
| Dividend Yield | `1.131` | 15% | 8 |
| P/S | `1.017` | 15% | 9 |
| Итоговый sector_score | `1.09` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Food & Staples` равна `1.09` относительно собственной 5-летней нормы. Это valuation-only слой; consumer staples plus restaurants; volume growth, pricing power and commodity inputs not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | P/E curr / avg / coeff | Forward P/E curr / avg / coeff | EV/EBITDA curr / avg / coeff | Dividend Yield curr / avg / coeff | P/S curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `WMT` | 40.75 / 35.15 / `1.16` | 38.81 / 29.33 / `1.32` | 21.99 / 16.27 / `1.35` | 0.86 / 1.23 / `1.43` | 1.27 / 0.89 / `1.42` |
| `COST` | 48.10 / 44.91 / `1.07` | 43.76 / 42.83 / `1.02` | 29.90 / 27.26 / `1.10` | 0.61 / 1.37 / `2.24` | 1.44 / 1.22 / `1.18` |
| `KO` | 24.85 / 25.51 / `0.97` | 23.93 / 23.03 / `1.04` | 22.18 / 24.27 / `0.91` | 2.68 / 2.95 / `1.10` | 6.90 / 6.11 / `1.13` |
| `PEP` | 22.63 / 26.18 / `0.86` | 16.36 / 21.51 / `0.76` | 12.78 / 16.97 / `0.75` | 3.95 / 3.03 / `0.77` | 2.06 / 2.55 / `0.81` |
| `MCD` | 23.01 / 27.00 / `0.85` | 21.11 / 24.84 / `0.85` | 16.95 / 19.51 / `0.87` | 2.66 / 2.18 / `0.82` | 7.23 / 8.28 / `0.87` |
| `SBUX` | 75.68 / 33.79 / `2.24` | 36.37 / 26.82 / `1.36` | 25.16 / 20.38 / `1.23` | 2.50 / 2.29 / `0.91` | 2.94 / 3.23 / `0.91` |
| `MDLZ` | 30.26 / 24.35 / `1.24` | 19.10 / 20.39 / `0.94` | 18.91 / 17.95 / `1.05` | 3.27 / 2.56 / `0.78` | 2.00 / 2.55 / `0.78` |
| `MNST` | 42.55 / 38.95 / `1.09` | 37.44 / 33.32 / `1.12` | 29.50 / 27.57 / `1.07` | n/a | 9.80 / 8.37 / `1.17` |
| `HSY` | 36.12 / 26.86 / `1.34` | 21.69 / 23.92 / `0.91` | 19.53 / 16.95 / `1.15` | 2.99 / 2.97 / `0.99` | 3.28 / 3.73 / `0.88` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `XLP`.

| Якорная дата | Фактическое закрытие | XLP close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 90.01 | `1.0856` |
| 2026-03-10 | 2026-03-10 | 85.72 | `1.0339` |
| 2026-03-20 | 2026-03-20 | 81.29 | `0.9805` |
| 2026-03-30 | 2026-03-30 | 81.88 | `0.9876` |
| 2026-04-10 | 2026-04-10 | 82.37 | `0.9935` |
| 2026-04-20 | 2026-04-20 | 82.39 | `0.9937` |
| 2026-04-30 | 2026-04-30 | 84.31 | `1.0169` |
| 2026-05-10 | 2026-05-08 | 84.18 | `1.0153` |
| 2026-05-20 | 2026-05-20 | 85.52 | `1.0315` |
| 2026-05-30 | 2026-05-29 | 82.91 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: XLP history](https://stockanalysis.com/etf/xlp/history/) |
| `WMT` ratios | [StockAnalysis](https://stockanalysis.com/stocks/wmt/financials/ratios/) |
| `COST` ratios | [StockAnalysis](https://stockanalysis.com/stocks/cost/financials/ratios/) |
| `KO` ratios | [StockAnalysis](https://stockanalysis.com/stocks/ko/financials/ratios/) |
| `PEP` ratios | [StockAnalysis](https://stockanalysis.com/stocks/pep/financials/ratios/) |
| `MCD` ratios | [StockAnalysis](https://stockanalysis.com/stocks/mcd/financials/ratios/) |
| `SBUX` ratios | [StockAnalysis](https://stockanalysis.com/stocks/sbux/financials/ratios/) |
| `MDLZ` ratios | [StockAnalysis](https://stockanalysis.com/stocks/mdlz/financials/ratios/) |
| `MNST` ratios | [StockAnalysis](https://stockanalysis.com/stocks/mnst/financials/ratios/) |
| `HSY` ratios | [StockAnalysis](https://stockanalysis.com/stocks/hsy/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `WMT`, `COST`, `KO`, `PEP`, `MCD`, `SBUX`, `MDLZ`, `MNST`, `HSY`.
2. Взять текущие `P/E`, `Forward P/E`, `EV/EBITDA`, `Dividend Yield`, `P/S`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `XLP` на последний торговый день до якоря.

## Компании и инструменты

- [COST](COST.md)
- [HSY](HSY.md)
- [KO](KO.md)
- [MCD](MCD.md)
- [MDLZ](MDLZ.md)
- [MNST](MNST.md)
- [PEP](PEP.md)
- [SBUX](SBUX.md)
- [WMT](WMT.md)
