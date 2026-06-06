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

### Следующий шаг: автоматизация загрузки данных

Чтобы не собирать точки вручную и не тратить токены на повторный поиск, нужна отдельная автоматическая загрузка.

Рабочая схема:

1. В конфиге хранить список секторов, тикеры корзины, метрики, веса, benchmark/ETF и ссылки на источники.
2. Скрипт сам определяет якорные даты: 10-е, 20-е, 30-е / конец месяца; если дата не торговая, берет последний торговый день до нее.
3. Для каждой компании и метрики скрипт скачивает реальное historical valuation data на эту дату или ближайший доступный valuation snapshot.
4. Скрипт считает `metric_coefficient` против 5-летней нормы, затем `sector_score`.
5. На выходе сохраняется CSV/JSON с полями `anchor_date`, `actual_trading_date`, `sector`, `metric`, `metric_coefficient`, `metric_weight`, `source`, `source_date`, `status`, `comment`.
6. Если историческая valuation-метрика недоступна, строка получает статус `missing` или `provisional`. Нельзя заменять ее масштабированием последней оценки по ETF.

Первый слой автоматизации по котировкам уже вынесен отдельно:

- скрипт: `scripts/fetch_anchor_quotes.py`;
- конфиг тикеров: `data/market_quotes/sector_quote_tickers.json`;
- результат CSV: `data/market_quotes/anchor_quotes.csv`;
- результат JSON: `data/market_quotes/anchor_quotes.json`;
- провайдеры как в старом сайте учета инвестиций: Financial Modeling Prep для US/global тикеров и MOEX ISS для российских инструментов;
- FMP key не хранится в текущем репозитории: скрипт сначала читает env vars, затем локально берет legacy key из старого проекта, если файл существует;
- старые FMP `/api/v3` endpoints сейчас возвращают legacy error, поэтому скрипт использует новые FMP `/stable` endpoints;
- строки со статусом `provider_error`, `missing` или `provisional` нельзя использовать как реальные котировки.

Прогон от 2026-06-01 по 10 якорным датам дал `1390` строк: `400` успешных и `990` со статусом `provider_error`. Главная причина ошибок - текущая подписка FMP не дает доступ к части ETF, ADR, foreign listings и некоторым US tickers через API. Эти строки сохранены как диагностика, но не подменяются другими данными.

Уточнение по FMP от 2026-06-01:

- для одиночной исторической цены правильный endpoint - `stable/historical-price-eod/full`;
- `batch-quote` и `batch-quote-short` дают текущие котировки, а не исторические закрытия 10/20/30;
- для массовой исторической загрузки правильный endpoint - `stable/eod-bulk?date=YYYY-MM-DD`;
- текущий ключ возвращает `HTTP 402: Restricted Endpoint` на `batch-quote`, `batch-quote-short` и `eod-bulk`;
- текущий ключ также возвращает `HTTP 402` по части тикеров даже на одиночном `historical-price-eod/full`, хотя другие тикеры на том же endpoint работают. Значит проблема не в формате запроса и не в лимите количества запросов, а в покрытии/подписке ключа.
- если покупать/обновлять FMP, для нашей задачи нужен план с `Global Coverage` и `Bulk and Batch Delivery`; по публичной странице FMP это соответствует уровню `Ultimate`.
- ссылки для следующего запуска: historical EOD `https://site.financialmodelingprep.com/developer/docs/stable/historical-price-eod-full`, EOD bulk `https://site.financialmodelingprep.com/developer/docs/stable/eod-bulk`, batch quote `https://site.financialmodelingprep.com/developer/docs/stable/batch-quote`, pricing `https://intelligence.financialmodelingprep.com/pricing-plans?direct=true`.

Бесплатные альтернативы для исторических закрытий:

- MOEX ISS остается основным бесплатным источником для российских инструментов.
- Twelve Data - лучший бесплатный fallback для US/global daily OHLCV: endpoint `time_series`, `interval=1day`, `start_date`, `end_date`; free plan дает `8` credits/minute и `800/day`, `time_series` стоит `1` credit per symbol. Скрипт уже подготовлен: если добавить `TWELVE_DATA_API_KEY` в `.env`, он будет пробовать Twelve Data после ошибки FMP и по умолчанию выдерживать паузу `8` секунд между такими запросами.
- Alpha Vantage можно держать резервом: `TIME_SERIES_DAILY` дает daily OHLCV, но free limit всего `25` requests/day, а `outputsize=full` для 20+ лет требует premium.
- Stooq теперь требует свой API key через captcha для CSV download, поэтому не подходит для полностью автоматической настройки без ручного шага.
- Yahoo Finance chart API неофициальный и в тесте вернул `Too Many Requests`; как основа автоматизации не подходит.

### Источники исторических фундаментальных данных

Обновлено: 2026-06-01.

Для полноценной секторной карты нужны не только цены. Минимальный набор данных:

- historical close на anchor date;
- последние доступные на anchor date квартальные/годовые отчеты: income statement, balance sheet, cash flow;
- дата публикации/принятия отчета (`filingDate`, `acceptedDate`, `filedDate`), чтобы не использовать будущую информацию;
- shares outstanding / diluted shares;
- debt, cash, equity;
- дивиденды и split/corporate actions;
- желательно готовые historical ratios/key metrics, но их можно пересчитать самостоятельно.

Рабочая формула: не искать готовый `historical P/E` как обязательный источник, а строить его самим:

```text
market_cap(anchor) = close(anchor) x shares_outstanding(anchor)
enterprise_value(anchor) = market_cap + total_debt - cash
P/E = market_cap / TTM net_income
P/S = market_cap / TTM revenue
P/B = market_cap / latest_common_equity
EV/EBITDA = enterprise_value / TTM EBITDA
FCF yield = TTM free_cash_flow / market_cap
ROE = TTM net_income / average_or_latest_equity
gross_margin = TTM gross_profit / TTM revenue
```

Обязательное point-in-time правило: для anchor date брать только отчеты, у которых `acceptedDate/filingDate <= anchor_date`. Если брать просто fiscal quarter без даты публикации, получится look-ahead bias.

Оценка источников:

| Источник | Что закрывает | Плюсы | Ограничения | Роль в проекте |
|---|---|---|---|---|
| SEC EDGAR Company Facts | US и SEC-reporting ADR: financial statements, XBRL facts, filing timeline | Бесплатно, официальный источник, есть ticker-CIK map, покрывает `AAPL`, `MS`, `HD`, `JPM`, `NVDA`, `AMD`, `TSM`, `ASML`, `BABA`, `NVO`, `SHEL` | Нужно нормализовать XBRL-теги, нет цен/EV готовыми, не все foreign/local listings | Главный бесплатный фундаментальный слой для US/ADR |
| FMP текущий ключ | Statement data и enterprise values по части тикеров | Уже подключен, есть `acceptedDate`, statements и EV; по `AAPL/JPM/BABA` работает | Текущий ключ дает `HTTP 402` по части тикеров (`MS`, `HD`, `ASML`, `700.HK`) и по готовым `key-metrics/ratios` | Использовать там, где работает; остальное закрывать fallback |
| SimFin | Statements, derived ratios, prices, common shares outstanding | Есть бесплатный аккаунт/API, rate limit free `2 requests/second`; есть `asreported` и point-in-time shares | Нужен ключ; покрытие и качество по нашим non-US/ETF нужно отдельно проверить | Хороший кандидат для бесплатного/дешевого фундаментального fallback |
| Alpha Vantage | Income statement, balance sheet, cash flow, earnings | Бесплатный ключ, простые endpoints | `25 requests/day`; `TIME_SERIES_DAILY full` premium; не решает массовую загрузку | Только резерв/ручная проверка |
| EODHD | Global EOD prices, fundamentals, ETF/funds/indices, historical market cap, macro/calendar | Глобальное покрытие, 70+ exchanges, fundamentals history; pricing выглядит дешевле FMP Ultimate | Платно для полной задачи; нужно проверить поля и качество на наших тикерах | Лучший кандидат на один практичный платный источник для global |
| Nasdaq Data Link / Sharadar | US fundamentals/prices, point-in-time, survivorship-bias aware | Хороший quant-grade вариант для US | Premium, в основном US; глобальные сектора не закроет | Рассмотреть, если делаем серьезный US-only backtest |
| Polygon/Massive | US prices, financials & ratios add-on | Удобно для US, есть financial statements/ratios | US-only; financials add-on, не закрывает глобальный список | Альтернатива для US, не главный global вариант |
| Tiingo | Historical prices, fundamentals statements, daily metrics | Есть daily fundamentals/metrics по тикерам | Нужно проверить текущий доступ/цены/покрытие на нашем ключе | Кандидат на тест, но не первый выбор |
| StockAnalysis/Finviz/ChartMill/WorldPERatio | Current/historical визуальные sector ratios | Удобны для сверки и sanity check | Не полноценная автоматизация по anchor dates | Контрольный слой, не primary data pipeline |

