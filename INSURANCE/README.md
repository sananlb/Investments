# Insurance

Insurance, health insurance, brokers, P&C, life insurance and diversified insurance holdings.

Группа в TradingView: `Insurance`.

## Ключевые компании

- [UNH](UNH.md) - UnitedHealth Group: health insurance and Optum health services.
- [BRK.B](BRK.B.md) - Berkshire Hathaway: GEICO, reinsurance and insurance float.
- [PGR](PGR.md) - Progressive: US auto insurance leader.
- [CB](CB.md) - Chubb: global property and casualty insurance.
- [AIG](AIG.md) - AIG: large diversified insurer.
- [MMC](MMC.md) - Marsh McLennan: insurance brokerage and risk advisory.
- [ALL](ALL.md) - Allstate: US personal lines insurer.
- [ACGL](ACGL.md) - Arch Capital: specialty P&C / reinsurance quality-value candidate.
- [HIG](HIG.md) - The Hartford: diversified P&C / benefits value candidate.
- [RNR](RNR.md) - RenaissanceRe: catastrophe reinsurance cyclical value.
- [RGA](RGA.md) - Reinsurance Group of America: life and health reinsurance value candidate.

## Инвестиционный разбор сектора

Обновлено: 2026-06-24. Рыночная сверка: официальный `KIE` / State Street на 2026-06-22, цена `KIE` по Schwab на закрытие 2026-06-23. Локальный фундаментальный снимок sector_score: `fyn_insurance_current_20260620.csv`, цены на 2026-06-18. Это аналитическая карта, не торговое поручение.

### Факты

- Страхование не является одним однородным бизнесом. В `KIE` входят brokers, life & health, multi-line, P&C и reinsurance; индекс модифицированно equal-weighted, поэтому это скорее ставка на отраслевую ширину, чем на мега-кап финансовый сектор.
- Локальный `sector_score` на 2026-06-20: `0.7729`, дешевле собственной 5-летней нормы. Компоненты: `P/B 0.7947`, `P/E 0.7468`; статус данных `ok`, 6 компаний из 6 в расчете.
- Корзинная медиана: P/E `11.76` против 5-летней нормы `15.75`, P/B `2.65` против `3.34`, P/S `1.41` против `1.59`, FCF yield `10.0%` против `7.9%`. Выручка растет на `8.2%` YoY, но прибыль медианно снижается на `2.9%` YoY, поэтому дешевизна частично объясняется страхом по earnings.
- Внешняя сверка по `KIE`: State Street показывает P/E `10.69`, FY1 P/E `10.59`, P/B `1.51`, estimated 3-5Y EPS growth `9.63%`, 30-day SEC yield `1.21%`. Это подтверждает, что низкая оценка видна не только в нашей корзине.
- По Finviz на 2026-06-24 страховые подотрасли выглядят недорого: P&C около P/E `10.05`, forward P/E `12.38`, P/B `2.04`; life insurance P/E `13.18`, forward P/E `9.17`; reinsurance P/E `6.95`.
- P&C фундаментально прошел сильную фазу. IRMI пишет, что в 2025 году US P&C получил около `$60.9B` underwriting gain и combined ratio около `92.9%`; S&P Global отдельно отмечает резкое улучшение homeowners и private auto loss ratios в 2025. Это поддерживает `PGR`, `ALL`, `CB` и страховой float Berkshire, но создает риск нормализации маржи.
- Health insurance остается более спорной частью. CMS финализировал для 2027 Medicare Advantage рост выплат на `2.48%`, или `4.98%` с учетом risk score trend, что сняло часть давления на managed care. Но KFF показывает, что в 2024 gross margins в Medicare Advantage снизились на `17%`, а regulatory / risk coding scrutiny остается ключевым риском для `UNH`.

### Гипотезы

