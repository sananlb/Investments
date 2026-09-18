# Drugs

Фармацевтика, biotech, obesity drugs, oncology, immunology and large pharma.

Группа в TradingView: `Drugs`.

## Ключевые компании

- [LLY](LLY.md) - Eli Lilly: obesity/diabetes leader, large pharma growth.
- [JNJ](JNJ.md) - Johnson & Johnson: diversified pharma and medtech.
- [MRK](MRK.md) - Merck: oncology, Keytruda franchise.
- [ABBV](ABBV.md) - AbbVie: immunology and pharma cash flow.
- [PFE](PFE.md) - Pfizer: large pharma, post-COVID reset.
- [NVO](NVO.md) - Novo Nordisk: GLP-1 obesity/diabetes leader.
- [NVS](NVS.md) - Novartis: global pharma.
- [RHHBY](RHHBY.md) - Roche: oncology and diagnostics.
- [AZN](AZN.md) - AstraZeneca: oncology and global pharma growth.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `LLY`, `JNJ`, `MRK`, `ABBV`, `PFE`, `NVO`, `NVS`, `AZN`.

ETF-proxy для декадного масштабирования: `XLV`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Drugs sector_score =
0.30 x Forward P/E coefficient
+ 0.25 x P/E coefficient
+ 0.20 x EV/EBITDA coefficient
+ 0.15 x P/FCF coefficient
+ 0.10 x P/S coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| Forward P/E | `1.035` | 30% | 5 |
| P/E | `0.796` | 25% | 8 |
| EV/EBITDA | `0.714` | 20% | 8 |
| P/FCF | `0.886` | 15% | 8 |
| P/S | `0.908` | 10% | 8 |
| Итоговый sector_score | `0.88` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Drugs` равна `0.88` относительно собственной 5-летней нормы. Это valuation-only слой; large pharma basket; pipeline rNPV, patent cliffs and clinical/regulatory risk not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | Forward P/E curr / avg / coeff | P/E curr / avg / coeff | EV/EBITDA curr / avg / coeff | P/FCF curr / avg / coeff | P/S curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `LLY` | 29.72 / 40.17 / `0.74` | 39.25 / 62.28 / `0.63` | 28.25 / 45.19 / `0.63` | 83.34 / 210.42 / `0.40` | 13.64 / 13.17 / `1.04` |
| `JNJ` | 19.09 / 16.51 / `1.16` | 26.09 / 20.62 / `1.27` | 16.76 / 15.15 / `1.11` | 27.68 / 22.63 / `1.22` | 5.63 / 5.02 / `1.12` |
| `MRK` | 19.22 / 13.42 / `1.43` | 33.20 / 168.63 / `0.20` | 11.40 / 19.71 / `0.58` | 20.77 / 20.87 / `1.00` | 4.46 / 4.25 / `1.05` |
| `ABBV` | 14.58 / 13.62 / `1.07` | 107.25 / 54.70 / `1.96` | 14.98 / 15.84 / `0.95` | 19.25 / 15.07 / `1.28` | 6.12 / 5.28 / `1.16` |
| `PFE` | 9.19 / 11.83 / `0.78` | 19.98 / 27.93 / `0.72` | 7.89 / 15.18 / `0.52` | 15.73 / 17.39 / `0.90` | 2.36 / 2.85 / `0.83` |
| `NVO` | n/a | 10.78 / 30.52 / `0.35` | 8.29 / 21.73 / `0.38` | 21.52 / 33.06 / `0.65` | 4.01 / 10.28 / `0.39` |
| `NVS` | n/a | 20.39 / 16.99 / `1.20` | 13.85 / 12.28 / `1.13` | 15.74 / 13.81 / `1.14` | 4.88 / 4.24 / `1.15` |
| `AZN` | n/a | 27.77 / 641.48 / `0.04` | 15.75 / 36.86 / `0.43` | 25.54 / 51.07 / `0.50` | 4.77 / 8.99 / `0.53` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `XLV`.

| Якорная дата | Фактическое закрытие | XLV close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 160.20 | `1.0718` |
| 2026-03-10 | 2026-03-10 | 153.15 | `1.0246` |
| 2026-03-20 | 2026-03-20 | 145.33 | `0.9723` |
| 2026-03-30 | 2026-03-30 | 143.82 | `0.9622` |
| 2026-04-10 | 2026-04-10 | 147.31 | `0.9855` |
| 2026-04-20 | 2026-04-20 | 147.42 | `0.9863` |
| 2026-04-30 | 2026-04-30 | 145.99 | `0.9767` |
| 2026-05-10 | 2026-05-08 | 143.49 | `0.9600` |
| 2026-05-20 | 2026-05-20 | 147.13 | `0.9843` |
| 2026-05-30 | 2026-05-29 | 149.47 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: XLV history](https://stockanalysis.com/etf/xlv/history/) |
| `LLY` ratios | [StockAnalysis](https://stockanalysis.com/stocks/lly/financials/ratios/) |
| `JNJ` ratios | [StockAnalysis](https://stockanalysis.com/stocks/jnj/financials/ratios/) |
| `MRK` ratios | [StockAnalysis](https://stockanalysis.com/stocks/mrk/financials/ratios/) |
| `ABBV` ratios | [StockAnalysis](https://stockanalysis.com/stocks/abbv/financials/ratios/) |
| `PFE` ratios | [StockAnalysis](https://stockanalysis.com/stocks/pfe/financials/ratios/) |
| `NVO` ratios | [StockAnalysis](https://stockanalysis.com/stocks/nvo/financials/ratios/) |
| `NVS` ratios | [StockAnalysis](https://stockanalysis.com/stocks/nvs/financials/ratios/) |
| `AZN` ratios | [StockAnalysis](https://stockanalysis.com/stocks/azn/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `LLY`, `JNJ`, `MRK`, `ABBV`, `PFE`, `NVO`, `NVS`, `AZN`.
2. Взять текущие `Forward P/E`, `P/E`, `EV/EBITDA`, `P/FCF`, `P/S`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `XLV` на последний торговый день до якоря.

## Компании и инструменты

- [ABBV](ABBV.md)
- [AMGN](AMGN.md)
- [AZN](AZN.md)
- [BAYER](BAYER.md)
- [BMY](BMY.md)
- [INCY](INCY.md)
- [JAZZ](JAZZ.md)
- [JNJ](JNJ.md)
- [LLY](LLY.md)
- [MRK](MRK.md)
- [NVO](NVO.md)
- [NVS](NVS.md)
- [PFE](PFE.md)
- [RHHBY](RHHBY.md)