Рекомендуемая архитектура:

1. Цены: `MOEX ISS` для РФ, `Twelve Data` free fallback и `FMP` там, где текущий ключ работает.
2. Фундаментал бесплатно: `SEC EDGAR Company Facts` для US/ADR; рассчитывать P/E, P/B, P/S, EV/EBITDA, FCF yield, ROE самостоятельно.
3. Фундаментал платно/глобально: первым тестировать `EODHD Fundamentals`, потому что он закрывает global/fundamentals/ETF шире и дешевле, чем FMP Ultimate.
4. FMP upgrade рассматривать только если хотим оставить FMP главным источником всего: prices bulk + global symbols + historical ratios/key metrics.
5. Для estimates/revisions/guidance отдельный слой. Это обычно платные данные; на первом этапе не блокировать sector_score, а помечать такие метрики как `missing/provisional`, если нет надежного источника.

Текущий статус автоматизации фундаментала: `scripts/fetch_anchor_fundamentals.py` уже создан. Он берет anchor dates, цены из `anchor_quotes`, фундаментал из SEC EDGAR, использует только отчеты с `filed <= anchor_date` и сохраняет сырые point-in-time метрики. Слой агрегации `scripts/build_sector_scores_preview.py` уже превращает сырые метрики компаний в `metric_coefficient` против 5-летней нормы и пишет итоговый `sector_score` по сектору. Реальные preview-точки на графике сейчас подставляются для `Banks`, `Semiconductors`, `Technology` и `Mining`; остальные сектора пока остаются legacy/prototype до сбора такого же raw/fundamental/baseline слоя.

Обновление 2026-06-03 по `Mining`: котировки на 10 якорных дат покрыты 7/7 через Twelve Data fallback; SEC-фундаментал покрывает 5/7 (`FCX`, `GOLD`, `NEM`, `SCCO`, `VALE`), `BHP` и `RIO` пока исключены из preview из-за отсутствия clean TTM net income window. Последняя автоматическая preview-точка на 2026-05-30 равна `1.22`; старое ручное значение `1.54` ниже в таблице остается legacy/prototype и не должно смешиваться с новым автоматическим слоем.

Ссылки на документацию источников:

- SEC EDGAR APIs: `https://www.sec.gov/edgar/sec-api-documentation`
- SEC ticker-CIK map: `https://www.sec.gov/files/company_tickers.json`
- FMP stable docs: `https://site.financialmodelingprep.com/developer/docs/stable`
- SimFin API docs: `https://simfin.readme.io/reference/getting-started-1`
- SimFin rate limits: `https://simfin.readme.io/reference/rate-limits`
- EODHD Fundamentals: `https://eodhd.com/financial-apis/stock-etfs-fundamental-data-feeds`
- EODHD pricing: `https://eodhd.com/pricing`
- Alpha Vantage fundamentals: `https://www.alphavantage.co/documentation/`
- Twelve Data time series: `https://twelvedata.com/docs#time-series`
- Polygon/Massive pricing: `https://massive.com/pricing`

### Пилотные данные: chart-ready sectors

Обновлено: 2026-05-31.

Сделана тестовая серия из последних 10 якорных точек: 2026-02-28, 2026-03-10, 2026-03-20, 2026-03-30, 2026-04-10, 2026-04-20, 2026-04-30, 2026-05-10, 2026-05-20, 2026-05-30.

Важно: текущая CSV-история в `sector_valuation_dashboard.html` является прототипом и содержит legacy benchmark-check строки. Ее нельзя считать финальной историей sector_score, пока точки не будут заменены реальными historical valuation data на 10/20/30.

Методика пилота:

- текущие мультипликаторы и годовые значения FY2021-FY2025 взяты из StockAnalysis по выбранным ключевым компаниям;
- `five_year_average` считается как среднее FY2021-FY2025;
- `metric_coefficient = current metric / five_year_average`;
- для yield-метрик используется обратная формула `5Y average yield / current yield`, чтобы выше `1.0` всегда означало дороже;
- каждая якорная дата 10/20/30 должна строиться по реальным valuation data на соответствующий торговый день, а не через масштабирование последней оценки по ETF-прокси;
- если метрика недоступна, отрицательная или экономически бессмысленная для конкретной компании, она исключается из средней по этой метрике;
- если вся метрика недоступна для сектора, она исключается, а веса нормализуются по оставшимся метрикам.

ETF-proxy по новым секторам:

- для Agriculture & Chemicals ETF-proxy - `XLB`.
- для AI Infrastructure ETF-proxy - `AIQ`.
- для China ETF-proxy - `MCHI`.
- для Commodities ETF-proxy - `PICK`.
- для Delivery & Logistics ETF-proxy - `IYT`.
- для Drugs ETF-proxy - `XLV`.
- для Food & Staples ETF-proxy - `XLP`.
- для Insurance ETF-proxy - `KIE`.
- для Medical Services ETF-proxy - `IHI`.
- для REIT ETF-proxy - `VNQ`.
- для Solar ETF-proxy - `TAN`.
- для Technology ETF-proxy - `XLK`.
- для Telecom & Streaming ETF-proxy - `XLC`.

Важно: это рабочая valuation-only версия графика, а не окончательная институциональная модель. Она нужна, чтобы проверить формат данных, механику одной точки на сектор и визуальную полезность графика.

Ключевые итоговые значения на якорную дату 2026-05-30, где фактическое торговое закрытие обычно 2026-05-29:

| Сектор | Компоненты | Итоговый `sector_score` | Интерпретация |
|---|---|---:|---|
| Medical Services | Forward P/E 0.65 x 30%<br>P/E 0.68 x 25%<br>EV/EBITDA 0.67 x 20%<br>P/S 0.68 x 15%<br>P/FCF 0.61 x 10% | `0.66` | дешевле своей 5-летней нормы |
| Telecom & Streaming | EV/EBITDA 0.75 x 30%<br>Forward P/E 0.73 x 25%<br>P/E 0.63 x 20%<br>P/S 0.91 x 15%<br>P/FCF 0.65 x 10% | `0.73` | дешевле своей 5-летней нормы |
| China | Forward P/E 0.79 x 30%<br>P/E 0.72 x 25%<br>P/S 0.79 x 20%<br>P/B 0.75 x 15%<br>EV/EBITDA 0.73 x 10% | `0.76` | дешевле своей 5-летней нормы |
| Consumer Discretionary | P/E 0.78 x 25%<br>Forward P/E 0.77 x 25%<br>EV/EBITDA 0.79 x 20%<br>P/S 0.76 x 15%<br>P/FCF 0.99 x 15% | `0.81` | дешевле своей 5-летней нормы |
| Technology | Forward P/E 0.80 x 30%<br>P/E 0.69 x 20%<br>EV/EBITDA 0.85 x 20%<br>P/S 0.93 x 20%<br>P/FCF 1.01 x 10% | `0.84` | дешевле своей 5-летней нормы |
| Insurance | P/B 0.89 x 35%<br>P/E 0.87 x 25%<br>Forward P/E 0.79 x 25%<br>P/S 0.93 x 15% | `0.87` | дешевле своей 5-летней нормы |
| Drugs | Forward P/E 1.03 x 30%<br>P/E 0.80 x 25%<br>EV/EBITDA 0.71 x 20%<br>P/FCF 0.89 x 15%<br>P/S 0.91 x 10% | `0.88` | дешевле своей 5-летней нормы |
| Agriculture & Chemicals | P/E 0.95 x 25%<br>Forward P/E 0.90 x 25%<br>EV/EBITDA 0.96 x 20%<br>P/S 0.95 x 15%<br>P/FCF 0.87 x 15% | `0.93` | около своей 5-летней нормы |
| Delivery & Logistics | EV/EBITDA 0.95 x 30%<br>Forward P/E 0.95 x 25%<br>P/E 1.00 x 20%<br>P/S 1.25 x 15%<br>P/FCF 0.66 x 10% | `0.98` | около своей 5-летней нормы |
| Utilities | P/E 0.87 x 25%<br>Forward P/E 1.03 x 25%<br>EV/EBITDA 0.92 x 20%<br>Dividend Yield 1.09 x 20%<br>P/B 1.02 x 10% | `0.98` | около своей 5-летней нормы |
| REIT | Dividend Yield 1.08 x 36%<br>P/B 1.18 x 29%<br>EV/EBITDA 1.00 x 21%<br>P/S 1.00 x 14% | `1.08` | около своей 5-летней нормы |
| Food & Staples | P/E 1.20 x 25%<br>Forward P/E 1.03 x 25%<br>EV/EBITDA 1.05 x 20%<br>Dividend Yield 1.13 x 15%<br>P/S 1.02 x 15% | `1.09` | около своей 5-летней нормы |
| Solar | Forward P/E 1.24 x 30%<br>EV/EBITDA 0.92 x 25%<br>P/S 1.06 x 20%<br>P/FCF 1.25 x 15%<br>P/B 1.03 x 10% | `1.10` | дороже своей 5-летней нормы |
| AI Infrastructure | Forward P/E 1.16 x 30%<br>P/S 1.53 x 25%<br>P/B 1.12 x 15%<br>EV/EBITDA 1.43 x 20%<br>P/FCF 1.40 x 10% | `1.32` | дороже своей 5-летней нормы |
| Banks | P/B 1.64 x 35%<br>P/TBV 1.49 x 25%<br>P/E 1.26 x 20%<br>Forward P/E 1.16 x 20% | `1.43` | дороже своей 5-летней нормы |
| Energy | EV/EBITDA 1.37 x 35%<br>P/FCF 1.79 x 30%<br>P/E 1.57 x 20%<br>P/B 1.10 x 15% | `1.50` | дороже своей 5-летней нормы |
| Commodities | EV/EBITDA 1.58 x 35%<br>P/FCF 1.36 x 25%<br>P/B 1.34 x 20%<br>P/E 1.85 x 20% | `1.53` | дороже своей 5-летней нормы |
| Mining | EV/EBITDA 1.59 x 35%<br>P/FCF 1.42 x 25%<br>P/B 1.59 x 20%<br>P/E 1.56 x 20% | `1.54` | дороже своей 5-летней нормы |
| Semiconductors | Forward P/E 1.30 x 30%<br>P/S 2.16 x 25%<br>P/B 2.24 x 20%<br>EV/EBITDA 1.74 x 25% | `1.82` | дороже своей 5-летней нормы |

Ограничения по готовности:

- `RUSSIA` не добавлен в этот график: для него нужна отдельная модель на базе MOEX/локальных мультипликаторов, ставок ЦБ РФ, валютного риска и ликвидности.
- `JUNIOR` не добавлен как обычный сектор: junior miners требуют NAV/cash runway/dilution-risk модели, а не простого P/E/P/B.
- `ETF`, `MY_PORTFOLIO`, `DECISIONS`, `ARCHIVE` и `COMPANIES` не являются секторными корзинами для этого графика.

Ряды добавлены в `sector_valuation_dashboard.html`.

### Аудит логики sector_score от 2026-06-01

Статус: текущий график полезен как `v0 / valuation-only radar`, но исторические точки, которые были построены через legacy ETF benchmark-check, нужно заменить на реальные valuation data по датам 10/20/30. Главная задача следующего шага - автоматизировать сбор этих точек скриптами, чтобы график строился по фактическим данным без ручного поиска.

#### Главные методологические выводы

