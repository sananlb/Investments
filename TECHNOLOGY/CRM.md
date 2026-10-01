# CRM

- Группа/сектор: `TECHNOLOGY`
- Источник добавления: ключевая компания сектора
- Статус: обновлённая аналитическая карточка (после Q2 FY2027, Investor Day и
  Dreamforce 2026). Прошла вторую независимую проверку: Codex `gpt-6.1-sol` с
  живым веб-поиском, 2026-10-01; исправления и дополнения внесены в тот же день.
  Предыдущая версия - первичная карточка от 2026-06-24.
- Дата анализа: 2026-10-01 (MSK)
- Обновлено: 2026-10-01
- Название: Salesforce
- Роль в секторе: enterprise SaaS, CRM, data/AI workflow

## Инвестиционный тезис

### Что изменилось с 2026-06-24

- Цена: `$151.78` (Nasdaq close 2026-06-18, якорь прошлой версии) ->
  `$229.57` (Nasdaq close 2026-09-30), то есть `+51%`. Локальный пик `$264.43`
  (close 2026-09-03), от пика `-13%`; с начала 2026 года `-13%` (close
  2025-12-31 `$264.91`). Минимум года `$146.32` intraday 2026-06-22. Источник:
  Nasdaq historical API, не секторный снимок.
- Q2 FY2027 (отчёт 2026-08-26): выручка `$11.35B`, `+11%` Y/Y и CC, на верхней
  границе гайденса; cRPO `+14%` CC (в Q1 `+13%` CC); гайденс FY2027 по выручке
  поднят до `$46.1-46.4B`. Акция `+22.6%` 2026-08-27 (`$205.62` -> `$252.05`).
- Рост выручки без Informatica в Q2 замедлился: `+6.4%` против `+8.7%` в Q1
  (nominal, наш расчёт). Это рост ex-Informatica: выручка других покупок
  (Regrello, Cimulate, Qualified, m3ter) в нём остаётся. Полная органика не
  раскрыта и не может быть выше этой цифры. Категория выручки Agentforce Apps
  ускорилась с `7%` до `8%` CC. Обещанное ускорение во втором полугодии пока
  видно только в гайденсе и NNAOV, а не в выручке.
- EPS в Q2 удвоился (`$4.29` GAAP, `$5.90` non-GAAP) в основном за счёт
  переоценки доли в Anthropic (`+$2.53` к non-GAAP EPS) и выкупа акций. GAAP
  operating income Q2 не вырос: `$2.331B` против `$2.332B` годом ранее.
- M&A: Contentful (соглашение - май 2026 по 10-Q, публичный анонс 2026-06-01;
  около `$1.5B`; закрыта 2026-09-01), Fin, бывший Intercom (соглашение -
  2026-06-15, около `$3.6B`; закрыта 2026-09-10), Listen Labs (анонс
  2026-09-29, цена не раскрыта, закрытие ожидается в Q4 FY2027). Ранее в 2026
  году закрыты Cimulate (2026-03-03) и m3ter (2026-07-01). В версии от
  2026-06-24 эти сделки не были отражены.
- Продукт и монетизация: с 2026-09-03 новые editions (Core `$195`, Advanced
  `$395`, Max `$550` за пользователя в месяц). 2026-09-17 анонсирована платная
  модель для внешних агентов через MCP/API (Headless Platform Interactions), но
  тариф пока не назначен. Партнёрства: Anthropic (Claudeforce, 2026-08-26),
  AWS (2026-09-15); на Dreamforce (2026-09-15...17) представлены AIforce и
  модель Koa.
- Investor Day (2026-09-16), ожидания менеджмента, а не факты: цель FY2030
  `$63B+` (установлена в мае 2026, включает Informatica и другие объявленные
  M&A); возврат акционерам `190%` FY2027 FCF; ожидаемое сокращение числа акций
  от ASR - не менее `14%` при средней цене `$182`. Финальный расчёт ASR -
  октябрь 2026.
- Оценка: P/S `2.9x` -> `4.3x`, FCF yield `11.8%` -> `8.0%`, FCF after SBC
  yield около `9%` -> около `6.1%`. Большая часть июньской дешевизны отыграна.
- Менеджмент: Srini Tallapragada 2026-08-06 оставил исполнительную должность
  President и Chief Engineering and Customer Success Officer; он остаётся
  Special Advisor CEO до 2027-08-06. Miguel Milano стал COO, Rohan Kumar
  (ex-Microsoft) - Chief Platform and Engineering Officer.

### Тезис

Исходный тезис (2026-06-24, сохранён как точка сравнения): Salesforce стал
дешевым не потому, что бизнес перестал генерировать cash flow, а потому что
рынок сомневается в качестве роста: органика замедляется, часть FY2027 роста
идет через Informatica, а крупный buyback профинансирован долгом.

Факт (на 2026-10-01): за три месяца рынок переоценил CRM вверх примерно на
`50%`. Причины: ротация в software в июле, сильный Q2, партнёрство с Anthropic.
Сомнения в качестве роста при этом сняты лишь частично:

- headline-рост `11%` примерно на `4-5 п.п.` обеспечен Informatica, с Q3 к
  этому добавятся Contentful и Fin;
- рост без Informatica в Q2 составил `6.4%`, полная органика не выше этого;
- скачок EPS имеет финансовую, а не операционную природу: переоценка доли в
  Anthropic и ASR.

Позитивные сигналы: ускоряется cRPO в CC и выручка Agentforce Apps, NNAOV
«сильнейший за 4 года» (по словам менеджмента). Общий attrition стабилен около
`8%`, но это не метрика удержания AI-продуктов.

Гипотеза: на уровне `$230` CRM уже не глубокий value-кейс, а ставка на то, что
во втором полугодии FY2027 и в FY2028 органический рост вернётся к `8%+`, а
AI/data ARR и платный headless-доступ начнут заметно влиять на выручку. Если
рост останется на `6-7%`, то около `17x` forward non-GAAP P/E без gains и около
`6%` FCF after SBC yield - это справедливая, а не дешёвая цена.

## Бизнес

Salesforce - крупнейшая CRM-платформа для enterprise customers. Бизнес включает
Sales Cloud, Service Cloud, Marketing/Commerce, Slack, Tableau, Data Cloud,
MuleSoft и Agentforce.

