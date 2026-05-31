# Рыночный дашборд

Этот файл предназначен для регулярного обновления общей картины рынка.

## Что отслеживать

- Ставки и ожидания по ставкам: США, РФ, Европа.
- Индексы: S&P 500, Nasdaq 100, Russell 2000, MOEX.
- Валюты: USD/RUB, USD/KZT, DXY.
- Доходности облигаций: UST 10Y, OFZ, корпоративные спреды.
- Сырье: нефть, золото, медь, lithium, uranium.
- AI-инфраструктура: semiconductors, HBM, advanced packaging, data centers, power.
- Портфель: крупнейшие позиции, концентрация, просадка, thesis drift.
- Секторная оценка: насколько сектор дорогой или дешевый относительно собственной истории и рынка.

## Секторная оценка

Цель: быстро видеть, какие сектора переоценены или недооценены относительно своей исторической нормы. Центральная линия графика - `1.0`.

### Базовый принцип графика

График строится не по отдельным мультипликаторам, а по итоговой декадной оценке сектора.

```text
1.0 = средневзвешенная нормальная оценка сектора за последние 5 лет
выше 1.0 = сектор дороже своей 5-летней нормы
ниже 1.0 = сектор дешевле своей 5-летней нормы
```

Каждый сектор имеет постоянный цвет. Точки ставятся не каждый день, а раз в 10 дней: 10-е, 20-е, 30-е число. Если якорная дата попадает на выходной или праздник, используется последний торговый день до этой даты. Для февраля или месяца без 30-го числа используется последний календарный день месяца как замена 30-го.

На графике отображаются последние 10 точек. На одну якорную дату появляется только одна точка по каждому сектору. Эта точка является итоговым `sector_score`, который складывается из нескольких метрик с весами.

Пример:

```text
Semiconductors 2026-05-30 = 1.82
```

Это означает не то, что один конкретный P/E выше нормы на 24%, а то, что средневзвешенная секторная оценка по выбранным метрикам примерно на 24% выше своей 5-летней нормы.

В данных обязательно сохраняются компоненты точки:

```text
anchor_date
sector
sector_score
metric
current_value
five_year_average
metric_coefficient
metric_weight
source
comment
actual_trading_date
```

На графике видна только одна точка `sector_score`, но при анализе должно быть понятно, из каких метрик она собрана.

### Готовые сервисы для секторной оценки

Рабочее правило: сначала использовать готовые секторные сервисы, а не собирать все руками. Наша библиотека должна быть надстройкой: берем текущие данные из внешних источников, а у себя сохраняем выводы, источники, дату и секторно-специфическую интерпретацию.

