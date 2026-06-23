# Система секторной оценки (sector pipeline)

Единое описание того, как устроена и как используется секторная система оценки этого
репозитория. Цель документа — чтобы и пользователь, и любой агент могли быстро понять
устройство и обновлять данные, не выискивая знания по отдельным скриптам.

Связанные источники истины (читать при необходимости):
- `AGENTS.md` → раздел «Известные проблемы и решения (sector pipeline)» — лаконичный список граблей.
- `02_MARKET_DASHBOARD.md` — методика, формулы мультипликаторов, веса по секторам.
- `data/market_quotes/norms_overview.md` — сравнительная таблица 5Y-норм и интерпретация.
- `data/market_quotes/norm_qa_report.md` — QA-проверка корректности норм.
- `data/market_quotes/pipeline_audit.md` — аудит, из которого выросли скользящее окно, архив и refresh.
- `data/market_quotes/archive/README.md` — описание append-only архива.

---

## 1. Обзор: что делает система

Система отвечает на один вопрос для каждого сектора: **насколько сектор сейчас дорог
или дёшев относительно собственной 5-летней нормы оценки.**

Главный показатель — `sector_score`:

- `sector_score = 1.0` — сектор оценён примерно как в среднем за последние 5 лет (его норма).
- `> 1.0` — сектор **дороже** своей нормы (например `1.5` ≈ на 50% дороже исторической нормы).
- `< 1.0` — сектор **дешевле** своей нормы.

Score считается как взвешенная сумма по нескольким мультипликаторам: для каждой метрики
берётся коэффициент `текущее_значение / норма` (для доходностных метрик — наоборот,
`норма / текущее`, см. ниже), коэффициенты умножаются на веса метрики в секторе и
суммируются. Это сравнение сектора **с самим собой во времени**, а не секторов между собой.

### 17 секторов

Норма построена ровно для 17 секторов (по одному файлу `fyn_<slug>_norm_summary.csv` на сектор).
Каноничный список (`slug` → отображаемое имя, корзина задана в `scripts/update_all.py`):

| slug | сектор | корзина (US-only) |
|---|---|---|
| `banks` | Banks | JPM, BAC, C, GS, MS |
| `energy` | Energy | XOM, CVX, COP, EOG, SLB |
| `telecom` | Telecom & Streaming | NFLX, DIS, CMCSA, VZ, T, TMUS, SPOT, CHTR |
| `delivery_logistics` | Delivery & Logistics | UPS, FDX, UBER, DASH, XPO |
| `insurance` | Insurance | UNH, PGR, CB, AIG, ALL, BRK-B, MRSH |
| `utilities` | Utilities | NEE, DUK, SO, AEP, D |
| `mining` | Mining | FCX, SCCO, NEM, GOLD, VALE |
| `drugs` | Drugs | LLY, JNJ, MRK, ABBV, PFE |
| `commodities` | Commodities | FCX, SCCO, ALB, NEM |
| `semis` | Semiconductors | NVDA, AMD, AVGO, TSM, ASML, MU, QCOM, TXN |
| `food` | Food & Staples | WMT, COST, KO, PEP, MDLZ, HSY, MNST |
| `technology` | Technology | AAPL, MSFT, GOOG, META, ADBE, CRM, NOW, ACN, IBM |
| `agriculture_chemicals` | Agriculture & Chemicals | LIN, APD, SHW, ECL, CTVA, NTR, FMC |
| `consumer_discretionary` | Consumer Discretionary | AMZN, HD, LOW, NKE, MCD, LULU |
| `medical_services` | Medical Services | ABT, ISRG, SYK, MDT, BSX, TMO, ALGN |
| `solar` | Solar | FSLR, NXT, ENPH, SEDG, RUN, CSIQ, SHLS |
| `reit` | REIT | WELL, PLD, EQIX, AMT, O, DLR, VICI |

### Что НЕ является сектором (и почему)

В библиотеке есть папки, которые **сознательно не выведены на секторную карту и не имеют
sector_score** (решение пользователя, зафиксировано в коде):

