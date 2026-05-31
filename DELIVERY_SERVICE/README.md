# Delivery Service

Parcel delivery, freight, logistics, last-mile delivery and e-commerce logistics.

Группа в TradingView: `Delivery service`.

## Ключевые компании

- [UPS](UPS.md) - UPS: global parcel and ground logistics.
- [FDX](FDX.md) - FedEx: express, freight and global logistics.
- [DHL.DE](DHL.DE.md) - DHL Group: global logistics, express and forwarding.
- [AMZN](AMZN.md) - Amazon: e-commerce logistics and fulfillment network.
- [UBER](UBER.md) - Uber: mobility and delivery network.
- [DASH](DASH.md) - DoorDash: food and local delivery platform.
- [XPO](XPO.md) - XPO: less-than-truckload and freight logistics.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `UPS`, `FDX`, `UBER`, `DASH`, `XPO`, `AMZN`.

ETF-proxy для декадного масштабирования: `IYT`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Delivery & Logistics sector_score =
0.30 x EV/EBITDA coefficient
+ 0.25 x Forward P/E coefficient
+ 0.20 x P/E coefficient
+ 0.15 x P/S coefficient
+ 0.10 x P/FCF coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| EV/EBITDA | `0.947` | 30% | 6 |
| Forward P/E | `0.948` | 25% | 6 |
| P/E | `1.004` | 20% | 6 |
| P/S | `1.251` | 15% | 6 |
| P/FCF | `0.662` | 10% | 5 |
| Итоговый sector_score | `0.98` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Delivery & Logistics` равна `0.98` относительно собственной 5-летней нормы. Это valuation-only слой; mixes parcel, freight, last-mile platforms and Amazon logistics; volumes, fuel and labor costs not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | EV/EBITDA curr / avg / coeff | Forward P/E curr / avg / coeff | P/E curr / avg / coeff | P/S curr / avg / coeff | P/FCF curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `UPS` | 9.59 / 10.81 / `0.89` | 14.18 / 15.65 / `0.91` | 17.26 / 16.35 / `1.06` | 1.03 / 1.40 / `0.73` | 20.08 / 18.93 / `1.06` |
| `FDX` | 11.42 / 9.37 / `1.22` | 19.47 / 12.56 / `1.55` | 21.91 / 14.73 / `1.49` | 1.07 / 0.71 / `1.52` | 22.48 / 19.32 / `1.16` |
| `UBER` | 20.76 / 44.75 / `0.46` | 19.18 / 38.26 / `0.50` | 17.40 / 33.76 / `0.52` | 2.67 / 3.16 / `0.84` | 14.62 / 50.21 / `0.29` |
| `DASH` | 49.75 / 87.25 / `0.57` | 28.39 / 97.52 / `0.29` | 75.93 / 342.39 / `0.22` | 4.71 / 6.36 / `0.74` | 32.28 / 59.48 / `0.54` |
| `XPO` | 22.40 / 14.07 / `1.59` | 42.73 / 23.56 / `1.81` | 73.59 / 36.69 / `2.01` | 3.03 / 1.28 / `2.37` | 54.92 / 220.29 / `0.25` |
| `AMZN` | 19.27 / 20.35 / `0.95` | 32.45 / 51.78 / `0.63` | 32.37 / 43.93 / `0.74` | 3.92 / 3.02 / `1.30` | n/a |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `IYT`.

| Якорная дата | Фактическое закрытие | IYT close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 81.78 | `0.9753` |
| 2026-03-10 | 2026-03-10 | 75.84 | `0.9045` |
| 2026-03-20 | 2026-03-20 | 73.08 | `0.8716` |
| 2026-03-30 | 2026-03-30 | 72.18 | `0.8608` |
| 2026-04-10 | 2026-04-10 | 77.37 | `0.9227` |
| 2026-04-20 | 2026-04-20 | 82.41 | `0.9828` |
| 2026-04-30 | 2026-04-30 | 81.27 | `0.9692` |
| 2026-05-10 | 2026-05-08 | 80.78 | `0.9634` |
| 2026-05-20 | 2026-05-20 | 81.46 | `0.9715` |
| 2026-05-30 | 2026-05-29 | 83.85 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: IYT history](https://stockanalysis.com/etf/iyt/history/) |
| `UPS` ratios | [StockAnalysis](https://stockanalysis.com/stocks/ups/financials/ratios/) |
| `FDX` ratios | [StockAnalysis](https://stockanalysis.com/stocks/fdx/financials/ratios/) |
| `UBER` ratios | [StockAnalysis](https://stockanalysis.com/stocks/uber/financials/ratios/) |
| `DASH` ratios | [StockAnalysis](https://stockanalysis.com/stocks/dash/financials/ratios/) |
| `XPO` ratios | [StockAnalysis](https://stockanalysis.com/stocks/xpo/financials/ratios/) |
| `AMZN` ratios | [StockAnalysis](https://stockanalysis.com/stocks/amzn/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `UPS`, `FDX`, `UBER`, `DASH`, `XPO`, `AMZN`.
2. Взять текущие `EV/EBITDA`, `Forward P/E`, `P/E`, `P/S`, `P/FCF`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `IYT` на последний торговый день до якоря.

## Компании и инструменты

- [AMZN](AMZN.md)
- [DASH](DASH.md)
- [DHL.DE](DHL.DE.md)
- [FDX](FDX.md)
- [UBER](UBER.md)
- [UPS](UPS.md)
- [XPO](XPO.md)
