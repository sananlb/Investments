# Mining

Large miners, gold, copper, lithium and diversified commodity producers.

Группа в TradingView: `Mining`.

## Секторная карта

Обновлено: 2026-05-29.

### Что это за сектор

Mining - это не один сектор, а несколько commodity-циклов под одной крышей:

| Подсектор | Примеры | Главный драйвер |
|---|---|---|
| Diversified miners | `BHP`, `RIO`, `VALE`, `GLN` | Iron ore, copper, coal, aluminum, China, capex cycle |
| Copper miners | `FCX`, `SCCO`, `BHP`, `RIO`, `GLN` | Copper price, mine supply, electrification, grid, AI data centers |
| Gold miners | `NEM`, `GOLD` | Gold price, real yields, USD, AISC, reserve quality |
| Lithium / battery metals | `ALB`, частично `LTC1_` | Lithium carbonate/hydroxide prices, EV/storage demand, oversupply/deficit |
| Junior / optionality | `BEZ`, smaller names | Resource optionality, funding risk, commodity momentum |

Главная ошибка в секторе - оценивать все компании одним P/E. У gold miners, copper miners, lithium producers и diversified miners разные циклы, разные метрики и разная чувствительность к ставкам.

### От чего зависят прибыли

Главные источники прибыли:

1. **Commodity price** - цена меди, золота, железной руды, лития, угля.
2. **Production volume** - сколько компания реально добывает и продает.
3. **Unit costs / AISC** - себестоимость добычи, энергия, труд, реагенты, логистика.
4. **Ore grade** - содержание металла в руде; падающие grades повышают себестоимость.
5. **Capex** - поддерживающий и growth capex, расширение шахт, новые проекты.
6. **FX** - выручка часто в USD, затраты могут быть в локальной валюте.
7. **Jurisdiction / royalties / taxes** - Чили, Перу, ДРК, Индонезия, Австралия, Канада, Казахстан и др.
8. **Balance sheet** - долг и ликвидность критичны, особенно для junior miners.
9. **By-product credits** - золото/молибден/серебро могут снижать cash cost меди.

### Главные драйверы сектора

- Китай: недвижимость, инфраструктура, производство, stimulus.
- Copper demand: grid, power infrastructure, EV, data centers, AI, defense.
- Supply discipline: grades, permitting, disruptions, strikes, weather, geopolitics.
- Inventories: LME/COMEX/SHFE stocks, concentrate availability.
- USD and real rates: особенно важно для золота и risk appetite.
- Energy prices: важны для себестоимости добычи.
- Capex cycle: если цены высокие слишком долго, компании расширяют capacity, создавая будущий oversupply.
- M&A: крупные miners покупают reserves и copper exposure, если органический рост ограничен.

### Зависимость от цикла ставок

| Сценарий ставок | Что обычно происходит с mining |
|---|---|
| Ставки падают, экономика не уходит в рецессию | Обычно хорошо: слабее USD, лучше risk appetite, промышленный спрос держится. |
| Ставки падают из-за рецессии | Смешанно: золото может выиграть, industrial metals могут пострадать от падения спроса. |
| Ставки растут из-за сильной экономики | Может быть хорошо для меди/железа, если спрос сильнее давления USD и discount rate. |
| Ставки растут резко, USD сильный | Обычно плохо для commodity equities и junior miners: financing risk, multiple compression. |
| Инфляция и отрицательные real rates | Может быть хорошо для commodities и gold miners, если costs не растут быстрее commodity price. |

Практическое правило: **mining любит не просто низкие ставки, а сильный физический спрос, ограниченное предложение и здоровую ликвидность**.

### Корреляция с S&P 500

Mining имеет положительную, но неполную связь с S&P 500. Это commodity beta, а не просто equity beta.

Текущие ETF-ориентиры:

- `PICK` beta `0.98` на 2026-05-29 - broad global metals/mining ex gold/silver;
- `XME` beta `1.24` на 2026-05-29 - US metals/mining, equal-weight, более цикличный;
- `COPX` beta `1.04` на 2026-05-29 - copper miners;
- `GDX` beta `0.61` по StockAnalysis на 2026-05-22 - gold miners, ниже связь с S&P 500;
- `LIT` beta `1.03` по StockAnalysis на 2026-05-22 - lithium/battery theme, не чистый mining.

Вывод:

- copper/diversified miners часто растут вместе с global growth;
- gold miners могут вести себя иначе, особенно при падении real yields или росте страха;
- junior miners часто имеют собственный funding/liquidity cycle и могут падать даже при хорошем commodity narrative.

### Оценка и средний P/E

Для mining нельзя использовать один P/E как главный показатель. P/E часто обманчив:

- на пике commodity price прибыль максимальная, P/E может выглядеть низким;
- на дне цикла прибыль падает, P/E может выглядеть высоким или бессмысленным;
- для gold/copper projects важнее NAV и долгосрочная цена металла;
- для junior miners P/E часто вообще неприменим.

Базовые метрики:

| Метрика | Зачем нужна |
|---|---|
| EV/EBITDA | Сравнение operating cash generation через цикл |
| FCF yield | Сколько cash реально остается акционеру |
| P/NAV | Оценка запасов и проектов при долгосрочной цене металла |
| AISC / cash cost | Насколько компания защищена при падении commodity price |
| Net debt / EBITDA | Риск баланса |
| Reserve life | Сколько лет добычи обеспечено запасами |
| Capex intensity | Сколько денег нужно, чтобы поддерживать добычу |

### Стартовые веса для оценки сектора

Для широкой mining-оценки:

```text
Mining valuation score =
0.25 x EV/EBITDA relative coefficient
+ 0.25 x P/NAV relative coefficient
+ 0.20 x FCF yield coefficient
+ 0.20 x commodity price / cycle adjustment
+ 0.10 x balance sheet / jurisdiction adjustment
```

Для copper miners:

```text
Copper miners score =
0.25 x P/NAV at long-term copper price
+ 0.20 x EV/EBITDA
+ 0.20 x FCF yield
+ 0.15 x copper price vs incentive price
+ 0.10 x production growth / reserve quality
+ 0.10 x jurisdiction and balance sheet risk
```

### Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована выбранная mining-корзина: `BHP`, `RIO`, `VALE`, `FCX`, `SCCO`, `NEM`, `GOLD`. Текущие мультипликаторы сравниваются со средним значением FY2021-FY2025 по StockAnalysis.

Стартовые веса для пилота:

```text
Mining sector_score =
0.35 x EV/EBITDA coefficient
+ 0.25 x P/FCF coefficient
+ 0.20 x P/B coefficient
+ 0.20 x P/E coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент |
|---|---:|
| EV/EBITDA | `1.589` |
| P/FCF | `1.415` |
| P/B | `1.594` |
| P/E | `1.564` |
| Итоговый sector_score | `1.54` |

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `PICK`, потому что за несколько торговых дней фундаментальные значения почти не меняются.

Ограничение: это пилотная valuation-only модель. В mining `P/B` используется как грубый proxy для `P/NAV`, но настоящий `P/NAV` требует модели запасов, проектов, cost curve и долгосрочных цен меди/золота/железной руды. Следующий шаг - добавить commodity price adjustment и debt/jurisdiction adjustment.

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: PICK history](https://stockanalysis.com/etf/pick/history/) |
| `BHP` ratios | [StockAnalysis: BHP financial ratios](https://stockanalysis.com/stocks/bhp/financials/ratios/) |
| `RIO` ratios | [StockAnalysis: RIO financial ratios](https://stockanalysis.com/stocks/rio/financials/ratios/) |
| `VALE` ratios | [StockAnalysis: VALE financial ratios](https://stockanalysis.com/stocks/vale/financials/ratios/) |
| `FCX` ratios | [StockAnalysis: FCX financial ratios](https://stockanalysis.com/stocks/fcx/financials/ratios/) |
| `SCCO` ratios | [StockAnalysis: SCCO financial ratios](https://stockanalysis.com/stocks/scco/financials/ratios/) |
| `NEM` ratios | [StockAnalysis: NEM financial ratios](https://stockanalysis.com/stocks/nem/financials/ratios/) |
| `GOLD` ratios | [StockAnalysis: GOLD financial ratios](https://stockanalysis.com/stocks/gold/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `BHP`, `RIO`, `VALE`, `FCX`, `SCCO`, `NEM`, `GOLD`.
2. Взять текущие `EV/EBITDA`, `P/FCF`, `P/B`, `P/E`.
3. Сравнить каждую метрику со средним FY2021-FY2025.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `PICK` на последний торговый день до якоря.
6. При появлении надежного источника `P/NAV` заменить `P/B` на `P/NAV` или добавить `P/NAV` отдельным компонентом.

### Текущая картина: copper

Медь сейчас особенно важна, потому что стала связующим звеном между старым industrial cycle и новым AI/electrification cycle.

Текущие ценовые ориентиры:

- Trading Economics: copper `6.37 USD/lb` на 2026-05-29;
- COMEX Live: COMEX copper около `6.3940 USD/lb` на 2026-05-29, last trade 22:17 GMT;
- Goldman Sachs ожидает LME copper в диапазоне `$10,000-$11,000/t` в 2026 и `$15,000/t` к 2035 в долгосрочном сценарии.

Фундаментальная картина неоднозначная:

- Trading Economics фиксирует, что copper в мае 2026 был около исторических максимумов.
- IEA в Global Critical Minerals Outlook 2025 предупреждает, что рынок может столкнуться с дефицитом supply около `30%` к 2035 при текущем project pipeline.
- IEA также выделяет три причины, почему новый supply сложно быстро нарастить: declining ore grades, rising project costs и slowdown in new resource discoveries / long lead times.
- Goldman Sachs считает, что в 2026 рынок может быть ближе к балансу/небольшому surplus, но долгосрочно bullish из-за grid and power infrastructure, AI и defense.
- ICSG в апреле 2026 ожидал refined copper surplus `96 kt` в 2026 и `377 kt` в 2027, но одновременно снизил прогноз mine output growth на 2026 до `1.6%`.

Вывод по меди:

```text
Краткосрочно: цена уже высокая, возможна волатильность и споры surplus/deficit.
Долгосрочно: supply response медленный, grades хуже, проекты дорогие и долгие, а grid/AI/electrification demand растет.
```

### Текущие ETF-ориентиры

`PICK` на 2026-05-29:

- цена: `$66.09`;
- PE Ratio: `19.30`;
- dividend yield: `2.23%`;
- beta: `0.98`;
- holdings: `295`;
- top holdings: `BHP` 12.92%, `RIO` 6.98%, `FCX` 5.32%, `GLEN` 4.48%, `VALE3` 3.48%, `AAL` 3.45%, `NUE` 3.28%.

`COPX` на 2026-05-29:

- цена: `$88.14`;
- PE Ratio: `18.55`;
- dividend yield: `2.18%`;
- beta: `1.04`;
- holdings: `54`;
- top holdings: `TECK.B` 5.36%, `HBM` 5.31%, `ANTO` 5.16%, `BHP` 5.07%, `KGHM` 4.98%, `FM` 4.95%, `SCCO` 4.91%, `GLEN` 4.79%.

`XME` на 2026-05-29:

- цена: `$125.21`;
- PE Ratio: `20.77`;
- beta: `1.24`;
- holdings: `38`;
- top holdings: `NUE` 5.76%, `STLD` 5.62%, `CLF` 5.55%, `RS` 4.93%, `CMC` 4.62%, `HCC` 4.60%, `AA` 4.42%, `FCX` 4.15%.

`GDX` и `LIT` не использовать как чистые mining-прокси:

- `GDX` - gold miners, полезен для real rates / gold thesis;
- `LIT` - lithium and battery chain, не чистый miner ETF.

### Главная особенность сектора

Mining - это бизнес с сильным operating leverage к commodity price. При росте цены металла прибыль может расти быстрее выручки, но при падении цены металла FCF может быстро исчезать.

Главное правило по сектору:

```text
В mining нельзя покупать только низкий P/E.
Нужно смотреть normalized commodity price, cost curve, FCF через цикл, NAV и баланс.
```

### Что отслеживать перед покупкой

1. Цена основного commodity: copper, gold, iron ore, lithium.
2. Запасы и inventories: LME/COMEX/SHFE для меди.
3. AISC / cash cost и положение на cost curve.
4. Production guidance и capex guidance.
5. Ore grades, reserve life, replacement of reserves.
6. Jurisdiction risk: налоги, лицензии, национализация, strikes.
7. Balance sheet: net debt/EBITDA, maturity wall.
8. FCF yield при текущей и нормализованной цене металла.
9. P/NAV при conservative long-term commodity price.
10. Для junior miners: funding runway, dilution risk, technical trend.

### Красные флаги

- P/E выглядит низким, потому что commodity price на пике;
- FCF исчезает при умеренном снижении цены металла;
- AISC растет быстрее commodity price;
- capex резко увеличивается, но production growth слабый;
- reserves не восполняются;
- проект находится в сложной юрисдикции без премии за риск;
- junior miner вынужден постоянно выпускать акции;
- тезис держится только на "дефиците через 10 лет", а текущий рынок в surplus.

### Источники

- [StockAnalysis: PICK ETF, 2026-05-29](https://stockanalysis.com/etf/pick/)
- [StockAnalysis: COPX ETF, 2026-05-29](https://stockanalysis.com/etf/copx/)
- [StockAnalysis: XME ETF, 2026-05-29](https://stockanalysis.com/etf/xme/)
- [Trading Economics: Copper](https://tradingeconomics.com/commodity/copper)
- [COMEX Live: Copper Futures](https://comexlive.org/copper/)
- [IEA: Global Critical Minerals Outlook 2025, overview of outlook for key minerals](https://www.iea.org/reports/global-critical-minerals-outlook-2025/overview-of-outlook-for-key-minerals)
- [Goldman Sachs: Copper prices are forecast to decline somewhat from record highs in 2026](https://www.goldmansachs.com/insights/articles/copper-prices-forecast-to-decline-from-record-highs-in-2026)
- [Mining Weekly / ICSG: Global refined copper market to swing to surplus in 2026](https://www.miningweekly.com/article/global-refined-copper-market-to-swing-to-surplus-in-2026-group-says-2026-04-23)

## Ключевые компании

- [BHP](BHP.md) - BHP Group: largest diversified mining company.
- [RIO](RIO.md) - Rio Tinto: iron ore, copper, aluminum.
- [VALE](VALE.md) - Vale: iron ore and base metals.
- [FCX](FCX.md) - Freeport-McMoRan: copper and gold, Grasberg/Morenci.
- [SCCO](SCCO.md) - Southern Copper: copper pure-play leader.
- [GLN](GLN.md) - Glencore: metals, coal, trading.
- [NEM](NEM.md) - Newmont: large gold miner.
- [GOLD](GOLD.md) - Barrick Gold: global gold miner.

## Компании и инструменты

- [ALB](ALB.md)
- [BEZ](BEZ.md)
- [BHP](BHP.md)
- [FCX](FCX.md)
- [GLN](GLN.md)
- [GOLD](GOLD.md)
- [LTC1_](LTC1_.md)
- [NEM](NEM.md)
- [RIO](RIO.md)
- [SCCO](SCCO.md)
- [VALE](VALE.md)
