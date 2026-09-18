# Banks And Funds

Банки, инвестиционные банки, управляющие активами, брокеры и платежные сети.

Группа в TradingView: `Bbanks & fonds`.

## Секторная карта

Обновлено: 2026-05-30.

### Что это за сектор

В этой папке не один чистый сектор, а финансовая группа:

| Подсектор | Примеры | От чего в основном зависит бизнес |
|---|---|---|
| Universal banks | `JPM`, `BAC`, `C`, `USB`, `D05` | Чистая процентная маржа, кредитный цикл, депозиты, качество баланса |
| Investment banks / capital markets | `GS`, `MS` | M&A, IPO, trading, underwriting, активность рынков |
| Asset managers / brokers | `BLK`, `SCHW`, частично `MS` | AUM, притоки/оттоки, уровень рынков, комиссии, денежные остатки клиентов |
| Payment networks | `V`, `MA` | Объем платежей, consumer spending, cross-border, take rate, регулирование |

Поэтому средний P/E по группе надо читать осторожно: `V` и `MA` обычно имеют намного более высокие мультипликаторы и качество маржи, чем классические банки; `JPM`, `BAC`, `C`, `USB` больше зависят от ставок, кредитного риска и капитала.

### От чего зависят прибыли

Главные источники прибыли финансового сектора:

1. **Net interest income / NIM** - разница между доходностью активов и стоимостью фондирования.
2. **Loan growth** - спрос на кредиты со стороны бизнеса и потребителей.
3. **Credit quality** - просрочки, charge-offs, резервы под кредитные потери.
4. **Deposit base** - устойчивость депозитов и скорость, с которой растет их стоимость.
5. **Capital markets activity** - IPO, M&A, размещения облигаций, trading volumes.
6. **AUM and fees** - для управляющих активами и брокеров.
7. **Payment volume** - для Visa/Mastercard: потребление, travel, cross-border.
8. **Regulation and capital return** - требования к капиталу, stress tests, buybacks, dividends.

### Главные драйверы сектора

- Форма кривой доходности: банкам лучше, когда кривая нормальная или steepening, а не глубоко инвертированная.
- Направление ставок: важно не только "ставки растут/падают", а почему это происходит.
- Кредитный цикл: рост просрочек и резервов быстро давит на прибыль.
- Состояние экономики: занятость, потребление, инвестиции бизнеса, рынок недвижимости.
- Рыночная активность: M&A, IPO, debt issuance, trading.
- Уровень фондового рынка: влияет на asset managers и wealth management.
- Регуляторный фон: капитал, ликвидность, ограничения на buybacks.

### Зависимость от цикла ставок

| Сценарий ставок | Что обычно происходит с сектором |
|---|---|
| Ставки растут умеренно, экономика сильная | Часто хорошо для банков: активы переоцениваются вверх, NIM может расширяться. |
| Ставки растут резко, кривая инвертируется | Риск: стоимость депозитов растет, стоимость облигаций падает, появляются unrealized losses, кредитный риск растет. |
| Ставки снижаются без рецессии | Часто хорошо для сектора: снижаются риски по кредитам, оживает M&A/IPO, улучшается стоимость securities, но NIM может сжиматься. |
| Ставки снижаются из-за рецессии или банковского стресса | Плохо: кредитные потери и резервы важнее выгоды от снижения ставок. |
| Кривая steepening после инверсии | Один из лучших режимов для банков, если экономика не падает в рецессию. |

Практическое правило: **банки любят не просто высокие ставки, а здоровую экономику, устойчивые депозиты, нормальную кривую доходности и контролируемые кредитные потери**.

### Корреляция с S&P 500

Финансовый сектор имеет высокую положительную связь с S&P 500, но не является полным дубликатом индекса.

Для ориентира можно использовать `XLF` - Financial Select Sector SPDR ETF. Он представляет финансовый сектор S&P 500. По данным FT на 2025-11-30, beta `XLF` к S&P 500 TR была около `1.04` за 5 лет, а R-squared около `62%`, что означает корреляцию примерно `0.79`. За 3 года beta была около `0.98`, R-squared около `50%`, то есть корреляция примерно `0.71`.

Вывод:

- сектор обычно движется вместе с рынком;
- это не защитный актив;
- в банковский стресс может сильно отставать от S&P 500;
- в раннем восстановлении и при нормализации кривой может обгонять рынок.

### Оценка и средний P/E

Для широкой финансовой группы текущий ориентир по оценке:

- `XLF` Price/Earnings Ratio FY1: `14.76`;
- Price/Book: `2.19`;
- Est. 3-5 Year EPS Growth: `11.84%`;
- данные State Street по `XLF` на 2026-03-31.

Это не "чистый банковский P/E": внутри `XLF` есть Berkshire, Visa, Mastercard, Goldman Sachs, Morgan Stanley, страховые и asset managers. Поэтому классические банки надо оценивать отдельно.

Для банков важнее смотреть:

- P/B и P/TBV;
- ROE / ROTCE;
- NIM;
- CET1 capital ratio;
- cost of deposits;
- loan growth;
- provisions / net charge-offs;
- efficiency ratio;
- buybacks and dividends.

Низкий P/E у банка не всегда означает дешевизну. Он может означать ожидание роста кредитных потерь, слабую доходность капитала, проблемы с депозитами или недоверие к балансу.