- **Базовая гипотеза:** sector_score ниже `0.8` дает право разбирать сектор как value opportunity, но покупать нужно не весь сектор автоматически, а лучшие подтипы внутри страхования.
- **P&C / personal lines:** `PGR` и `ALL` выглядят дешево потому, что рынок закладывает нормализацию сверхсильной underwriting-фазы. Возможность есть, если pricing discipline и loss ratio не откатятся быстро.
- **Quality P&C:** `CB` выглядит менее дешевым, но качественнее: глобальная диверсификация, высокая маржа, меньше зависимости от одного автоцикла.
- **Health insurance:** `UNH` - special situation, а не простой defensive compounder. Дисконт по P/B и P/S интересен, но P/E высокий из-за падения earnings и регуляторного риска. Вход имеет смысл только после подтверждения стабилизации medical cost trend, Medicare Advantage margins и DOJ/CMS риска.
- **Brokers:** `MMC` - качественный компаундер с более asset-light моделью, но секторная дешевизна в нем выражена слабее. Это кандидат на watchlist при просадке, не главный value-кейс.
- **AIG / life / diversified:** дешевизна ниже качеством. Там важны reserve quality, capital return, rate sensitivity и дисциплина underwriting, а не только низкий P/B.

### Риски

- Низкий P/E у P&C может быть циклической ловушкой после пика underwriting profitability.
- Catastrophe losses, social inflation, attorney-represented claims и рост severity могут быстро испортить combined ratio.
- В health insurance главный риск - medical cost trend выше pricing, Medicare Advantage risk adjustment, Star Ratings, coding scrutiny и DOJ/регуляторные расследования.
- Снижение ставок помогает mark-to-market bond portfolios, но ухудшает будущую доходность reinvestment income; резкий рост ставок наоборот может давить на book value.
- `KIE` и наша корзина не идентичны: `KIE` шире и equal-weighted, а локальная корзина включает `UNH`, `BRK.B`, `PGR`, `CB`, `AIG`, `MMC`, `ALL`.

### Инвестиционные действия

- Не покупать весь сектор только из-за `sector_score < 1.0`. Сначала разделить страхование на 4 корзины: P&C quality, personal lines turnaround, health insurance special situation, brokers / asset-light compounders.
- Первичный порядок для дальнейшего разбора: `CB` как quality anchor, `PGR` как лучший personal-lines оператор, `UNH` как high-risk recovery, `ALL` как более циклический turnaround, `MMC` как quality-at-right-price, `AIG` как lower-quality value.
- Для ETF-экспозиции `KIE` подходит как диверсифицированная ставка на insurance industry, но не заменяет выбор отдельных качественных компаний. Его плюс - низкая концентрация; минус - много mid/small names и меньше контроля над качеством.
- Перед реальным действием проверить: последние quarterly combined ratios у `PGR`, `ALL`, `CB`; reserve development; catastrophe losses; pricing vs loss cost inflation; medical care ratio у `UNH`; комментарии CMS/DOJ; относительный тренд `KIE` против `XLF` и `SPY`.
- Рабочее решение сейчас: сектор перевести в active watchlist, но не считать его готовой покупкой без проверки Q2 2026 отчетов и качества earnings.

### Разбор компаний и shortlist

Обновлено: 2026-06-24. Цены и мультипликаторы: Finviz / market snapshots на 2026-06-23, локальный `fyn_insurance_current_20260620.csv` для текущей корзины, earnings releases Q1 2026 и Progressive May 2026 monthly results.