- **AI / AI Infrastructure** — не сектор, а исследовательская тема. Для чиповой оценки
  использовать `semis` (Semiconductors). В `compute_sector_scores.py` есть явный комментарий
  «AI Infrastructure intentionally NOT a sector/chart … Do not re-add here». Сюда же отнесён
  TSLA (классификация пользователя: AI/robotics/robotaxi-теза, не Consumer Discretionary).
- **China** — не сектор. У китайских ADR баг market_cap из-за ADR-ratio (например BABA P/E ~216,
  завышен в ~8 раз). Явный комментарий в коде «China intentionally NOT a sector/chart … Do not re-add».
- **RUSSIA, COMPANIES, ETF, JUNIOR, MY_PORTFOLIO, ARCHIVE, DECISIONS** и т.п. — это
  организационные папки библиотеки (отдельные идеи, портфель, архив), а не сектора с
  собственной 5Y-нормой.

Корзины секторов — **US-only**. Иностранные эмитенты (TSM/ASML/GOLD/VALE и пр.) либо
исключаются из ценовых метрик, либо помечаются `incomplete` — см. раздел 6.

---

## 2. Архитектура данных: три уровня

Система разделена на три уровня по частоте обновления. Это ключ к пониманию всего пайплайна.

| Уровень | Что это | Как часто пересобирается | Где лежит |
|---|---|---|---|
| **5Y НОРМА** | средняя историческая оценка сектора за 5 фискальных лет | раз в год / при сдвиге окна (скользящее) | `fyn_<slug>_norm_summary.csv` |
| **ТЕКУЩАЯ ТОЧКА** | сегодняшний снимок мультипликаторов (новая цена + актуальный локальный/SEC-фундаментал) | цены каждые 10 дней; полный SEC-аудит 4 раза в год | `fyn_<slug>_current_summary.csv` (+ датированные) |
| **SCORE** | `текущая / норма` по весам → одна точка на сектор | мгновенно, локально из двух уровней выше | `sector_scores*.csv`, `sector_scores_preview*.csv` |

### Уровень 1 — 5Y НОРМА (медленный, дорогой)

- Это не point-in-time прогулка по истории, а «лучшее значение того, чем FY20XX реально был»:
  берётся последний пересмотренный годовой факт (10-K) за каждый фискальный год.
- Окно — **скользящее**: последние 5 завершённых фискальных лет, доступных в SEC на дату.
  Функция `default_fy_years(as_of)` в `build_fy_norm.py` учитывает лаг подачи 10-K
  (`FY_FILING_LAG_CUTOFF_MONTH = 4`, апрель): до апреля «свежий» FY = текущий год − 2, с апреля = − 1.
  Для любой даты 2026 года окно = `[2021, 2022, 2023, 2024, 2025]` (защита `SAFE_2026_FY_YEARS`,
  чтобы случайно не пересобрать уже собранные нормы на другом окне).
- Норма каждой метрики = **двухуровневая медиана**: сначала медиана по годам внутри
  каждой компании, потом медиана по компаниям (см. раздел 6, почему не pooled).

### Уровень 2 — ТЕКУЩАЯ ТОЧКА (регулярный апдейт)

- Снимок «сегодня» = последняя доступная цена × последние SEC-факты с `filed <= as_of`.
- Обновляется каждые 10 дней (якоря 10/20/30 числа; если не торговый день — последний
  торговый день до якоря; для февраля/месяца без 30-го — последний календарный день).
- Режим по умолчанию — `--refresh-mode auto`: на каждом якоре обновляются цены и локально
  пересчитываются все price-derived метрики. Полный SEC-аудит корзины выполняется 20 марта,
  20 мая, 20 августа и 20 ноября. Между этими датами проверяется лёгкий SEC submissions
  metadata; XBRL обновляется только для компаний с новой релевантной формой
  (`10-Q/10-K/20-F/40-F/6-K` и amendments).
