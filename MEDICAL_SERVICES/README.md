# Medtech & Life Science Tools

Medical devices, diagnostics, robotic surgery, dental tech and life science tools.

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

ETF-proxy / benchmark для проверки состава и цен: `IHI`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Medtech & Life Science Tools sector_score =
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

Вывод по первой версии: текущая оценка корзины `Medtech & Life Science Tools` равна `0.66` относительно собственной 5-летней нормы. Это valuation-only слой; procedure volumes, reimbursement, diagnostics demand, hospital capex and product cycles not yet modeled.

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

Декадная динамика в `sector_valuation_dashboard.html` должна строиться по реальным valuation data на каждую якорную дату: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется последний торговый день до нее. Исторические точки не должны рассчитываться простым масштабированием последнего `sector_score` по `IHI`; `IHI` используется как benchmark/source-check и вспомогательный ценовой ориентир.

Таблица ниже сохранена как legacy benchmark-check по ETF close. Ее нельзя использовать как финальный источник `sector_score`; строки графика должны быть заменены реальными historical valuation data.


| Якорная дата | Фактическое закрытие | IHI close | Legacy scale, не использовать для sector_score |
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
5. Для каждой якорной даты получить реальные valuation data на последний торговый день до якоря; `IHI` использовать только как benchmark/source-check и вспомогательный ценовой ориентир.

## Компании и инструменты

- [ABT](ABT.md)
- [ALGN](ALGN.md)
- [BSX](BSX.md)
- [INMD](INMD.md)
- [ISRG](ISRG.md)
- [MDT](MDT.md)
- [SYK](SYK.md)
- [TMO](TMO.md)

## Инвестиционный разбор корзины

Обновлено: 2026-06-24. Рыночные цены - последний доступный trade 2026-06-23 UTC; фундаментальный снимок sector_score - `fyn_medical_services_current_20260620.csv` с ценами на 2026-06-18. Это аналитическая карта, не торговое поручение.

### Факты

- Секторный `sector_score` на 2026-06-20: `0.6653`, дешевле собственной 5-летней нормы. Компоненты: P/E `0.6403`, EV/EBITDA `0.6645`, P/S `0.7165`.
- Корзина sector_score: `ABT`, `ISRG`, `SYK`, `MDT`, `BSX`, `TMO`, `ALGN`. `INMD` есть в папке, но не входит в расчет sector_score.
- Медианные текущие показатели корзины: P/E `25.15`, P/S `3.41`, EV/EBITDA `14.79`, FCF yield `4.48%`, net margin `13.9%`, revenue growth YoY `8.4%`, earnings growth YoY `5.3%`.
- На 2026-06-23 цены/капитализация/TTM P/E: `ABT` $90.53 / $158.2B / 25.4; `ISRG` $403.18 / $145.1B / 49.0; `SYK` $310.00 / $119.8B / 35.9; `MDT` $80.63 / $104.0B / 22.5; `BSX` $45.60 / $68.2B / 19.1; `TMO` $469.35 / $175.1B / 25.8; `ALGN` $168.49 / $12.1B / 28.3; `INMD` $13.35 / $1.1B / P/E n/a.
- Последние отчеты: Abbott Q1 2026 sales $11.2B, adjusted EPS $1.15, growth led by Medical Devices and Established Pharmaceuticals; Intuitive Q1 2026 da Vinci procedure growth about 16%, Ion procedure growth about 39%, guidance for 2026 da Vinci procedure growth 13.5%-15.5%; Stryker Q1 2026 organic sales +2.4% after cyber incident, but full-year organic sales guidance kept at 8.0%-9.5%; Medtronic Q4 FY26 organic revenue +6.6%, FY26 organic revenue +5.8%, cardiac ablation +78% globally in Q4; Boston Scientific Q1 2026 sales +11.6% reported / +9.4% organic, FY26 organic sales guidance 6.5%-8.0%; Thermo Fisher Q1 2026 revenue +6%, organic revenue +1%; Align Q1 2026 revenue +6.2%, clear aligner volume +6.7%; InMode Q1 2026 revenue +5%, but GAAP EPS fell from $0.26 to $0.18 and operating margin compressed from 20% to 12%.

### Гипотезы

