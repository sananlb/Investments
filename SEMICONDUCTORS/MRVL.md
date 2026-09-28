# MRVL / Marvell Technology

- Тикер: `MRVL`
- Компания: Marvell Technology, Inc.
- Сектор библиотеки: `SEMICONDUCTORS`
- Основная тема: AI data center infrastructure, custom silicon, optical/networking, storage accelerators
- Статус: основной разбор компании
- Последнее обновление: 2026-07-05
- Базовый вывод: `watch / hold-review`, не `core rent-owner`

## Короткий вывод

Marvell становится все более чистой ставкой на AI data center infrastructure: дата-центры уже дают около трех четвертей выручки, а менеджмент направляет капитал в custom XPU, optical interconnect, Ethernet, CXL/storage acceleration и scale-up/scale-out connectivity. Это уже не старая диверсифицированная semiconductor-компания, а почти специализированный поставщик инфраструктурных чипов для AI-фабрик.

Главная проблема инвестиционного тезиса: Marvell участвует в дефицитной цепочке AI-инфраструктуры, но не является таким же чистым владельцем ренты, как NVIDIA, ASML, TSMC или в networking-слое потенциально Arista. В custom ASIC/XPU большая часть экономической силы остается у hyperscaler-клиента: клиент задает roadmap, контролирует workload/IP, может давить маржу и со временем мультисорсить.

Поэтому рабочий статус: **оставить в watch / пересматривать как позицию в портфеле, но не считать автоматическим "докупать на AI hype"**. Для повышения статуса нужны доказательства, что рост data center превращается в устойчивый FCF per share и удержание gross margin, а не только в рост выручки и R&D/M&A.

## Что делает компания

Marvell - fabless-разработчик чипов и IP для инфраструктуры данных. В AI data center ее продукты удобно делить на три блока:

1. **Logic / custom silicon**
   - custom XPU / accelerated processing units для конкретных hyperscaler workloads;
   - это альтернатива или дополнение к GPU, но не универсальная платформа как NVIDIA CUDA;
   - крупный клиент из видео - Amazon, но точную структуру клиентов нужно проверять по свежим раскрытиям и call transcript.

2. **Networking / optical / interconnect**
   - 800G и 1.6T optics;
   - Ethernet scale-out switches;
   - scale-up optical solutions, NPO/CPO, DCI;
   - DSP, silicon photonics, optical modulation.

3. **Storage / memory-adjacent infrastructure**
   - storage accelerators;
   - CXL-related products;
   - продукты, которые работают вокруг storage/memory, но Marvell не является производителем памяти.

Инвестиционно Marvell похожа на "baby Broadcom": custom silicon + networking + data infrastructure, но меньше по масштабу и с меньшей диверсификацией. Сравнение полезно, но неполное: Broadcom имеет более широкую полупроводниковую базу и большой software-блок после VMware, а Marvell стала более концентрированной ставкой на AI data center.

## Факты и свежая сверка

Факты ниже обновлены на 2026-07-05 по официальным релизам Marvell и пользовательским транскриптам видео. Рыночную цену и forward-мультипликаторы перед сделкой нужно проверять заново.

- Q1 FY2027: выручка $2.418 млрд, +28% г/г; non-GAAP gross margin 58.9%; non-GAAP EPS $0.80; operating cash flow $638.8 млн, рекордный для компании.
- Q1 FY2027 data center revenue: $1.833 млрд, +27% г/г и +11% кв/кв; доля data center в выручке - 76%.
- Guidance Q2 FY2027: выручка $2.7 млрд +/- 5%; non-GAAP EPS $0.93 +/- $0.05; non-GAAP gross margin 58.25-59.25%.
- FY2026: выручка $8.195 млрд, +42% г/г; non-GAAP EPS $2.84; Q4 FY2026 выручка $2.219 млрд.
- После продажи Automotive Ethernet Infineon за $2.5 млрд Marvell еще сильнее сместилась в сторону data center; автомобильный Ethernet больше не должен вносить вклад после закрытия сделки 14.08.2025.
- Marvell завершила покупки Celestial AI и XConn в феврале 2026; Q1 FY2027 уже включает их результаты с даты закрытия.
- NVIDIA и Marvell объявили партнерство вокруг NVLink Fusion; NVIDIA также инвестировала $2 млрд в Marvell.
- В апреле 2026 Marvell купила Polariton Technologies для усиления optical roadmap на 3.2T+ и silicon photonics/plasmonics.
- В июне 2026 назначен новый CFO Dan Durn; компания одновременно подтвердила Q2 FY2027 outlook.