- Недатированный «сегодняшний» снимок (`fyn_<slug>_current_summary.csv`) перезаписывается
  на каждом прогоне; датированные снимки (`--as-of`) копят историю и не трутся.

### Уровень 3 — SCORE (мгновенный, офлайн)

- `compute_sector_scores.py` делит текущую точку на норму по весам — **сети не требует**,
  только локальные CSV. Поэтому score можно пересчитать когда угодно бесплатно.

### Где какие файлы лежат — `data/market_quotes/`

```
data/market_quotes/
├── fyn_<slug>_norm.csv / .json            # 5Y НОРМА, detail: строка на company×FY + BASKET_AVG
├── fyn_<slug>_norm_summary.csv            # 5Y НОРМА, summary: metric, five_year_average, n_companies, status
├── fyn_<slug>_current.csv / .json         # ТЕКУЩАЯ точка, detail (перезаписывается)
├── fyn_<slug>_current_summary.csv         # ТЕКУЩАЯ точка, summary: metric, value, n_companies, status
├── fyn_<slug>_current_<YYYYMMDD>*.csv     # датированные снимки (история якорей, не трутся)
├── sector_scores.csv / .json              # SCORE: компонентные строки (date×sector×metric)
├── sector_scores_preview.csv / .json      # декадный preview для дашборда (1 точка/дата/сектор)
├── sector_scores_preview_monthly.csv      # месячный preview (1-е число) для дашборда
├── sector_score_components_preview.csv    # разбивка компонент score
├── anchor_quotes.csv / .json              # исторические цены на якорные даты
├── anchor_fundamentals.csv / .json        # point-in-time мультипликаторы из SEC
├── fund_*.csv / .json                     # вспомогательные корзины фундаментала
├── .sec_cache/                            # дисковый кэш SEC companyconcept (TTL 7 дней)
├── .norm_window.json                      # маркер окна, на котором собраны нормы (для refresh_norm)
└── archive/                               # append-only архив (см. раздел 4)
    ├── sector_metrics_archive.csv         #   единая таблица date×sector×metric×value
    ├── norms/fyn_<slug>_norm_<YYYYMMDD>_summary.csv   # версии норм
    ├── raw_index.csv                       #   индекс сырых файлов
    └── README.md
```

Суффиксы имён задаются в `build_fy_norm.py`: `norm` для нормы, `current` для текущей точки,
`current_<YYYYMMDD>` когда передан `--as-of`.

---

## 3. Скрипты

Все скрипты в `scripts/`. Команды — из реальных `--help` / кода. По умолчанию пути
относительны корня репозитория, скрипты сами находят `data/market_quotes/`.

### `build_fy_norm.py` — построитель нормы и текущего снимка

Главный сборщик. Один скрипт строит и 5Y-норму, и текущую точку для сектора.

- **Норма** (по умолчанию, без `--current`): FY-история по скользящему окну
  `default_fy_years(--as-of или сегодня)`. Источники: SEC EDGAR XBRL (годовые факты),
  цены — Twelve Data `adjust=none` (as-reported close на дату FY-end, чтобы сплиты не ломали
  market_cap).
- **Текущий снимок** (`--current`): TTM-мультипликаторы на дату (`--as-of`, по умолчанию сегодня).
- **Скользящее окно**: `default_fy_years()` сама вычисляет годы; `--years` явно переопределяет.
- **Провайдер цен**: `--price-provider {twelve,fmp,nasdaq,auto}`; в режиме `auto` цепочка
  `twelve → fmp → nasdaq` (главный обход лимита Twelve Data, см. раздел 6).
- **SEC-кэш**: companyconcept-факты кэшируются на диск (`.sec_cache/`, TTL 7 дней); `--no-cache`
  форсирует сеть. Цены не кэшируются.
- **Режим обновления current**: `--refresh-mode auto` выбирает `full`, `incremental` или
  `prices-only`. `--refresh-mode full` принудительно перечитывает SEC для всей корзины;
  `--refresh-mode prices-only` вообще не обращается к SEC и требует локальный базовый снимок.
  В JSON сохраняются режим, базовый файл, даты фундаментала и последние accession numbers.
