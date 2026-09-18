# Consumer

Consumer discretionary и брендовые потребительские компании: retail, apparel, housing, home improvement, restaurants.

Группа в TradingView: `Consumer`.

## Ключевые компании

- [AMZN](AMZN.md) - Amazon: крупнейший consumer discretionary по market cap.
- [HD](HD.md) - Home Depot: home improvement bellwether.
- [LOW](LOW.md) - Lowe's: home improvement peer.
- [NKE](NKE.md) - Nike: global athletic brand.
- [MCD](MCD.md) - McDonald's: global quick-service restaurants.
- [LULU](LULU.md) - Lululemon: premium athletic apparel.

Важно: `TSLA` не включается в Consumer Discretionary sector_score. Рабочая классификация для нашей библиотеки: Tesla - это AI / robotics / autonomous taxi thesis, а не автомобильная consumer-компания. Файл перенесен в `AI/TSLA.md`.

## Кратко о секторе

Consumer discretionary - циклический потребительский сектор. Прибыли зависят от доходов домохозяйств, занятости, потребительского кредита, ипотечных ставок, confidence, discretionary spending, трафика в магазинах/ресторанах, gross margin и способности брендов удерживать цены.

Главные драйверы:

- реальный доход потребителей, занятость и wage growth;
- ставки и доступность кредита: особенно важны для housing, autos, durable goods и high-ticket discretionary spending;
- инфляция и gross margin: сырье, логистика, промо-активность и discounting;
- same-store sales / traffic / average ticket: главный операционный сигнал для retail и restaurants;
- брендовая сила и pricing power;
- e-commerce, loyalty, supply chain и inventory cycle.

Корреляция с S&P 500 обычно положительная и выше средней, потому что сектор чувствителен к экономическому циклу, risk appetite и ожиданиям по прибыли. При снижении ставок и мягкой посадке сектор часто получает поддержку через потребительский кредит, housing и multiple expansion. При росте ставок, ослаблении занятости и падении consumer confidence сектор обычно страдает.

Главная особенность: в Consumer Discretionary нельзя смотреть только P/E. Дешевый P/E может быть ловушкой, если падают traffic, gross margin, inventory quality и EPS revisions. Для финальной модели нужно добавить операционные метрики: same-store sales, gross margin trend, inventory turnover и consumer cycle signal.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина без `TSLA`: `AMZN`, `HD`, `LOW`, `NKE`, `MCD`, `LULU`.

ETF-proxy для декадного масштабирования: `XLY`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен или искажен, он не включается в среднее по конкретной метрике. Например, у `AMZN` текущий `P/FCF` в источнике отсутствует, поэтому в среднем `P/FCF` он пропущен.

Стартовые веса для пилота:

```text
Consumer Discretionary sector_score =
0.25 x P/E coefficient
+ 0.25 x Forward P/E coefficient
+ 0.20 x EV/EBITDA coefficient
+ 0.15 x P/S coefficient
+ 0.15 x P/FCF coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент |
|---|---:|
| P/E | `0.782` |
| Forward P/E | `0.765` |
| EV/EBITDA | `0.794` |
| P/S | `0.761` |
| P/FCF | `0.991` |
| Итоговый sector_score | `0.81` |

Вывод по первой версии: выбранная consumer discretionary корзина сейчас ниже своей 5-летней valuation-нормы. Основной дисконт дают `LULU`, `NKE`, а также home improvement и restaurants около или ниже своих исторических уровней. Это valuation-only слой: без проверки same-store sales, margin trend и EPS revisions он не должен автоматически означать "покупать сектор".

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | P/E curr / avg / coeff | Fwd P/E curr / avg / coeff | EV/EBITDA curr / avg / coeff | P/S curr / avg / coeff | P/FCF curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `AMZN` | 32.37 / 43.93 / `0.74` | 32.45 / 51.78 / `0.63` | 19.27 / 20.35 / `0.95` | 3.92 / 3.03 / `1.30` | n/a / 147.18 / n/a |
| `HD` | 22.52 / 24.01 / `0.94` | 20.75 / 23.40 / `0.89` | 15.17 / 16.27 / `0.93` | 1.90 / 2.34 / `0.81` | 22.09 / 25.86 / `0.85` |
| `LOW` | 18.12 / 20.24 / `0.90` | 16.86 / 18.75 / `0.90` | 12.86 / 13.75 / `0.93` | 1.36 / 1.58 / `0.86` | 15.78 / 19.43 / `0.81` |
| `NKE` | 30.48 / 31.23 / `0.98` | 28.29 / 31.04 / `0.91` | 18.53 / 23.54 / `0.79` | 1.47 / 3.34 / `0.44` | 65.33 / 32.06 / `2.04` |
| `MCD` | 23.01 / 27.00 / `0.85` | 21.11 / 24.84 / `0.85` | 16.95 / 19.51 / `0.87` | 7.23 / 8.28 / `0.87` | 28.18 / 30.81 / `0.91` |
| `LULU` | 9.89 / 33.45 / `0.30` | 10.68 / 25.64 / `0.42` | 5.54 / 18.95 / `0.29` | 1.35 / 4.70 / `0.29` | 16.29 / 48.49 / `0.34` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `XLY`.

| Якорная дата | Фактическое закрытие | XLY close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 116.86 | `0.9668` |
| 2026-03-10 | 2026-03-10 | 114.44 | `0.9468` |
| 2026-03-20 | 2026-03-20 | 107.74 | `0.8914` |
| 2026-03-30 | 2026-03-30 | 105.66 | `0.8742` |
| 2026-04-10 | 2026-04-10 | 112.89 | `0.9340` |
| 2026-04-20 | 2026-04-20 | 119.87 | `0.9917` |
| 2026-04-30 | 2026-04-30 | 118.35 | `0.9792` |
| 2026-05-10 | 2026-05-08 | 120.20 | `0.9945` |
| 2026-05-20 | 2026-05-20 | 117.94 | `0.9758` |
| 2026-05-30 | 2026-05-29 | 120.87 | `1.0000` |

Ограничение: это пилотная valuation-only модель. В финальной версии нужно добавить same-store sales / traffic, gross margin trend, EPS revisions, inventory quality и consumer income / credit stress signal.

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: XLY history](https://stockanalysis.com/etf/xly/history/) |
| `AMZN` ratios | [StockAnalysis: AMZN financial ratios](https://stockanalysis.com/stocks/amzn/financials/ratios/) |
| `HD` ratios | [StockAnalysis: HD financial ratios](https://stockanalysis.com/stocks/hd/financials/ratios/) |
| `LOW` ratios | [StockAnalysis: LOW financial ratios](https://stockanalysis.com/stocks/low/financials/ratios/) |
| `NKE` ratios | [StockAnalysis: NKE financial ratios](https://stockanalysis.com/stocks/nke/financials/ratios/) |
| `MCD` ratios | [StockAnalysis: MCD financial ratios](https://stockanalysis.com/stocks/mcd/financials/ratios/) |
| `LULU` ratios | [StockAnalysis: LULU financial ratios](https://stockanalysis.com/stocks/lulu/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `AMZN`, `HD`, `LOW`, `NKE`, `MCD`, `LULU`.
2. Взять текущие `P/E`, `Forward P/E`, `EV/EBITDA`, `P/S`, `P/FCF`.
3. Сравнить каждую метрику со средним FY2021-FY2025.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `XLY` на последний торговый день до якоря.
6. `TSLA` не добавлять в расчет Consumer; для Tesla использовать `AI/TSLA.md`.

## Компании и инструменты

- [AMZN](AMZN.md)
- [GT](GT.md)
- [HD](HD.md)
- [LEN](LEN.md)
- [LOW](LOW.md)
- [LULU](LULU.md)
- [MCD](MCD.md)
- [MMM](MMM.md)
- [NKE](NKE.md)
- [RL](RL.md)
- [ULTA](ULTA.md)