- Самая интересная зона для дальнейшего анализа: `BSX`, `MDT`, `TMO`.
- `BSX` - лучший growth/value кандидат в корзине: оценка сильно ниже собственной истории, при этом бизнес растет быстрее сектора. Главный вопрос - насколько снижение FY26 guidance уже отражено в цене и нет ли скрытого ухудшения в Urology / Watchman / U.S. volumes.
- `MDT` - value/turnaround с дивидендом и улучшением роста. Важно проверить, является ли ускорение устойчивым, а не разовым эффектом портфеля и M&A.
- `TMO` - quality compounder для watchlist: текущая оценка уже разумная, но органический рост пока слабый. Идея становится сильнее при признаках восстановления biotech/pharma capex и лабораторного спроса.
- `ISRG` и `SYK` - очень качественные компании, но сейчас больше похожи на "ждать правильную цену", чем на немедленную value-идею.
- `ABT` - защитный diversified healthcare, но инвестиционный тезис менее чистый для medtech: смесь diagnostics, devices, pharma/nutrition и эффект Exact Sciences.
- `ALGN` и `INMD` - более цикличные/спекулятивные истории. Низкая оценка здесь требует большего дисконта, потому что риск value trap выше.

### Риски

- Секторная дешевизна частично объясняется сжатием premium multiples после ковидной/постковидной базы 2021-2022, а не только недооценкой.
- Тарифы и supply chain могут давить на gross margin; это явно упоминает Intuitive в guidance.
- Elective procedures, hospital capex, reimbursement and tender cycles могут быстро менять спрос.
- Для `TMO` ключевой риск - затяжная слабость biotech funding, pharma R&D budgets и лабораторного оборудования.
- Для `ALGN` и `INMD` риск структурного давления выше: discretionary consumer spend, конкуренция, pricing, эстетические процедуры/стоматология.

### Инвестиционные действия

- `BSX` - приоритет 1 для отдельного deep dive: сегменты Cardiovascular / EP / Watchman, причина guidance reset, FCF conversion, долговая нагрузка, конкурентная позиция.
- `MDT` - приоритет 2: проверить качество FY27 guidance, устойчивость cardiac ablation, Hugo RAS, margin recovery и dividend safety.
- `TMO` - приоритет 3: ждать подтверждения organic growth recovery; интереснее как quality buy при слабости рынка или при улучшении заказов.
- `ISRG` - держать в watchlist как лучший бизнес, но требовать margin of safety; текущий P/E около 49 оставляет мало права на ошибку.
- `SYK` - watchlist, но после Q1 2026 нужен контроль восстановления после cyber incident и исполнения guidance.
- `ABT` - watchlist как defensive compounder; отдельный анализ Exact Sciences / diagnostics нужен до решения.
- `ALGN` - только speculative recovery, не core position без признаков устойчивого роста adult/teen cases и margin recovery.
- `INMD` - не включать в sector_score и не рассматривать как core medtech; только small-cap special situation после стабилизации управления, маржи и спроса.

Источники: локальный `data/market_quotes/fyn_medical_services_current_20260620.csv`; [Abbott Q1 2026 newsroom](https://www.abbott.com/en-us/corpnewsroom/strategy-and-strength/q1-progress-positions-Abbott-for-accelerating-growth-in-2026); [Intuitive Q1 2026 earnings release](https://isrg.intuitive.com/node/23036/pdf); [Stryker Q1 2026 earnings release](https://investors.stryker.com/files/doc_financials/2026/q1/Q1-26-Earnings-Press-Release.pdf); [Medtronic FY26 Q4 release](https://news.medtronic.com/2026-06-03-Medtronic-reports-fourth-quarter-and-full-year-fiscal-2026-results-delivers-highest-annual-revenue-growth-in-10-years); [Boston Scientific Q1 2026 release](https://news.bostonscientific.com/2026-04-22-Boston-Scientific-announces-results-for-first-quarter-2026); [Thermo Fisher Q1 2026 release](https://ir.thermofisher.com/investors/news-events/news/news-details/2026/Thermo-Fisher-Scientific-Reports-First-Quarter-2026-Results/default.aspx); [Align Q1 2026 release](https://investor.aligntech.com/news-releases/news-release-details/align-technology-announces-first-quarter-2026-financial-results); [InMode Q1 2026 release](https://www.prnewswire.com/news-releases/inmode-reports-first-quarter-2026-financial-results-quarterly-gaap-revenue-of-82-million-represents-5-year-over-year-increase-302763182.html); market price snapshot 2026-06-23 UTC.