1. Базовая логика `current company multiple / FY2021-FY2025 average company multiple` остается основной. Это именно то, что нужно графику: насколько текущая оценка корзины выше или ниже своей 5-летней нормы.
2. `Relative valuation vs S&P 500` можно добавить позже как дополнительный слой, но не как замену базовой 5-летней логике. Он нужен, если мы захотим понять, дорогой ли сектор не только относительно себя, но и относительно рынка.
3. Исторические точки нельзя строить через движение ETF вместо реальных мультипликаторов. Для каждой даты 10/20/30 нужны фактические valuation data на этот день или последний торговый день до него. Если источник не хранит исторические мультипликаторы, точку нужно подтянуть другим источником или оставить как `missing/provisional`, а не подменять ее движением ETF.
4. Общие корзины пока сохраняем. Цель графика - видеть общую картину, а не сразу дробить рынок на десятки узких подотраслей. Разделение нужно только там, где смешивание начинает явно искажать смысл.
5. Исключение `TSLA` из Consumer Discretionary остается правильным рабочим решением пользователя. Tesla в этой библиотеке относится к AI / robotics / autonomous taxi thesis, а не к обычной consumer/autos оценке.
6. Для ETF-proxy надо хранить два источника: официальный сайт эмитента ETF для проверки состава/назначения фонда и StockAnalysis ETF history только для цен закрытия.
7. Нужна защита от выбросов: среднее по мультипликаторам может ломаться из-за разовых очень высоких/низких P/E, P/FCF или временно отрицательной прибыли. В следующей версии рассмотреть median или winsorized mean.
8. Valuation-only score не должен означать "покупать". Его нужно читать вместе с `earnings_signal`, бизнес-циклом, ставками, commodity backdrop и трендом.

#### Проверка ETF-proxy и корзин

| Сектор | Статус корзины/proxy | Что уточнить |
|---|---|---|
| Banks | Корзина `JPM`, `BAC`, `C`, `GS`, `MS` логична как large-cap banks / capital markets basket. `KBE` как proxy шире и включает regional banks. | Проверить официальный состав `KBE`; решить, насколько нас устраивает этот proxy для large-bank корзины. Добавить ROE/ROTCE и credit quality как следующий слой. |
| Semiconductors | `SOXX` подходит как официальный semiconductor proxy. Корзина в целом правильная. | Проверить официальный состав `SOXX`; решить, нужны ли `AMAT`, `LRCX`, `KLAC`, `MRVL`. Добавить gross margin и EPS revisions. |
| Mining | Корзина дает общую картину metals/mining, но смешивает diversified/base metals и gold miners. `PICK` ориентирован на broad metals/mining proxy. | Проверить официальный состав `PICK`; оставить общую картину, но пометить, где gold miners могут искажать связь с proxy. Добавить P/NAV и commodity price adjustment. |
| Energy | Корзина majors + service логична. `XLE` - хороший US energy proxy, но не полностью отражает `SHEL`/`TTE`. | Проверить официальный состав `XLE`; пока оставить как грубый proxy. Добавить oil/gas price adjustment, reserve life, production cost, leverage. |
| Utilities | Корзина regulated utilities подходит к `XLU`. | Проверить официальный состав `XLU`; gas infrastructure пока не добавлять в общий score без отдельной midstream логики. |
| Consumer Discretionary | Корзина без `TSLA` соответствует пользовательской классификации. `XLY` остается грубым benchmark, хотя официальный `XLY` может включать TSLA. | Проверить официальный состав `XLY`; в файле сектора явно писать, что TSLA исключена осознанно, а `XLY` используется только для проверки состава и ценового контекста, не для расчета исторического sector_score. |
| Agriculture & Chemicals | Корзина логична для chemicals/ag inputs, `XLB` подходит как broad materials proxy, но не чистый agriculture proxy. | Проверить официальный состав `XLB`; оставить mixed basket, но добавить fertilizer cycle и raw material input costs. |
| AI Infrastructure | Это thematic basket, а не классический GICS-сектор. `AIQ` подходит как тематический proxy. | Проверить официальный состав `AIQ`; везде называть это theme score. Добавить capex/compute demand, EPS revisions, AI revenue exposure. |
| China | `MCHI` подходит как broad China proxy, но корзина неполная для китайского рынка. | Проверить официальный состав `MCHI`; позже добавить недостающих лидеров, если есть надежные ratio sources. |
| Commodities | Общая commodities-корзина дает нужную широкую картину, но пересекается с Mining и использует тот же `PICK`. | Проверить официальный состав `PICK`; оставить общую картину, но явно пометить пересечение с Mining и разные commodity cycles. |
| Delivery & Logistics | `IYT` официально дает transportation exposure, а наша корзина шире: parcel/freight плюс platforms и Amazon logistics. | Проверить официальный состав `IYT`; решить, достаточно ли он подходит как price proxy для такой широкой корзины. |
| Drugs | Large pharma basket логична. `XLV` слишком широкий, но подходит как broad healthcare fallback. | Проверить официальный состав `XLV`; позже добавить patent cliff/pipeline/rNPV. |
| Food & Staples | `XLP` хорошо подходит для staples, но `MCD` и `SBUX` дают restaurant exposure. | Проверить официальный состав `XLP`; пока оставить общую картину Food & Staples, но пометить restaurant exposure. |
| Insurance | `KIE` подходит для insurance industry. Текущая корзина шире: P&C, health insurance, broker and Berkshire. | Проверить официальный состав `KIE`; решить, оставлять ли broad insurance basket или сузить его под pure insurance proxy. |
| Medical Services | `IHI` - medical devices ETF. Корзина больше похожа на medtech/devices + life sciences tools. | Проверить официальный состав `IHI`; возможно переименовать score в `Medical Devices / MedTech`, если корзина остается такой. |
| REIT | `VNQ` подходит как broad real estate/REIT proxy. | Проверить официальный состав `VNQ`; добавить P/FFO, AFFO yield, NAV discount/premium, cap rates, debt maturity/cost. |
| Solar | `TAN` подходит как solar proxy; корзина в целом логична. | Проверить официальный состав `TAN`; добавить bookings, gross margin, policy/rates и balance-sheet risk. |
| Technology | Корзина шире официального `XLK`, потому что включает `GOOG`/`META`. Это допустимо для нашей общей technology-картины, но `XLK` является грубым proxy. | Проверить официальный состав `XLK`; решить, нужен ли custom basket proxy для широкой technology-корзины. Для software добавить EV/Sales, FCF margin, growth/Rule of 40. |
| Telecom & Streaming | `XLC` подходит как broad communication services proxy; корзина смешивает telecom operators, streaming, media and platforms. | Проверить официальный состав `XLC`; пока оставить общую communication/streaming картину. Для telecom добавить FCF yield, leverage, dividend sustainability, capex intensity. |