## Разбор видеоисточников

Видеоисточники полезны как качественный тезис, а не как самостоятельная финансовая модель.

Ключевые мысли из видео Chip Stock Investor:

- data center revenue у Marvell "идет вертикально вверх"; авторы ожидают, что доля data center может стать выше 80% выручки;
- Marvell продает/деприоритизирует legacy-направления, включая consumer и automotive Ethernet, и становится почти all-in AI data center infrastructure play;
- продукты Marvell объясняются через три блока: logic/custom XPU, networking/interconnect/switching, storage accelerators/CXL;
- главный клиент в custom XPU, упомянутый в видео, - Amazon;
- баланс стал здоровее после притока cash от продажи Automotive Ethernet;
- компания потратила капитал на R&D, M&A и buybacks;
- reverse DCF из видео: при цене около $90 и FCF/share $1.61 в акции была заложена примерно 30% годовая скорость роста FCF на 5 лет плюс 5% terminal growth;
- вывод авторов: акция не дешевая, но если менеджмент прав и выручка почти удвоится за 2-3 года, shareholders могут получить сильный результат.

Ключевые мысли из видео Rick Orford от 2026-06-06:

- главный вопрос: Marvell остается привлекательной AI infrastructure stock или рынок уже заложил слишком много оптимизма;
- кастомные AI-чипы полезны не как замена NVIDIA вообще, а как оптимизация конкретных workloads: inference, cloud computing, recommendation systems и крупные data-center задачи;
- hyperscalers переходят от "строить любой ценой" к оптимизации efficiency: performance per watt, tokens per watt, ограничения power, memory и networking capacity;
- Marvell выигрывает не только от самого accelerator, но и от attach-компонентов вокруг системы: optical connectivity, Ethernet, storage/data movement, system-level infrastructure;
- design wins дают visibility, но не certainty: программы могут задерживаться, priorities клиента могут меняться, следующие поколения дизайна могут уйти конкурентам;
- ключевой риск симметричен upside: клиенты хотят снизить зависимость от NVIDIA, но так же могут снижать зависимость от Marvell через in-house silicon или Broadcom/других поставщиков.

Ключевые мысли из видео Parkev Tatevosian / Motley Fool конца июня 2026:

- сравнение `MRVL` и `AVGO` идет не в пользу Marvell по масштабу, cash-flow margin, ROIC и valuation;
- Broadcom в видео подается как более крупная и качественная cash-flow машина, а Marvell - как меньшая, потенциально более быстрорастущая, но более дорогая ставка на AI custom silicon/optics;
- автор утверждает, что по forward P/E и DCF на дату видео Broadcom выглядел дешевле, а Marvell - переоцененной; эти конкретные числа не считать текущими без новой проверки терминала;
- важная рамка: Marvell может иметь больший процентный upside из-за меньшей базы, но это не отменяет вопроса о качестве earnings, SBC, M&A и FCF;
- в комментариях, по пересказу транскрипта, спор шел вокруг трех тем: оптический козырь Marvell, преимущество Broadcom по фундаменталу и риск того, что semiconductor-цикличность не исчезнет из-за долгосрочных соглашений.

Мой перевод этого в инвестиционный язык: видео хорошо показывают upside-сценарий, но главный вопрос остается не "растет ли выручка", а **какая часть этого роста останется у Marvell в виде долгосрочной маржи и FCF на акцию**. По сравнению с Broadcom у Marvell выше optionality, но ниже доказанное качество cash engine.

## Инвестиционный тезис

**Бычий тезис**

Marvell может быть одним из главных бенефициаров перехода AI-инфраструктуры от простого GPU-cluster к более сложным системам, где нужны custom silicon, optical links, Ethernet switching, CXL, DCI и memory/storage-adjacent acceleration. Чем больше AI-фабрики масштабируются, тем важнее становится передача данных между ускорителями, racks, clusters и дата-центрами.

Если hyperscaler capex продолжит расти, а Marvell удержит design wins и валовую маржу около текущих уровней, компания может несколько лет расти быстрее среднего semiconductor-рынка. В этом сценарии Marvell - не "обычная циклическая semiconductor beta", а специализированный поставщик критичных компонентов AI factory.

**Медвежий тезис**