- **Офлайн-пересборка summary**: `--resummarize-from-detail` собирает `_norm_summary.csv` из
  уже лежащего `_norm.csv` без сети.
- **Исключения цен**: `--exclude-price TICKER` добавляет к базовым `{TSM, ASML, GOLD}`.

Примеры:
```bash
# Текущий снимок одного сектора (как делает update_all)
python3 scripts/build_fy_norm.py --sector Banks --tickers JPM BAC C GS MS --slug banks --current

# Пересборка 5Y-нормы на явном окне (как печатает refresh_norm при сдвиге окна)
python3 scripts/build_fy_norm.py --sector "Energy" --slug energy --years 2022 2023 2024 2025 2026

# Снимок на историческую дату через запасной провайдер
python3 scripts/build_fy_norm.py --sector Mining --slug mining --current --as-of 2026-05-10 --price-provider nasdaq

# Только новые цены, без SEC-запросов
python3 scripts/build_fy_norm.py --sector Banks --slug banks --current --as-of 2026-06-30 --price-provider nasdaq --refresh-mode prices-only

# Офлайн-пересборка summary из detail (без сети)
python3 scripts/build_fy_norm.py --sector Food --slug food --resummarize-from-detail
```

### `compute_sector_scores.py` — расчёт score

Берёт текущие точки и нормы, считает `sector_score` и пишет preview для дашборда.

- Для каждой `(sector, дата, метрика)` агрегирует корзину **медианой** (устойчиво к выбросам;
  `--aggregate mean` доступен, но не рекомендуется).
- `metric_coefficient = текущее / норма`. Для доходностных метрик (`YIELD_METRICS = {fcf_yield}`)
  формула **инвертируется**: `норма / текущее`, чтобы `> 1.0` всегда значило «дороже».
- Веса метрик — из таблицы `SECTOR_WEIGHTS` (= «Стартовые веса по секторам» в `02_MARKET_DASHBOARD.md`).
  Метрики без данных выбрасываются, оставшиеся веса **перенормируются** до суммы 1.0.
- `sector_score = Σ (metric_coefficient × вес)`.
- **Правило честности**: если есть реальный `fyn_<slug>_norm_summary.csv` со `status=ok` —
  норма реальная, строка `status=ok`. Иначе используется self-baseline (медиана метрики по
  истории) и строка помечается `status=provisional` с явным комментарием.
- Режимы preview: `--mode {decade,monthly}` (см. раздел 5).

Пример:
```bash
python3 scripts/compute_sector_scores.py \
  data/market_quotes/anchor_fundamentals.csv \
  --norms-dir data/market_quotes \
  --out-csv data/market_quotes/sector_scores.csv \
  --out-json data/market_quotes/sector_scores.json
```

### `update_all.py` — обновление одной командой (рабочая лошадка)

Декадный апдейт. По порядку: (1) для каждого сектора обновляет текущий снимок через
`build_fy_norm.py --current --refresh-mode auto`, (2) пересчитывает score через
`compute_sector_scores.py`. Nasdaq используется как ценовой провайдер по умолчанию.

- 5Y-норму **не трогает** (это раз-в-год job).
- Сектора идут **строго последовательно**; сектор с большой долей пропавших цен
  автоматически ретраится один раз. Для Twelve Data сохраняется увеличенная пауза,
  но штатный Nasdaq не требует ожидания по 8 секунд на запрос.

```bash
python3 scripts/update_all.py                 # все сектора, потом score
python3 scripts/update_all.py --only banks energy
python3 scripts/update_all.py --refresh-mode full       # принудительный SEC-аудит
python3 scripts/update_all.py --refresh-mode prices-only # SEC не вызывается
python3 scripts/update_all.py --skip-current  # только пересчитать score (офлайн, без сети)
python3 scripts/update_all.py --sector-pause 12
```
Прочие флаги: `--retry-wait`, `--min-ok-fraction`, `--refresh-mode`, `--price-provider`.

