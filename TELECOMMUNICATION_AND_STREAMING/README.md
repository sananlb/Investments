# Telecommunication And Streaming

Telecom operators, broadband, streaming, media platforms and content distribution.

Группа в TradingView: `Telecomunication and streaming`.

## Ключевые компании

- [NFLX](NFLX.md) - Netflix: streaming leader.
- [DIS](DIS.md) - Disney: content, parks and streaming.
- [CMCSA](CMCSA.md) - Comcast: cable, broadband and media.
- [VZ](VZ.md) - Verizon: US telecom operator.
- [T](T.md) - AT&T: US telecom operator.
- [TMUS](TMUS.md) - T-Mobile US: wireless growth leader.
- [META](META.md) - Meta Platforms: social media and video distribution.
- [SPOT](SPOT.md) - Spotify: audio streaming.
- [CHTR](CHTR.md) - Charter Communications: cable and broadband.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `NFLX`, `DIS`, `CMCSA`, `VZ`, `T`, `TMUS`, `META`, `SPOT`, `CHTR`.

ETF-proxy для декадного масштабирования: `XLC`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Telecom & Streaming sector_score =
0.30 x EV/EBITDA coefficient
+ 0.25 x Forward P/E coefficient
+ 0.20 x P/E coefficient
+ 0.15 x P/S coefficient
+ 0.10 x P/FCF coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| EV/EBITDA | `0.746` | 30% | 9 |
| Forward P/E | `0.735` | 25% | 9 |
| P/E | `0.626` | 20% | 9 |
| P/S | `0.912` | 15% | 9 |
| P/FCF | `0.646` | 10% | 9 |
| Итоговый sector_score | `0.73` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Telecom & Streaming` равна `0.73` относительно собственной 5-летней нормы. Это valuation-only слой; mixes telecom, streaming and communication platforms; subscriber growth, ARPU and content/capex intensity not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | EV/EBITDA curr / avg / coeff | Forward P/E curr / avg / coeff | P/E curr / avg / coeff | P/S curr / avg / coeff | P/FCF curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `NFLX` | 25.66 / 32.37 / `0.79` | 25.87 / 37.14 / `0.70` | 27.79 / 41.18 / `0.67` | 7.72 / 7.59 / `1.02` | 30.45 / 52.12 / `0.58` |
| `DIS` | 11.08 / 21.95 / `0.50` | 13.65 / 22.98 / `0.59` | 16.27 / 66.20 / `0.25` | 1.82 / 2.48 / `0.73` | 24.87 / 77.58 / `0.32` |
| `CMCSA` | 4.92 / 7.23 / `0.68` | 7.00 / 10.14 / `0.69` | 4.85 / 14.38 / `0.34` | 0.71 / 1.33 / `0.53` | 4.36 / 9.31 / `0.47` |
| `VZ` | 7.66 / 7.12 / `1.08` | 9.53 / 8.62 / `1.11` | 11.64 / 10.19 / `1.14` | 1.43 / 1.30 / `1.10` | 9.85 / 9.69 / `1.02` |
| `T` | 7.21 / 9.91 / `0.73` | 10.54 / 8.71 / `1.21` | 8.29 / 9.69 / `0.86` | 1.36 / 1.16 / `1.17` | 9.93 / 7.86 / `1.26` |
| `TMUS` | 9.49 / 11.41 / `0.83` | 16.42 / 24.25 / `0.68` | 19.93 / 36.59 / `0.54` | 2.24 / 2.41 / `0.93` | 11.15 / 41.14 / `0.27` |
| `META` | 14.74 / 14.56 / `1.01` | 19.27 / 21.68 / `0.89` | 23.01 / 22.98 / `1.00` | 7.47 / 6.91 / `1.08` | 33.27 / 24.84 / `1.34` |
| `SPOT` | 33.91 / 88.95 / `0.38` | 32.88 / 70.57 / `0.47` | 33.50 / 62.63 / `0.53` | 5.06 / 3.87 / `1.31` | 27.68 / 188.86 / `0.15` |
| `CHTR` | 5.29 / 7.46 / `0.71` | 3.27 / 11.53 / `0.28` | 3.89 / 13.24 / `0.29` | 0.37 / 1.11 / `0.33` | 4.95 / 12.16 / `0.41` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `XLC`.

| Якорная дата | Фактическое закрытие | XLC close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 118.05 | `1.0204` |
| 2026-03-10 | 2026-03-10 | 117.38 | `1.0146` |
| 2026-03-20 | 2026-03-20 | 112.23 | `0.9701` |
| 2026-03-30 | 2026-03-30 | 107.96 | `0.9332` |
| 2026-04-10 | 2026-04-10 | 113.95 | `0.9850` |
| 2026-04-20 | 2026-04-20 | 118.75 | `1.0264` |
| 2026-04-30 | 2026-04-30 | 116.51 | `1.0071` |
| 2026-05-10 | 2026-05-08 | 116.94 | `1.0108` |
| 2026-05-20 | 2026-05-20 | 116.10 | `1.0035` |
| 2026-05-30 | 2026-05-29 | 115.69 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: XLC history](https://stockanalysis.com/etf/xlc/history/) |
| `NFLX` ratios | [StockAnalysis](https://stockanalysis.com/stocks/nflx/financials/ratios/) |
| `DIS` ratios | [StockAnalysis](https://stockanalysis.com/stocks/dis/financials/ratios/) |
| `CMCSA` ratios | [StockAnalysis](https://stockanalysis.com/stocks/cmcsa/financials/ratios/) |
| `VZ` ratios | [StockAnalysis](https://stockanalysis.com/stocks/vz/financials/ratios/) |
| `T` ratios | [StockAnalysis](https://stockanalysis.com/stocks/t/financials/ratios/) |
| `TMUS` ratios | [StockAnalysis](https://stockanalysis.com/stocks/tmus/financials/ratios/) |
| `META` ratios | [StockAnalysis](https://stockanalysis.com/stocks/meta/financials/ratios/) |
| `SPOT` ratios | [StockAnalysis](https://stockanalysis.com/stocks/spot/financials/ratios/) |
| `CHTR` ratios | [StockAnalysis](https://stockanalysis.com/stocks/chtr/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `NFLX`, `DIS`, `CMCSA`, `VZ`, `T`, `TMUS`, `META`, `SPOT`, `CHTR`.
2. Взять текущие `EV/EBITDA`, `Forward P/E`, `P/E`, `P/S`, `P/FCF`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `XLC` на последний торговый день до якоря.

## Компании и инструменты

- [AKAM](AKAM.md)
- [CHTR](CHTR.md)
- [CMCSA](CMCSA.md)
- [DIS](DIS.md)
- [META](META.md)
- [NFLX](NFLX.md)
- [ROKU](ROKU.md)
- [SPOT](SPOT.md)
- [T](T.md)
- [TMUS](TMUS.md)
- [VZ](VZ.md)