Custom ASIC и optical/networking могут оказаться менее прибыльными, чем рынок сейчас закладывает. Hyperscaler-клиенты крупные, технически сильные и склонны забирать economics себе. Они могут использовать Marvell как engineering partner, но не отдавать ей платформенную ренту. При этом конкуренты сильные: Broadcom, NVIDIA, AMD, Intel, Arista, Coherent, Lumentum, Credo, Astera Labs и внутренние ASIC-команды клиентов.

Если рост выручки идет через более низкомаржинальный custom silicon, M&A, повышенный R&D и customer concentration, то valuation может оказаться завышенной даже при красивой AI-истории.

## Моат и рента

Рабочая оценка: **partial rent owner**.

Где рента есть:

- optical DSP / connectivity IP;
- инженерная экспертиза в custom silicon;
- глубокая интеграция с hyperscaler roadmaps;
- switching/interconnect design wins;
- потенциальное усиление через Celestial AI, XConn и Polariton.

Где рента ограничена:

- custom XPU часто строится под конкретного клиента, а не как универсальная платформа;
- клиент может владеть workload/IP и иметь сильную переговорную позицию;
- switching costs есть, но они не равны CUDA-lock-in;
- hyperscalers могут мультисорсить или переносить часть разработки внутрь;
- NVIDIA-партнерство повышает релевантность Marvell, но одновременно закрепляет зависимость от NVIDIA ecosystem.

Вывод: Marvell участвует в AI bottleneck, но не полностью владеет bottleneck economics. Это важное отличие от компаний, где дефицитный ресурс невоспроизводим или защищен платформой.

## Финансы: что важно смотреть

Ключевой контрольный вопрос: **растет ли FCF per share вместе с data center revenue?**

Нужные метрики:

- data center revenue growth;
- non-GAAP gross margin, особенно при росте custom XPU mix;
- operating cash flow и free cash flow;
- FCF per share после buybacks и dilution;
- R&D как % выручки;
- customer concentration;
- доля stock-based compensation;
- GAAP profitability и разницу между GAAP/non-GAAP earnings;
- net debt после M&A и выпуска preferred/инвестиций;
- inventory и receivables: не идет ли рост через build-up перед заказами, которые могут быть перенесены.

Сигнал качества: выручка data center растет, gross margin удерживается около 58-60%, FCF per share растет быстрее share count/dilution, а backlog/design wins превращаются в cash.

Сигнал слабости: выручка растет, но FCF per share стоит на месте; gross margin падает из-за custom mix; R&D и M&A съедают операционный leverage; зависимость от 1-2 клиентов растет.

## Пять вопросов перед покупкой

Перед увеличением позиции MRVL нужно заново ответить на пять вопросов:

1. Может ли Marvell продолжать выигрывать крупные custom silicon programs у hyperscaler-клиентов?
2. Станут ли optical networking и data-center connectivity устойчивыми growth engines, а не коротким циклом AI capex?
3. Может ли Marvell защищать позицию против Broadcom, NVIDIA и внутренних silicon-команд клиентов?
4. Управляема ли customer concentration, если большую часть роста дают несколько hyperscalers?
5. Дает ли текущая оценка достаточный margin of safety, если AI spending замедлится или program ramps сдвинутся вправо?

## Оценка

Оценка без свежего терминала не фиксируется как постоянная. Из видео:

- при цене около $90;
- FCF/share $1.61;
- reverse DCF требовал примерно 30% роста FCF в год на 5 лет и 5% terminal growth.

Это означает, что даже в момент видео акция уже требовала сильного исполнения. Если текущая цена выше, то запас прочности еще меньше; если цена сильно ниже - нужно заново посчитать, насколько снизились ожидания и не ухудшился ли тезис.

Практический подход:

- не покупать только потому, что "AI data center revenue растет";
- перед покупкой считать reverse DCF от текущей цены;
- отдельно моделировать optimistic/base/bear cases по FCF per share, а не только по revenue;
- требовать margin of safety, потому что customer concentration и capex-cycle risk высокие.

### Reverse DCF / проверка цены на 2026-07-05

Обновлено 2026-07-05. Последний закрытый торговый день перед праздничными выходными США: 2026-07-02, close `MRVL` около **$245.29**.

База для расчета:

- FY2026 operating cash flow: $1.7505 млрд.
- FY2026 capex: $354.1 млн.
- FY2026 FCF: около **$1.40 млрд**, или примерно **$1.6 FCF/share**.
- Q1 FY2027 operating cash flow: $638.8 млн.
- Q1 FY2027 capex: $155.7 млн.
- Q1 FY2027 annualized FCF run-rate: около **$1.93 млрд**, или примерно **$2.16 FCF/share** на diluted share count Q1.