### `backfill_history.py` — массовый исторический сбор

Заполняет историю: для каждой пары `(сектор, дата)` запускает `build_fy_norm.py --current --as-of`
**строго последовательно**, по умолчанию с Nasdaq и `--refresh-mode auto`. Готовые снимки (с
нормальным числом компаний в P/E) пропускаются — безопасно возобновляется. После сбора
пересобирает канонический preview (17 секторов × 10 дат). По умолчанию даты — 10 месячных
якорей; `--rebuild-preview-only` собирает preview из уже лежащих снимков **без сети**.

```bash
python3 scripts/backfill_history.py
python3 scripts/backfill_history.py --only banks --dates 2026-05-10
python3 scripts/backfill_history.py --rebuild-preview-only   # офлайн
```
Прочие флаги: `--pause`, `--preview-csv`, `--no-cache`, `--refresh-mode`.

### `refresh_norm.py` — детектор ежемесячного пересчёта нормы

Дешёвый **офлайн** детектор + планировщик. **Не ходит в сеть и не запускает сборщики.**
Сравнивает скользящее окно для сегодня (или `--as-of`) с окном, на котором собраны нормы:

- если окно **не изменилось** → `norm window unchanged, skip` (код 0);
- если окно **сдвинулось** → печатает план: (1) `archive_history.py` (заархивировать старые
  нормы), (2) точные команды `build_fy_norm.py … --years <новое окно>` по каждому сектору,
  (3) команду записать новый маркер. Сами команды **не выполняет** — это делает координатор/update_all.

Окно «на котором собраны нормы» берётся из маркера `.norm_window.json`, иначе из метаданных
`fyn_<slug>_norm.json`. `--write-marker` записывает текущее окно как baseline (тоже без сети).

```bash
python3 scripts/refresh_norm.py                      # детект на сегодня
python3 scripts/refresh_norm.py --as-of 2027-06-07   # проверить будущую дату
python3 scripts/refresh_norm.py --write-marker       # записать baseline-окно
python3 scripts/refresh_norm.py --only semis energy
```

### `archive_history.py` — append-only архив

Только локально, **без сети**, безопасно при работающем backfill. Делает три вещи:

1. **Единая append-only таблица точек** `archive/sector_metrics_archive.csv`
   (`snapshot_date, sector, slug, metric, value, n_companies, status, source_file, archived_at`),
   собранная из датированных и недатированных current-снимков и `sector_scores*.csv`. Дедуп по
   `(snapshot_date, sector, metric, source_file)`; существующие строки не переписываются.
2. **Версионирование норм**: копирует каждый `fyn_<slug>_norm_summary.csv` в
   `archive/norms/fyn_<slug>_norm_<YYYYMMDD>_summary.csv` (идемпотентно).
3. **Лёгкий индекс сырья** `archive/raw_index.csv` (без копирования данных).

```bash
python3 scripts/archive_history.py            # обновить архив
python3 scripts/archive_history.py --dry-run  # показать, что добавилось бы
```
Прочие флаги: `--archive-dir`, `--source-dir`.

### `fetch_anchor_quotes.py` — котировки на якорные даты

Тянет закрытия корзины на якорные даты (декада 10/20/30 или 1-е число месяца). Источники:
Financial Modeling Prep (US/global), MOEX ISS (российские). Пишет `anchor_quotes.csv/.json`.
Ключи не пишутся в файлы.

```bash
python3 scripts/fetch_anchor_quotes.py --mode decade --count 10
python3 scripts/fetch_anchor_quotes.py --sector Banks --merge
```
Прочие флаги: `--as-of`, `--lookback-days`, `--twelve-data-min-interval`, `--yahoo-min-interval`.

### `fetch_anchor_fundamentals.py` — point-in-time фундаментал

