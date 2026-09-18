# Commodities

Сырьевые идеи: copper, iron ore, gold, lithium, rare earths and broad commodity cycle.

## Ключевые компании

- [BHP](BHP.md) - BHP Group: diversified mining anchor.
- [RIO](RIO.md) - Rio Tinto: iron ore and copper.
- [FCX](FCX.md) - Freeport-McMoRan: copper and gold.
- [SCCO](SCCO.md) - Southern Copper: copper pure-play.
- [GLN](GLN.md) - Glencore: metals, coal, commodity trading.
- [ALB](ALB.md) - Albemarle: lithium benchmark.
- [NEM](NEM.md) - Newmont: gold miner.
- [GOLD](GOLD.md) - Barrick Gold: gold miner.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `BHP`, `RIO`, `FCX`, `SCCO`, `GLNCY`, `ALB`, `NEM`, `GOLD`.

ETF-proxy для декадного масштабирования: `PICK`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Commodities sector_score =
0.35 x EV/EBITDA coefficient
+ 0.25 x P/FCF coefficient
+ 0.20 x P/B coefficient
+ 0.20 x P/E coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| EV/EBITDA | `1.580` | 35% | 8 |
| P/FCF | `1.359` | 25% | 7 |
| P/B | `1.344` | 20% | 8 |
| P/E | `1.846` | 20% | 7 |
| Итоговый sector_score | `1.53` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Commodities` равна `1.53` относительно собственной 5-летней нормы. Это valuation-only слой; equity proxy overlaps Mining; spot commodity curves, cost curves and NAV models not yet included.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | EV/EBITDA curr / avg / coeff | P/FCF curr / avg / coeff | P/B curr / avg / coeff | P/E curr / avg / coeff |
|---|---:|---:|---:|---:|
| `BHP` | 9.51 / 4.96 / `1.92` | 23.01 / 9.60 / `2.40` | 4.11 / 2.84 / `1.45` | 22.23 / 12.56 / `1.77` |
| `RIO` | 10.03 / 4.06 / `2.47` | 40.99 / 12.07 / `3.40` | 2.75 / 1.61 / `1.71` | 18.49 / 9.61 / `1.92` |
| `FCX` | 10.34 / 8.28 / `1.25` | 53.92 / 53.26 / `1.01` | 4.84 / 3.69 / `1.31` | 34.76 / 25.25 / `1.38` |
| `SCCO` | 18.27 / 11.42 / `1.60` | 37.33 / 23.88 / `1.56` | 13.54 / 7.73 / `1.75` | 32.44 / 21.25 / `1.53` |
| `GLNCY` | 10.61 / 6.79 / `1.56` | n/a | 2.67 / 1.61 / `1.66` | 246.93 / 54.70 / `4.51` |
| `ALB` | 20.35 / 14.72 / `1.38` | 36.16 / 99.57 / `0.36` | 2.73 / 16.84 / `0.16` | n/a |
| `NEM` | 6.96 / 14.89 / `0.47` | 12.69 / 114.74 / `0.11` | 3.37 / 2.08 / `1.62` | 14.27 / 23.62 / `0.60` |
| `GOLD` | 15.78 / 7.93 / `1.99` | 5.93 / 8.84 / `0.67` | 1.42 / 1.30 / `1.09` | 13.77 / 11.42 / `1.21` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `PICK`.

| Якорная дата | Фактическое закрытие | PICK close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 64.34 | `0.9735` |
| 2026-03-10 | 2026-03-10 | 58.77 | `0.8892` |
| 2026-03-20 | 2026-03-20 | 51.83 | `0.7842` |
| 2026-03-30 | 2026-03-30 | 53.93 | `0.8160` |
| 2026-04-10 | 2026-04-10 | 61.29 | `0.9274` |
| 2026-04-20 | 2026-04-20 | 63.39 | `0.9591` |
| 2026-04-30 | 2026-04-30 | 61.60 | `0.9321` |
| 2026-05-10 | 2026-05-08 | 64.83 | `0.9809` |
| 2026-05-20 | 2026-05-20 | 62.69 | `0.9486` |
| 2026-05-30 | 2026-05-29 | 66.09 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: PICK history](https://stockanalysis.com/etf/pick/history/) |
| `BHP` ratios | [StockAnalysis](https://stockanalysis.com/stocks/bhp/financials/ratios/) |
| `RIO` ratios | [StockAnalysis](https://stockanalysis.com/stocks/rio/financials/ratios/) |
| `FCX` ratios | [StockAnalysis](https://stockanalysis.com/stocks/fcx/financials/ratios/) |
| `SCCO` ratios | [StockAnalysis](https://stockanalysis.com/stocks/scco/financials/ratios/) |
| `GLNCY` ratios | [StockAnalysis](https://stockanalysis.com/quote/otc/GLNCY/financials/ratios/) |
| `ALB` ratios | [StockAnalysis](https://stockanalysis.com/stocks/alb/financials/ratios/) |
| `NEM` ratios | [StockAnalysis](https://stockanalysis.com/stocks/nem/financials/ratios/) |
| `GOLD` ratios | [StockAnalysis](https://stockanalysis.com/stocks/gold/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `BHP`, `RIO`, `FCX`, `SCCO`, `GLNCY`, `ALB`, `NEM`, `GOLD`.
2. Взять текущие `EV/EBITDA`, `P/FCF`, `P/B`, `P/E`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `PICK` на последний торговый день до якоря.

## Компании и инструменты

- [ALB](ALB.md)
- [BHP](BHP.md)
- [FCX](FCX.md)
- [GLN](GLN.md)
- [GOLD](GOLD.md)
- [NEM](NEM.md)
- [RIO](RIO.md)
- [SCCO](SCCO.md)