Модель `r=10%`, terminal growth `4%`, 5-летний explicit period:

| База FCF/share | Нужный FCF/share CAGR 5 лет для цены ~$245 |
|---|---:|
| FY2026 ~$1.6 | ~65% |
| Q1 FY2027 run-rate ~$2.16 | ~55% |

Exit multiple cross-check при `r=10%`:

| База FCF/share | Exit multiple 35x | Exit multiple 50x |
|---|---:|---:|
| FY2026 ~$1.6 | ~45% CAGR | ~36% CAGR |
| Q1 FY2027 run-rate ~$2.16 | ~37% CAGR | ~28% CAGR |

Вывод: текущая цена уже требует почти безошибочного исполнения. Даже если взять ускоренный Q1 run-rate, акция требует многолетнего роста FCF/share, который ближе к **40-55% CAGR**, если не ставить очень высокий terminal multiple. Это не невозможно при сценарии FY2028 revenue $16.5 млрд и custom silicon >$10 млрд в FY2029, но margin of safety слабый.

Дополнительный sanity check: если Marvell выйдет к FY2028 на revenue $16.5 млрд, non-GAAP operating margin 38-40%, налог около 11%, и diluted shares 915-950 млн, то грубый non-GAAP EPS/FCF proxy получается около **$5.7-6.3**. При цене $245 это все еще примерно **39-43x FY2028 earnings/FCF proxy**. То есть даже успешный FY2028 уже частично заложен в цену.

## Драйверы data center growth

Marvell не раскрывает полный точный split data center revenue по всем продуктам, поэтому ниже - рабочая карта по раскрытиям менеджмента, а не точная модель по строкам P&L.

FY2026 data center revenue: **$6.100 млрд**, 74% выручки, +46% г/г. Q1 FY2027 data center revenue: **$1.833 млрд**, 76% выручки, +27% г/г и +11% кв/кв. Менеджмент ожидает data center growth около **50% в FY2027** и около **55% в FY2028**.

Главные блоки:

1. **Interconnect / optical / DCI**
   - крупнейшая часть data center business;
   - FY2027 expected growth: >70% г/г;
   - 800G растет, 1.6T быстро ramp-up;
   - DCI modules: около $500 млн revenue в FY2026, line of sight к $1 млрд annualized в FY2028;
   - тезис: AI clusters растут через scale-out, scale-up и scale-across, поэтому data movement становится bottleneck.

2. **Switching**
   - scale-out switches: FY2027 revenue >$600 млн, примерно удвоение от FY2026;
   - annualized run-rate >$1 млрд в FY2028;
   - scale-up switching усиливается через XConn: PCIe/CXL, UALink, eSUN, NVLink Fusion.

3. **Scale-up optics / silicon photonics**
   - самый ранний, но потенциально важный новый слой;
   - Celestial AI добавляет photonic fabric;
   - Polariton усиливает 3.2T+ roadmap;
   - менеджмент говорит о значимом ramp в FY2028, но это пока execution risk.

4. **Custom silicon / XPU / XPU attach**
   - FY2027 custom revenue expected growth: >20% г/г;
   - FY2028: expected to more than double;
   - долгосрочная цель: >$10 млрд custom business revenue в FY2029;
   - драйверы: flagship XPU, новый tier-1 XPU program, >10 XPU-attach programs, NIC, CXL memory attach.

Ключевой вывод по пункту 5: для оценки Marvell важнее всего не просто data center growth, а **микс роста**. Лучший сценарий - interconnect/optics/switching растут быстрее custom XPU и держат margin. Худший сценарий - выручка растет за счет customer-owned custom silicon с более слабой маржой и большей bargaining power hyperscalers.

## Bottleneck pricing power

Обновлено 2026-07-05. Вопрос: может ли Marvell получить эффект "бутылочного горлышка" как в HDD/storage, где физическая емкость ограничена, поставщики sold out, а покупатели вынуждены платить больше?

Критерии настоящей bottleneck-рентабельности:

- спрос нельзя отложить без потери стратегической позиции;
- поставщиков мало, capacity/know-how нельзя быстро скопировать;
- продукт критичен для всей системы, но стоит малую долю от общей стоимости AI factory;
- есть долгие lead times, customer prepayments или capacity reservations;
- поставщик может поднять ASP/mix быстрее, чем растут издержки;
- customer switching cost выше, чем экономия от давления на цену.