Строит исторические мультипликаторы на якорные даты из бесплатного SEC EDGAR XBRL: цены берёт
из `anchor_quotes.csv`, факты — из SEC с `filed <= anchor_date` (без look-ahead), TTM из четырёх
последних непересекающихся кварталов. Считает P/E, P/S, P/B, EV/EBITDA, FCF yield + growth-сигналы
(revenue/earnings YoY как замена недоступному forward P/E). Пишет `anchor_fundamentals.csv/.json`.

```bash
python3 scripts/fetch_anchor_fundamentals.py
python3 scripts/fetch_anchor_fundamentals.py --sector Banks
```

---

## 4. Как обновлять данные

### Обычный декадный апдейт (раз в 10 дней)

```bash
python3 scripts/update_all.py
```
Обновит текущие снимки всех 17 секторов и пересчитает score. Только этот шаг и нужен между
сезонами отчётности. На обычном якоре он обновит цены, проверит список новых SEC-форм и
пересоберёт фундаментал только затронутых компаний. Полные SEC-аудиты сработают автоматически
20 марта, 20 мая, 20 августа и 20 ноября. Дашборд берёт результат из
`sector_scores_preview*.csv`.

Только пересчитать score офлайн (без сети, если снимки уже свежие):
```bash
python3 scripts/update_all.py --skip-current
```

### Пересчёт 5Y-нормы (раз в год / при сдвиге окна)

1. Проверить, сдвинулось ли окно (офлайн):
   ```bash
   python3 scripts/refresh_norm.py
   ```
2. Если печатает `norm window unchanged, skip` — ничего делать не нужно.
3. Если печатает `NORM WINDOW MOVED` — выполнить напечатанный план:
   - сперва заархивировать старые нормы: `python3 scripts/archive_history.py`;
   - затем пересобрать каждую норму напечатанными командами
     `python3 scripts/build_fy_norm.py --sector "<Name>" --slug <slug> --years <новое окно>`
     (через координатор/паузы, чтобы не упереться в лимиты SEC/цен);
   - после успеха записать новое окно: `python3 scripts/refresh_norm.py --as-of <дата> --write-marker`.

### Архивирование (периодически / перед пересчётом нормы)

```bash
python3 scripts/archive_history.py
```
Дописывает новые точки в `archive/sector_metrics_archive.csv` и версионирует нормы. Безопасно
запускать в любой момент, в т.ч. при работающем backfill.

### Массовый исторический сбор (разовый/донабор)

```bash
python3 scripts/backfill_history.py
```
Используется для заполнения пропущенной истории якорей. Долгий сетевой job — запускать
последовательно, не параллелить с другими сетевыми сборщиками.

---

## 5. Режимы графика на дашборде

`sector_valuation_dashboard.html`: layout 75/25 — основной столбец с графиком и боковая
панель (CSS `grid-template-columns: minmax(0, 3fr) minmax(260px, 1fr)`, т.е. ~3:1 = 75/25).
На графике отображаются последние 10 точек, по одной итоговой точке на сектор на дату.

Переключатель периодичности (`.mode-toggle`, две кнопки `data-sector-mode`):

| Кнопка | Режим | Якоря | preview-файл |
|---|---|---|---|
| **Декада (10/20/30)** | `decade` (по умолчанию) | 10, 20, 30 числа каждого месяца | `data/market_quotes/sector_scores_preview.csv` |
| **Месяц (1-е число)** | `monthly` | 1 точка на месяц на 1-е число | `data/market_quotes/sector_scores_preview_monthly.csv` |

- Дашборд грузит соответствующий CSV через `fetch(...)` при переключении кнопки (объект
  `sectorDataSources` в JS), парсит и перерисовывает график.
- **Декадный** preview — прямые точки на якорях 10/20/30 (`compute_sector_scores.py`, `--mode decade`).
- **Месячный** preview — производится из декадных точек: на каждое 1-е число берётся ближайшая
  декадная точка **на/до** этой даты (без look-ahead); если её нет, допускается точка чуть
  ПОЗЖE в пределах `MONTHLY_FORWARD_PROXY_DAYS` (помечается forward-proxy); иначе месяц
  помечается `missing` с пустым коэффициентом (числа не выдумываются — правило честности).
