# Technology

Large-cap technology, software, cloud, platforms, consulting and payments.

Группа в TradingView: `Tehnology`.

## Ключевые компании

- [AAPL](AAPL.md) - Apple: consumer hardware ecosystem.
- [MSFT](MSFT.md) - Microsoft: cloud, enterprise software, AI.
- [GOOG](GOOG.md) - Alphabet: search, cloud, AI.
- [AMZN](AMZN.md) - Amazon: AWS and e-commerce platform.
- [META](META.md) - Meta Platforms: social platforms and AI.
- [ADBE](ADBE.md) - Adobe: creative software and digital media.
- [CRM](CRM.md) - Salesforce: enterprise SaaS.
- [NOW](NOW.md) - ServiceNow: workflow automation SaaS.
- [ACN](ACN.md) - Accenture: IT consulting and implementation.

## Данные для sector_score графика

Обновлено: 2026-06-23.

### Актуальная оценка на 2026-06-20

Источник текущей точки: SEC EDGAR XBRL-факты с `filed <= 2026-06-20` и закрытие
Nasdaq от 2026-06-18 (последний торговый день перед якорем). Норма — двухуровневая
медиана FY2021-FY2025 из `data/market_quotes/fyn_technology_norm.csv`.

| Метрика | Сейчас | 5Y-норма | Коэффициент |
|---|---:|---:|---:|
| P/E | `21.77` | `29.93` | `0.727` |
| EV/EBITDA | `15.35` | `25.36` | `0.605` |
| P/S | `6.88` | `8.30` | `0.829` |
| FCF yield | `4.73%` | `3.52%` | `0.745` (инверсия yield) |
| Итоговый `sector_score` | `0.724` | `1.000` | сектор дешевле нормы |

#### Факты: бизнес не зарабатывает меньше

У всех девяти компаний корзины текущая TTM-чистая прибыль выше FY2025 и FY2021.
Медианная net margin корзины равна `27.15%` против 5Y-нормы `25.31%`; медианный
рост прибыли — `25.98%` против нормы `18.72%`. Медианный рост выручки немного
замедлился: `12.76%` против `13.87%`.

| Компания | TTM revenue | TTM net income | Изм. прибыли к FY2025 | Цена к FY2025 close | P/E сейчас / собственная 5Y-медиана |
|---|---:|---:|---:|---:|---:|
| AAPL | `$451.4B` | `$122.6B` | `+9%` | `+17%` | `35.7 / 27.5` |
| MSFT | `$318.3B` | `$125.2B` | `+23%` | `-24%` | `22.5 / 34.4` |
| GOOG | `$422.5B` | `$160.2B` | `+21%` | `+17%` | `27.8 / 23.8` |
| META | `$215.0B` | `$70.6B` | `+17%` | `-13%` | `21.0 / 24.8` |
| ADBE | `$25.2B` | `$7.2B` | `+1%` | `-39%` | `10.7 / 40.2` |
| CRM | `$42.8B` | `$8.0B` | `+30%` | `-56%` | `15.5 / 67.5` |
| NOW | `$14.0B` | `$1.8B` | `+1%` | `-38%` | `55.8 / 154.3` |
| ACN | `$73.1B` | `$7.8B` | `+1%` | `-51%` | `10.2 / 29.9` |
| IBM | `$68.9B` | `$10.8B` | `+2%` | `-18%` | `21.8 / 26.7` |

#### Интерпретация

- Дешевизна сосредоточена в software/IT-services: ADBE, CRM, NOW и ACN. У них
  прибыль не обвалилась, но цена снизилась на `38-56%` относительно FY2025 close.
- AAPL и GOOG, наоборот, дороже собственных норм. Они удерживают общий score от
  ещё более низкого значения.
- Главный отрицательный компонент — EV/EBITDA (`0.605` нормы), затем P/E (`0.727`).
- Диагностическое разделение той же методикой показывает неоднородность корзины:
  platforms (`AAPL/MSFT/GOOG/META`) около `1.11`, enterprise software
  (`ADBE/CRM/NOW`) около `0.24`, IT services/legacy (`ACN/IBM`) около `0.65`.
  Это не отдельные официальные sector scores, а проверка причины: формулировка
  «Technology дешёвый» фактически означает сильный de-rating enterprise software
  и IT services, а не дешевизну всех mega-cap платформ.