**Где Marvell похожа на bottleneck:**

- Connectivity действительно становится следующим узким местом после compute и memory: scale-out, scale-up и scale-across требуют больше optics, DSP, SerDes, switches и DCI.
- Marvell имеет first-to-market позиции: 1.6T ZR/ZR+ pluggable, 2nm coherent DSP, MACsec, CoherentLight, PAM4, silicon photonics.
- DCI business уже имеет доказанную базу: менеджмент говорит о DCI revenue около $500 млн в FY2026 и line of sight к $1 млрд annualized в FY2028.
- Celestial AI дает опцион на уникальный слой: Photonic Fabric для scale-up optical interconnect внутри rack/system/package, где copper может стать физическим ограничением.
- Polariton/plasmonics добавляет roadmap на 3.2T+ и потенциально более низкий energy per bit.
- NVIDIA partnership через NVLink Fusion повышает вероятность, что Marvell окажется в архитектурном стандарте, а не только рядом с ним.

**Где Marvell НЕ похожа на HDD/storage bottleneck:**

- HDD-рынок ближе к физическому capacity oligopoly: если nearline disks sold out, hyperscaler платит за терабайты и срок поставки. У Marvell bottleneck больше технологический, а не физически ограниченный commodity output.
- Hyperscalers активно требуют multi-vendor/open ecosystem. OCI MSA с AMD, Broadcom, NVIDIA, Microsoft, Meta и OpenAI показывает, что покупатели не хотят одного закрытого поставщика optics/scale-up.
- Broadcom, NVIDIA, AMD, Cisco, Credo, Astera, Coherent, Lumentum и internal silicon teams ограничивают долгосрочную монополию.
- Custom XPU и XPU attach дают объем, но клиент часто владеет roadmap/workload/IP, поэтому Marvell может получить engineering economics, а не platform economics.
- Если Marvell станет слишком дорогой, hyperscalers будут финансировать альтернативы, мультисорсинг и стандартизацию.

Сценарная оценка. Это рабочие вероятности, не точный прогноз:

| Сценарий | Вероятность | Суть | Что будет видно в цифрах |
|---|---:|---|---|
| **Temporary bottleneck premium** | ~45% | Marvell получает 1-3 года сильного роста и mix benefit в optics/interconnect, но без монополии. | Data center >50% growth, non-GAAP GM около 58-60%, FCF/share растет, но без резкого margin expansion. |
| **Durable unique tech rent** | ~25% | Celestial/Polariton/NVLink Fusion/1.6T-3.2T optics дают Marvell де-факто незаменимую позицию в scale-up/scale-across. | GM расширяется, design wins становятся multi-year take-or-pay/capacity commitments, FCF/share растет быстрее revenue. |
| **Volume without rent** | ~20% | Выручка растет, но hyperscalers и конкуренты забирают economics. | Revenue beats, но GM/FCF/share не ускоряются; custom mix растет быстрее optics. |
| **Bottleneck breaks / standards commoditize** | ~10% | OCI/MSA, Broadcom/NVIDIA/internal designs быстро снижают уникальность Marvell. | Gross margin pressure, customer concentration warnings, delays in Celestial/scale-up optics. |

Рабочий вывод: вероятность, что Marvell получит **некоторый bottleneck premium**, достаточно высокая. Вероятность, что технология станет **HDD-like scarce asset с резким и устойчивым pricing power**, пока умеренная или низкая. Главный upside - не в том, что Marvell сможет просто "поднять цены", а в том, что optics/interconnect mix станет больше, чем рынок ждет, и будет иметь достаточно высокую маржу.

Что подтвердит настоящий bottleneck:

- gross margin растет выше 60% при ускорении data center;
- клиенты делают prepayments/capacity reservations именно под optics/interconnect, а не только под wafers/substrates;
- Celestial AI достигает $500 млн run-rate к Q4 FY2028 без сильной dilution/earnout drag;
- Marvell раскрывает крупные tier-1 scale-up optics wins;
- DCI/CoherentLight/COLORZ revenue растет быстрее custom XPU;
- конкуренты не успевают с сопоставимым 1.6T/3.2T power/performance и high-volume manufacturing.

Что опровергнет:

- non-GAAP GM остается flat/down при росте выручки;
- FCF/share не растет из-за SBC, capex/prepayments, earnouts и acquisitions;
- hyperscalers публично продвигают multi-vendor OCI/UALink/NVLink alternatives без явной роли Marvell;
- Broadcom/NVIDIA/Cisco/Coherent/Lumentum получают основные scale-up optics wins;
- Celestial/Polariton остаются roadmap story без revenue contribution.

## Hyperscaler capex risk map

Обновлено 2026-07-05. Для MRVL это главный внешний фактор: если AI capex продолжает расти, Marvell получает tailwind; если hyperscalers начинают оптимизировать/переносить capex, multiple и revenue expectations могут быстро сжаться.

| Клиент / группа | Свежий capex сигнал | Что это значит для MRVL | Риск |
|---|---|---|---|
| **Amazon / AWS** | Q1 2026 AWS sales +28%; TTM FCF Amazon упал до $1.2 млрд из-за роста PPE, связанного с AI investments. | Плюс для custom silicon/XPU, Trainium-adjacent infrastructure, CXL/NIC/connectivity. | Amazon технически силен и может забирать economics внутрь; если AWS FCF pressure станет политически/инвесторски болезненным, capex может тормозить. |
| **Microsoft / Azure** | FY2026 Q3 capex $31.9 млрд; около 2/3 capex - short-lived assets, в основном GPUs/CPUs; добавлен 1 GW capacity за квартал. | Плюс для networking, CXL/NIC, optical и custom attach. | Microsoft строит свой silicon stack (Maia/Cobalt/Azure Boost); Marvell может быть поставщиком attach/connectivity, но не обязательно главным rent owner. |
| **Alphabet / Google** | Q1 2026 capex $35.7 млрд; 60% technical infrastructure spend в servers, 40% в data centers/networking; FY2026 capex guide $180-190 млрд; Google Cloud backlog $462 млрд. | Сильный спрос на TPU/GPU infrastructure и networking; потенциально позитивно для optical/scale-across. | Google владеет TPU stack и может использовать собственную вертикальную интеграцию для давления на поставщиков. |
| **Meta** | Q1 2026 capex $19.84 млрд; FY2026 capex guide поднят до $125-145 млрд из-за component pricing и DC capacity. | Плюс для AI cluster networking, optics, switching, custom attach. | Meta может быстро менять архитектуру и поставщиков; если AI monetization lag станет проблемой, capex guide может стать уязвимым. |
| **Oracle / OCI** | FY2026 capex $55.7 млрд; FY2026 FCF -$23.7 млрд; RPO $638 млрд, большая часть роста связана с AI contracts, включая customer-prepaid/customer-supplied hardware. | Косвенный плюс для AI infrastructure demand и cloud capacity race. | Самый leveraged capex story: если financing/customer prepayments ухудшатся, это warning sign для всего AI infra chain. |

Что отслеживать каждый квартал:

- hyperscaler capex guidance: повышается, удерживается или режется;
- доля capex в short-lived assets против DC/networking/power;
- комментарии о GPU/TPU utilization и ROI;
- cloud backlog/RPO quality, а не только headline amount;
- признаки переноса заказов, customer prepayments, vendor financing;
- рост depreciation/energy/DC opex как давление на cloud margins.

Рабочий вывод по пункту 7: спрос пока подтвержден очень сильными capex-сигналами. Но именно это уже заложено в цену MRVL. Для покупки нужно не просто "capex растет", а доказательство, что Marvell получает растущую долю wallet и удерживает FCF/margin.

## MRVL vs AVGO

Сравнение с Broadcom - обязательный sanity check перед покупкой Marvell, потому что обе компании участвуют в custom silicon/networking для AI, но качество и структура риска разные.

**Аргументы в пользу Marvell:**

- меньшая база выручки, поэтому при успешных hyperscaler programs процентный рост может быть выше;
- более чистая ставка на AI data center infrastructure после продажи legacy-направлений;
- сильная позиция в optical DSP / PAM4 / 800G-1.6T / connectivity;
- потенциальный upside от Celestial AI, XConn, Polariton и NVLink Fusion;
- momentum может долго поддерживаться, если рынок продолжит платить за "next AI infrastructure winner".

**Аргументы в пользу Broadcom:**

- больше масштаб и более доказанный cash-flow engine;
- выше историческое качество profitability/ROIC;
- сильнее диверсификация: custom ASIC, networking и software/VMware;
- больше финансовая устойчивость, дивиденды и buyback capacity;
- valuation может быть ниже при сопоставимой или лучшей доказанности AI economics.