Сила бизнеса - installed base и данные клиентов. Salesforce уже встроен в
процессы продаж, сервиса, customer data и workflow. Слабое место - сложность
продукта и риск, что AI-агенты снизят ценность традиционных seat-based SaaS
моделей.

Дополнения на 2026-10-01 (факты; источники - Q2 FY2027 press release, 10-Q,
анонсы Salesforce):

- Salesforce - один операционный сегмент, сегментных маржей нет. С Q1 FY2027
  subscription & support выручка раскрывается двумя категориями:
  - Agentforce Apps (Sales, Service, Marketing, Commerce, Flex Credits, Slack):
    `$7.19B` в Q2, `+8%` CC;
  - Data 360, Headless Platform & Other (Data 360, Platform, Headless,
    Informatica, MuleSoft, Tableau): `$3.62B`, `+20%` CC, включая Informatica.
- Покупки 2025-2026 годов:
  - Regrello (октябрь 2025);
  - Informatica (ноябрь 2025, около `$8B`);
  - Cimulate (AI product discovery для commerce, закрыта 2026-03-03);
  - Qualified (апрель 2026);
  - m3ter (metering и rating для consumption billing, закрыта 2026-07-01);
  - Contentful (content layer для Headless 360);
  - Fin (AI-native customer service agent, `30,000+` клиентов);
  - Listen Labs (AI customer research, сделка не закрыта).
- Strategic investments `$11.3B` на 2026-07-31, из них Anthropic около `$5.1B`,
  примерно `45%` портфеля. Это в основном private holdings по балансовой
  оценке: крупный неоперационный актив и главный источник волатильности EPS,
  но не ликвидный резерв.
- Ценовые модели:
  - per-user, consumption (Flex Credits), outcome-based, AELA для крупных
    внедрений;
  - с 2026-09-03 упаковка Core / Advanced / Max (`$195` / `$395` / `$550` за
    пользователя в месяц). В пакеты включены Agentforce, Slack/Slackbot,
    analytics, security, Premier Success и Flex Credits (от `500k` до `2.75M`).
    Клиенты Agentforce 1 могут бесплатно перейти на Max, цены legacy editions
    не меняются;
  - по словам менеджмента (Q2), на premium editions перешли только `5%`
    knowledge workers в Sales/Service, премия к цене - `60-80%`.
- Headless/MCP-монетизация (анонс 2026-09-17): каждый успешный вызов
  зарегистрированного внешнего агента через MCP/API будет учитываться как
  Headless Platform Interaction (HPI) с оплатой Flex Credits. Тариф пока «TBA»,
  учёт не начат, Salesforce обещает уведомить за 30 дней до начала. Headless
  Toolkit запланирован на ноябрь 2026. Экономический эффект не подтверждён.
- Модели и дистрибуция:
  - Claude - основная reasoning-модель в Agentforce/Slack (Claudeforce);
  - Amazon Bedrock (2026-09-15) даёт доступ к Anthropic и NVIDIA, OpenAI - «coming
    soon»;
  - собственная CRM reasoning model Koa на NVIDIA Nemotron;
  - продукты Salesforce доступны в AWS Marketplace в 33 странах: клиенты могут
    засчитывать покупки в свои AWS commitments.
- Госсектор: VA (2026-07-24), контракт AELA с потолком `$1.6B` - один базовый
  год плюс две годовые опции продления. Всю сумму нельзя считать гарантированной
  выручкой или backlog.

## Секторная оценка

Внутри нашей `TECHNOLOGY`-корзины CRM входит в группу enterprise software, где
и сосредоточен основной de-rating сектора. GAAP P/E-сравнение с 5-летней
медианой нужно читать осторожно: исторические P/E Salesforce были искажены
низкой GAAP-прибылью. Более полезные метрики - P/S, EV/EBITDA, FCF yield и
owner FCF после SBC.

Обновление по секторному снимку `fyn_technology_current_20260920` (данные
скрипта, не пересчитывались и внешней проверкой не подтверждались; close CRM
`$237.92` от 2026-09-18):

| Метрика | CRM | Медиана корзины | Комментарий |
|---|---:|---:|---|
| P/E TTM | `20.3` | `20.3` | CRM сейчас и есть медиана корзины |
| EV/EBITDA | `22.2` | `22.2` | `n=5`, тоже на уровне медианы |
| P/S | `4.46` | `7.94` | по выручке CRM всё ещё дешевле корзины |
| FCF yield | `7.7%` | `3.3%` | по cash flow CRM заметно дешевле корзины |

Вывод: по P/E и EV/EBITDA CRM больше не выделяется дешевизной внутри корзины.
Дисконт сохраняется только по P/S и FCF yield, причём FCF yield частично
завышен SBC (см. owner FCF ниже).

## Финансы

TTM-факты (SEC XBRL; секторные снимки `fyn_technology_current_20260620` и
`fyn_technology_current_20260920`, SBC и marketable securities - из 8-K):

| Метрика | на 2026-06-24 (TTM до 2026-04-30) | на 2026-10-01 (TTM до 2026-07-31) |
|---|---:|---:|
| TTM revenue | `$42.8B` | `$43.9B` |
| TTM net income | `$8.0B` | `$9.7B` (включая около `$4.2B` pre-tax gains on strategic investments) |
| TTM GAAP operating income | `$8.7B` | `$8.7B` |
| TTM OCF | `$15.2B` | `$15.75B` |
| TTM FCF | `$14.7B` | `$15.15B` |
| TTM SBC | около `$3.4B` (run-rate, оценка) | `$3.67B` (FY26 `$3.51B` плюс разница H1) |
| Net margin | `18.7%` | `22.0%` (искажена gains) |
| Revenue growth YoY | `11.0%` | `11.2%` |
| Earnings growth YoY | `29.3%` | `45.0%` (за счёт gains, не операций) |
| Cash / debt | `$8.9B / $39.3B` | `$8.3B` cash + `$3.1B` marketable securities / `$39.3B` |

Q1 FY2027 (отчёт от 2026-05-27, оставлено для сравнения): выручка `$11.1B`,
рост `13%` YoY / `12%` constant currency, включая `$444M` вклада Informatica.
Subscription & support revenue `$10.6B`, рост `14%` YoY / `12%` CC, включая
`$428M` Informatica. GAAP operating margin `21.1%`, non-GAAP operating margin
`34.8%`; operating cash flow `$6.7B`, FCF `$6.6B`.

