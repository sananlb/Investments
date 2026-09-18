# Medical Services

Medical devices, diagnostics, healthcare services and medtech leaders.

Группа в TradingView: `medical services`.

## Ключевые компании

- [ABT](ABT.md) - Abbott Laboratories: diagnostics, devices, diversified healthcare.
- [ISRG](ISRG.md) - Intuitive Surgical: robotic surgery leader.
- [SYK](SYK.md) - Stryker: orthopedics and medtech.
- [MDT](MDT.md) - Medtronic: large diversified medtech.
- [BSX](BSX.md) - Boston Scientific: cardiology and medical devices.
- [TMO](TMO.md) - Thermo Fisher: life science tools and diagnostics.
- [ALGN](ALGN.md) - Align Technology: clear aligners and dental tech.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `ABT`, `ISRG`, `SYK`, `MDT`, `BSX`, `TMO`, `ALGN`.

ETF-proxy для декадного масштабирования: `IHI`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Medical Services sector_score =
0.30 x Forward P/E coefficient
+ 0.25 x P/E coefficient
+ 0.20 x EV/EBITDA coefficient
+ 0.15 x P/S coefficient
+ 0.10 x P/FCF coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| Forward P/E | `0.645` | 30% | 7 |
| P/E | `0.679` | 25% | 7 |
| EV/EBITDA | `0.672` | 20% | 7 |
| P/S | `0.679` | 15% | 7 |
| P/FCF | `0.612` | 10% | 7 |
| Итоговый sector_score | `0.66` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Medical Services` равна `0.66` относительно собственной 5-летней нормы. Это valuation-only слой; medtech/services pilot; procedure volumes, reimbursement and product cycles not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | Forward P/E curr / avg / coeff | P/E curr / avg / coeff | EV/EBITDA curr / avg / coeff | P/S curr / avg / coeff | P/FCF curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `ABT` | 15.28 / 25.19 / `0.61` | 23.98 / 29.21 / `0.82` | 14.98 / 19.62 / `0.76` | 3.30 / 4.89 / `0.67` | 20.21 / 30.23 / `0.67` |
| `ISRG` | 39.87 / 60.73 / `0.66` | 51.60 / 74.03 / `0.70` | 37.54 / 54.39 / `0.69` | 14.21 / 19.28 / `0.74` | 53.06 / 110.48 / `0.48` |
| `SYK` | 19.50 / 26.07 / `0.75` | 35.31 / 43.10 / `0.82` | 18.68 / 27.34 / `0.68` | 4.63 / 5.57 / `0.83` | 25.59 / 37.85 / `0.68` |
| `MDT` | 12.67 / 17.65 / `0.72` | 20.62 / 32.33 / `0.64` | 12.11 / 18.33 / `0.66` | 2.67 / 4.11 / `0.65` | 17.52 / 25.33 / `0.69` |
| `BSX` | 14.00 / 27.36 / `0.51` | 20.21 / 67.29 / `0.30` | 14.80 / 29.92 / `0.49` | 3.48 / 6.23 / `0.56` | 20.66 / 50.48 / `0.41` |
| `TMO` | 19.38 / 25.82 / `0.75` | 27.07 / 32.80 / `0.83` | 19.74 / 22.25 / `0.89` | 4.05 / 5.16 / `0.79` | 27.12 / 32.26 / `0.84` |
| `ALGN` | 15.30 / 29.29 / `0.52` | 29.39 / 45.09 / `0.65` | 13.01 / 24.78 / `0.52` | 3.06 / 5.88 / `0.52` | 21.47 / 41.44 / `0.52` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `IHI`.

| Якорная дата | Фактическое закрытие | IHI close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 60.20 | `1.2296` |
| 2026-03-10 | 2026-03-10 | 56.41 | `1.1522` |
| 2026-03-20 | 2026-03-20 | 54.44 | `1.1119` |
| 2026-03-30 | 2026-03-30 | 52.60 | `1.0743` |
| 2026-04-10 | 2026-04-10 | 53.24 | `1.0874` |
| 2026-04-20 | 2026-04-20 | 53.86 | `1.1001` |
| 2026-04-30 | 2026-04-30 | 51.06 | `1.0429` |
| 2026-05-10 | 2026-05-08 | 49.01 | `1.0010` |
| 2026-05-20 | 2026-05-20 | 50.90 | `1.0396` |
| 2026-05-30 | 2026-05-29 | 48.96 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: IHI history](https://stockanalysis.com/etf/ihi/history/) |
| `ABT` ratios | [StockAnalysis](https://stockanalysis.com/stocks/abt/financials/ratios/) |
| `ISRG` ratios | [StockAnalysis](https://stockanalysis.com/stocks/isrg/financials/ratios/) |
| `SYK` ratios | [StockAnalysis](https://stockanalysis.com/stocks/syk/financials/ratios/) |
| `MDT` ratios | [StockAnalysis](https://stockanalysis.com/stocks/mdt/financials/ratios/) |
| `BSX` ratios | [StockAnalysis](https://stockanalysis.com/stocks/bsx/financials/ratios/) |
| `TMO` ratios | [StockAnalysis](https://stockanalysis.com/stocks/tmo/financials/ratios/) |
| `ALGN` ratios | [StockAnalysis](https://stockanalysis.com/stocks/algn/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `ABT`, `ISRG`, `SYK`, `MDT`, `BSX`, `TMO`, `ALGN`.
2. Взять текущие `Forward P/E`, `P/E`, `EV/EBITDA`, `P/S`, `P/FCF`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `IHI` на последний торговый день до якоря.

## Компании и инструменты

- [ABT](ABT.md)
- [ALGN](ALGN.md)
- [BSX](BSX.md)
- [INMD](INMD.md)
- [ISRG](ISRG.md)
- [MDT](MDT.md)
- [SYK](SYK.md)
- [TMO](TMO.md)
