# NVDA

- Группа TradingView: `Semiconductor`
- Источник: `TRADINGVIEW_WATCHLISTS.md`; разбор в рамках AI-boom темы — см. [AI/AI_BOOM_DEEPDIVE.md](../AI/AI_BOOM_DEEPDIVE.md)
- Статус: разобрана (deep-dive, Фаза 5)
- Обновлено: 2026-06-24
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

## Решение

**BUY** с дисциплиной. Вход $185-205 (в зоне), добор <$170, тремя траншами. Размер 2-5% портфеля — high-beta core, не «безопасная» позиция. Цель 12-18 мес ~$280-320. Триггер на пересмотр: два квартала digestion в DC-выручке или рост vendor-financing на балансе.

## Источники

- [NVIDIA Q1 FY2027 results, checked 2026-06-24](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027)
- [StockAnalysis: NVDA statistics, checked 2026-06-24](https://stockanalysis.com/stocks/nvda/statistics/)
- [NVIDIA Form 10-Q for quarter ended 2026-04-26, checked 2026-06-24](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm)
- [Barron's: Nvidia customer / ASIC risk, checked 2026-06-24](https://www.barrons.com/articles/nvidia-stock-price-ai-chips-5af3e659)
- [Morgan Stanley / investingLive summary: Nvidia underperformance and ASIC concerns, checked 2026-06-24](https://investinglive.com/stocks/morgan-stanley-sticks-with-nvidia-says-underperformance-is-overblown-20260130/)
