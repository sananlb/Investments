# Market Quotes Data

Этот каталог хранит автоматическую загрузку котировок для секторной карты.

## Файлы

- `sector_quote_tickers.json` - список секторных корзин и провайдеров.
- `anchor_quotes.csv` - закрытия на якорные даты 10/20/30 в табличном виде.
- `anchor_quotes.json` - те же данные с metadata.

## Команда обновления

```bash
python3 scripts/fetch_anchor_quotes.py --as-of 2026-06-01 --count 10
```

Без `--as-of` скрипт берет текущую дату.

Для Twelve Data fallback по бесплатному ключу скрипт по умолчанию держит паузу `8` секунд между запросами, чтобы не превысить free limit `8` credits/minute. При платном ключе это можно изменить:

```bash
python3 scripts/fetch_anchor_quotes.py --twelve-data-min-interval 0
```

## Источники

- Financial Modeling Prep `/stable/historical-price-eod/full` для US/global тикеров: https://site.financialmodelingprep.com/developer/docs/stable/historical-price-eod-full
- Financial Modeling Prep `/stable/eod-bulk` для массовой исторической загрузки по дате: https://site.financialmodelingprep.com/developer/docs/stable/eod-bulk
- Financial Modeling Prep `/stable/batch-quote` для текущих batch-котировок: https://site.financialmodelingprep.com/developer/docs/stable/batch-quote
- Financial Modeling Prep pricing: https://intelligence.financialmodelingprep.com/pricing-plans?direct=true
- Twelve Data `/time_series` как бесплатный fallback для дневных исторических цен: https://twelvedata.com/docs#time-series
- Twelve Data pricing/free limits: https://twelvedata.com/pricing
- Alpha Vantage `TIME_SERIES_DAILY` как резервный бесплатный источник: https://www.alphavantage.co/documentation/#daily
- MOEX ISS history для российских инструментов.

FMP key не хранится в этом репозитории. Скрипт читает `FMP_API_KEY`, `FINANCIAL_MODELING_PREP_API_KEY` или `FINANCIALMODELINGPREP_API_KEY`; если их нет, локально использует legacy key из старого проекта на рабочем столе.
Twelve Data key тоже не хранится в репозитории. Для бесплатного fallback нужно добавить в `.env` переменную `TWELVE_DATA_API_KEY`.

## Как правильно использовать FMP

Проверено 2026-06-01 по официальной документации FMP и реальными тестовыми запросами с текущим локальным ключом.

### Для исторических закрытий

Обычный endpoint:

```text
https://financialmodelingprep.com/stable/historical-price-eod/full?symbol=AAPL&from=2026-05-20&to=2026-05-20&apikey=...
```

Он возвращает `open`, `high`, `low`, `close`, `volume`, `change`, `changePercent`, `vwap`.

Это правильный endpoint для одиночного тикера и конкретной даты/диапазона дат. На текущем ключе он работает, например, для `AAPL`, `JPM`, `SPY`, `GOOGL`, но дает `HTTP 402` для части тикеров и ETF. Значит проблема не в формате запроса.

### Batch и bulk

FMP имеет два разных типа "много данных за один запрос":

- `batch-quote` / `batch-quote-short` - текущие котировки по нескольким тикерам, не исторические закрытия 10/20/30.
- `eod-bulk?date=YYYY-MM-DD` - исторические end-of-day цены по множеству символов за одну дату.

Для нашей задачи правильный массовый вариант - `eod-bulk`, потому что нам нужны реальные закрытия на конкретные даты.

На текущем ключе `batch-quote`, `batch-quote-short` и `eod-bulk` возвращают:

```text
HTTP 402: Restricted Endpoint
```

Это означает ограничение подписки, а не ошибку запроса.

### Лимиты и подписки FMP

По публичной странице FMP pricing:

- `Basic`: 250 calls/day, end-of-day historical data, profile/reference data.
- `Starter`: 300 calls/minute, up to 5 years historical data, US coverage.
- `Premium`: 750 calls/minute, up to 30 years historical data, UK/Canada coverage, full fundamentals/ratios.
- `Ultimate`: 3000 calls/minute, global coverage, ETF/mutual fund holdings, full historical access, bulk and batch delivery.

Для нашей секторной карты:

- если остаемся на текущем ключе/уровне, нужно делать per-symbol запросы и принимать, что часть тикеров будет `provider_error`;
- если нужен полный автоматический сбор через FMP по всем секторам, ETF и foreign listings, нужен уровень с global coverage и bulk/batch delivery, то есть ориентир - `Ultimate`;
- если нужен только US large-cap без ETF/foreign listings, возможно хватит `Starter/Premium`, но текущие тесты показывают, что даже часть US тикеров сейчас закрыта для нашего ключа.

Практический вывод: после апгрейда ключа скрипт нужно переводить на схему `eod-bulk` по каждой якорной дате, а затем фильтровать нужные тикеры локально. Это даст примерно `10` запросов на 10 точек вместо сотен per-symbol запросов.

## Бесплатные варианты для исторических дат

Проверено 2026-06-01.

### Twelve Data

Лучший бесплатный кандидат для fallback-слоя.

Endpoint:

```text
https://api.twelvedata.com/time_series?symbol=AAPL&interval=1day&start_date=2026-05-20&end_date=2026-05-21&apikey=...
```

Важно: для одной даты в тесте нужно ставить `end_date` следующим календарным днем, иначе Twelve Data может вернуть `No data is available on the specified dates`.

Плюсы:

- есть бесплатный ключ;
- `time_series` стоит `1` credit per symbol;
- free plan дает `8` API credits/minute и `800/day`;
- есть `start_date` и `end_date`, значит можно точно брать якорные даты.

Минусы:

- это per-symbol источник, а не bulk по всей бирже;
- нужен свой бесплатный ключ, `demo` работает только для знакомства и не подходит для всех тикеров;
- покрытие по foreign listings/ETF нужно проверить на нашем ключе.

Скрипт уже умеет использовать Twelve Data как fallback после ошибки FMP, если в окружении есть `TWELVE_DATA_API_KEY`.
По умолчанию скрипт выдерживает паузу `8` секунд между Twelve Data запросами.

### Alpha Vantage

Рабочий бесплатный резерв, но слабый для полной автоматизации.

- `TIME_SERIES_DAILY` возвращает daily OHLCV и покрывает 20+ лет.
- На free key доступен `compact` outputsize, то есть последние `100` daily points.
- Стандартный бесплатный лимит - `25` API requests/day.
- `full` outputsize для `TIME_SERIES_DAILY` доступен premium key.

Вывод: годится для ручной проверки или очень медленного дозаполнения, но не для регулярной полной загрузки всех секторных корзин.

### Stooq

CSV-источник потенциально полезен, но теперь требует Stooq API key через captcha:

```text
https://stooq.com/q/d/l/?s=aapl.us&d1=20260520&d2=20260520&i=d
```

В тесте вместо CSV Stooq вернул инструкцию `Get your apikey`. Это можно настроить только после ручного получения ключа; покрытие ETF/ADR/foreign listings нужно проверять отдельно.

### Yahoo Finance

Неофициальный источник без ключа. В тесте `query1.finance.yahoo.com/v8/finance/chart/...` вернул `Too Many Requests`.

Вывод: можно держать только как ручной/аварийный источник, но нельзя строить на нем основную автоматизацию.

### MOEX ISS

Для российских бумаг это лучший бесплатный источник: официальный, без ключа, уже используется скриптом.

## Статусы

- `ok` - котировка найдена.
- `missing` - котировка не найдена в пределах lookback окна до якорной даты.
- `provider_error` - провайдер ответил ошибкой, например ограничение подписки FMP.

Строки без `ok` нельзя использовать как фактические данные графика.
