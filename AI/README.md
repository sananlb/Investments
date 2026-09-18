# AI

Искусственный интеллект как инвестиционная тема: AI infrastructure, hyperscalers, semiconductors, модели, дата-центры и enterprise AI.

## Research

- [AI Research 2026](AI_Research_2026.md)
- [AMD vs NVIDIA Analysis 2026](AMD_vs_NVIDIA_Analysis_2026.md)

## Company Exports

- AMD: Google Docs export
- Astera Labs / Oracle: Google Docs export
- Marvell Technology: MHTML export

## Ключевые компании

- [NVDA](NVDA.md) - NVIDIA: ключевой поставщик GPU и AI accelerators.
- [MSFT](MSFT.md) - Microsoft: Azure, OpenAI partnership, enterprise AI distribution.
- [GOOG](GOOG.md) - Alphabet: Google Cloud, Gemini, TPU, AI research.
- [AMZN](AMZN.md) - Amazon: AWS, Trainium/Inferentia, AI infrastructure.
- [META](META.md) - Meta Platforms: open-source AI models, capex, social AI distribution.
- [AVGO](AVGO.md) - Broadcom: custom ASICs and networking for AI data centers.
- [TSM](TSM.md) - TSMC: foundry backbone for advanced AI chips.
- [AMD](AMD.md) - AMD: GPU/CPU alternative in AI compute.
- [ORCL](ORCL.md) - Oracle: cloud infrastructure and AI data center capacity.
- [TSLA](TSLA.md) - Tesla: robotics, autonomous taxi and autonomy platform thesis.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `NVDA`, `MSFT`, `GOOG`, `AMZN`, `META`, `AVGO`, `TSM`, `AMD`, `ORCL`, `TSLA`.

ETF-proxy для декадного масштабирования: `AIQ`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
AI Infrastructure sector_score =
0.30 x Forward P/E coefficient
+ 0.25 x P/S coefficient
+ 0.15 x P/B coefficient
+ 0.20 x EV/EBITDA coefficient
+ 0.10 x P/FCF coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| Forward P/E | `1.159` | 30% | 9 |
| P/S | `1.526` | 25% | 10 |
| P/B | `1.124` | 15% | 10 |
| EV/EBITDA | `1.434` | 20% | 10 |
| P/FCF | `1.395` | 10% | 8 |
| Итоговый sector_score | `1.32` | 100% |  |

Вывод по первой версии: текущая оценка корзины `AI Infrastructure` равна `1.32` относительно собственной 5-летней нормы. Это valuation-only слой; theme basket overlaps semiconductors and mega-cap technology; capex/compute demand and EPS revisions not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | Forward P/E curr / avg / coeff | P/S curr / avg / coeff | P/B curr / avg / coeff | EV/EBITDA curr / avg / coeff | P/FCF curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `NVDA` | 21.24 / 38.45 / `0.55` | 20.17 / 22.49 / `0.90` | 26.16 / 30.45 / `0.86` | 30.65 / 51.11 / `0.60` | 42.95 / 72.50 / `0.59` |
| `MSFT` | 24.36 / 32.23 / `0.76` | 10.51 / 12.08 / `0.87` | 8.07 / 12.26 / `0.66` | 18.39 / 23.01 / `0.80` | 45.87 / 40.95 / `1.12` |
| `GOOG` | 30.04 / 23.53 / `1.28` | 10.86 / 6.65 / `1.63` | 9.58 / 6.91 / `1.39` | 28.24 / 18.40 / `1.53` | 71.19 / 31.32 / `2.27` |
| `AMZN` | 32.45 / 51.78 / `0.63` | 3.92 / 3.02 / `1.30` | 6.59 / 8.03 / `0.82` | 19.27 / 20.35 / `0.95` | n/a |
| `META` | 19.27 / 21.68 / `0.89` | 7.47 / 6.91 / `1.08` | 6.59 / 6.32 / `1.04` | 14.74 / 14.56 / `1.01` | 33.27 / 24.84 / `1.34` |
| `AVGO` | 33.44 / 24.10 / `1.39` | 30.98 / 13.28 / `2.33` | 26.49 / 13.05 / `2.03` | 58.23 / 27.20 / `2.14` | 73.17 / 30.83 / `2.37` |
| `TSM` | n/a | 15.16 / 9.68 / `1.57` | 10.48 / 6.81 / `1.54` | 20.98 / 13.59 / `1.54` | 57.88 / 46.09 / `1.26` |
| `AMD` | 59.29 / 37.09 / `1.60` | 22.47 / 8.68 / `2.59` | 13.05 / 7.75 / `1.68` | 112.12 / 42.28 / `2.65` | 98.15 / 86.92 / `1.13` |
| `ORCL` | 29.99 / 19.15 / `1.57` | 10.13 / 5.99 / `1.69` | 19.35 / 92.49 / `0.21` | 28.15 / 18.66 / `1.51` | n/a |
| `TSLA` | 202.64 / 114.24 / `1.77` | 16.72 / 12.86 / `1.30` | 19.45 / 19.17 / `1.01` | 144.93 / 90.29 / `1.61` | 233.82 / 217.25 / `1.08` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `AIQ`.

