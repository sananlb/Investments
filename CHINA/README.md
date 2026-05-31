# China

Китайские и гонконгские компании: internet platforms, banks, telecom, energy, consumer champions.

Группа в TradingView: `China`.

## Ключевые компании

- [700](700.md) - Tencent: internet ecosystem, gaming, WeChat.
- [BABA](BABA.md) - Alibaba: e-commerce, cloud, China internet proxy.
- [PDD](PDD.md) - PDD Holdings: e-commerce, Temu, price disruption.
- [JD](JD.md) - JD.com: e-commerce and logistics.
- [941](941.md) - China Mobile: крупнейший telecom operator.
- [1398](1398.md) - ICBC: крупнейший китайский банк.
- [600519](600519.md) - Kweichow Moutai: premium consumer, China luxury/liquor proxy.
- [857](857.md) - PetroChina: state energy champion.
- [1810](1810.md) - Xiaomi: consumer electronics and EV optionality.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `700.HK`, `BABA`, `PDD`, `JD`, `1810.HK`, `1398.HK`, `600519.SS`.

ETF-proxy для декадного масштабирования: `MCHI`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
China sector_score =
0.30 x Forward P/E coefficient
+ 0.25 x P/E coefficient
+ 0.20 x P/S coefficient
+ 0.15 x P/B coefficient
+ 0.10 x EV/EBITDA coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| Forward P/E | `0.788` | 30% | 5 |
| P/E | `0.722` | 25% | 7 |
| P/S | `0.791` | 20% | 7 |
| P/B | `0.747` | 15% | 7 |
| EV/EBITDA | `0.735` | 10% | 6 |
| Итоговый sector_score | `0.76` | 100% |  |

Вывод по первой версии: текущая оценка корзины `China` равна `0.76` относительно собственной 5-летней нормы. Это valuation-only слой; pilot uses available StockAnalysis lines for ADR/HK/Shanghai proxies; China Mobile and PetroChina are not yet included due source coverage.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | Forward P/E curr / avg / coeff | P/E curr / avg / coeff | P/S curr / avg / coeff | P/B curr / avg / coeff | EV/EBITDA curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `700.HK` | n/a | 14.40 / 18.45 / `0.78` | 4.41 / 5.47 / `0.81` | 2.79 / 3.55 / `0.79` | 10.97 / 18.93 / `0.58` |
| `BABA` | 18.50 / 12.78 / `1.45` | 19.47 / 22.04 / `0.88` | 1.91 / 1.95 / `0.98` | 1.88 / 1.83 / `1.03` | 17.45 / 12.63 / `1.38` |
| `PDD` | 7.59 / 22.07 / `0.34` | 9.02 / 28.06 / `0.32` | 1.87 / 4.31 / `0.43` | 1.93 / 5.21 / `0.37` | 4.10 / 19.14 / `0.21` |
| `JD` | 8.09 / 17.01 / `0.48` | 21.81 / 24.69 / `0.88` | 0.20 / 0.43 / `0.47` | 0.96 / 2.06 / `0.47` | 17.42 / 21.11 / `0.83` |
| `1810.HK` | 22.48 / 22.86 / `0.98` | 18.67 / 38.82 / `0.48` | 1.43 / 1.51 / `0.95` | 2.38 / 2.88 / `0.83` | 15.77 / 20.35 / `0.78` |
| `1398.HK` | n/a | 5.78 / 5.47 / `1.06` | 3.70 / 2.88 / `1.28` | 0.57 / 0.50 / `1.14` | n/a |
| `600519.SS` | 18.93 / 27.50 / `0.69` | 20.08 / 31.17 / `0.64` | 9.64 / 15.57 / `0.62` | 5.90 / 9.61 / `0.61` | 14.24 / 22.34 / `0.64` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `MCHI`.

| Якорная дата | Фактическое закрытие | MCHI close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 59.06 | `1.0719` |
| 2026-03-10 | 2026-03-10 | 58.70 | `1.0653` |
| 2026-03-20 | 2026-03-20 | 55.21 | `1.0020` |
| 2026-03-30 | 2026-03-30 | 54.95 | `0.9973` |
| 2026-04-10 | 2026-04-10 | 57.18 | `1.0377` |
| 2026-04-20 | 2026-04-20 | 59.30 | `1.0762` |
| 2026-04-30 | 2026-04-30 | 57.57 | `1.0448` |
| 2026-05-10 | 2026-05-08 | 58.32 | `1.0584` |
| 2026-05-20 | 2026-05-20 | 56.62 | `1.0276` |
| 2026-05-30 | 2026-05-29 | 55.10 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: MCHI history](https://stockanalysis.com/etf/mchi/history/) |
| `700.HK` ratios | [StockAnalysis](https://stockanalysis.com/quote/otc/TCEHY/financials/ratios/) |
| `BABA` ratios | [StockAnalysis](https://stockanalysis.com/stocks/baba/financials/ratios/) |
| `PDD` ratios | [StockAnalysis](https://stockanalysis.com/stocks/pdd/financials/ratios/) |
| `JD` ratios | [StockAnalysis](https://stockanalysis.com/stocks/jd/financials/ratios/) |
| `1810.HK` ratios | [StockAnalysis](https://stockanalysis.com/quote/hkg/1810/financials/ratios/) |
| `1398.HK` ratios | [StockAnalysis](https://stockanalysis.com/quote/hkg/1398/financials/ratios/) |
| `600519.SS` ratios | [StockAnalysis](https://stockanalysis.com/quote/sha/600519/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `700.HK`, `BABA`, `PDD`, `JD`, `1810.HK`, `1398.HK`, `600519.SS`.
2. Взять текущие `Forward P/E`, `P/E`, `P/S`, `P/B`, `EV/EBITDA`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `MCHI` на последний торговый день до якоря.

## Компании и инструменты

- [1398](1398.md)
- [1810](1810.md)
- [600519](600519.md)
- [700](700.md)
- [857](857.md)
- [941](941.md)
- [BABA](BABA.md)
- [JD](JD.md)
- [PDD](PDD.md)
