# Utilities And Gas Infrastructure

Electric utilities, regulated power, gas infrastructure, pipelines and energy infrastructure.

Группа в TradingView: `Utilities & Gas infrastructure`.

## Ключевые компании

- [NEE](NEE.md) - NextEra Energy: largest US utility and renewables leader.
- [DUK](DUK.md) - Duke Energy: large regulated electric utility.
- [SO](SO.md) - Southern Company: regulated utility and power generation.
- [AEP](AEP.md) - American Electric Power: transmission and regulated utility.
- [D](D.md) - Dominion Energy: regulated utility and data-center power exposure.
- [KMI](KMI.md) - Kinder Morgan: US gas pipeline infrastructure.
- [WMB](WMB.md) - Williams Companies: natural gas infrastructure.
- [ET](ET.md) - Energy Transfer: midstream energy infrastructure.
- [EQT](EQT.md) - EQT: large US natural gas producer.

## Кратко о секторе

Utilities - защитный и капиталоемкий сектор. Прибыли зависят не столько от свободной рыночной цены, сколько от regulated rate base, разрешенной доходности капитала, стоимости долга, спроса на электроэнергию, capex-программы и решений регуляторов.

Главные драйверы:

- ставки и доходности облигаций: при росте ставок сектор обычно получает давление через стоимость долга и конкуренцию с bonds/dividend yield;
- regulated rate base и allowed ROE: рост базы активов поддерживает EPS, но требует большого capex;
- спрос на электроэнергию: data centers и AI усиливают долгосрочный спрос, особенно в регионах с grid bottleneck;
- топливо и генерация: газ, nuclear, renewables, transmission и storage влияют на себестоимость и устойчивость;
- регуляторный риск: тарифы, political pressure и affordability для потребителей.

Корреляция с S&P 500 обычно ниже, чем у циклических и growth-секторов. Сектор часто ведет себя как defensive / bond-proxy: лучше смотрится при падающих ставках и ухудшении экономического цикла, хуже - при резком росте доходностей облигаций.

Главная особенность: дешевизну utilities нельзя оценивать только по P/E. Нужно смотреть dividend yield, debt cost, regulated returns и качество capex. Дешевая utility с плохим балансом или неблагоприятным регулятором может оставаться value trap.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована regulated utilities корзина: `NEE`, `DUK`, `SO`, `AEP`, `D`. Это не вся папка `Utilities & Gas infrastructure`: pipelines (`KMI`, `WMB`, `ET`) и gas producers (`EQT`) пока не включены, потому что их нужно считать отдельной midstream/gas sub-group с другой методикой.

ETF-proxy для декадного масштабирования: `XLU`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Для `Dividend Yield` коэффициент инвертирован:

```text
Dividend Yield coefficient = 5Y average dividend yield / current dividend yield
```

Так сохраняется общий смысл графика: выше `1.0` = дороже нормы, ниже `1.0` = дешевле нормы.

Стартовые веса для пилота:

```text
Utilities sector_score =
0.25 x P/E coefficient
+ 0.25 x Forward P/E coefficient
+ 0.20 x EV/EBITDA coefficient
+ 0.20 x Dividend Yield coefficient
+ 0.10 x P/B coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент |
|---|---:|
| P/E | `0.866` |
| Forward P/E | `1.028` |
| EV/EBITDA | `0.924` |
| Dividend Yield | `1.095` |
| P/B | `1.021` |
| Итоговый sector_score | `0.98` |

Вывод по первой версии: выбранная regulated utilities корзина сейчас около своей 5-летней нормы, чуть дешевле по trailing P/E и EV/EBITDA, но не выглядит явно дешевой из-за forward P/E, dividend yield и P/B.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; финансовые TTM данные в источнике идут до 2026-03-31. Историческая база - среднее FY2021-FY2025.

| Тикер | P/E curr / avg / coeff | Fwd P/E curr / avg / coeff | EV/EBITDA curr / avg / coeff | Div yield curr / avg / coeff | P/B curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `NEE` | 22.10 / 30.77 / `0.72` | 21.48 / 25.23 / `0.85` | 20.05 / 21.56 / `0.93` | 2.86% / 2.49% / `0.87` | 3.29 / 3.56 / `0.92` |
| `DUK` | 18.87 / 23.95 / `0.79` | 18.22 / 18.74 / `0.97` | 11.21 / 12.11 / `0.93` | 3.44% / 3.94% / `1.14` | 1.79 / 1.64 / `1.09` |
| `SO` | 23.51 / 22.95 / `1.02` | 20.08 / 19.47 / `1.03` | 12.79 / 14.13 / `0.91` | 3.29% / 3.60% / `1.09` | 2.80 / 2.60 / `1.08` |
| `AEP` | 18.75 / 18.44 / `1.02` | 19.73 / 17.07 / `1.16` | 13.15 / 12.42 / `1.06` | 2.97% / 3.61% / `1.21` | 2.17 / 2.33 / `0.93` |
| `D` | 19.77 / 25.23 / `0.78` | 18.64 / 16.48 / `1.13` | 13.44 / 16.80 / `0.80` | 3.96% / 4.55% / `1.15` | 2.09 / 1.92 / `1.09` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `XLU`.

| Якорная дата | Фактическое закрытие | XLU close | Scale к 2026-05-29 |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 47.73 | `1.0745` |
| 2026-03-10 | 2026-03-10 | 46.56 | `1.0482` |
| 2026-03-20 | 2026-03-20 | 44.65 | `1.0052` |
| 2026-03-30 | 2026-03-30 | 45.92 | `1.0338` |
| 2026-04-10 | 2026-04-10 | 46.96 | `1.0572` |
| 2026-04-20 | 2026-04-20 | 45.75 | `1.0299` |
| 2026-04-30 | 2026-04-30 | 46.85 | `1.0547` |
| 2026-05-10 | 2026-05-08 | 44.72 | `1.0068` |
| 2026-05-20 | 2026-05-20 | 44.51 | `1.0020` |
| 2026-05-30 | 2026-05-29 | 44.42 | `1.0000` |

Ограничение: это пилотная valuation-only модель. В финальной версии нужно добавить debt cost / interest coverage, allowed ROE, rate base growth, capex funding gap и regulator quality. Для midstream/gas infrastructure нужна отдельная модель с EV/EBITDA, FCF yield, leverage, contracted cash flows и commodity exposure.

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: XLU history](https://stockanalysis.com/etf/xlu/history/) |
| `NEE` ratios | [StockAnalysis: NEE financial ratios](https://stockanalysis.com/stocks/nee/financials/ratios/) |
| `DUK` ratios | [StockAnalysis: DUK financial ratios](https://stockanalysis.com/stocks/duk/financials/ratios/) |
| `SO` ratios | [StockAnalysis: SO financial ratios](https://stockanalysis.com/stocks/so/financials/ratios/) |
| `AEP` ratios | [StockAnalysis: AEP financial ratios](https://stockanalysis.com/stocks/aep/financials/ratios/) |
| `D` ratios | [StockAnalysis: D financial ratios](https://stockanalysis.com/stocks/d/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `NEE`, `DUK`, `SO`, `AEP`, `D`.
2. Взять текущие `P/E`, `Forward P/E`, `EV/EBITDA`, `Dividend Yield`, `P/B`.
3. Сравнить каждую метрику со средним FY2021-FY2025.
4. Для `Dividend Yield` использовать обратную формулу: `5Y average yield / current yield`.
5. Посчитать weighted score по весам выше.
6. Для якорных дат масштабировать компоненты по закрытию `XLU` на последний торговый день до якоря.

## Компании и инструменты

- [AEP](AEP.md)
- [D](D.md)
- [DUK](DUK.md)
- [EQT](EQT.md)
- [ET](ET.md)
- [KMI](KMI.md)
- [NEE](NEE.md)
- [NFE](NFE.md)
- [SO](SO.md)
- [SWX](SWX.md)
- [UGI](UGI.md)
- [VLO](VLO.md)
- [WMB](WMB.md)