| Компания | Тип идеи | Оценка дешевизны | Что нравится | Главный риск | Статус |
|---|---|---:|---|---|---|
| `CB` | quality P&C anchor | разумно дешево, не deep value | Q1 P&C combined ratio `84.0%`, premium growth `10.7%`, forward P/E около `11x` | цена уже отражает часть качества; cat/social inflation | лучший risk-adjusted кандидат в текущей корзине |
| `PGR` | лучший personal auto operator | дешево по trailing P/E, fair по normalized | May 2026 combined ratio `82.1`, policies +8% YoY, сильная underwriting-машина | EPS может нормализоваться вниз после суперцикла auto pricing | покупать только на откате или после проверки устойчивости CR |
| `ALL` | turnaround / reserve-release | самое дешевое в корзине | P/E около `5x`, forward P/E около `9x`, Q1 property-liability CR `82.0` | значимая часть Q1 улучшения от reserve releases; homeowners/cat риск | высокая upside/volatility, не quality anchor |
| `UNH` | health insurance recovery | дешево по P/S/P/B к истории, не дешево по P/E | Q1 medical care ratio `83.9%`, guidance raised to adj. EPS `>18.25` | DOJ/CMS/MA risk coding, medical cost trend, политический риск | special situation, нужна отдельная проверка |
| `AIG` | lower-quality value | дешево по forward P/E и около book | Q1 adjusted EPS +80%, CR `87.3`, dividend +11% | качество ниже, сложная структура, volatile earnings | кандидат только после сравнения с `HIG`/`ACGL` |
| `MRSH` / legacy `MMC` | broker compounder | не дешево | asset-light, organic growth, high margins | valuation выше сектора, litigation charge | watchlist при просадке |
| `BRK.B` | diversified compounder | скорее fair | страховой float + cash + BNSF/BHE/operating businesses | не pure insurance; valuation зависит от look-through earnings | держать как качество, не как дешевый insurance pick |
| `ACGL` | specialty P&C / reinsurance | дешево для качества | P/E около `7x`, forward P/E около `9x`, Q1 CR `81.7`, ROE mid-teens | specialty/reinsurance cycle and cat losses | лучший кандидат вне текущей корзины |
| `RNR` | catastrophe reinsurance | очень дешево, но циклично | P/E около `5x`, forward P/E около `7.5x`, Q1 CR `73.0` | cat year can erase earnings; mark-to-market investments | high-conviction only with cat-cycle thesis |
| `HIG` | diversified P&C / benefits | дешево и качественно | P/E/Fwd P/E около `9x`, core ROE около `20%`, BI underlying CR `89.2` | workers comp / commercial cycle / reserve risk | сильный кандидат для сравнения с `CB` |
| `RGA` | life reinsurance | дешево по forward P/E/book | forward P/E около `7x`, P/B около `1x`, adjusted operating ROE `15%+` | mortality/morbidity assumptions, capital model | интересный non-P&C diversifier |

Рабочий рейтинг после первого company-level прохода:

1. `ACGL` - лучший баланс дешевизны и качества вне исходной корзины.
2. `CB` - самый чистый quality anchor в исходной корзине.
3. `HIG` - дешевая качественная альтернатива `CB` с лучшей valuation.
4. `PGR` - очень качественный оператор, но normalized EPS надо перепроверять.
5. `RNR` - максимальная дешевизна, но требует отдельного взгляда на cat-cycle.
6. `UNH` - потенциально большой recovery, но это уже health-policy special situation.
7. `ALL` - дешево, но качество earnings хуже из-за reserve releases и катастрофического риска.

### Внешние аналитики: что могли пропустить

Обновлено: 2026-06-24.

- `ACGL`: внешние разборы подтверждают качество underwriting и buybacks, но Wall Street не так агрессивен, как наш первичный ranking: MarketBeat дает consensus `Hold`, 8 buy / 7 hold / 1 sell, средний target около `$106.81`, то есть примерно `14%` upside от `$93.71`. Что мы могли недооценить: слабый рост в отдельных сегментах. В Q1 2026 insurance segment имел combined ratio `96.5`, net premiums written `-1.4%`; reinsurance net premiums written `-6.0`, net premiums earned `-9.7`; mortgage underwriting income `-12.3%`. Вывод: `ACGL` остается #1, но это не "рост + дешево", а disciplined capital allocator в более мягком pricing cycle.
- `CB`: аналитики признают качество, но не видят большого near-term upside. MarketBeat показывает consensus `Hold` и price target близко к текущей цене; StockStory отмечает сильный beat по revenue/combined ratio/EPS, но book value per share ниже ожиданий (`$189.93` vs `$206.98`). Что мы могли недооценить: `CB` скорее надежный compounder, чем переоценка вверх на 30-50%.
- `HIG`: внешние источники делают вывод менее чистым. MarketBeat target около `$147.31` дает `~12%` upside, но StockStory отмечает miss по combined ratio, adjusted EPS и book value per share. Seeking Alpha формулирует тезис как strong cash flows, но "not a clean growth story"; upside больше зависит от underwriting discipline и capital return, чем от organic growth. Вывод: `HIG` оставить в top-4, но не ставить выше `CB` без проверки reserve quality и Q2.
- `PGR`: аналитики подтверждают качество, но спорят о valuation. MarketBeat consensus `Hold`, target около `$237.58` (`~10%` upside), при этом BofA сохранил Buy, но снизил target с `$331` до `$313`; StockStory отмечает beat по combined ratio, но miss по GAAP EPS и book value. Что мы могли недооценить: рынок боится не текущего CR, а нормализации auto margins и softening personal auto pricing.

