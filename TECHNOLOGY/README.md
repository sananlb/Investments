# Technology

Large-cap technology, software, cloud, platforms, consulting and payments.

Группа в TradingView: `Tehnology`.

## Ключевые компании

- [AAPL](AAPL.md) - Apple: consumer hardware ecosystem.
- [MSFT](MSFT.md) - Microsoft: cloud, enterprise software, AI.
- [GOOG](GOOG.md) - Alphabet: search, cloud, AI.
- [AMZN](AMZN.md) - Amazon: AWS and e-commerce platform.
- [META](META.md) - Meta Platforms: social platforms and AI.
- [ADBE](ADBE.md) - Adobe: creative software and digital media.
- [CRM](CRM.md) - Salesforce: enterprise SaaS.
- [NOW](NOW.md) - ServiceNow: workflow automation SaaS.
- [ACN](ACN.md) - Accenture: IT consulting and implementation.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `AAPL`, `MSFT`, `GOOG`, `META`, `ADBE`, `CRM`, `NOW`, `ACN`, `IBM`.

ETF-proxy для декадного масштабирования: `XLK`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Technology sector_score =
0.30 x Forward P/E coefficient
+ 0.20 x P/E coefficient
+ 0.20 x EV/EBITDA coefficient
+ 0.20 x P/S coefficient
+ 0.10 x P/FCF coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| Forward P/E | `0.799` | 30% | 9 |
| P/E | `0.694` | 20% | 9 |
| EV/EBITDA | `0.854` | 20% | 9 |
| P/S | `0.927` | 20% | 9 |
| P/FCF | `1.008` | 10% | 9 |
| Итоговый sector_score | `0.84` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Technology` равна `0.84` относительно собственной 5-летней нормы. Это valuation-only слой; large-cap tech/software basket; AI capex, cloud growth and EPS revisions not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | Forward P/E curr / avg / coeff | P/E curr / avg / coeff | EV/EBITDA curr / avg / coeff | P/S curr / avg / coeff | P/FCF curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `AAPL` | 34.24 / 28.42 / `1.20` | 37.83 / 30.08 / `1.26` | 28.26 / 22.58 / `1.25` | 10.15 / 7.50 / `1.35` | 35.48 / 28.81 / `1.23` |
| `MSFT` | 24.36 / 32.23 / `0.76` | 26.82 / 33.96 / `0.79` | 18.39 / 23.01 / `0.80` | 10.51 / 12.08 / `0.87` | 45.87 / 40.95 / `1.12` |
| `GOOG` | 30.04 / 23.53 / `1.28` | 28.63 / 24.44 / `1.17` | 28.24 / 18.40 / `1.53` | 10.86 / 6.65 / `1.63` | 71.19 / 31.32 / `2.27` |
| `META` | 19.27 / 21.68 / `0.89` | 23.01 / 22.98 / `1.00` | 14.74 / 14.56 / `1.01` | 7.47 / 6.91 / `1.08` | 33.27 / 24.84 / `1.34` |
| `ADBE` | 10.76 / 28.70 / `0.37` | 15.11 / 41.61 / `0.36` | 10.99 / 29.37 / `0.37` | 4.28 / 11.60 / `0.37` | 10.16 / 29.27 / `0.35` |
| `CRM` | 13.74 / 32.96 / `0.42` | 22.18 / 220.98 / `0.10` | 14.52 / 27.03 / `0.54` | 3.65 / 7.04 / `0.52` | 10.68 / 27.70 / `0.39` |
| `NOW` | 28.68 / 61.64 / `0.47` | 74.04 / 229.54 / `0.32` | 42.52 / 81.61 / `0.52` | 9.19 / 16.20 / `0.57` | 27.68 / 52.18 / `0.53` |
| `ACN` | 13.07 / 26.78 / `0.49` | 15.33 / 29.00 / `0.53` | 8.94 / 17.14 / `0.52` | 1.59 / 3.19 / `0.50` | 9.19 / 21.66 / `0.42` |
| `IBM` | 23.65 / 17.93 / `1.32` | 26.38 / 36.94 / `0.71` | 20.34 / 17.99 / `1.13` | 4.06 / 2.80 / `1.45` | 21.68 / 15.28 / `1.42` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `XLK`.

| Якорная дата | Фактическое закрытие | XLK close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 138.76 | `0.7264` |
| 2026-03-10 | 2026-03-10 | 139.76 | `0.7317` |
| 2026-03-20 | 2026-03-20 | 135.29 | `0.7083` |
| 2026-03-30 | 2026-03-30 | 127.50 | `0.6675` |
| 2026-04-10 | 2026-04-10 | 142.62 | `0.7466` |
| 2026-04-20 | 2026-04-20 | 154.56 | `0.8091` |
| 2026-04-30 | 2026-04-30 | 159.50 | `0.8350` |
| 2026-05-10 | 2026-05-08 | 175.52 | `0.9189` |
| 2026-05-20 | 2026-05-20 | 177.14 | `0.9273` |
| 2026-05-30 | 2026-05-29 | 191.02 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: XLK history](https://stockanalysis.com/etf/xlk/history/) |
| `AAPL` ratios | [StockAnalysis](https://stockanalysis.com/stocks/aapl/financials/ratios/) |
| `MSFT` ratios | [StockAnalysis](https://stockanalysis.com/stocks/msft/financials/ratios/) |
| `GOOG` ratios | [StockAnalysis](https://stockanalysis.com/stocks/goog/financials/ratios/) |
| `META` ratios | [StockAnalysis](https://stockanalysis.com/stocks/meta/financials/ratios/) |
| `ADBE` ratios | [StockAnalysis](https://stockanalysis.com/stocks/adbe/financials/ratios/) |
| `CRM` ratios | [StockAnalysis](https://stockanalysis.com/stocks/crm/financials/ratios/) |
| `NOW` ratios | [StockAnalysis](https://stockanalysis.com/stocks/now/financials/ratios/) |
| `ACN` ratios | [StockAnalysis](https://stockanalysis.com/stocks/acn/financials/ratios/) |
| `IBM` ratios | [StockAnalysis](https://stockanalysis.com/stocks/ibm/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `AAPL`, `MSFT`, `GOOG`, `META`, `ADBE`, `CRM`, `NOW`, `ACN`, `IBM`.
2. Взять текущие `Forward P/E`, `P/E`, `EV/EBITDA`, `P/S`, `P/FCF`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `XLK` на последний торговый день до якоря.

## Компании и инструменты

- [AAPL](AAPL.md)
- [ACN](ACN.md)
- [ADBE](ADBE.md)
- [AMZN](AMZN.md)
- [CRM](CRM.md)
- [GOOG](GOOG.md)
- [IBM](IBM.md)
- [META](META.md)
- [MSFT](MSFT.md)
- [NOW](NOW.md)
- [PAYC](PAYC.md)
- [PYPL](PYPL.md)
- [TSLA](TSLA.md)