- Последние официальные отчёты не показывают общего слома бизнеса: Adobe сообщил
  рекордную квартальную выручку и повысил FY26 targets; Salesforce показал рост
  subscription & support revenue и GAAP operating margin; ServiceNow сохранил
  рост выручки `22%`; Microsoft увеличил квартальную выручку `18%`, а operating
  income `20%`.

#### Внешняя сверка и различие корзин

Сверка на 2026-06-23 показывает, что локальный вывод «Technology дешевле нормы»
нельзя автоматически переносить на официальный S&P 500 Information Technology /
XLK. В нашей секторной карте полупроводники выделены в отдельный сектор
`SEMICONDUCTORS`, а `TECHNOLOGY` — это платформы, enterprise software, consulting
и legacy IT.

Внешние ориентиры дают другую картину для официального tech-сектора:

- State Street XLK на 2026-06-22: `Semiconductors & Semiconductor Equipment`
  занимают `50.56%` фонда; крупнейшие позиции — NVDA `15.15%`, AAPL `13.08%`,
  MSFT `8.18%`, MU `5.64%`, AVGO `5.56%`, AMD `4.97%`.
- WorldPERatio для S&P 500 Information Technology на 2026-06-23: trailing P/E
  `36.56`, выше 5Y среднего `32.44` и немного выше верхней границы 1σ
  `[28.78; 36.11]`; источник классифицирует сектор как overvalued.
- Finviz Groups на 2026-06-23: Technology P/E `40.20`, forward P/E `28.06`,
  P/S `7.97`, P/B `11.40`, P/FCF `30.69`.
- Damodaran sector dataset обновлён в январе 2026: software/system &
  application и semiconductors всё ещё торгуются с высокими forward P/E
  около `34-37x`, поэтому широкая внешняя tech-корзина не выглядит дешёвой
  в абсолютном смысле.

Итог: локальный `sector_score=0.724` — это сигнал de-rating внутри нашей
non-semis technology basket. Для публичного XLK/S&P IT нужен отдельный вывод,
потому что он уже наполовину semiconductor/AI hardware.

#### Риски и ограничения вывода

- Норма FY2021-FY2025 включает период низкой стоимости капитала и высоких оценок
  growth-компаний, а также очень высокие ранние P/E CRM/NOW при небольшой
  GAAP-прибыли. Поэтому часть
  дисконта — нормализация прежней переоценки, а не гарантированная недооценённость.
- Рынок закладывает риски AI-disruption для Adobe/SaaS, слабый consulting growth у
  Accenture, интеграцию приобретений у Salesforce/ServiceNow и высокий AI capex у
  hyperscalers. Рост прибыли сам по себе не доказывает, что старые мультипликаторы
  должны восстановиться.
- `sector_score` — valuation-only сигнал. Перед инвестиционным действием нужны
  forward growth, EPS revisions, organic growth, SBC/dilution и FCF после AI capex.

#### Предварительный shortlist внутри дешёвой части корзины

| Компания | Revenue growth | Earnings growth | Net margin | P/E | EV/EBITDA | FCF yield | Предварительная оценка |
|---|---:|---:|---:|---:|---:|---:|---|
| ADBE | `11.5%` | `5.2%` | `28.7%` | `10.7` | `7.9` | `13.3%` | Самая сильная комбинация качества и цены; главный риск — AI-disruption |
| CRM | `11.0%` | `29.3%` | `18.7%` | `15.5` | `15.3` | `11.8%` | Привлекательно, но проверить organic growth, Informatica, debt и SBC |
| ACN | `6.7%` | `-2.0%` | `10.7%` | `10.2` | `n/a` | `15.8%` | Дёшево, но низкий growth и риск AI-давления на labor-based consulting |
| NOW | `21.7%` | `14.2%` | `12.6%` | `55.8` | `35.1` | `4.7%` | Качественный рост, но не дешёвая акция в абсолютном выражении |

FCF yield для software необходимо дополнительно корректировать на экономическую
стоимость stock-based compensation и dilution. Без этого ADBE/CRM/ACN могут
выглядеть дешевле, чем после расчёта owner earnings.