Обновленный вывод после чтения аналитиков: порядок `ACGL -> CB -> HIG -> PGR` пока сохраняется, но разрыв между `HIG` и `PGR` небольшой. `HIG` дешевле по consensus upside, `PGR` качественнее как оператор, но сильнее зависит от auto margin normalization.

### Источники для текущего разбора

- [State Street: KIE](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-insurance-etf-kie) - официальный ETF-proxy, характеристики и valuation на 2026-06-22.
- [Schwab: KIE portfolio](https://www.schwab.wallst.com/Prospect/Research/etfs/portfolio.asp?symbol=kie) - цена закрытия и holdings snapshot.
- [Finviz Groups: Financial / Insurance industries](https://finviz.com/groups?g=industry&o=name&sg=financial&v=122) - текущие отраслевые P/E, forward P/E, P/B и performance.
- [Finviz Screener: Insurance industries](https://finviz.com/screener.ashx?v=121&f=sec_financial,ind_insurancepropertycasualty,cap_midover,fa_pe_u15&o=pe) - company-level valuation screen.
- [MarketBeat: ACGL](https://www.marketbeat.com/stocks/NASDAQ/ACGL/) - consensus rating, price target and analyst coverage.
- [MarketBeat: CB](https://www.marketbeat.com/stocks/NYSE/CB/) - consensus rating and valuation snapshot.
- [MarketBeat: HIG forecast](https://www.marketbeat.com/stocks/NYSE/HIG/forecast/) - analyst targets.
- [MarketBeat: PGR](https://www.marketbeat.com/stocks/NYSE/PGR/) - consensus rating and price target.
- [StockStory: CB Q1 2026](https://stockstory.org/us/stocks/nyse/cb/news/earnings/chubb-nysecb-exceeds-q1-cy2026-expectations) - analyst estimate comparison.
- [StockStory: HIG](https://stockstory.org/us/stocks/nyse/hig) - analyst estimate comparison.
- [StockStory: PGR](https://stockstory.org/us/stocks/nyse/pgr) - analyst estimate comparison.
- [Progressive IR: financial news](https://investors.progressive.com/financials/financial-news-releases/default.aspx) - monthly financial results.
- [S&P Global: P&C profitability](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/03/spectacular-p-and-c-statutory-profitability-may-prove-fleeting) - динамика loss ratios и риск нормализации.
- [IRMI: 2025 Insurance Year in Review and 2026 Developments](https://www.irmi.com/articles/expert-commentary/2025-insurance-year-in-review-and-2026-developments) - P&C combined ratio и underwriting gain.
- [CMS: 2027 Medicare Advantage and Part D Rate Announcement](https://www.cms.gov/newsroom/fact-sheets/2027-medicare-advantage-part-d-rate-announcement) - финальные MA rates на 2027.
- [KFF: Health Insurer Financial Performance in 2024](https://www.kff.org/medicare/health-insurer-financial-performance/) - gross margins и MLR по health insurance markets.
- [Allianz Global Insurance Report 2026](https://www.allianz.com/en/economic_research/insights/publications/specials_fmo/260528-global-insurance-report.html) - долгосрочный growth контекст по global insurance.

## Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована корзина: `UNH`, `BRK.B`, `PGR`, `CB`, `AIG`, `MMC`, `ALL`.

ETF-proxy / benchmark для проверки состава и цен: `KIE`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Insurance sector_score =
0.35 x P/B coefficient
+ 0.25 x P/E coefficient
+ 0.25 x Forward P/E coefficient
+ 0.15 x P/S coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| P/B | `0.889` | 35% | 6 |
| P/E | `0.870` | 25% | 6 |
| Forward P/E | `0.794` | 25% | 5 |
| P/S | `0.931` | 15% | 6 |
| Итоговый sector_score | `0.87` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Insurance` равна `0.87` относительно собственной 5-летней нормы. Это valuation-only слой; mixes health insurance, P&C, brokers and Berkshire; combined ratio, reserve quality and float/investment income not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | P/B curr / avg / coeff | P/E curr / avg / coeff | Forward P/E curr / avg / coeff | P/S curr / avg / coeff |
|---|---:|---:|---:|---:|
| `UNH` | 3.53 / 5.32 / `0.66` | 28.71 / 26.49 / `1.08` | 20.04 / 20.51 / `0.98` | 0.77 / 1.26 / `0.61` |
| `BRK.B` | 1.40 / 1.44 / `0.97` | 14.12 / 10.74 / `1.32` | n/a | 2.73 / 2.48 / `1.10` |
| `PGR` | 3.47 / 4.51 / `0.77` | 9.68 / 36.13 / `0.27` | 12.02 / 19.35 / `0.62` | 1.24 / 1.53 / `0.81` |
| `CB` | 1.64 / 1.62 / `1.01` | 11.01 / 12.51 / `0.88` | 11.35 / 12.30 / `0.92` | 1.98 / 2.00 / `0.99` |
| `AIG` | 0.98 / 1.01 / `0.97` | 13.04 / 9.75 / `1.34` | 9.05 / 10.91 / `0.83` | 1.47 / 1.49 / `0.99` |
| `MMC` | n/a | n/a | n/a | n/a |
| `ALL` | 1.80 / 1.91 / `0.94` | 4.55 / 13.43 / `0.34` | 7.80 / 12.54 / `0.62` | 0.78 / 0.72 / `1.09` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` должна строиться по реальным valuation data на каждую якорную дату: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется последний торговый день до нее. Исторические точки не должны рассчитываться простым масштабированием последнего `sector_score` по `KIE`; `KIE` используется как benchmark/source-check и вспомогательный ценовой ориентир.

Таблица ниже сохранена как legacy benchmark-check по ETF close. Ее нельзя использовать как финальный источник `sector_score`; строки графика должны быть заменены реальными historical valuation data.


| Якорная дата | Фактическое закрытие | KIE close | Legacy scale, не использовать для sector_score |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 58.13 | `1.0538` |
| 2026-03-10 | 2026-03-10 | 56.06 | `1.0163` |
| 2026-03-20 | 2026-03-20 | 54.34 | `0.9851` |
| 2026-03-30 | 2026-03-30 | 54.41 | `0.9864` |
| 2026-04-10 | 2026-04-10 | 55.90 | `1.0134` |
| 2026-04-20 | 2026-04-20 | 58.40 | `1.0587` |
| 2026-04-30 | 2026-04-30 | 57.33 | `1.0393` |
| 2026-05-10 | 2026-05-08 | 56.37 | `1.0219` |
| 2026-05-20 | 2026-05-20 | 57.79 | `1.0477` |
| 2026-05-30 | 2026-05-29 | 55.16 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: KIE history](https://stockanalysis.com/etf/kie/history/) |
| `UNH` ratios | [StockAnalysis](https://stockanalysis.com/stocks/unh/financials/ratios/) |
| `BRK.B` ratios | [StockAnalysis](https://stockanalysis.com/stocks/brk.b/financials/ratios/) |
| `PGR` ratios | [StockAnalysis](https://stockanalysis.com/stocks/pgr/financials/ratios/) |
| `CB` ratios | [StockAnalysis](https://stockanalysis.com/stocks/cb/financials/ratios/) |
| `AIG` ratios | [StockAnalysis](https://stockanalysis.com/stocks/aig/financials/ratios/) |
| `MMC` ratios | [StockAnalysis](https://stockanalysis.com/stocks/mmc/financials/ratios/) |
| `ALL` ratios | [StockAnalysis](https://stockanalysis.com/stocks/all/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `UNH`, `BRK.B`, `PGR`, `CB`, `AIG`, `MMC`, `ALL`.
2. Взять текущие `P/B`, `P/E`, `Forward P/E`, `P/S`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для каждой якорной даты получить реальные valuation data на последний торговый день до якоря; `KIE` использовать только как benchmark/source-check и вспомогательный ценовой ориентир.

## Компании и инструменты

- [AIG](AIG.md)
- [ACGL](ACGL.md)
- [ALL](ALL.md)
- [BRK.B](BRK.B.md)
- [CB](CB.md)
- [HIG](HIG.md)
- [MMC](MMC.md)
- [PGR](PGR.md)
- [RGA](RGA.md)
- [RNR](RNR.md)
- [UNH](UNH.md)