### Данные для sector_score графика

Обновлено: 2026-05-31.

Для первой версии графика использована выбранная банковская корзина: `JPM`, `BAC`, `C`, `GS`, `MS`. Текущие мультипликаторы сравниваются со средним значением FY2021-FY2025 по StockAnalysis.

Стартовые веса:

```text
Banks sector_score =
0.35 x P/B coefficient
+ 0.25 x P/TBV coefficient
+ 0.20 x P/E coefficient
+ 0.20 x Forward P/E coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент |
|---|---:|
| P/B | `1.635` |
| P/TBV | `1.491` |
| P/E | `1.265` |
| Forward P/E | `1.159` |
| Итоговый sector_score | `1.43` |

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `KBE`, потому что за несколько торговых дней фундаментальные значения почти не меняются.

Ограничение: это пилотная модель. Следующий шаг - добавить ROE/ROTCE adjustment и credit quality, чтобы высокая P/B оценивалась вместе с качеством доходности капитала.

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: KBE history](https://stockanalysis.com/etf/kbe/history/) |
| `JPM` ratios | [StockAnalysis: JPM financial ratios](https://stockanalysis.com/stocks/jpm/financials/ratios/) |
| `BAC` ratios | [StockAnalysis: BAC financial ratios](https://stockanalysis.com/stocks/bac/financials/ratios/) |
| `C` ratios | [StockAnalysis: C financial ratios](https://stockanalysis.com/stocks/c/financials/ratios/) |
| `GS` ratios | [StockAnalysis: GS financial ratios](https://stockanalysis.com/stocks/gs/financials/ratios/) |
| `MS` ratios | [StockAnalysis: MS financial ratios](https://stockanalysis.com/stocks/ms/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `JPM`, `BAC`, `C`, `GS`, `MS`.
2. Взять текущие `P/B`, `P/TBV`, `P/E`, `Forward P/E`.
3. Сравнить каждую метрику со средним FY2021-FY2025.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `KBE` на последний торговый день до якоря.

### Текущая картина по банкам США

По FDIC за Q1 2026:

- квартальная прибыль банковской индустрии выросла до `$80.5B`;
- NIM снизилась до `3.31%`;
- loan growth вырос на `7.1%` год к году;
- депозиты росли седьмой квартал подряд;
- asset quality в целом оставалась благоприятной, но CRE, multifamily, credit cards и auto требуют наблюдения;
- unrealized losses on securities выросли за квартал до `$325.1B`, хотя были ниже год к году.

Вывод: сектор не выглядит как явный кризисный сектор, но главные риски остаются в NIM, стоимости фондирования, securities losses и кредитном качестве.

### Главная особенность сектора

Банки - это бизнес доверия и баланса. Они работают с большим финансовым рычагом: небольшое ухудшение качества активов, стоимости фондирования или доверия к депозитам может сильно ударить по капиталу и цене акции.

Главное правило по сектору:

```text
В банках нельзя покупать только "дешевый P/E".
Нужно покупать качество баланса, устойчивые депозиты, нормальный ROE и понятный кредитный риск.
```

### Что отслеживать перед покупкой

1. Кривая доходности: `10Y-2Y`, `10Y-3M`.
2. NIM и cost of deposits.
3. Loan growth.
4. Просрочки, net charge-offs, provisions.
5. CRE exposure, особенно office / non-owner-occupied CRE.
6. CET1, stress test, buybacks.
7. Динамика book value / tangible book value.
8. M&A / IPO / capital markets cycle для `GS` и `MS`.
9. AUM, net inflows и fee pressure для `BLK`, `SCHW`, `MS`.
10. Payment volume, cross-border и regulation для `V`, `MA`.

### Источники

- [State Street: XLF Fact Sheet, 2026-03-31](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-xlf.pdf)
- [FDIC: Quarterly Banking Profile, Q1 2026](https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-first-quarter-2026.pdf)
- [FT Markets: XLF risk measures](https://markets.ft.markitdigital.com/data/etfs/tearsheet/risk?s=XLF%3APCQ%3AUSD)
- [Fidelity: Financials sector guide](https://www.fidelity.com/learning-center/trading-investing/markets-sectors/guide-to-industry-sectors)
- [Fidelity: Business cycle and sector investing](https://www.fidelity.com/viewpoints/investing-ideas/sector-investing-business-cycle)

## Ключевые компании

- [JPM](JPM.md) - JPMorgan Chase: эталон качества среди крупных банков США.
- [BAC](BAC.md) - Bank of America: крупный universal bank, чувствителен к ставкам.
- [C](C.md) - Citigroup: global bank, restructuring/value case.
- [GS](GS.md) - Goldman Sachs: investment banking and markets.
- [MS](MS.md) - Morgan Stanley: wealth management + investment banking.
- [BLK](BLK.md) - BlackRock: крупнейший asset manager.
- [V](V.md) - Visa: платежная сеть с высокой маржинальностью.
- [MA](MA.md) - Mastercard: global payments network.

## Компании и инструменты

- [BAC](BAC.md)
- [BLK](BLK.md)
- [C](C.md)
- [D05](D05.md)
- [GS](GS.md)
- [JPM](JPM.md)
- [MA](MA.md)
- [MS](MS.md)
- [SCHW](SCHW.md)
- [USB](USB.md)
- [V](V.md)