**Рабочий вывод:** если цель - максимальный high-beta upside от AI custom silicon/optics, Marvell может быть интереснее. Если цель - качество ренты, cash flow и риск/доходность, Broadcom выглядит как более сильный benchmark. Поэтому MRVL нельзя оценивать изолированно: перед докупкой нужно доказать, почему именно Marvell лучше `AVGO` на текущей цене.

## Катализаторы

- Повышение FY2027/FY2028 revenue outlook.
- Новые hyperscaler design wins в custom XPU и XPU-attach.
- Рост 800G/1.6T optics и Ethernet scale-out.
- Реальная монетизация Celestial AI, XConn и Polariton в revenue и margin.
- NVLink Fusion/NVIDIA partnership, если оно превращается в масштабируемые продукты, а не только в стратегический заголовок.
- Удержание non-GAAP gross margin около 58-60% при росте AI mix.
- Buybacks, если они реально поднимают FCF per share, а не только компенсируют dilution.

## Риски

- **Customer concentration.** Несколько hyperscaler-программ могут давать непропорционально большую часть роста.
- **Bargaining power клиентов.** Amazon, Microsoft, Google, Meta и другие могут давить pricing и забирать economics.
- **Custom ASIC margin risk.** Рост custom XPU может иметь ниже маржу, чем optical/networking IP.
- **Competition.** Broadcom сильнее и шире; NVIDIA расширяет networking; Credo/Astera атакуют connectivity niches; AMD/Intel и внутренние команды клиентов тоже участвуют.
- **GAAP/non-GAAP gap и SBC.** Если рост прибыли держится в основном на non-GAAP adjustments, а SBC/M&A продолжают размывать акционеров, FCF per share может отставать от нарратива.
- **Cyclicality is delayed, not dead.** Долгосрочные customer agreements могут сгладить цикл, но не отменяют риск переноса заказов, пересмотра capex и юридических escape clauses при слабой монетизации AI.
- **AI capex cycle.** Если hyperscaler capex замедлится, Marvell может пострадать одновременно по custom silicon, optics и networking.
- **Supply chain.** Fabless-модель зависит от TSMC, advanced packaging, optics supply chain и общей semiconductor-инфраструктуры.
- **M&A integration.** Celestial AI, XConn, Polariton должны доказать коммерческую отдачу.
- **Valuation risk.** Акция может быть права по бизнесу, но дорогой по цене, если рынок уже заложил почти идеальный рост.
- **Macro/geopolitics.** Видео отдельно отмечало риски supply chain от oil shock / Strait of Hormuz / Middle East; это не тезис по Marvell, но фактор для semiconductor chain.

## Что меняет решение

Повысить статус до `keep / candidate to add`, если:

- revenue growth сопровождается ростом FCF per share;
- gross margin удерживается или растет несмотря на custom silicon mix;
- появляется больше доказательств, что Marvell имеет pricing power, а не только engineering work-for-hire;
- customer base расширяется за пределы 1-2 крупных hyperscaler programs;
- рынок дает цену, где reverse DCF не требует 25-30% FCF CAGR на 5 лет.

Понизить статус до `reduce / avoid`, если:

- data center revenue растет, но FCF per share не растет;
- gross margin начинает устойчиво снижаться;
- появляется негатив по ключевому hyperscaler-клиенту;
- management делает дорогие M&A вместо органического operating leverage;
- цена требует сценария почти безошибочного исполнения.

## Инвестиционное действие

На текущем уровне информации: **не считать MRVL автоматической докупкой только из-за AI-инфраструктуры**.

Если позиция уже есть в портфеле, логика такая:

- держать под наблюдением как AI networking/custom silicon exposure;
- перед увеличением доли пересчитать текущую оценку и перечитать Google Sheets `Портфель`;
- не позволять позиции становиться скрытым дублем уже существующей экспозиции на AMD/NVIDIA/Broadcom/AI capex;
- при сильной переоценке или ухудшении FCF/margin рассматривать сокращение, но только после свежей проверки портфеля и рыночных данных.

Если позиции нет, логика такая:

- покупать только при понятном margin of safety;
- требовать подтверждения FCF per share;
- сравнивать не только с Broadcom, но и с ANET, ALAB, CRDO, AVGO, NVDA, TSM по критерию "кто реально забирает AI rent";
- не превращать идею "get paid to wait" через cash-secured puts в автоматическое действие: опционы требуют отдельного расчета риска, размера обеспечения и явного решения.

## Источники