### Q2 FY2027 (квартал до 2026-07-31, отчёт 2026-08-26)

Факты (press release / 8-K Exhibit 99.1; ключевые цифры независимо
подтверждены Codex):

- Revenue `$11,345M`, `+11%` Y/Y и CC, включая `$456M` Informatica. Гайденс был
  `$11.27-11.35B`.
- Subscription & support `$10,820M`, `+12%` Y/Y / `+11%` CC, включая `$440M`
  Informatica.
- cRPO `$33.5B`, `+14%` Y/Y и CC (Q1: `+14%` Y/Y / `+13%` CC); RPO `$66.3B`,
  `+11%`. Вклад Informatica в cRPO не раскрыт. База Q2 FY2026 была без
  Informatica, поэтому рост cRPO без неё заметно ниже `14%`; точно оценить
  нельзя.
- GAAP operating margin `20.5%` (год назад `22.8%`); GAAP operating income
  `$2,331M` против `$2,332M`. Non-GAAP operating margin `34.1%` (год назад
  `34.3%`); non-GAAP operating income `+10%`.
- GAAP EPS `$4.29` (`+119%`), non-GAAP EPS `$5.90` (`+103%`). Gains on strategic
  investments `$2,613M` (из них `$2.7B` unrealized gain по Anthropic) добавили
  `$2.43` к GAAP EPS и `$2.53` к non-GAAP EPS. Salesforce не исключает эти gains
  из non-GAAP.
- Расчёт: non-GAAP EPS без gains около `$3.37`. Это `+16%` к `$2.91` годом
  ранее и на `$0.10-0.12` выше гайденса `$3.25-3.27`. Заголовки вида «beat на
  80%» сравнивают `$5.90` с консенсусом `$3.27` и вводят в заблуждение.
- OCF `$1,269M` (`+71%`), FCF `$1,098M` (`+81%`). Q2 сезонно слабый: за H1 OCF
  `$7.97B`, FCF `$7.65B`.
- SBC `$906M` (cash flow statement; год назад `$793M`). Interest expense `$473M`
  против `$67M`.
- Diluted shares `821M` против `962M` годом ранее (`-15%`).

Рост без Informatica (наш расчёт по раскрытым цифрам). Informatica закрыта в
ноябре 2025, в базе прошлого года её нет. Это не полная органика: выручка
Regrello, Cimulate, Qualified и m3ter остаётся внутри.

| | Q1 FY2027 | Q2 FY2027 |
|---|---:|---:|
| Revenue ex-Informatica, nominal | `+8.7%` | `+6.4%` |
| Revenue ex-Informatica, CC (грубая оценка) | около `7.5%` | около `6.5%` |
| S&S ex-Informatica, nominal | `+9.3%` | `+7.1%` |
| Agentforce Apps, CC (раскрыто) | `7%` | `8%` |
| Data 360, Headless & Other, CC (раскрыто, вкл. Informatica) | `23%` | `20%` |
| cRPO, CC (раскрыто, вкл. Informatica) | `13%` | `14%` |

Комментарий:

- CC-оценки опираются на округлённые CC-ставки компании (точность около
  `±0.5 п.п.`). Направление - замедление с Q1 на Q2 - видно и в nominal-цифрах.
- В Data 360/Headless входят term licenses MuleSoft и Tableau с признанием
  выручки upfront, поэтому квартальные цифры волатильны. Менеджмент сам назвал
  license revenue volatility фактором, частично компенсирующим силу AI.

### Гайденс FY2027: что изменилось

| Метрика FY2027 | Гайденс 2026-05-27 (Q1) | Гайденс 2026-08-26 (Q2) |
|---|---:|---:|
| Revenue | `$45.9-46.2B` | `$46.1-46.4B` |
| Рост Y/Y / CC | `11%` / `10-11%` CC | `11-12%` / около `11%` CC |
| Вклад Informatica | около `3 п.п.` | чуть выше `3 п.п.` |
| Вклад Contentful + Fin | - | около `$200M` |
| S&S growth | чуть ниже `12%` / около `11%` CC | чуть выше `12%` / чуть ниже `12%` CC |
| GAAP operating margin | `20.6%` | `20.1%` |
| Non-GAAP operating margin | `34.3%` | `34.3%` |
| GAAP EPS | `$7.93-7.99` | `$10.21-10.25` |
| Non-GAAP EPS | `$14.06-14.12` | `$16.67-16.71` |
| Non-GAAP EPS без gains (расчёт) | около `$13.5-13.6` | около `$13.66-13.70` |
| OCF / FCF growth | около `4-5%` / `4-5%` | около `4-5%` / `4-5%` |
| SBC | не проверено | `9.0%` выручки, `$4.96`/акцию, около `$4.2B` |

- Как считается EPS без gains: H1 gains `$3.171B` с non-GAAP налогом `20.5%`
  делятся на годовой знаменатель `838M` diluted shares, получается около
  `$3.01`/акцию. Это аналитическая корректировка, не официальный гайденс.
- Подъём выручки на `$200M` (`$300M` в CC) состоит из `$100M` органики, `$200M`
  от Contentful и Fin и `-$100M` FX. Значит, органическое улучшение
  гайденса составляет только около `0.2%` выручки.
- Рост EPS-гайденса почти целиком объясняется gains on strategic investments.
  Операционный рост EPS-гайденса - около `+$0.1`.
- GAAP margin снижен из-за acquisition-related costs (`0.8%` выручки в
  reconciliation).
- Исходный гайденс FY2027 от февраля 2026 (8-K Q4 FY2026): revenue
  `$45.8-46.2B`, non-GAAP EPS `$13.11-13.19`, OCF growth около `9-10%`. В мае
  OCF/FCF growth снижен до `4-5%`, в основном из-за процентов по долгу ASR.
- Q3 FY2027: revenue `$11.42-11.50B` (`+11-12%` Y/Y и CC), Informatica чуть выше
  `4 п.п.`; cRPO около `+14%` (без Contentful и Fin); GAAP EPS `$1.81-1.83`,
  non-GAAP `$3.42-3.44`. Консенсус Yahoo Finance на 2026-10-01: EPS `$3.45`,
  revenue `$11.46B`.