- Если CSV недоступен, дашборд оставляет уже загруженные данные и пишет предупреждение в консоль.

---

## 6. Известные ограничения и решения

Подробно — в `AGENTS.md` → «Известные проблемы и решения (sector pipeline)». Кратко:

- **HTTP 429 от Twelve Data при параллельном запуске.** Free план = 8 запросов/мин.
  Параллельный прогон роняет цены, компании выпадают, мультипликаторы завышаются (так
  Technology-норма раздувалась до P/E 53 вместо 33). РЕШЕНИЕ: сектора **строго
  последовательно** с паузой. Признак недобора: в `fyn_<slug>_current_summary.csv` у `pe`
  поле `n_companies` меньше размера корзины.
- **Запасной провайдер — Nasdaq.** При лимите Twelve Data использовать `--price-provider nasdaq`
  (или `auto`: цепочка `twelve → fmp → nasdaq`). Это главный обход 429; Nasdaq ~в 8× быстрее.
- **ADR-баг market_cap.** Для ADR (TSM, ASML, GOLD/Barrick, китайские BABA/PDD/JD) ADR-цена ×
  число ОБЫКНОВЕННЫХ акций → market_cap и P/E завышены в N раз. РЕШЕНИЕ: базовое исключение
  `BASE_PRICE_RATIO_EXCLUDE = {TSM, ASML, GOLD}`; новые битые добавлять `--exclude-price`.
  China и AI вообще убраны как сектора.
- **Иностранные IFRS-филеры (20-F) без us-gaap фактов.** BHP, RIO, SHEL, TTE и часть ADR не
  имеют квартальных us-gaap XBRL → статус `incomplete`. Это **ожидаемо, не баг**, данные не выдумываются.
- **REIT/Solar: P/E неинформативен.** У REIT амортизация занижает GAAP-прибыль (P/E структурно
  50–60 → смотреть P/B). У Solar убыточные годы (P/E 90+ → смотреть P/S). Это реальность, не баг.
- **Агрегация — двухуровневая медиана, не pooled.** Сначала медиана по годам внутри компании,
  потом по компаниям. Pooled даёт перекос в пользу компаний с длинной историей (Food P/E
  завышался 33.9 вместо 29.3).
- **Дорогой интернет → кэш + skip.** SEC-факты кэшируются на диск (`.sec_cache/`, TTL 7 дней),
  цены не кэшируются. Score пересчитывается **офлайн** из готовых norm/current-summary
  (`update_all.py --skip-current`). Backfill пропускает уже собранные снимки.

---

## 7. Источники данных

- **SEC EDGAR (фундаментал, бесплатно).** Официальный point-in-time источник годовых и
  квартальных XBRL-фактов (companyconcept). Нужен только описательный User-Agent, ключ не
  требуется. Используется и нормой, и текущими снимками; кэшируется в `.sec_cache/`.
- **Цены.** Twelve Data (основной, free ~8 req/min, `adjust=none`), FMP / Financial Modeling
  Prep (`/stable` endpoints, ключ из `.env`), Nasdaq historical API (`api.nasdaq.com/api/quote`,
  пауза ~1 сек, без ключа — главный запасной для обхода 429). Выбор/цепочка через
  `--price-provider`. MOEX ISS — для российских инструментов в `fetch_anchor_quotes.py`.
- **Сверка с внешним эталоном.** Damodaran NYU Stern (P/E по индустриям, бесплатно) и Seeking
  Alpha V-score (Fred Piard, та же логика median vs история). Совпадаем там, где корзины
  похожи; где расходимся — наша корзина чище (median лидеров vs pooled вся индустрия). Для
  быстрой сверки также: WorldPERatio, Finviz Groups, ChartMill, Fidelity/Yardeni/State Street.

Ключи API никогда не пишутся в репозиторий и в выходные файлы (читаются из `.env` / окружения).