- Marvell Q1 FY2027 results, 2026-05-27: https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results
- Marvell Q1 FY2027 Form 10-Q, filed 2026-05-28: https://investor.marvell.com/sec-filings/all-sec-filings/content/0001835632-26-000019/mrvl-20260502.htm
- Marvell FY2026 Form 10-K, filed 2026-03-11: https://investor.marvell.com/sec-filings/all-sec-filings/content/0001835632-26-000011/mrvl-20260131.htm
- Marvell Q1 FY2027 earnings call transcript, 2026-05-27: https://www.fool.com/earnings/call-transcripts/2026/05/27/marvell-mrvl-q1-2027-earnings-transcript/
- Marvell Q4/FY2026 results, 2026-03-05: https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results
- Marvell divestiture of Automotive Ethernet to Infineon, closed 2025-08-14: https://investor.marvell.com/news-events/press-releases/detail/88/marvell-completes-divestiture-of-automotive-ethernet-business-to-infineon-for-2-5-billion-in-all-cash-transaction
- Marvell 1.6T ZR/ZR+ pluggable and 2nm coherent DSPs, 2026-03-05: https://www.marvell.com/company/newsroom/marvell-1-6t-zr-zr-plus-pluggable-2nm-coherent-dsp-ai-interconnects.html
- NVIDIA/Marvell NVLink Fusion partnership, 2026-03-31: https://investor.marvell.com/news-events/press-releases/detail/1019/nvidia-ai-ecosystem-expands-as-marvell-joins-forces-through-nvlink-fusion
- Marvell to acquire Celestial AI, 2025-12-02: https://investor.marvell.com/news-events/press-releases/detail/1000/marvell-to-acquire-celestial-ai-accelerating-scale-up-connectivity-for-next-generation-data-centers
- Polariton acquisition, 2026-04-22: https://investor.marvell.com/news-events/press-releases/detail/1020/marvell-announces-acquisition-of-polariton-technologies-advancing-optical-performance-scaling-to-3-2t-and-beyond
- CFO transition and reaffirmed Q2 FY2027 outlook, 2026-06-11: https://investor.marvell.com/news-events/press-releases/detail/1025/marvell-announces-cfo-transition
- MRVL close price 2026-07-02, WSJ/FactSet: https://www.wsj.com/market-data/quotes/MRVL/historical-prices
- OCI MSA / optical scale-up interconnect overview, Tom's Hardware, 2026-03-12: https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-broadcom-and-nvidia-join-hyperscalers-to-define-optical-scale-up-interconnect-of-the-future-for-ai-clusters-meta-microsoft-and-openai-to-benefit-as-speeds-eventually-scale-to-3-2-tb-s
- Western Digital Q2 FY2026 results, 2026-01-29: https://investor.wdc.com/news-releases/news-release-details/western-digital-reports-fiscal-second-quarter-2026-financial
- Seagate Q3 FY2026 results, 2026-04-28: https://investors.seagate.com/news/news-details/2026/Seagate-Technology-Reports-Fiscal-Third-Quarter-2026-Financial-Results/default.aspx
- Seagate Q3 FY2026 earnings transcript, Motley Fool, 2026-04-28: https://www.fool.com/earnings/call-transcripts/2026/04/28/seagate-stx-q3-2026-earnings-transcript/
- Amazon Q1 2026 results: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx
- Microsoft FY2026 Q3 earnings call: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3
- Alphabet Q1 2026 earnings call: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx
- Meta Q1 2026 results: https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx
- Oracle Q4/FY2026 results: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/default.aspx
- Видеотранскрипт пользователя: `/Users/aleksejnalbantov/.codex/attachments/9cf7b95d-3f7b-4046-8b91-aa4f3a7ffb9e/pasted-text.txt`
- Видеотранскрипт Rick Orford от 2026-06-06: `/Users/aleksejnalbantov/.codex/attachments/a3d6a0b9-1f41-4d59-88fd-acc6833e077e/pasted-text.txt`
- Видеотранскрипт Parkev Tatevosian / Motley Fool и пересказ комментариев, конец июня 2026: `/Users/aleksejnalbantov/.codex/attachments/45b2a554-b4ed-436f-b850-5c671220fa4c/pasted-text.txt`
- Старый экспорт Google Docs по Marvell: `AI/Анализ инвестиционной привлекательности Marvell Technology - Google Документы.mhtml`
- Локальный AI universe: `AI/AI_BOOM_UNIVERSE.md`