- Гипотеза (грубая оценка): из гайденса следует рост без Informatica, Contentful
  и Fin около `6.5-7%` в Q3 и около `7%` во втором полугодии. Точно восстановить
  эти цифры нельзя: гайденс округлён, выручка купленных компаний не раскрыта.

### Баланс, долг и возврат капитала (на 2026-07-31)

Факты (10-Q Q2 FY2027, press release):

- Долг: principal `$39.5B` (carrying `$39.288B`, весь noncurrent) против
  `$14.4B` на 2026-01-31.
  - Выпуски марта 2026: senior notes с купонами от `4.50%` до `6.70%`
    (погашения 2028-2066).
  - `$6.0B` term loan с плавающей ставкой (`4.24%` - средняя за период,
    погашение 2031) рефинансировал bridge-кредиты на покупку Informatica.
- Cash `$8.31B` + marketable securities `$3.09B` = `$11.4B`. Net debt около
  `$27.9B` на 2026-07-31 (около `$4.9B` на 2026-01-31). Net debt / TTM EBITDA
  (GAAP operating income + D&A из cash flow, `$12.7B`) - около `2.2x` (расчёт;
  оговорку об EBITDA см. в «Оценке»).
- Interest expense: Q2 `$473M`, H1 `$790M`. Около `$1.9B` в год - это наша
  экстраполяция Q2, не прогноз компании. GAAP EBIT / interest в Q2 - около
  `4.9x`.
- ASR на `$25B`:
  - соглашения заключены в марте 2026, вся сумма уплачена тогда же;
  - первая поставка - около `103M` акций по `$198.34`, около `80%` ожидаемого
    объёма;
  - финальный расчёт в октябре 2026 (Q3 FY2027) - это допоставка акций, а не
    новый платёж.
- Open market buyback: Q1 - `11M` акций по `$192` (`$2.145B`), Q2 - `0`. Остаток
  авторизации - `$22.9B` из `$50B` (февраль 2026).
- Акций в обращении около `823M` на 2026-08-20.
- Investor Day (ожидания менеджмента): средняя цена ASR `$182`, сокращение числа
  акций не менее `14%`. Гипотеза (расчёт): `$25B / $182` = около `137M` акций,
  то есть в октябре поставят ещё около `30-35M` акций, и в обращении останется
  около `790M` (без учёта dilution). Итог ASR на 2026-10-01 не подтверждён.
- Дивиденд `$0.44` в квартал (`$364M` выплачено в Q2), yield около `0.8%`.
- Strategic investments `$11.3B`, из них Anthropic около `$5.1B`. На 2026-01-31
  доля Anthropic была `22%` портфеля, на 2026-07-31 - `45%`.
- Гипотеза (сценарий, не подтверждено): на Contentful и Fin в Q3 уйдёт около
  `$5.1B` cash, плюс Listen Labs. Если сделки оплачены из кэша, net debt
  вырастет примерно до `$33B` до поступления сезонно сильного Q4 FCF.

Owner earnings check (расчёт; знаменатель - market cap, потому что FCF уже
после процентов):

- TTM: FCF `$15.15B` - SBC `$3.67B` = owner FCF около `$11.5B`. На 2026-06-24
  было около `$11.2B`. Yield `6.1%` на market cap `$188.9B` (цена `$229.57`,
  2026-09-30); в июне было около `9%`.
- FY2027: FCF около `$15.0B` (гайденс `+4-5%` к `$14.4B` FY2026; на Investor Day
  названо около `$15B`) минус SBC около `$4.2B` (гайденс). Owner FCF около
  `$10.8-11.0B`, то есть на уровне FY2026 (`$14.4B - $3.5B` = около `$10.9B`).
  SBC растёт быстрее FCF: `8.5%` выручки в FY2026 против `9.0%` в FY2027.
- На акцию owner FCF вырастет примерно с `$11.4` (`956M` diluted, FY2026) до
  около `$13.0` (`838M`, FY2027): около `+14%`. Весь этот рост даёт
  debt-funded buyback, а не бизнес.

## Оценка

Секторный anchor (данные скрипта, не пересчитывались):

| Метрика | Снимок `..._20260620` | Снимок `..._20260920` |
|---|---:|---:|
| Close price | `$151.78` (2026-06-18) | `$237.92` (2026-09-18) |
| Market cap | `$124.3B` | `$195.8B` |
| Enterprise value | `$154.7B` | `$226.8B` |
| P/E TTM | `15.5` | `20.3` |
| EV/EBITDA | `15.3` | `22.2` |
| P/S | `2.9` | `4.46` |
| FCF yield | `11.8%` | `7.7%` |

Наш расчёт на Nasdaq close 2026-09-30 `$229.57` (не из секторного снимка;
`823M` акций; TTM до 2026-07-31). Сравнение с 5-летней медианой - по
`fyn_technology_norm.csv`:

| Метрика | 2026-06-20 | 2026-09-30 | 5Y-медиана | Комментарий |
|---|---:|---:|---:|---|
| P/E TTM | `15.5` | `19.6` | `67.5` | см. методику ниже |
| EV/EBITDA | `15.3` | `21.5` | `87.1` | методика снимка; `17.4x` - только справочно |
| P/S | `2.9` | `4.3` | `8.3` | EV/S `5.0x` |
| FCF yield | `11.8%` | `8.0%` | `3.4%` | |
| FCF after SBC yield | около `9%` | `6.1%` | - | на market cap |

- P/E, методика. `19.6x` - это market cap / TTM net income, так же считают
  снимки, поэтому цифра сопоставима с `15.5` и `20.3`.
  - Price / TTM diluted EPS даёт около `21x`: сумма diluted EPS за 4 квартала
    `$10.96` -> `20.9x`. Codex и StockAnalysis дают `21.3x` при EPS `$10.79`.
  - Разница возникает из-за того, что в капитализации - текущее число акций, а
    в EPS - средневзвешенное до выкупа.
  - Без TTM gains on strategic investments (около `$4.2B` pre-tax) P/E около
    `29x`.
- EV/EBITDA, оговорка о сопоставимости.
  - `21.5x` посчитан по методике снимка (D&A tag TTM `$1.49B`) и сопоставим с
    `15.3x` и 5Y-медианой только внутри этой методики.
  - `17.4x` (D&A из cash flow, `$3.92B`) нельзя сравнивать ни с историей, ни с
    конкурентами: эта строка включает impairment и амортизацию ROU-активов.
  - Ни одна из цифр не доказывает дисконт сама по себе. Для выводов
    опираемся на P/S и FCF/owner FCF yield.
