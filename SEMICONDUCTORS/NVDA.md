# NVDA

- Группа TradingView: `Semiconductor`
- Источник: `TRADINGVIEW_WATCHLISTS.md`; разбор в рамках AI-boom темы — см. [AI/AI_BOOM_DEEPDIVE.md](../AI/AI_BOOM_DEEPDIVE.md)
- Статус: разобрана (deep-dive, Фаза 5)
- Обновлено: 2026-09-22
- Название: NVIDIA
- Роль: GPU/AI accelerators; toll-road на capex всей AI-индустрии (звено Compute)

## Инвестиционный тезис

Toll-road на капзатраты всей AI-индустрии (CUDA-замок + продажа целых rack-систем Rubin), торгуется по forward P/E ~21-23 против своей 10Y-нормы ~54 — рынок оценивает её как зрелый полупроводник, хотя растёт на +85% YoY. Платишь за доказанное (загрузка фабрик, backlog), а не за фантазию; зашитый в цену бар ниже фактической траектории. По valuation-скрину — **cheap-and-improving** (единственный «качественный» с большим дисконтом к своей истории).

## Бизнес

Три усиливающих слоя ренты: CUDA-стек (18 лет lock-in, «ОС AI-инфраструктуры»), rack-scale системы (моат сместился с «быстрого чипа» на системную интеграцию суперкомпьютера), networking (NVLink/InfiniBand как «клей» кластера). Ров глубокий на тренинге, мельче на инференсе. Главная угроза — кастомные ASIC гиперскейлеров (TPU/Trainium/Maia), ставящие потолок доли в крупнейшем будущем сегменте. AMD дисциплинирует цены; China = безвозвратная потеря TAM за стеной экспортконтроля.

## Финансы

GM ~73-75% (software-природа ренты), FCF-машина (fabless, capex малый), net-cash. Концентрация: топ-несколько гиперскейлеров >40% DC-выручки — те же, кто строит ASIC. Качество выручки отличное по марже/кэшу, уязвимое по концентрации и цикличности (это capex покупателей, режется первым при развороте).

Обновлено 2026-06-24: официальный релиз Q1 FY2027 NVIDIA подтверждает revenue `$81.6B` (+85% YoY), Data Center revenue `$75.2B` (+92% YoY), GAAP gross margin `74.9%`. Ранее отмеченный конфликт агрегаторов по DC-выручке снят; источник для факта — NVIDIA Investor Relations / Q1 FY2027 earnings release.

## Оценка

Forward P/E ~21-23 vs 10Y-норма ~54; PEG ~0.25. В цену уже зашит сценарий замедления + эрозии маржи. База fair value ~$280-340; downside даже в жёстком сценарии ~–15-25%. Асимметрия благоприятна (~+50% / ~–20%).

## Катализаторы

Rubin/Vera Rubin ramp (новый ASP-цикл); beat-and-raise при сжатом мультипле = переоценка вверх без роста P/E; China H200-разблокировка (гайденс закладывает ноль → upside-опцион).

## Риски

Длительность capex-цикла (главный — циклический бизнес в секулярной одежде); круговое финансирование (NVDA→OpenAI→Oracle→CoreWeave) надувает спрос; потеря Китая; ASIC-эрозия инференса; концентрация клиентов.

### Дополнительная проверка bearish/neutral аналитиков

Обновлено: 2026-06-24.

Что могли недооценивать в первичном bull-case:

- Низкий forward P/E может быть ловушкой "E на пике": Q1 FY2027 net margin
  `71.5%` включает не только операционную силу, но и крупный `Other income`
  (`19.5%` от revenue). Операционный бизнес все равно исключительный
  (`65.6%` operating margin), но headline P/E может выглядеть дешевле из-за
  неоперационных инвестиционных gains.
- Концентрация сильнее, чем кажется: в Q1 FY2027 три direct customers дали
  `21%`, `17%` и `16%` total revenue; три direct customers также дали `30%`,
  `18%` и `16%` accounts receivable. Это не просто "много клиентов в AI", а
  высокая зависимость от нескольких каналов закупки.
- 10-Q прямо отмечает indirect concentration: одна AI research and deployment
  company внесла meaningful revenue, покупая cloud services у клиентов NVIDIA.
  Это усиливает риск circular / vendor-financed AI ecosystem, даже если прямой
  покупатель в отчетности другой.
- Баланс NVIDIA уже стал частью AI-инфраструктурной системы: non-marketable
  equity securities выросли до `$42.3B`, additions за квартал `$17.9B`,
  investment commitments `$27B`, facility lease guarantees maximum gross exposure
  `$3.5B`. Это не классический простой fabless balance sheet; часть спроса и
  экосистемы может поддерживаться инвестициями/гарантиями.
- Manufacturing / supply / capacity commitments достигли `$119B`, из них `$95B`
  к оплате в оставшейся части FY2027; cloud service commitments `$30B`. Это
  подтверждает уверенность в спросе, но при резком охлаждении AI capex повышает
  operating leverage и inventory / purchase obligation risk.
