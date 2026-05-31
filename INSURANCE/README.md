# Insurance

Insurance, health insurance, brokers, P&C, life insurance and diversified insurance holdings.

Группа в TradingView: `Insurance`.

## Ключевые компании

- [UNH](UNH.md) - UnitedHealth Group: health insurance and Optum health services.
- [BRK.B](BRK.B.md) - Berkshire Hathaway: GEICO, reinsurance and insurance float.
- [PGR](PGR.md) - Progressive: US auto insurance leader.
- [CB](CB.md) - Chubb: global property and casualty insurance.
- [AIG](AIG.md) - AIG: large diversified insurer.
- [MMC](MMC.md) - Marsh McLennan: insurance brokerage and risk advisory.
- [ALL](ALL.md) - Allstate: US personal lines insurer.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `UNH`, `BRK.B`, `PGR`, `CB`, `AIG`, `MMC`, `ALL`.

ETF-proxy для декадного масштабирования: `KIE`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Insurance sector_score =
0.35 x P/B coefficient
+ 0.25 x P/E coefficient
+ 0.25 x Forward P/E coefficient
+ 0.15 x P/S coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| P/B | `0.889` | 35% | 6 |
| P/E | `0.870` | 25% | 6 |
| Forward P/E | `0.794` | 25% | 5 |
| P/S | `0.931` | 15% | 6 |
| Итоговый sector_score | `0.87` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Insurance` равна `0.87` относительно собственной 5-летней нормы. Это valuation-only слой; mixes health insurance, P&C, brokers and Berkshire; combined ratio, reserve quality and float/investment income not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | P/B curr / avg / coeff | P/E curr / avg / coeff | Forward P/E curr / avg / coeff | P/S curr / avg / coeff |
|---|---:|---:|---:|---:|
| `UNH` | 3.53 / 5.32 / `0.66` | 28.71 / 26.49 / `1.08` | 20.04 / 20.51 / `0.98` | 0.77 / 1.26 / `0.61` |
| `BRK.B` | 1.40 / 1.44 / `0.97` | 14.12 / 10.74 / `1.32` | n/a | 2.73 / 2.48 / `1.10` |
| `PGR` | 3.47 / 4.51 / `0.77` | 9.68 / 36.13 / `0.27` | 12.02 / 19.35 / `0.62` | 1.24 / 1.53 / `0.81` |
| `CB` | 1.64 / 1.62 / `1.01` | 11.01 / 12.51 / `0.88` | 11.35 / 12.30 / `0.92` | 1.98 / 2.00 / `0.99` |
| `AIG` | 0.98 / 1.01 / `0.97` | 13.04 / 9.75 / `1.34` | 9.05 / 10.91 / `0.83` | 1.47 / 1.49 / `0.99` |
| `MMC` | n/a | n/a | n/a | n/a |
| `ALL` | 1.80 / 1.91 / `0.94` | 4.55 / 13.43 / `0.34` | 7.80 / 12.54 / `0.62` | 0.78 / 0.72 / `1.09` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `KIE`.

| Якорная дата | Фактическое закрытие | KIE close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 58.13 | `1.0538` |
| 2026-03-10 | 2026-03-10 | 56.06 | `1.0163` |
| 2026-03-20 | 2026-03-20 | 54.34 | `0.9851` |
| 2026-03-30 | 2026-03-30 | 54.41 | `0.9864` |
| 2026-04-10 | 2026-04-10 | 55.90 | `1.0134` |
| 2026-04-20 | 2026-04-20 | 58.40 | `1.0587` |
| 2026-04-30 | 2026-04-30 | 57.33 | `1.0393` |
| 2026-05-10 | 2026-05-08 | 56.37 | `1.0219` |
| 2026-05-20 | 2026-05-20 | 57.79 | `1.0477` |
| 2026-05-30 | 2026-05-29 | 55.16 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: KIE history](https://stockanalysis.com/etf/kie/history/) |
| `UNH` ratios | [StockAnalysis](https://stockanalysis.com/stocks/unh/financials/ratios/) |
| `BRK.B` ratios | [StockAnalysis](https://stockanalysis.com/stocks/brk.b/financials/ratios/) |
| `PGR` ratios | [StockAnalysis](https://stockanalysis.com/stocks/pgr/financials/ratios/) |
| `CB` ratios | [StockAnalysis](https://stockanalysis.com/stocks/cb/financials/ratios/) |
| `AIG` ratios | [StockAnalysis](https://stockanalysis.com/stocks/aig/financials/ratios/) |
| `MMC` ratios | [StockAnalysis](https://stockanalysis.com/stocks/mmc/financials/ratios/) |
| `ALL` ratios | [StockAnalysis](https://stockanalysis.com/stocks/all/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `UNH`, `BRK.B`, `PGR`, `CB`, `AIG`, `MMC`, `ALL`.
2. Взять текущие `P/B`, `P/E`, `Forward P/E`, `P/S`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `KIE` на последний торговый день до якоря.

## Компании и инструменты

- [AIG](AIG.md)
- [ALL](ALL.md)
- [BRK.B](BRK.B.md)
- [CB](CB.md)
- [MMC](MMC.md)
- [PGR](PGR.md)
- [UNH](UNH.md)