- Market cap около `$188.9B`. EV около `$219.9B` (долг минус cash, как в
  снимке) или `$216.8B` с учётом marketable securities. Strategic investments
  `$11.3B` в EV не вычитались.
- Forward P/E (расчёт): non-GAAP FY2027 по середине гайденса `$16.69` -
  `13.8x`; без gains (около `$13.68`) - `16.8x`. GAAP FY2027 `$10.23` -
  `22.4x`, без gains около `31x`.
- Консенсус (Yahoo Finance и StockAnalysis/S&P Global на 2026-10-01):
  - FY2027: EPS `$16.76`, revenue `$46.29B`;
  - FY2028 (год до января 2028): EPS `$16.01` (`53` аналитика, диапазон
    `$14.66-18.12`), то есть `14.3x`; revenue `$50.79B` (`+9.7%`);
  - консенсус ждёт, что EPS в FY2028 снизится на `4.5%`: gains Anthropic не
    повторятся. Сопоставимый ряд пересмотров EPS без gains не найден.
- Forward FCF yield FY2027 (около `$15.0B`) - около `7.9-8.0%`; owner FCF after
  SBC - около `5.7-5.8%`.

Консенсус и позиционирование (источники расходятся по выборке и датам):

- StockAnalysis (2026-09-29/10-01): Buy, `55` аналитиков, средний target
  `$281.08`, диапазон `$160-475`. Широта оптимизма снижается: с апреля по
  сентябрь число Strong Buy + Buy сократилось с `44` до `38`, Hold выросло с `11`
  до `15` (по проверке Codex).
- MarketBeat (2026-09-30): Moderate Buy, средний target `$275.14`; 3 Strong Buy
  / 30 Buy / 14 Hold / 3 Sell.
- TipRanks (2026-09-17, окно 3 месяца): Moderate Buy, 28 Buy / 10 Hold / 1 Sell,
  средний target `$272.54`.
- Отдельные пересмотры брокеров (по вторичным источникам; Codex их не
  подтвердил):
  - Guggenheim - повышение до Buy (2026-07-01, target `$228`, позже `$300`);
  - Stifel и Canaccord - `$300` (2026-09-17);
  - Jefferies - Buy `$300` (2026-09-21);
  - Oppenheimer - Buy `$275` (2026-09-29);
  - UBS - Hold `$260` (2026-09-18);
  - DA Davidson - `$225` (2026-09-17);
  - Morgan Stanley - Equal-weight `$235` (конец сентября).
- Short interest на расчётную дату 2026-09-15: около `32.35M` акций, `+10.7%`
  к 2026-08-31. Это около `3.9%` акций в обращении (StockAnalysis) или `4.07%`
  float (ChartMill). Данные середины сентября, не live.
- Инсайдеры (Form 4), сигналы разнонаправленные:
  - директор Craig Conway 2026-09-04 продал `4,500` акций по около `$260.5-260.7`
    (около `$1.17M`, отметки 10b5-1 нет);
  - директор David Kirk 2026-09-18 купил `4,176` акций по `$239.33` (около
    `$1.0M`);
  - новые продажи Benioff в сентябре не подтверждены.

Вывод по оценке (обновлено): CRM по-прежнему дешевле своей 5-летней истории и
software-корзины по P/S и FCF yield. Но после переоценки на `+51%` это уже
умеренная, а не экстремальная дешевизна: около `14-17x` forward non-GAAP P/E и
около `6%` owner FCF yield. «Качество дешевой цены» с июня не улучшилось: рост
EPS опирается на Anthropic mark-up и debt-funded ASR, а рост без M&A ещё не
ускорился.

## Катализаторы

- Organic acceleration во второй половине FY2027, как обещает менеджмент.
  Статус на 2026-10-01: не подтверждено в выручке. NNAOV «сильнейший за 4
  года», Agentforce Apps ускорился до `8%` CC. Проверка - отчёт Q3 FY2027
  (обычно начало декабря; дата на 2026-10-01 не объявлена).
- Рост Agentforce/Data 360 ARR.
  - Q1 FY2027: combined AI and data ARR около `$3.4B`, включая `$1.2B`
    Agentforce ARR и `$1.1B` Informatica Cloud ARR.
  - Q2 FY2027: Agentforce + Data 360 ARR почти `$3.9B` (`+210%` Y/Y), Agentforce
    ARR больше `$1.5B` (`+240%`) - подтверждено официально. С Q2 в Agentforce ARR
    включены AI offerings, Slackbot и Headless 360, поэтому `$1.2B` -> `$1.5B` не
    сопоставимы like-for-like.
  - Data 360 ARR `$2.4B` (`+200%+`) включает Informatica Cloud - по пересказу
    презентации (Investing.com), первичного раскрытия нет.
- Сокращение share count после ASR на `$25B`: первая поставка `103M` акций,
  финальный расчёт в октябре 2026 (оценка: ещё около `30-35M` акций).
- Подтверждение, что Agentforce увеличивает attach rate и retention, а не
  просто заменяет seat-based продукты. Данные Q2:
  - `2,000` платящих клиентов переведены в production (`+70%` Q/Q); это не
    обязательно новые клиенты Salesforce;
  - `50%` Agentforce bookings - пополнение кредитов (refill);
  - bookings premium SKU (Agentforce One Edition и Agentforce for Apps)
    удвоились Q/Q;
  - AWUs `3.2B` в Q2 (`+97%` Q/Q).
- Платный headless-доступ (HPI): Headless Toolkit в ноябре 2026, затем учёт
  после 30-дневного уведомления. Это главный потенциальный ответ на риск ухода
  интерфейса в Claude и другие системы; тариф и маржа пока неизвестны.
- Новая упаковка editions (с 2026-09-03) и AWS Marketplace (с 2026-09-15) могут
  упростить продажи и закупку.
- Сохранение GAAP operating margin около `20%+`. Q2 - `20.5%`, гайденс FY2027
  снижен с `20.6%` до `20.1%` из-за acquisition-related costs.
- Новые продукты Dreamforce 2026:
  - AIforce: Claudeforce (beta), Slackforce (GA в октябре), Agentforce Coworker
    (GA);
  - Agent Optimizer (GA в октябре);
  - Koa (pilot, GA Winter 2026);
  - long-horizon agents (GA в ноябре 2026);
  - набор готовых агентов, включая Fin.