- Barron's формулирует главный конкурентный риск не как AMD, а как собственные
  клиенты: Microsoft, Meta, Google, Amazon и другие хотят снизить стоимость AI
  compute через ASIC / in-house silicon / Broadcom-style custom chips. Morgan
  Stanley считает эти страхи overstated и ждет сохранения высокой доли NVIDIA,
  но это именно ключевой спор в оценке.

Практический вывод: NVDA не выглядит "дешевой защитной quality stock". Она
выглядит дешевой относительно текущего темпа прибыли, но этот темп зависит от
очень высокой AI-capex интенсивности, концентрации покупателей, способности
клиентов финансировать buildout и сохранения 70%+ gross margin. Покупка
рациональна только малым/средним весом и с мониторингом capex, customer
financing, inventory provisions и ASIC share.

## Обновление 2026-09-22: Q2 FY2027 и оценка

Факты (источники ниже, данные на 21-22.09.2026):

- Цена $227.38 (закрытие 21.09), $228.93 (22.09, внутри дня); капитализация $5.53T; +22% YTD; 52w $164-236, максимум закрытия $235.74 (14.05.2026).
- Q2 FY2027 (26.08.2026): revenue `$96.2B` (+106% YoY), Data Center `$89.0B` (+117%), GM `75.0%`, non-GAAP EPS `$2.22`, GAAP EPS `$2.46` (GAAP выше за счёт `$7.8B` прибыли по equity securities, headline-P/E на GAAP занижен).
- Гайденс Q3: `$108B` ±2%, GM `74.0%`; в Q4 ожидается дно маржи 71-72% (рост цен на память), восстановление до 72-73% в FY2028. Китайский DC compute в гайденсе = 0.
- Первый в истории годовой прогноз: FY2028 revenue ~+70% (~$690-700B, «ограничено поставками») против консенсуса LSEG +44% (~$570B).
- Консенсус FY2027: EPS `$9.31`, revenue `$411.5B` (S&P Global через StockAnalysis); средний таргет `$329`.
- Мультипликаторы: P/E FY2027 ~24.6; forward P/E (NTM) 18.9; при FY2028 по гайденсу (net margin ~55%) EPS ~$15-16 -> P/E ~14-15. Trailing P/E 28.8 против 12M-среднего ~40.6 и 3Y-среднего ~51.

Вывод аналитика: дёшево к собственной истории и к темпу роста, но это цена цикла, а не ошибка рынка: рынок закладывает пик прибыли около FY2028-29. Сценарии от $229: сохранение роста в FY2029 при 20x -> ~$370 (+63%); 18x FY2028 -> ~$290 (+28%); digestion-год (EPS −35%) при 20x -> ~$210 (−8%); жёсткий спад (EPS −50%) при 18x -> ~$145 (−36%).

Портфель (Google Sheets, 22.09.2026): 100 акций, средняя $194, вес 7.5% — выше лимита карточки 2-5%; полупроводники вместе (MRVL 18.5% + AMD 12.2% + NVDA 7.5%) ≈ 38%.

Предложение аналитика от 2026-09-22 (ожидает подтверждения пользователя): **HOLD, не добирать** — позиция уже выше лимита, цена выше зоны входа, бета 2.2 при незакрытом вопросе по ФРС. Что проверять: GM не ниже 71% в Q4, capex-гайденсы гиперскейлеров в конце октября, рост non-marketable equity / vendor financing в 10-Q за Q2.

## Решение

**BUY** с дисциплиной. Вход $185-205 (в зоне), добор <$170, тремя траншами. Размер 2-5% портфеля — high-beta core, не «безопасная» позиция. Цель 12-18 мес ~$280-320. Триггер на пересмотр: два квартала digestion в DC-выручке или рост vendor-financing на балансе.

## Источники

- [NVIDIA Q1 FY2027 results, checked 2026-06-24](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027)
- [StockAnalysis: NVDA statistics, checked 2026-06-24](https://stockanalysis.com/stocks/nvda/statistics/)
- [NVIDIA Form 10-Q for quarter ended 2026-04-26, checked 2026-06-24](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm)
- [Barron's: Nvidia customer / ASIC risk, checked 2026-06-24](https://www.barrons.com/articles/nvidia-stock-price-ai-chips-5af3e659)
- [Morgan Stanley / investingLive summary: Nvidia underperformance and ASIC concerns, checked 2026-06-24](https://investinglive.com/stocks/morgan-stanley-sticks-with-nvidia-says-underperformance-is-overblown-20260130/)
- [NVIDIA Q2 FY2027 results, checked 2026-09-22](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027)
- [StockAnalysis: NVDA statistics, checked 2026-09-22](https://stockanalysis.com/stocks/nvda/statistics/)
- [StockAnalysis: NVDA forecast (S&P Global consensus), checked 2026-09-22](https://stockanalysis.com/stocks/nvda/forecast/)
- [CNBC: 70% FY2028 growth vs 44% LSEG estimate, 2026-08-26](https://www.cnbc.com/2026/08/26/nvidia-70percent-growth-forecast-puts-it-on-track-to-be-tech-no-2-company.html)
- [Money365: Q2 FY2027 margin step-down, equity gains, checked 2026-09-22](https://www.money365.market/articles/nvidia-q2-fy2027-earnings-analysis)
- Nasdaq API: дневные цены NVDA 02.09.2025-21.09.2026