Официальные источники обновления: [Adobe Q2 FY2026](https://news.adobe.com/news/2026/06/adobe-q2fy26-financial-results),
[Salesforce quarterly results](https://investor.salesforce.com/financials/quarterly-results/default.aspx),
[ServiceNow Q1 2026](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-First-Quarter-2026-Financial-Results/default.aspx),
[Accenture Q3 FY2026](https://newsroom.accenture.com/news/2026/accenture-reports-third-quarter-fiscal-2026-results),
[Microsoft FY2026 Q3](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q3/performance).

Для первой версии графика использована корзина: `AAPL`, `MSFT`, `GOOG`, `META`, `ADBE`, `CRM`, `NOW`, `ACN`, `IBM`.

ETF-proxy / benchmark для проверки состава и цен: `XLK`.

Текущие мультипликаторы сравниваются со средним FY2021-FY2025 по StockAnalysis. Если показатель недоступен, отрицательный или экономически бессмысленный для конкретной компании, он не включается в среднее по этой метрике.

Стартовые веса после проверки доступности данных:

```text
Technology sector_score =
0.30 x Forward P/E coefficient
+ 0.20 x P/E coefficient
+ 0.20 x EV/EBITDA coefficient
+ 0.20 x P/S coefficient
+ 0.10 x P/FCF coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент | Вес | Компаний в расчете |
|---|---:|---:|---:|
| Forward P/E | `0.799` | 30% | 9 |
| P/E | `0.694` | 20% | 9 |
| EV/EBITDA | `0.854` | 20% | 9 |
| P/S | `0.927` | 20% | 9 |
| P/FCF | `1.008` | 10% | 9 |
| Итоговый sector_score | `0.84` | 100% |  |

Вывод по первой версии: текущая оценка корзины `Technology` равна `0.84` относительно собственной 5-летней нормы. Это valuation-only слой; large-cap tech/software basket; AI capex, cloud growth and EPS revisions not yet modeled.

### Собранные данные по компаниям

Источник: StockAnalysis financial ratios. Текущие значения - TTM/текущие данные на последний торговый день 2026-05-29; историческая база - среднее FY2021-FY2025.

| Тикер | Forward P/E curr / avg / coeff | P/E curr / avg / coeff | EV/EBITDA curr / avg / coeff | P/S curr / avg / coeff | P/FCF curr / avg / coeff |
|---|---:|---:|---:|---:|---:|
| `AAPL` | 34.24 / 28.42 / `1.20` | 37.83 / 30.08 / `1.26` | 28.26 / 22.58 / `1.25` | 10.15 / 7.50 / `1.35` | 35.48 / 28.81 / `1.23` |
| `MSFT` | 24.36 / 32.23 / `0.76` | 26.82 / 33.96 / `0.79` | 18.39 / 23.01 / `0.80` | 10.51 / 12.08 / `0.87` | 45.87 / 40.95 / `1.12` |
| `GOOG` | 30.04 / 23.53 / `1.28` | 28.63 / 24.44 / `1.17` | 28.24 / 18.40 / `1.53` | 10.86 / 6.65 / `1.63` | 71.19 / 31.32 / `2.27` |
| `META` | 19.27 / 21.68 / `0.89` | 23.01 / 22.98 / `1.00` | 14.74 / 14.56 / `1.01` | 7.47 / 6.91 / `1.08` | 33.27 / 24.84 / `1.34` |
| `ADBE` | 10.76 / 28.70 / `0.37` | 15.11 / 41.61 / `0.36` | 10.99 / 29.37 / `0.37` | 4.28 / 11.60 / `0.37` | 10.16 / 29.27 / `0.35` |
| `CRM` | 13.74 / 32.96 / `0.42` | 22.18 / 220.98 / `0.10` | 14.52 / 27.03 / `0.54` | 3.65 / 7.04 / `0.52` | 10.68 / 27.70 / `0.39` |
| `NOW` | 28.68 / 61.64 / `0.47` | 74.04 / 229.54 / `0.32` | 42.52 / 81.61 / `0.52` | 9.19 / 16.20 / `0.57` | 27.68 / 52.18 / `0.53` |
| `ACN` | 13.07 / 26.78 / `0.49` | 15.33 / 29.00 / `0.53` | 8.94 / 17.14 / `0.52` | 1.59 / 3.19 / `0.50` | 9.19 / 21.66 / `0.42` |
| `IBM` | 23.65 / 17.93 / `1.32` | 26.38 / 36.94 / `0.71` | 20.34 / 17.99 / `1.13` | 4.06 / 2.80 / `1.45` | 21.68 / 15.28 / `1.42` |

### Якорные даты для графика

Декадная динамика в `sector_valuation_dashboard.html` должна строиться по реальным valuation data на каждую якорную дату: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется последний торговый день до нее. Исторические точки не должны рассчитываться простым масштабированием последнего `sector_score` по `XLK`; `XLK` используется как benchmark/source-check и вспомогательный ценовой ориентир.

Таблица ниже сохранена как legacy benchmark-check по ETF close. Ее нельзя использовать как финальный источник `sector_score`; строки графика должны быть заменены реальными historical valuation data.


| Якорная дата | Фактическое закрытие | XLK close | Legacy scale, не использовать для sector_score |
|---|---|---:|---:|
| 2026-02-28 | 2026-02-27 | 138.76 | `0.7264` |
| 2026-03-10 | 2026-03-10 | 139.76 | `0.7317` |
| 2026-03-20 | 2026-03-20 | 135.29 | `0.7083` |
| 2026-03-30 | 2026-03-30 | 127.50 | `0.6675` |
| 2026-04-10 | 2026-04-10 | 142.62 | `0.7466` |
| 2026-04-20 | 2026-04-20 | 154.56 | `0.8091` |
| 2026-04-30 | 2026-04-30 | 159.50 | `0.8350` |
| 2026-05-10 | 2026-05-08 | 175.52 | `0.9189` |
| 2026-05-20 | 2026-05-20 | 177.14 | `0.9273` |
| 2026-05-30 | 2026-05-29 | 191.02 | `1.0000` |

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: XLK history](https://stockanalysis.com/etf/xlk/history/) |
| `AAPL` ratios | [StockAnalysis](https://stockanalysis.com/stocks/aapl/financials/ratios/) |
| `MSFT` ratios | [StockAnalysis](https://stockanalysis.com/stocks/msft/financials/ratios/) |
| `GOOG` ratios | [StockAnalysis](https://stockanalysis.com/stocks/goog/financials/ratios/) |
| `META` ratios | [StockAnalysis](https://stockanalysis.com/stocks/meta/financials/ratios/) |
| `ADBE` ratios | [StockAnalysis](https://stockanalysis.com/stocks/adbe/financials/ratios/) |
| `CRM` ratios | [StockAnalysis](https://stockanalysis.com/stocks/crm/financials/ratios/) |
| `NOW` ratios | [StockAnalysis](https://stockanalysis.com/stocks/now/financials/ratios/) |
| `ACN` ratios | [StockAnalysis](https://stockanalysis.com/stocks/acn/financials/ratios/) |
| `IBM` ratios | [StockAnalysis](https://stockanalysis.com/stocks/ibm/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `AAPL`, `MSFT`, `GOOG`, `META`, `ADBE`, `CRM`, `NOW`, `ACN`, `IBM`.
2. Взять текущие `Forward P/E`, `P/E`, `EV/EBITDA`, `P/S`, `P/FCF`.
3. Сравнить каждую метрику со средним FY2021-FY2025; для yield-метрик использовать обратную формулу `5Y average yield / current yield`.
4. Посчитать weighted score по весам выше.
5. Для каждой якорной даты получить реальные valuation data на последний торговый день до якоря; `XLK` использовать только как benchmark/source-check и вспомогательный ценовой ориентир.

## Компании и инструменты

- [AAPL](AAPL.md)
- [ACN](ACN.md)
- [ADBE](ADBE.md)
- [AMZN](AMZN.md)
- [CRM](CRM.md)
- [GOOG](GOOG.md)
- [IBM](IBM.md)
- [META](META.md)
- [MSFT](MSFT.md)
- [NOW](NOW.md)
- [PAYC](PAYC.md)
- [PYPL](PYPL.md)
- [TSLA](TSLA.md)