- Интеграция Contentful и Fin: около `$200M` выручки в FY2027 и усиление
  Agentforce Service. Госзаказ: VA, потолок `$1.6B` (см. «Бизнес»).
- Дальнейшая переоценка доли в Anthropic: поднимает EPS, но это неоперационный
  и обратимый фактор.

## Риски

- Рост без M&A может оказаться слабее headline-роста. Статус: подтверждается.
  Рост без Informatica в Q2 - `6.4%` при headline `11%`. Полная органика ещё
  ниже или равна этой цифре (внутри Cimulate, Qualified, m3ter), с Q3 добавятся
  Contentful и Fin. Ряд аналитиков опасается, что рост без M&A останется около
  `6%`, пока агенты замещают seats.
- `$25B` debt-funded ASR повышает финансовый риск и делает EPS менее чистым
  индикатором.
  - Net debt около `$27.9B` на июль, до кэш-оплаты Contentful и Fin около
    `$5.1B`; проценты около `$1.9B` в год (run-rate).
  - Q2 подтвердил риск: EPS удвоился при flat GAAP operating income.
  - Это красный флаг из `Принципы инвестиций.md`: «EPS растет за счет buyback,
    а не за счет бизнеса».
- Качество non-GAAP EPS: Salesforce включает gains on strategic investments в
  non-GAAP. Anthropic - `45%` портфеля strategic investments; переоценка вниз
  ударит по EPS так же резко.
- AI-disruption и конкуренция:
  - agentic workflows могут снизить ценность классической CRM-seat модели;
  - Microsoft (2026-09-25) представила Copilot Home/Code/Autopilot с опорой на
    данные Dynamics 365 и Power Platform, модель оплаты - USL + usage-based;
  - ServiceNow (2026-04-09, по проверке Codex) включила AI во все продукты и
    пакеты;
  - Sierra (2026-09-28) запустила Ghostwriter - агента-«коллегу» прямо в
    Slack/Teams, то есть Slack становится каналом и для сторонних агентов;
  - Fin сам был AI-native конкурентом, и его покупка - отчасти защитный шаг;
  - данных о фактической потере доли CRM не найдено.
- Зависимость от моделей: Claudeforce привязывает Salesforce к Anthropic.
  Противовесы - Bedrock (Anthropic, NVIDIA, позже OpenAI) и собственная Koa;
  преимущества по стоимости и качеству не доказаны. Гипотеза: интерфейс может
  сместиться в Claude/Slack, а Salesforce станет «harness» с меньшей pricing
  power.
- Переупаковка искажает AI-метрики (гипотеза): AI включён в editions, кредиты
  входят в пакеты, клиенты Agentforce 1 переходят на Max бесплатно. Adoption
  может расти без сопоставимого прироста выручки.
- Монетизация headless может вызвать сопротивление клиентов. Тариф, эластичность
  и валовая маржа после inference costs неизвестны (гипотеза).
- Наблюдаемость тезиса: по пересказу презентации Q2 (Investing.com), компания
  переходит от квартального раскрытия Agentforce/Data 360 ARR к раскрытию по
  достижении milestones. Первичного подтверждения нет.
- Безопасность: Zenity 2026-09-24 опубликовала уязвимость Agentforce
  «SalesBleed» - утечку CRM-данных через indirect prompt injection.
  - Хронология: сообщено 2026-06-01, исправлено Salesforce 2026-08-18,
    подтверждено исследователями 2026-08-19.
  - Свидетельств реальной эксплуатации нет.
  - Риск - расходы на защиту и задержки внедрения у осторожных клиентов.
- SBC остается значимым экономическим расходом: headline FCF нужно регулярно
  корректировать. Доля SBC растёт: `8.5%` выручки в FY2026, `9.0%` по гайденсу
  FY2027 (около `$4.2B`).
- Сложность портфеля и M&A-интеграция: Slack, Tableau, MuleSoft, Data Cloud,
  Informatica, Agentforce, а в 2026 году ещё Cimulate, Qualified, m3ter,
  Contentful, Fin и Listen Labs. Серийные покупки размывают видимость органики.
- Текучка менеджмента:
  - Tallapragada оставил исполнительную роль 2026-08-06 (Special Advisor до
    2027-08-06, переходный период смягчает риск);
  - ранее в 2026 году ушли Adam Evans (руководитель Salesforce AI/Agentforce),
    CEO Slack и CEO Tableau;
  - вопрос преемственности после Benioff остаётся открытым.
- Операционный риск: глобальный сбой core-сервисов 2026-09-16 в день открытия
  Dreamforce (устранён в тот же день).
- Оценочный риск: после `+51%` запас прочности меньше. Акция волатильна: `-13%`
  от сентябрьского пика за четыре недели, `-8%` за неделю Dreamforce. Short
  interest растёт.

## Решение

Предварительная оценка (2026-10-01): `бизнес не хуже, чем в июне, но цена
выросла быстрее качества роста; июньская дешевизна в основном отыграна`.
Прежняя оценка (2026-06-24): `интересно, но требует подтверждения органики`.
Вторая проверка (Codex, 2026-10-01) пришла к тому же выводу: статус
«наблюдать» обоснован.

Ответы на 4 пункта проверки (на данных 2026-10-01, с учётом проверки Codex):