#### Источники для проверки ETF-proxy

- `XLY`, `XLK`, `XLC`, `XLV`, `XLP`, `XLE`, `XLB`, `XLU` - официальный сайт [State Street / Select Sector SPDR](https://www.ssga.com/us/en/intermediary/capabilities/equities/sector-investing/select-sector-etfs).
- `SOXX` - официальный сайт [iShares Semiconductor ETF](https://www.ishares.com/us/products/239705/ishares-semiconductor-etf).
- `IYT` - официальный сайт [iShares U.S. Transportation ETF](https://www.ishares.com/us/products/239501/ishares-us-transportation-etf).
- `PICK` - официальный сайт [iShares MSCI Global Metals & Mining Producers ETF](https://www.ishares.com/us/products/239655/ishares-msci-global-metals-mining-producers-etf).
- `IHI` - официальный сайт [iShares U.S. Medical Devices ETF](https://www.ishares.com/us/products/239516/ishares-us-medical-devices-etf).
- `VNQ` - официальный сайт [Vanguard Real Estate ETF](https://investor.vanguard.com/investment-products/etfs/profile/vnq).
- `AIQ` - официальный сайт [Global X Artificial Intelligence & Technology ETF](https://www.globalxetfs.com/funds/aiq/).
- `KIE` - официальный сайт [State Street SPDR S&P Insurance ETF](https://www.ssga.com/us/en/intermediary/etfs/spdr-sp-insurance-etf-kie).
- StockAnalysis ETF history использовать только как источник цен ETF/benchmark и для проверки рыночного движения, но не как замену фактических historical valuation data.

#### Правило качества перед следующими расчетами

Перед тем как добавлять или обновлять секторную точку, нужно ответить на четыре вопроса:

1. Это GICS-like sector, theme basket или custom idea basket?
2. ETF-proxy действительно отражает эту корзину или используется только как грубый price proxy?
3. Вес метрик соответствует экономике сектора или это временная valuation-only замена?
4. Есть ли earnings/cycle signal, который объясняет, почему дороговизна может быть оправданной, а дешевизна может быть ловушкой?

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