| Якорная дата | Фактическое закрытие | AIQ close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 50.26 | `0.7466` |
| 2026-03-10 | 2026-03-10 | 49.67 | `0.7378` |
| 2026-03-20 | 2026-03-20 | 47.37 | `0.7037` |
| 2026-03-30 | 2026-03-30 | 44.78 | `0.6652` |
| 2026-04-10 | 2026-04-10 | 49.37 | `0.7334` |
| 2026-04-20 | 2026-04-20 | 53.91 | `0.8008` |
| 2026-04-30 | 2026-04-30 | 55.88 | `0.8301` |
| 2026-05-10 | 2026-05-08 | 62.31 | `0.9256` |
| 2026-05-20 | 2026-05-20 | 61.87 | `0.9190` |
| 2026-05-30 | 2026-05-29 | 67.32 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: AIQ history](https://stockanalysis.com/etf/aiq/history/) |
| `NVDA` ratios | [StockAnalysis](https://stockanalysis.com/stocks/nvda/financials/ratios/) |
| `MSFT` ratios | [StockAnalysis](https://stockanalysis.com/stocks/msft/financials/ratios/) |
| `GOOG` ratios | [StockAnalysis](https://stockanalysis.com/stocks/goog/financials/ratios/) |
| `AMZN` ratios | [StockAnalysis](https://stockanalysis.com/stocks/amzn/financials/ratios/) |
| `META` ratios | [StockAnalysis](https://stockanalysis.com/stocks/meta/financials/ratios/) |
| `AVGO` ratios | [StockAnalysis](https://stockanalysis.com/stocks/avgo/financials/ratios/) |
| `TSM` ratios | [StockAnalysis](https://stockanalysis.com/stocks/tsm/financials/ratios/) |
| `AMD` ratios | [StockAnalysis](https://stockanalysis.com/stocks/amd/financials/ratios/) |
| `ORCL` ratios | [StockAnalysis](https://stockanalysis.com/stocks/orcl/financials/ratios/) |
| `TSLA` ratios | [StockAnalysis](https://stockanalysis.com/stocks/tsla/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `NVDA`, `MSFT`, `GOOG`, `AMZN`, `META`, `AVGO`, `TSM`, `AMD`, `ORCL`, `TSLA`.
2. Взять текущие `Forward P/E`, `P/S`, `P/B`, `EV/EBITDA`, `P/FCF`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `AIQ` на последний торговый день до якоря.

## Компании

- [AMD](AMD.md)
- [AMZN](AMZN.md)
- [AVGO](AVGO.md)
- [GOOG](GOOG.md)
- [META](META.md)
- [MSFT](MSFT.md)
- [NVDA](NVDA.md)
- [ORCL](ORCL.md)
- [TSLA](TSLA.md)
- [TSM](TSM.md)