| Вопрос | Статус | Ответ |
|---|---|---|
| 1. Revenue growth ex-Informatica | История отвечена; ускорение не подтверждено | Q2 `+6.4%` против `+8.7%` в Q1 (nominal). Полная органика без всех M&A и точный CC-рост не раскрыты. Опережающие индикаторы лучше: cRPO CC `13%` -> `14%`, Agentforce Apps `7%` -> `8%` CC, NNAOV - максимум за 4 года. Ускорение во втором полугодии - гипотеза (грубая оценка около `7%`). |
| 2. Net debt и проценты после ASR | Частично отвечен | На 2026-07-31: net debt около `$27.9B`, около `2.2x` TTM EBITDA; interest `$473M` за Q2 (около `$1.9B` в год как run-rate), EBIT coverage около `4.9x`; погашения 2028-2066, term loan плавающий. Баланс после сентябрьских M&A (около `$5B+` cash) и итог ASR не подтверждены; `$33B` - сценарий. Strategic investments `$11.3B` - неликвидный буфер. |
| 3. FCF after SBC | TTM отвечен; FY2027 - расчёт по гайденсу | TTM owner FCF около `$11.5B` (июнь: около `$11.2B`), yield `6.1%` на market cap. FY2027 около `$10.8-11.0B`, на уровне FY2026: SBC растёт до `9%` выручки. На акцию около `+14%`, но только за счёт выкупа в долг. |
| 4. Adoption/retention Agentforce/Data 360 | Adoption отвечен частично; retention не отвечен | Есть production-внедрения (`2,000` клиентов переведены в production, `+70%` Q/Q), refill `50%` bookings, AWUs `+97%` Q/Q. Нет like-for-like ARR без M&A и смены определений, AI-cohort NRR и churn. Общий attrition около `8%` (без Informatica, новых покупок и Slack self-service) - это потеря контрактной стоимости, а не удержание AI. Agentforce ARR около `$1.5B` - около `3%` годовой выручки. |

### Bull case / Bear case

Bull case (гипотеза):

- Экономическая ценность сохраняется при смене интерфейса. Данные, права
  доступа и workflows остаются в Salesforce, а HPI позволяет брать плату за
  обращения любых внешних агентов (Claude, Bedrock, MCP).
- Есть признаки реального потребления: переход в production и refill кредитов
  важнее числа пилотов. Менеджмент сообщает о росте seats в Sales, Service и
  Slack и о сильнейшем за 4 года NNAOV.
- Упаковка и дистрибуция ускоряют продажи: единые editions, AWS Marketplace, а
  m3ter даёт технологию consumption billing.
- Денежный поток около `$15B` в год финансирует переход, а сокращение акций на
  `14%+` усиливает результат на акцию. Если рост без M&A вернётся к `8%+`,
  оценка `14-17x` forward P/E станет дешёвой.

Bear case (гипотеза):

- Операционное ускорение не доказано: рост без Informatica замедлился, GAAP
  operating income квартала не изменился. Headline growth и EPS сильнее базового
  бизнеса.
- AI ARR трудно отделить от покупок и переупаковки: расширенное определение,
  bundled credits, бесплатные upgrades, переход на milestone-раскрытие.
- Конкуренты (Microsoft, ServiceNow, Sierra) встраивают AI в более широкие
  предложения и командные интерфейсы, снижая отдельную AI-наценку.
- Возврат капитала в долг при стагнирующем owner FCF: проценты, растущая SBC и
  кэш-покупки ограничивают рост экономического денежного потока.
- Headless-монетизация может встретить сопротивление клиентов; платные
  обращения пока возможность, а не доказанная компенсация потери seats.

Наш вывод: на 2026-10-01 доказательная база сильнее у bear case по выручке и
качеству EPS, у bull case - по опережающим индикаторам (cRPO, NNAOV,
production/refill) и по стратегическому ответу (HPI). Решающий тест -
рост без M&A в Q3-Q4 FY2027 и первые данные по платному headless-доступу.

### Что мониторить дальше

Календарь ближайших точек проверки:

- Октябрь 2026: финальный расчёт ASR (число допоставленных акций); Slackforce
  и Agent Optimizer GA.
- Ноябрь 2026: Headless Toolkit и long-horizon agents GA; уведомление о
  тарифе HPI, после него 30 дней до начала платного учёта.
- Начало декабря 2026 (дата не объявлена): Q3 FY2027. Рост без Informatica,
  Contentful и Fin `>= 7%`; cRPO `>= 14%` CC; Agentforce Apps `>= 8%` CC; доля
  gains в EPS; net debt после M&A.
- Q4 FY2027 (ноябрь 2026 - январь 2027): ожидаемое закрытие Listen Labs; способ
  финансирования.
- Февраль-март 2027: Q4 FY2027 и первый гайденс FY2028 - органика, SBC в %
  выручки, FCF growth с процентами за полный год.

Постоянно:

- like-for-like Agentforce ARR, Data 360 ARR без Informatica, AI-cohort
  retention; продолжится ли квартальное раскрытие ARR;
- конкурентные запуски Microsoft, ServiceNow и AI-native игроков;
- оценка доли в Anthropic;
- short interest и инсайдерские сделки;
- цена и техника: 50-day MA `$217.69`, 200-day MA `$191.00` (MarketBeat,
  2026-09-30, не перепроверялись). Правило из `Принципы инвестиций.md` - не
  покупать падающую акцию и ждать признаков разворота.

### Условия для действия

Ориентиры для решения пользователя, не рекомендация:

- Аргументы за рассмотрение позиции: рост без M&A `>= 7-8%` в Q3/Q4 FY2027,
  cRPO без замедления, начало платного учёта HPI, owner FCF after SBC yield
  `>= 6.5-7%` на цене входа, признаки стабилизации цены. Расчёт: при owner FCF
  около `$11B` и около `790M` акций после ASR yield `7%` соответствует цене
  около `$199`, а `6%` - около `$232`.
- Аргументы против или за выход из shortlist: рост без M&A `< 6%`, cRPO `< 12%`
  CC, рост attrition, прекращение квартального раскрытия AI ARR без замены, net
  debt/EBITDA `> 2.5-3x`, новые крупные кэш-сделки при стагнирующем owner FCF.

Инвестиционное действие сейчас: оставить CRM в shortlist в статусе
«наблюдать». Ключевая точка проверки - отчёт Q3 FY2027. Июньский аргумент
«дёшево по cash flow» после роста на `51%` в значительной мере исчерпан.

## Источники

Локальные данные (скрипты; не пересчитывались):
`market/data/market_quotes/fyn_technology_current_20260620.csv`,
`market/data/market_quotes/fyn_technology_current_20260920.csv`,
`market/data/market_quotes/fyn_technology_current_20260920_summary.csv`,
`market/data/market_quotes/fyn_technology_norm.csv` (старый путь
`data/market_quotes/`), SEC companyfacts `CIK0001108524`.

Отчётность Salesforce и SEC:

- Q1 FY2027: https://www.salesforce.com/news/press-releases/2026/05/27/fy27-q1-earnings/ ;
  https://www.sec.gov/Archives/edgar/data/0001108524/000110852426000125/crm-q1fy27xexhibit991.htm