| Источник | Что брать | Как использовать |
|---|---|---|
| [WorldPERatio: S&P 500 sectors](https://worldperatio.com/sp-500-sectors/) | P/E по 11 секторам S&P 500, 5/10/20-летние средние, отклонение в sigma, оценка Fair/Overvalued/Undervalued | Базовый быстрый радар: какой сектор дорогой/дешевый по P/E против собственной истории |
| [Finviz Groups](https://finviz.com/groups.ashx?g=sector&o=pb&v=120) | P/E, Forward P/E, PEG, P/S, P/B, P/FCF, EPS growth, performance по секторам и индустриям | Проверка valuation и performance по широким группам; удобно смотреть индустрии внутри сектора |
| [ChartMill Sector Dashboard](https://www.chartmill.com/stock/sector) | GICS/NAICS, sector/group/industry/subindustry, performance, valuation, ROE, ROIC, weighted/equal-weighted view | Второй слой после WorldPERatio: сравнение не только по P/E, но и по quality/profitability |
| [Fidelity Sectors](https://digital.fidelity.com/prgw/digital/research/sector) | Sector performance, business-cycle view, sector outlook, institutional methodology | Контекст бизнес-цикла и earnings/valuation views |
| [Yardeni sector valuation charts](https://www.yardeni.com/charts/us-stock-market/stock-market-valuation/sp-500-sectors-forward-p-e-ratios) | Forward P/E по секторам S&P 500 | Макро-проверка forward valuation |
| [State Street Select Sector SPDR](https://www.ssga.com/us/en/intermediary/capabilities/equities/sector-investing/select-sector-etfs) | Данные по секторным ETF, holdings, факторы, sector scorecard methodology | Официальный слой для ETF-прокси `XLK`, `XLF`, `XLE`, `XLB` и т.д. |
| [TradingView sectors](https://www.tradingview.com/markets/stocks-usa/sectorandindustry-sector/) | Визуальная карта performance, momentum, heatmap | Визуальная проверка тренда и market mood |

### Рабочий порядок обновления

1. Открыть WorldPERatio и взять текущие P/E, 10-летние средние и оценки по 11 секторам S&P 500.
2. Быстро сверить Finviz Groups и ChartMill: нет ли сильного расхождения по P/B, P/S, Forward P/E, ROE/ROIC и performance.
3. Для выбранного сектора открыть Fidelity/Yardeni/State Street, чтобы понять business-cycle view, forward valuation и ETF-состав.
4. Для наших специальных папок (`BANKS_AND_FUNDS`, `SEMICONDUCTORS`, `MINING`) добавить sector-specific metrics: банки - P/B/ROE/NIM/credit losses; semis - forward P/E/P/S/gross margin/EPS revisions; mining - EV/EBITDA/P/NAV/FCF/commodity cycle.
5. Итог записать в `README.md` сектора и при необходимости добавить строку в `sector_valuation_dashboard.html`.

Интерпретация:

- `1.10` - сектор примерно на 10% дороже своей исторической нормы.
- `1.00` - сектор около исторической нормы.
- `0.80` - сектор примерно на 20% дешевле своей исторической нормы.

### Базовая формула

Лучше считать не абсолютный P/E сектора, а относительную оценку сектора к рынку:

```text
Relative valuation today = Sector multiple today / Market multiple today

Historical norm = среднее или медиана Relative valuation за 10-15 лет

Sector valuation coefficient = Relative valuation today / Historical norm
```

Пример:

```text
Если Technology обычно торгуется с премией 1.30 к S&P 500,
а сегодня торгуется с премией 1.56,
то коэффициент = 1.56 / 1.30 = 1.20.

Это значит: сектор примерно на 20% дороже своей обычной относительной оценки.
```

### Почему так лучше

Если весь рынок стал дорогим из-за низких ставок или сильных earnings, абсолютный P/E всех секторов может быть выше истории. Относительная оценка показывает, дорогой ли именно сектор относительно S&P 500 и своей обычной премии/дисконта.

### Какие метрики использовать

Базовый набор:

- `P/E`;
- `Forward P/E` или `NTM P/E`;
- `P/B`;
- `P/S`.

Но это только общий набор. У каждого сектора своя экономическая логика, поэтому один и тот же мультипликатор нельзя одинаково применять ко всем.

### Как это делают профессиональные методологии

#### 1. Сначала задают правильную классификацию

Профессиональные инвесторы обычно начинают с GICS - классификации MSCI/S&P Dow Jones. Она делит рынок на 11 секторов, 25 industry groups, 74 industries и 163 sub-industries. Это нужно, чтобы сравнивать компанию не с "рынком вообще", а с экономически похожими бизнесами.

Для нашей библиотеки это важно: папки TradingView не всегда совпадают с GICS. Например, `BANKS_AND_FUNDS` объединяет банки, asset managers и платежные сети, а это разные бизнес-модели.

#### 2. Сравнивают сектор с собственной историей

MSCI прямо пишет, что сравнение текущих sector valuations с долгосрочными средними помогает инвесторам принимать решения о sector rotation. Смысл: `Technology` почти всегда дороже `Utilities`, поэтому нельзя сказать, что tech дорогой только потому, что его P/E выше. Нужно смотреть, насколько он дорог относительно собственной истории.

#### 3. Сравнивают сектор с рынком

Fidelity считает relative valuation так: valuation metrics каждого сектора берутся относительно S&P 500, затем текущая относительная оценка делится на 10-летнюю историческую среднюю relative valuation. Чтобы выбросы не ломали статистику, Fidelity исключает верхние 5% и нижние 5% значений.

#### 4. Используют несколько метрик, а не одну

State Street в Sector Scorecard использует `P/B`, trailing `P/E`, `NTM P/E`, `P/S` и смотрит их percentile rank за 15 лет. Отдельно считается:

- absolute valuation - сектор против собственной истории;
- relative valuation - сектор против S&P 500 и собственной истории relative valuation;
- earnings sentiment - изменения EPS estimates, upgrade/downgrade ratio, earnings surprise;
- momentum - доходность за 3, 6 и 12 месяцев;
- volatility - realized и implied volatility.

Это правильная логика: дешевая оценка без улучшения прибыли может быть value trap, а дорогая оценка при резком росте прибыли может быть оправданной.

#### 5. Иногда используют bottom-up fair value

Morningstar оценивает компании через fair value estimate, economic moat, uncertainty и текущую цену. Потом агрегирует price/fair value по рынку или сектору. Это более фундаментальный подход, чем простые мультипликаторы, но он зависит от качества DCF-моделей аналитиков.

Для нашей практики это можно использовать как дополнительный сигнал: если есть доступ к Morningstar price/fair value по сектору или ETF, его можно записывать рядом с нашим коэффициентом.

### Метрики по секторам

Для разных секторов веса должны отличаться:

| Сектор | Что важнее |
|---|---|
| Банки | P/B, P/TBV, ROE/ROTCE, P/E, NIM, CET1, credit losses |
| Страхование | P/B, ROE, combined ratio, investment income, reserve quality |
| Asset managers / brokers | P/E, AUM, net flows, fee rate, operating margin |
| Платежные сети | P/E, EV/EBITDA, revenue growth, margins, cross-border volume |
| REIT | P/FFO, AFFO yield, dividend yield, debt cost, occupancy, cap rates |
| Energy | EV/EBITDA, FCF yield, dividend/buyback yield, oil/gas price, reserve life |
| Mining / Materials | EV/EBITDA, P/NAV, FCF yield, commodity price, cost curve |
| Semiconductors | Forward P/E, P/S, EV/Sales, gross margin, EPS revisions, inventory cycle |
| Software / Internet | Forward P/E, EV/Sales, FCF margin, revenue growth, Rule of 40 |
| Consumer discretionary | P/E, EV/EBITDA, same-store sales, gross margin, consumer income |
| Consumer staples / Food | P/E, EV/EBITDA, dividend yield, pricing power, volume growth |
| Health care services / medtech | P/E, EV/EBITDA, procedure volumes, margins, reimbursement risk |
| Pharma / biotech | P/E for mature pharma, EV/Sales or rNPV for pipeline biotech, patent cliff |
| Utilities | P/E, dividend yield, EV/EBITDA, regulated asset base, allowed ROE, debt cost |
| Telecom | EV/EBITDA, FCF yield, dividend sustainability, leverage, capex intensity |

### Что именно строить на графике

Для простого читаемого графика нужна одна линия на сектор:

```text
Sector valuation coefficient = current relative valuation / historical relative valuation norm
```

Но внутри расчета должна быть не одна метрика, а weighted composite. Каждая важная метрика получает свой вес, а итоговая точка на графике - это средневзвешенный коэффициент.

```text
valuation_score = weighted average of:
- P/E coefficient
- Forward P/E coefficient
- P/B coefficient
- P/S coefficient
- sector-specific metric coefficient
```

Формула:

```text
sector_score =
metric_1_coefficient x metric_1_weight
+ metric_2_coefficient x metric_2_weight
+ metric_3_coefficient x metric_3_weight
+ ...
```

Сумма весов должна быть равна `100%`.

Важно: каждая метрика сначала переводится в один формат, где:

```text
1.00 = около исторической нормы
1.10 = примерно на 10% дороже нормы
0.80 = примерно на 20% дешевле нормы
```

Если метрика обратная, например `FCF yield`, `dividend yield` или `earnings yield`, ее нужно инвертировать, чтобы смысл остался единым:

```text
Для valuation multiples: выше = дороже.
Для yield metrics: ниже yield = дороже, выше yield = дешевле.
```

Пример для банков:

```text
Bank valuation score =
0.40 x P/B relative coefficient
+ 0.25 x P/E relative coefficient
+ 0.25 x P/TBV relative coefficient
+ 0.10 x ROE-adjusted score
```

Пример для semiconductors:

```text
Semiconductor valuation score =
0.35 x Forward P/E relative coefficient
+ 0.25 x P/S relative coefficient
+ 0.20 x P/B relative coefficient
+ 0.20 x EPS revisions adjustment
```

### Стартовые веса по секторам

Эти веса не являются вечными. Это рабочая версия для нашей библиотеки. Если по сектору появится более качественная метрика, веса можно менять, но изменение нужно фиксировать в файле сектора.

| Сектор | Метрики и веса |
|---|---|
| Banks | P/B 35%, P/TBV 25%, P/E 20%, ROE/ROTCE adjustment 20% |
| Insurance | P/B 30%, P/E 25%, ROE 25%, combined ratio / underwriting quality 20% |
| Asset managers / brokers | P/E 30%, P/AUM or AUM yield 20%, operating margin 20%, net flows 15%, market beta/AUM sensitivity 15% |
| Payment networks | Forward P/E 35%, EV/EBITDA 25%, P/S 20%, revenue growth / cross-border volume 20% |
| REIT | P/FFO 35%, NAV discount/premium 25%, dividend yield 20%, debt cost / leverage 20% |
| Energy | EV/EBITDA 30%, FCF yield 30%, P/E 15%, reserve life / production cost 15%, commodity price adjustment 10% |
| Mining / Materials | EV/EBITDA 25%, P/NAV 25%, FCF yield 20%, commodity price adjustment 20%, balance sheet 10% |
| Semiconductors | Forward P/E 30%, P/S 20%, P/B 15%, gross margin 15%, EPS revisions / guidance 20% |
| Software / Internet | Forward P/E 25%, EV/Sales 25%, FCF margin 20%, revenue growth 20%, Rule of 40 10% |
| Consumer discretionary | Пилот: P/E 25%, Forward P/E 25%, EV/EBITDA 20%, P/S 15%, P/FCF 15%. Финальная версия: добавить gross margin, same-store sales / volume и consumer cycle |
| Consumer staples / Food | P/E 30%, EV/EBITDA 25%, dividend yield 15%, pricing power / gross margin 20%, volume growth 10% |
| Health care services / medtech | P/E 30%, EV/EBITDA 25%, revenue growth 15%, margins 15%, reimbursement / regulatory risk 15% |
| Pharma / mature health care | P/E 30%, EV/EBITDA 20%, dividend/FCF yield 20%, pipeline / patent cliff adjustment 20%, balance sheet 10% |
| Biotech / unprofitable growth | EV/Sales 25%, cash runway 25%, pipeline/rNPV 30%, dilution risk 20% |
| Utilities | Пилот: P/E 25%, Forward P/E 25%, EV/EBITDA 20%, dividend yield 20%, P/B 10%. Финальная версия: добавить allowed ROE / regulated asset base и debt cost |
| Telecom | EV/EBITDA 30%, FCF yield 25%, dividend sustainability 20%, leverage 15%, capex intensity 10% |

### Как добавлять точку в график

Для каждой якорной даты и сектора сохраняем:

```text
anchor_date
sector
metric
metric_coefficient
metric_weight
source
comment
actual_trading_date
```

Потом считаем итог:

```text
sector_score = сумма(metric_coefficient x metric_weight)
```

На графике рисуется только `sector_score`, но в данных должны оставаться все компоненты. Это важно, чтобы потом понимать, почему сектор получился дорогим или дешевым.

### Пилотные данные: Banks, Semiconductors, Mining, Energy, Utilities и Consumer Discretionary

Обновлено: 2026-05-31.

Сделана первая тестовая серия из последних 10 якорных точек: 2026-02-28, 2026-03-10, 2026-03-20, 2026-03-30, 2026-04-10, 2026-04-20, 2026-04-30, 2026-05-10, 2026-05-20, 2026-05-30.

Методика пилота:

- текущие мультипликаторы и годовые значения FY2021-FY2025 взяты из StockAnalysis по выбранным ключевым компаниям;
- `five_year_average` считается как среднее FY2021-FY2025;
- `metric_coefficient = current metric / five_year_average`;
- для якорных дат до последней даты коэффициенты масштабируются по закрытию ETF-прокси на последний торговый день до якорной даты, потому что фундаментальные мультипликаторы внутри коротких промежутков почти не меняются;
- для Banks ETF-proxy - `KBE`;
- для Semiconductors ETF-proxy - `SOXX`;
- для Mining ETF-proxy - `PICK`;
- для Energy ETF-proxy - `XLE`.
- для Utilities ETF-proxy - `XLU`.
- для Consumer Discretionary ETF-proxy - `XLY`.

Важно: это первая рабочая версия графика, а не окончательная институциональная модель. Она нужна, чтобы проверить формат данных, механику одной точки в день и визуальную полезность графика.

Ключевые итоговые значения на якорную дату 2026-05-30, где фактическое торговое закрытие - 2026-05-29:

| Сектор | Компоненты | Итоговый `sector_score` | Интерпретация |
|---|---|---:|---|
| Banks | P/B 35%, P/TBV 25%, P/E 20%, Forward P/E 20% | `1.43` | выбранная банковская корзина торгуется примерно на 43% выше своей 5-летней нормы по этим мультипликаторам |
| Semiconductors | Forward P/E 30%, P/S 25%, P/B 20%, EV/EBITDA 25% | `1.82` | выбранная semiconductor-корзина торгуется примерно на 82% выше своей 5-летней нормы по этим мультипликаторам |
| Mining | EV/EBITDA 35%, P/FCF 25%, P/B 20%, P/E 20% | `1.54` | выбранная mining-корзина торгуется примерно на 54% выше своей 5-летней нормы по этим мультипликаторам |
| Energy | EV/EBITDA 35%, P/FCF 30%, P/E 20%, P/B 15% | `1.50` | выбранная energy-корзина торгуется примерно на 50% выше своей 5-летней нормы по этим мультипликаторам |
| Utilities | P/E 25%, Forward P/E 25%, EV/EBITDA 20%, Dividend Yield 20%, P/B 10% | `0.98` | выбранная regulated utilities-корзина около своей 5-летней нормы; trailing P/E и EV/EBITDA дешевле нормы, но dividend yield и forward P/E не дают явного дисконта |
| Consumer Discretionary | P/E 25%, Forward P/E 25%, EV/EBITDA 20%, P/S 15%, P/FCF 15% | `0.81` | выбранная consumer discretionary-корзина без `TSLA` торгуется примерно на 19% ниже своей 5-летней нормы по этим мультипликаторам |

Ограничение по Mining: в пилоте `P/B` используется как грубый proxy для `P/NAV`, потому что настоящий `P/NAV` требует моделей запасов, проектов и долгосрочной цены металлов. Для финальной версии mining лучше добавить `P/NAV`, cost curve и commodity price adjustment.

Ограничение по Energy: в пилоте пока нет commodity price adjustment по нефти/газу и reserve life / production cost. Поэтому это valuation-only слой по выбранной корзине, а не полный through-cycle energy score.

Ограничение по Utilities: в пилоте считаются только regulated electric utilities (`NEE`, `DUK`, `SO`, `AEP`, `D`) через `XLU`. Pipeline/gas infrastructure внутри папки нужно считать отдельно, потому что у midstream другая экономика: EV/EBITDA, FCF yield, leverage, contracted cash flows и commodity exposure.

Ограничение по Consumer Discretionary: `TSLA` не включается в расчет, потому что в нашей библиотеке это AI / robotics / autonomous taxi thesis, а не consumer/autos thesis. В пилоте пока нет same-store sales, gross margin, inventory quality и EPS revisions, поэтому это valuation-only слой.

Ряды уже добавлены в `sector_valuation_dashboard.html`.

### Как учитывать прибыль

Оценка сектора без прибыли неполная. Поэтому рядом с valuation coefficient нужно хранить earnings signal:

```text
earnings_signal:
+1 = EPS estimates растут, отчеты лучше ожиданий
 0 = нейтрально
-1 = EPS estimates падают, отчеты хуже ожиданий
```

Практическая интерпретация:

| Valuation | Earnings | Вывод |
|---|---|---|
| Дешево | Улучшается | Лучший вариант для поиска идей |
| Дешево | Ухудшается | Возможная value trap |
| Дорого | Улучшается | Может быть оправданный premium sector |
| Дорого | Ухудшается | Риск переоценки |

### Как учитывать бизнес-цикл

Fidelity отдельно связывает sector views с исторической вероятностью outperformance и стадиями цикла. Для нас это значит: коэффициент дешевизны не должен автоматически означать "покупать".

Нужна связка:

```text
valuation coefficient + earnings signal + cycle regime + technical trend
```

Например:

- банки дешевы, но кривая инвертирована, credit losses растут - покупку откладываем;
- semiconductors дороги, но EPS revisions резко растут и AI capex ускоряется - дороговизна может быть оправдана;
- energy дешевый, но нефть падает и FCF ухудшается - это не обязательно возможность;
- utilities дорогие при росте доходностей облигаций - это риск.

### Практическая версия для нашей библиотеки

Для декадной версии графика используем простой коэффициент:

```text
coefficient = current relative valuation / historical average relative valuation
```

Дополнительно сохраняем:

- текущий P/E;
- текущий P/B;
- текущий P/S;
- forward P/E, если доступен;
- источник;
- дату данных;
- комментарий, почему сектор дорогой или дешевый.

### Более профессиональная версия

State Street в Sector Scorecard использует 15-летнюю историю и считает percentile rankings для абсолютных и относительных valuation metrics: `P/B`, `P/E`, `NTM P/E`, `P/S`. Затем метрики стандартизируются через z-score и объединяются в composite score.

Fidelity использует похожую идею: относительные valuation metrics сектора к S&P 500 сравниваются с 10-летней исторической средней относительной оценкой; крайние 5% значений сверху и снизу исключаются, чтобы снизить влияние выбросов.

Для нашей практики это означает:

1. Сначала делаем простой коэффициент `current / historical norm`.
2. Потом добавляем percentile или z-score, если будет достаточно истории.
3. На графике показываем коэффициент, а рядом храним исходные мультипликаторы.
4. Не делаем решение только по valuation coefficient: обязательно смотрим earnings, цикл ставок, макро и техническую картину.

### Источники методологии

- [State Street Sector Scorecard, methodology](https://www.ssga.com/library-content/pdfs/etf/us/spdr-sector-scorecard.pdf)
- [Fidelity Quarterly Sector and Investment Research Update, methodology](https://www.fidelity.com/bin-public/600_Fidelity_Com_English/documents/learning-center/Quarterly-Sector-and-Investment-Research-Update-Q1-2026.pdf)
- [Fidelity Q2 2026 Quarterly Sector and Investment Research Update](https://clearingcustody.fidelity.com/insights/topics/market-commentary/second-quarter-2026-quarterly-sector-and-investment-research-update)
- [MSCI: Valuations Can Help in Evaluating Sectors](https://www.msci.com/research-and-insights/quick-take/valuations-can-help-in-evaluating-sectors)
- [Morningstar Equity Research Methodology](https://advisor.morningstar.com/Enterprise/VTC/MasterEquityResearchMethodology_Oct2020.pdf)
- [MSCI/S&P Dow Jones: GICS methodology](https://www.msci.com/indexes/documents/methodology/1_MSCI_Global_Industry_Classification_Standard_GICS_Methodology_20250220.pdf)

## Формат обновления

```text
Дата:
Режим рынка:
Главные события:
Что изменилось для портфеля:
Что проверить дальше:
```