- Q2 FY2027 press release (2026-08-26):
  https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/ ;
  https://s205.q4cdn.com/626266368/files/doc_financials/2027/q2/CRM-Q2-FY27-Earnings-Press-Release.pdf ;
  https://www.sec.gov/Archives/edgar/data/1108524/000110852426000187/crm-q2fy27xexhibit991.htm
- 10-Q Q2 FY2027: https://www.sec.gov/Archives/edgar/data/0001108524/000110852426000190/crm-20260731.htm
- Q4 FY2026 (исходный гайденс FY2027, FY2026 SBC/FCF/EPS):
  https://www.sec.gov/Archives/edgar/data/1108524/000110852426000056/crm-q4fy26xexhibit991.htm
- 8-K от 2026-08-05 (Tallapragada):
  https://www.sec.gov/Archives/edgar/data/0001108524/000110852426000160/crm-20260805.htm
- Investor Day 2026-09-16: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000210/investorday2026.htm ;
  пересказ 8-K: https://www.stocktitan.net/sec-filings/CRM/8-k-salesforce-inc-reports-material-event-d41ccfdd5811.html
- Form 4 Conway (2026-09-04): https://www.sec.gov/Archives/edgar/data/1108524/000110852426000199/xslF345X06/form4.xml
- Form 4 Kirk (2026-09-18): https://www.sec.gov/Archives/edgar/data/1108524/000110852426000212/xslF345X06/form4.xml

Анонсы Salesforce:

- Editions (2026-09-03): https://www.salesforce.com/news/stories/salesforce-simplifies-editions-2026/
- HPI / Headless Toolkit (2026-09-17): https://help.salesforce.com/s/articleView?id=005360285&language=pt_BR&type=1
- AWS (2026-09-15): https://www.salesforce.com/news/stories/aws-salesforce-enterprise-ai-expansion/
- Dreamforce 2026: https://www.salesforce.com/blog/dreamforce-2026-announcements/
- Listen Labs (2026-09-29): https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-listen-labs/
- m3ter: https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-m3ter/
- Cimulate: https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-cimulate/
- VA (2026-07-24): https://investor.salesforce.com/news/news-details/2026/VA-Awards-Salesforce-1-6B-Contract-to-Transform-Veteran-Care-and-Services/default.aspx

Котировки, мультипликаторы, консенсус, позиционирование:

- Nasdaq historical API: https://api.nasdaq.com/api/quote/CRM/historical
- https://stockanalysis.com/stocks/crm/statistics/ ;
  https://stockanalysis.com/stocks/crm/forecast/ ;
  https://stockanalysis.com/stocks/crm/history/
- https://finance.yahoo.com/quote/CRM/analysis/
- https://www.marketbeat.com/instant-alerts/price-salesforce-nyse-crm-stock-price-up-2-heres-what-happened-2026-09-30/
- https://www.tipranks.com/news/salesforce-stock-crm-falls-despite-analyst-price-target-raises-as-dreamforce-2026-ends-why-are-analysts-bullish
- Short interest: https://www.chartmill.com/stock/quote/CRM/ownership/short-interest

Конкуренты и риски:

- Microsoft Copilot (2026-09-25): https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/
- ServiceNow (2026-04-09): https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-moves-beyond-the-sidecar-AI-era-giving-customers-a-complete-AI-native-experience-across-all-products-and-packages/default.aspx
- Sierra Ghostwriter (2026-09-28): https://sierra.ai/blog/ghostwriter-ai-tool-to-teammate
- Zenity SalesBleed (2026-09-24): https://labs.zenity.io/post/salesbleed-0-click-data-exfiltration-on-agentforce

События и контекст:

- Earnings call Q2 FY2027: https://www.fool.com/earnings/call-transcripts/2026/08/31/salesforce-crm-q2-2027-earnings-call-transcript/
- Реакция акции 2026-08-27: https://www.fool.com/coverage/stock-market-today/2026/08/27/stock-market-today-aug-27-salesforce-surges-23-on-anthropic-partnership-and-q2-earnings-beat/
- Слайды Q2 (Data 360 ARR с Informatica Cloud, milestone-раскрытие):
  https://www.investing.com/news/company-news/salesforce-q2-fy27-slides-ai-drives-tripledigit-arr-growth-93CH-4878058 ;
  https://uk.investing.com/news/stock-market-news/salesforce-q2-fy27-slides-ai-drives-tripledigit-arr-growth-93CH-4848687
- Июльский рост и апгрейд Guggenheim: https://www.fool.com/investing/2026/07/01/why-salesforce-stock-is-up-today/ ;
  https://247wallst.com/investing/2026/07/27/salesforce-surges-7-servicenow-jumps-8-workday-jumps-10-as-software-rebounds-on-ai-rotation/
- Fin закрыта: https://www.investing.com/news/company-news/salesforce-completes-acquisition-of-ai-customer-service-firm-fin-93CH-4896012
- Contentful закрыта: https://dotfusion.com/blogs/salesforce-contentful-acquisition-closed-what-it-means
- Listen Labs, реакция акции: https://www.proactiveinvestors.com/companies/news/1099393/salesforce-up-3-2-after-announcing-listen-labs-acquisition-1099393.html
- Сбой 2026-09-16: https://www.salesforceben.com/salesforce-hit-by-global-service-disruption-during-dreamforce-2026/
- Claudeforce: https://finance.yahoo.com/technology/ai/articles/salesforce-claudeforce-deal-anthropic-signals-102859998.html
- Менеджмент: https://www.cnbc.com/2026/08/05/marc-benioff-gets-a-new-coo-as-salesforce-promotes-miguel-milano-.html
- Рост без M&A (вторичные обзоры): https://beancount.io/blog/2026/09/13/salesforce-fy2027-q2-earnings-analysis ;
  https://howtheymake.money/en/blog/crm-q2-fy27-eps-doubled-but-not-from-operations
  (второй источник - только по поисковой выдаче, страница не открывалась)
- Настроения в конце сентября, Morgan Stanley EW `$235` (пересказ):
  https://finance.yahoo.com/markets/stocks/articles/salesforce-stock-down-nearly-12-123926159.html
- Независимая проверка: Codex `gpt-6.1-sol` с живым веб-поиском, 2026-10-01
  (ключевые находки перепроверены по первоисточникам: 10-Q, Form 4, анонсы
  Salesforce, Investor Day, Zenity, Microsoft, Sierra).
