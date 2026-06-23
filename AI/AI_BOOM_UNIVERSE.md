# AI-boom Universe — кандидаты на покупку (Фаза 1)

- Обновлено: 2026-06-23
- Назначение: единый universe бенефициаров бума ИИ с rent/quality-тегами для отбора 2-4 акций. См. методологию в [AI_BOOM_PLAN.md](AI_BOOM_PLAN.md).
- Статус: **ревизия Фазы 1 после fact-check 2026-06-23**. Проверены только материальные свежие цифры по последним кварталам/релизам и крупным контрактам; forward-мультипликаторы в этом файле считать грубыми оценками и перед сделкой перепроверять в терминале/модели.
- Главный фильтр на этом этапе — НЕ оценка, а вопрос: «почему компания заработает СВЕРХНОРМАЛЬНУЮ прибыль от ИИ?» (rent owner Y/N).

## Как читать теги

- **Rent owner Y** — владеет невоспроизводимым дефицитным ресурсом / софт-lock-in / pricing power.
- **Rent owner N** — поставщик второго порядка, commodity, или арендатор чужого дефицита.
- **Предв. тег:** `keep` (в дальнейший скрин) / `watch` (потенциал, но риск концентрации/цикла/баланса) / `drop-weak` (тезис слабый).

**Источники точечной проверки (июнь-2026):** последние IR-релизы/презентации CEG, VST, GEV, VRT, ANET, MRVL, CIEN, ALAB, MU, ASML, AMAT, LRCX, KLAC, NVDA, AMD, AVGO, TSM, ORCL, MSFT, AMZN, GOOGL, CRWV, NBIS; по FERC/PJM — FERC fact sheet и отраслевые разборы co-location order. Не все строки таблицы являются одинаково подтвержденными: где нет подтверждения в релизе, стоит `н.д. / проверить` или явно указано `оценка`. Ключевые проверенные ссылки: [Oracle Q4 FY26](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/default.aspx), [CoreWeave Q1 2026](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/), [Micron FQ2 2026](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-second-quarter-fiscal-2026), [NVIDIA Q1 FY27](https://investor.nvidia.com/financial-info/financial-reports/default.aspx), [Broadcom Q2 FY26](https://www.broadcom.com/company/news/financial-releases/64371), [TSMC Q1 2026](https://investor.tsmc.com/english/quarterly-results/2026/q1), [GE Vernova Q1 2026](https://www.gevernova.com/news/press-releases/ge-vernova-reports-first-quarter-2026-financial), [FERC/PJM co-location fact sheet](https://www.ferc.gov/news-events/news/fact-sheet-ferc-directs-nations-largest-grid-operator-create-new-rules-embrace).

---

## Корзина 1 — Power bottleneck (энергия и оборудование для ЦОД)

| Ticker | Компания / роль | AI-exposure | Bottleneck / дефицитный ресурс | Rent owner? | Pricing power | GM ~% | FCF | Баланс | Конц. клиентов | Зависимость от входов | Backlog quality | Capex | Моат | Revisions | Тег |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CEG** | Constellation — крупнейший нукл. парк США | H — 20-летние нукл. PPA с гиперскейлерами + Calpine | Существующий нукл. baseload в PJM (нельзя быстро построить) | **Y** — владеет дефицитными работающими реакторами | H | EBITDA margin ~оценка; Q1'26 EPS вырос после Calpine | Сильный | Долг/левередж ↑ после Calpine; точный net debt проверить | M — несколько мегасделок (MSFT, Meta) | Grid/топливо; PTC-floor (IRA) защищает низ | Контракт. выпуск + 20-летние PPA — высокое | L | long | up | **keep** |
| **VST** | Vistra — ERCOT/PJM gas+nuclear парк | H — нукл./газ в ERCOT/PJM + DC PPA pipeline | Dispatchable baseload/peaker в дефиц. сетях | **Y** — нукл.+gas peakers в дефиц. сетях | H (98% hedged'26 → апсайд '27-28) | EBITDA высокий | Сильный; buyback | Закредитован, управляемо ⚠️ | M — растущая база DC | Grid/газ; цены power-зависимы | Хедж **98/89/65%** '26/'27/'28 — высокая видимость | L | med-long | up | **keep** |
| **TLN** | Talen — нукл. Susquehanna (single-asset) | H — $18B 17-летний PPA c AWS (1920 МВт) | Один крупный нукл. актив рядом с DC | **Y** — но концентрация в одном PPA | H | н/п | Генерит; мало диверсиф. | Умеренный (после банкротства) ⚠️ | H ⚠️ — фактически один клиент (AWS) | Grid; behind-the-meter заблокир. → обычный PPA | Один большой PPA — высокий, но хрупкий | L | med | up | **watch** |
| **GEV** | GE Vernova — gas-турбины + grid | H — gas/grid demand; backlog/slot reservations sharply ↑ | Слоты на gas-турбины (HA) — дефицит до ~2030 | **Y** — олигополист по большим газ.турбинам | H — price/cost positive | ~25% Power margin оценка | Генерит, растёт | **Net-cash** ✅ | L-M — диверсиф. | Цепочка турбин (она же узкое горло) | Gas Power backlog + slot reservations **100 GW** в Q1'26 | M | long | up | **keep** |
| **VRT** | Vertiv — power/thermal для ЦОД | H — Q1'26 sales +30%, liquid cooling | Liquid cooling + power при высокой плотности | **partial** — лидер, но без невоспроизводимого ресурса | M-H | GM ~н.д.; adj op margin 20.8% Q1'26 | Генерит; Q1 FCF сильный | Умеренный; делевередж | M — концентр. в гиперскейлерах ⚠️ | Завязан на NVDA/AI capex-цикл | Backlog был $15.0B на Q4'25; Q1 backlog н.д. | M | med | up | **watch** |
| **ETN** | Eaton — электрооборуд./switchgear | M-H — Electrical Americas orders +42% | Электрораспределение/switchgear (lead-times) | **N** — quality compounder, не rent owner | M | ~38% | Сильный | Умеренный, инвест-грейд ✅ | L — очень диверсиф. | Своя цепочка; меньше AI-завязки | Backlog растёт, AI — часть портфеля | M | med | up | **watch** |
| **PWR** | Quanta — EPC ЛЭП/подстанций/grid | M (storytelling-наклон) | Дефицит квалифиц. бригад для grid-build | **N** — commodity-услуга, цикличный EPC | L-M | ~15-19% | Генерит, lumpy | Умеренный; M&A-роллап | L — диверсиф. utility | Зависит от capex utilities; нет уник. ресурса | Backlog $48.5B, но низкомаржинальный | M | short-med | up | **watch** |

**Вывод:** настоящие rent owners — **CEG и VST** (невоспроизводимый dispatchable/нукл. baseload в перегруженных PJM/ERCOT; FERC/PJM co-location order от 18.12.2025 снял часть неопределенности после отказа по Talen-Amazon ISA в 2024, но тарифная механика еще не полностью доказана). **GEV** — второй bottleneck другого типа: олигополия на большие газ-турбины, слот-дефицит до конца десятилетия, net-cash; риск — уже высокая цена за execution. **VRT** понижен до `watch`: AI-рост реален, но это не владелец уникального ресурса, а качественный поставщик в конкурентной цепочке. **TLN** — реальный актив, но single-asset/single-client. **ETN/PWR** — слабее как AI-rent: диверсифицированный compounder / низкомаржинальный EPC.

**Что меняет тезис в 2026:** 1) финальные правила PJM/FERC по co-location и сколько grid charges останется у BTM/FTM-сделок; 2) новые 10-20-летние PPA с раскрытой ценой/MW и кредитным качеством покупателя; 3) конверсия GEV slot reservations в твердый backlog без ухудшения маржи.

**Ключевой риск:** рынок платит за дефицит power как за бессрочную ренту, а регулятор/сети могут забрать часть economics через тарифы, queue reforms и обязательства по надежности.

---

## Корзина 2 — Networking / optics (передача данных)

| Ticker | Компания / роль | AI-exposure | Bottleneck / дефицитный ресурс | Rent owner? | Pricing power | GM ~% | FCF | Баланс | Конц. клиентов | Зависимость от входов | Backlog quality | Capex | Моат | Revisions | Тег |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ANET** | Arista — Ethernet-свитчи для AI-кластеров | H — AI networking FY26 target ~$3.5B оценка; Q1'26 revenue +35% | EOS-софт + co-design; не commodity | **Y** — софт-lock-in + системная интеграция | H | **62.4%** Q1'26 GM | Сильный (~оценка $3-4B/год) | Net-cash, нет долга ✅ | H — MSFT+Meta всё еще ключевые; 10%+ новые клиенты могут снизить риск | Fabless TSMC + Broadcom; NVDA — конкурент | Сильный, но cloud titan mix давит GM | L | long | up | **keep** |
| **MRVL** | Marvell — custom-silicon (XPU) + optical DSP | H — DC **$1.83B / ~76%** Q1 FY27 revenue | Custom-ASIC дизайн + 800G/1.6T DSP | **partial** — DSP/IP rent есть, custom ASIC rent ограничена: IP/объем у клиента | M — custom маржа ниже, switching cost высокий | **58.9%** non-GAAP GM | Генерит; record OCF Q1 FY27 | Умеренный; долг после M&A проверить | H — несколько hyperscaler-программ ⚠️ | TSMC; NVDA partnership помогает, но усиливает dependency | Pipeline сильный, но lumpy и customer-owned | M | med | up (FY28 target/оценка $16.5B) | **watch** |
| **CIEN** | Ciena — оптич. транспорт + DCI | M→H — Q2 FY26 revenue **$1.57B +40%**, FY26 guide ~$6.3B | WaveLogic coherent DSP | **partial/N** — хороший продукт, но рынок конкурентен | M | **44.9%** adj GM Q2'26 | Генерит умеренно; Q2 FCF $219M | Умеренный, небольшой долг | M — телеком+cloud, диверсиф. | Компоненты/foundry; меньше single-vendor | Растущий backlog, но pricing power не как у ANET | M | med | up | **watch** |
| **COHR** | Coherent — трансиверы 800G/1.6T + лазеры | H — AI optics реальны, свежие цифры в этом файле не подтверждены | InP/лазеры, vertical integration | **N/partial** — вертикаль помогает, но transceiver-рынок ценовой | M | ~39-40% ⚠️ / проверить | Генерит | **Закредитован** ⚠️ долг после II-VI/Finisar | M — NVDA/hyperscalers | InP-субстраты (плюс); продаёт NVDA | Растёт, но transceiver = ценовая конкуренция | M-H | short-med | up | **drop-weak** |
| **ALAB** | Astera Labs — connectivity (PCIe/CXL retimers, Scorpio) | H — Q1'26 revenue **$308M +93% YoY** | Retimers/Scorpio в scale-up фабрике | **Y, но молодой** — высокая маржа показывает rent, длительность моата не доказана | H (пока) | **76.3%** GAAP GM Q1'26 | Прибыльна | Net-cash, IPO-кэш ✅ | H — NVIDIA-экосистема + 1-2 hyperscaler ⚠️⚠️ | NVDA/PCIe/CXL cycle; риск UALink/конкурентов | Сильный ramp, но короткая публичная история | L | med | up | **watch** (priced for perfection) |

**Вывод:** единственный чистый rent owner корзины — **ANET**: EOS/software + cloud co-design дают больше pricing power, чем обычные коробки. **MRVL** понижен до `watch`: рост data center реальный, но custom ASIC — это не полная рента, потому что крупный клиент контролирует roadmap/IP и может давить маржу или мультисорсить. **ALAB** оставлен как `watch`, не shortlist: economics отличные, но моат молодой, а valuation требует почти безошибочного Scorpio/retimer ramp. **CIEN/COHR** — AI-бенефициары, но ближе к циклической optics supply chain, не к владельцам ренты.

**Что меняет тезис в 2026:** 1) доля Ethernet vs InfiniBand в новых AI-кластерах и сможет ли ANET получить 10%+ новых cloud customers; 2) у MRVL — валовая маржа и OCF при росте custom silicon, а не только revenue; 3) у ALAB — темп Scorpio и признаки второй/третьей платформы вне NVIDIA-цикла.

**Ключевой риск:** optics/networking выглядит как bottleneck, но часть прибыли может уйти гиперскейлерам и Broadcom/NVIDIA через reference design, component pricing и customer-owned ASIC/IP.

---

## Корзина 3 — Memory / semiconductor equipment

| Ticker | Компания / роль | AI-exposure | Bottleneck / дефицитный ресурс | Rent owner? | Pricing power | GM ~% | FCF | Баланс | Конц. клиентов | Зависимость от входов | Backlog quality | Capex | Моат | Revisions | Тег |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **MU** | Micron — DRAM/NAND + HBM3E/HBM4 | H — Q2 FY26 revenue **$23.86B**, Cloud Memory $7.75B | HBM/DRAM tight supply; базовый DRAM/NAND все равно commodity | **Частично Y** — HBM tightness, но memory-рента циклическая | H сейчас, но cycle-sensitive | **74.9%** non-GAAP Q2; Q3 guide **~81%** | Генерит; Q2 adj FCF $6.9B после $5.0B capex | Кэш $16.7B; цикличность баланса ⚠️ | M — гиперскейлеры/HBM long-term | EUV/WFE; спрос через NVDA/AI capex | HBM contracts хорошие; DRAM/NAND могут быстро развернуться | H | short→med (HBM share ниже SK Hynix) | up | **watch** — не chase на пике маржи |
| **ASML** | Монополия на litho; единств. EUV/High-NA | H — без EUV нет 3/2nm и HBM-DRAM | 100% монополия EUV/High-NA | **Y** — единственный в мире | H | **53.0%** Q1'26; FY26 guide 51-53% | Сильно генерит | **Net-cash** ✅ | M — TSMC/Samsung/Intel/SK Hynix | Zeiss/supply chain; export controls | Высокое — backlog/заказы требуют проверки в свежем 20-F/IR | M-H | long — глубочайший моат | up (2026 €36-40B) | **keep** |
| **AMAT** | Applied Materials — широкий WFE + packaging | M-H — «лопаты» AI-капекса | Дифференц. WFE, но не монополия | **Частично Y** — рента в нишах (epi, implant, packaging) | M | **~50%** non-GAAP Q2'26 | Сильно генерит, байбэки | **Net-cash-ish / проверить** | M — TSMC/Samsung/Intel/память | Зависит от fab-капекса; China exposure ⚠️ | Хороший, но cycle/China-sensitive | M | med | up | **watch** — quality, но не rent shortlist |
| **LRCX** | Lam Research — etch & deposition (NAND/HBM) | M-H — etch для high-layer NAND и HBM TSV | Сильная позиция, но дублируемая (TEL, AMAT) | **Частично Y** — рента в etch для памяти | M | ~48-50% | Сильно генерит, байбэки | **Net-cash** ✅ | M-H — завязка на memory-капекс ⚠️ | Memory-цикл; China ~35% — самый высокий ⚠️ | Улучшается (adv. packaging) | M | med | up (Citi $450) | **watch** — лучший memory-leverage, но China+цикл |
| **KLAC** | KLA — монополист process control / metrology | M-H — больше узлов/HBM = больше контроля | ~50%+ доли в inspection/metrology | **Y** — доминирует в process control | H — лучший после ASML | Q4 FY26 guide **~61.8%** non-GAAP GM | Очень сильно генерит; LTM FCF ~$4.0B | Умеренный, net-cash-ish / проверить | M — диверсиф. logic+memory | Меньше memory-завис.; China exposure ⚠️ | Хороший; не нужен пик WFE для плана | L-M | med-long | up | **keep** |

**Вывод:** структурный bottleneck с длинным моатом — **ASML и KLAC**: здесь рента технологическая, а не просто cyclical shortage. **MU** исправлен: 81% GM — не storytelling, а Q3 FY26 guide после Q2 non-GAAP GM 74.9%; но именно поэтому его нельзя читать как “качественный rent owner” — это память на экстремальном циклическом пике. **AMAT/LRCX** — качественные “лопаты”, но не монополии и под China/export-control навесом; AMAT понижен до `watch`, потому что в shortlist нужны владельцы ренты, а не broad WFE beta.

**Что меняет тезис в 2026:** 1) ASML bookings/backlog по EUV/High-NA и любые новые экспортные ограничения; 2) у KLAC — удержание 60%+ GM при росте memory/HBM mix; 3) у MU — контрактность HBM4 и signs of DRAM/NAND supply response после маржинального пика.

**Ключевой риск:** инвестор покупает equipment/memory как “AI forever”, но получает классический WFE/memory cycle с China/export-control shock в момент, когда forward estimates уже на пике.

---

## Корзина 4 — Compute / silicon (чипы и foundry)

| Ticker | Компания / роль | AI-exposure | Bottleneck / дефицитный ресурс | Rent owner? | Pricing power | GM ~% | FCF | Баланс | Конц. клиентов | Зависимость от входов | Backlog quality | Capex | Моат | Revisions | Тег |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **NVDA** | NVIDIA — GPU-платформа №1 | H — Q1 FY27 revenue **$81.6B**, DC **$75.2B / 92%** | CUDA-софт + rack-системы; HBM/CoWoS лимит | **Y** — CUDA-замок + полная стек-платформа | H | **~75%** Q1 FY27 GM | Огромный FCF | Net-cash; supply dependency TSM/HBM | M — hyperscale ~50% DC, остальное AI clouds/enterprise/sovereign | TSM, HBM, CoWoS — узкое горло | Очень сильный, visibility на Blackwell/GB300; backlog не раскрыт как RPO | L | long (CUDA) | up | **keep** |
| **AMD** | AMD — GPU-челленджер (MI355/400) + EPYC | H — Q1'26 revenue **$10.3B**, non-GAAP GM 55%; DC GPU $15B'26 = оценка/проверить | Второй источник AI compute; ROCm слабее CUDA | **N/partial** — догоняющий, рента ограничена bargaining power покупателей | M (дисконт vs NVDA) | **55%** non-GAAP | Генерит умеренно | Net-cash, скромнее | M-H — рост завязан на нескольких крупных AI customers | TSM/HBM; second-source thesis | Растущий, но менее законтрактованный | L | med (x86 прочнее GPU) | up | **watch** |
| **AVGO** | Broadcom — custom ASIC (XPU) + networking | H — Q2 FY26 AI semiconductor **$10.8B +143% YoY** | switch-ASIC/networking + custom silicon co-design | **Y/partial** — networking-рента сильная; custom XPU rent делится с клиентом | H (networking), M (XPU) | ~68-70% incl. VMware / проверить | Мощный FCF | Закредитован после VMware, обслуживаемо ⚠️ | H — Google/Meta/OpenAI/Anthropic/Apple | TSM; capex гиперскейлеров | Сильный backlog/RPO, но Google-TPU/AI targets требуют проверки | L | long | up | **keep** |
| **TSM** | TSMC — foundry-бэкбон для ВСЕХ | H — Q1'26 revenue **$35.9B**, HPC/AI доля >50% / точный AI% н.д. | сам И ЕСТЬ горло: 2nm + CoWoS, leading-edge foundry | **Y** — единств. credible foundry для leading-edge scale | H (цены/slots) | **66.2%** Q1'26; Q2 guide 65.5-67.5% | Генерит, но capex высокий | Net-cash; гео-риск Тайвань ⚠️ | L-M — диверсиф., Apple/NVDA крупные | grid/энергия Тайваня; ASML/CoWoS | Очень сильный: 2nm/CoWoS capacity tight | H | long (process-монополия) | up | **keep** |

**Вывод:** **NVDA** остается самым сильным rent owner операционно: доля DC уже ~92% выручки, GM ~75%, CUDA/rack ecosystem пока монетизируется без видимого margin collapse. Но формулировку “не priced-for-perfection по forward P/E 21-23x” удалить из инвестиционного вывода: forward P/E/PEG нужно пересчитать перед сделкой на свежей цене и EPS revisions. **TSM** — более “нейтральный” сборщик ренты со всего AI silicon слоя, но с binary Taiwan/geopolitical risk и высоким capex. **AVGO** — сильный №2 после NVDA в AI silicon economics, однако custom ASIC рента менее чистая, чем кажется: customer-owned workloads/IP и multisourcing ограничивают take rate; чистая рента Broadcom сильнее в networking/switching. **AMD** — high-beta second-source option, не core rent owner.

**Что меняет тезис в 2026:** 1) NVDA DC GM/lead time при GB300 и доля non-hyperscaler спроса; 2) TSM CoWoS/2nm capacity, pricing и capex без ухудшения FCF; 3) AVGO AI semiconductor run-rate: сколько роста идет из networking vs lower-margin custom XPU.

**Ключевой риск:** hyperscaler capex budget становится единой точкой отказа: если OpenAI/Meta/Microsoft/Amazon замедляют AI factories, одновременно страдают NVDA/AMD/AVGO/TSM и downstream cloud/neocloud.

---

## Корзина 5 — Cloud / data-center operators

| Ticker | Компания / роль | AI-exposure | Bottleneck / дефицитный ресурс | Rent owner? | Pricing power | GM ~% | FCF | Баланс | Конц. клиентов | Зависимость от входов | Backlog quality | Capex | Моат | Revisions | Тег |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ORCL** | Oracle — БД + OCI, Stargate/OpenAI exposure | H — Q4 FY26 OCI IaaS +93%; RPO **$638B** | БД-франшиза + leased/financed AI DC capacity | **Частично Y** — DB-рента реальна; AI-облако пока не доказало ROIC | M (DB high, OCI lower) | ~65% total / OCI-AI ниже, проверить | **FCF -$23.7B FY26** | Capex **$55.7B FY26**; debt/equity funding ↑ ⚠️ | H — крупная часть RPO связана с OpenAI/Stargate, точная доля н.д. | NVDA + grid/power + debt markets ⚠️ | RPO огромный, но quality зависит от кредитоспособности AI customers | H (~80%+ of revenue) | DB long / OCI med | rev up, FCF/margins down | **watch** |
| **MSFT** | Microsoft — Azure + OpenAI, Copilot | H — Azure AI, OpenAI-стек | Capital + GPU-allocation; дистрибуция/инсталл-база | **Y** — софт-рента (Office/Windows/Azure lock-in) | H | Microsoft Cloud GM **66%** Q3 FY26 | Огромный, но FCF давит capex | Крепкий баланс | L — диверсиф. | NVDA + power (умеренно) | Azure bookings/RPO сильные | H; exact capex/sales проверить | long | flat→up | **keep** |
| **AMZN** | Amazon — AWS + Trainium/Anthropic | H — AWS Q1'26 op income **$14.2B**, AI demand | Capital + power; retail/AWS платформа | **Y** — AWS-рента (инфра lock-in) | H (AWS) | AWS margin strong; total GM н.д. | Генерит, FCF под давлением capex | Крепкий баланс | L | NVDA частично снят Trainium-ом (плюс) | AWS backlog растёт; $364B = оценка/проверить | H; Q1 capex ~$43B оценка | long | flat/up | **keep** |
| **GOOGL** | Alphabet — Google Cloud + TPU/Gemini | H — Google Cloud Q1'26 revenue **$20.0B +63%**, backlog >$460B | Capital + power; TPU = собственный чип | **Y** — search/ad рента + TPU/cloud | H | total GM н.д.; cloud op income sharply ↑ | Сильный, capex давит | **Net-cash**, очень крепкий | L | Наименьшая завис. от NVDA (TPU) — плюс | Cloud backlog быстро растёт | H; Q1 capex ~$35.7B оценка | long | up | **keep** |
| **CRWV** | CoreWeave — чистый GPU-cloud («neocloud») | H — Q1'26 revenue **$2.08B**, backlog **$99.4B** | GPU-доступ, но сама = commodity-арендатор | **N** — арендует чужой дефицит | L→M | низкий после D&A; adjusted metrics не заменяют FCF | **Жжёт** жёстко | **Закредитован — красный флаг**; точные maturities проверить | H критично — OpenAI + Meta; Meta new $21B commitment | NVDA-зависим тотально + power/debt markets ⚠️ | Backlog большой, качество ниже из-за customer/vendor financing risk | очень H | short | up (backlog), риск-флаг | **drop-weak** |
| **NBIS** | Nebius — AI-cloud (экс-Yandex), GPU + own DC | H — Meta/MSFT contracts, owned/leased DC capacity | GPU + power; вертикальнее CRWV | **N/partial** — больше инфраструктуры в собственности, но still renter of GPU scarcity | L→M | растёт, тонкий / проверить | **Жжёт**; funding-driven growth | Asset-backed/debt funding; softer than CRWV but dilution/debt risk | H — Meta $27B structure: $12B firm + $15B conditional/resale; MSFT amount проверить | NVDA + power ⚠️ | Качество выше CRWV по контрагентам, но economics не доказаны | очень H | short→med | up | **watch** |

**Вывод:** реальные rent owners — только мегакапы **GOOGL, MSFT, AMZN**: рента сидит в search/software/AWS-франшизах, а AI capex они могут финансировать из существующего cash engine. **GOOGL** поднят выше в корзине из-за TPU и меньшей зависимости от NVDA. **ORCL** — не чистый AI rent owner: DB-рента есть, но OCI/Stargate превращает компанию в levered AI-infrastructure financier; RPO $638B впечатляет, но качество RPO зависит от способности AI-клиентов монетизировать compute. **CRWV** понижен до `drop-weak`: backlog огромный, но economics похожи на арендаторскую модель с debt/GPU/customer concentration. **NBIS** лучше CRWV по структуре контрактов и контрагентам, но это все еще funding story, не proven rent.

**Что меняет тезис в 2026:** 1) у мегакапов — AI capex как % revenue/OCF и cloud gross margin, а не только AI bookings; 2) у ORCL — доля RPO от OpenAI/Stargate, условия финансирования и сроки ввода мощностей; 3) у CRWV/NBIS — FCF after growth capex, refinancing terms и utilization после первых крупных ramp.

**Ключевой риск:** “contracted backlog” маскирует круговое финансирование AI-capex: vendor financing + customer prepayments + GPU debt могут создать выручку без устойчивой экономической прибыли.

---

## Упорядоченный shortlist rent owners (до оценки)

Порядок по уверенности в **праве на ренту**, не по дешевизне акции:

1. **NVDA** — рента уже доказана в P&L: Q1 FY27 DC $75.2B, GM ~75%, CUDA/rack ecosystem монетизируется сейчас.
2. **TSM** — берет ренту со всего leading-edge AI silicon слоя, но ниже NVDA из-за Taiwan/geopolitical tail risk и высокого capex.
3. **ASML** — самый чистый технологический monopoly-rent, но nearer-term upside зависит от WFE orders/export controls, а не напрямую от AI revenue.
4. **KLAC** — квази-монополия process control с software-like margin profile; чуть ниже ASML из-за меньшей уникальности.
5. **GOOGL** — лучшая cloud-рента в AI по сочетанию Search cash engine + TPU; главный риск — ROIC massive capex.
6. **ANET** — сильный Ethernet/software lock-in, но customer concentration и cloud-titan mix давят уверенность.
7. **MSFT** — софт-рента мощная, но OpenAI/Azure capex economics менее прозрачны, чем у GOOGL TPU-stack.
8. **GEV** — физический bottleneck gas turbines/grid с длинным backlog, но execution/valuation уже жесткие.
9. **CEG** — nuclear baseload rent реален, но Calpine/leverage и регуляторика co-location снижают чистоту тезиса.
10. **AVGO** — отличный AI beneficiary, но custom ASIC rent делится с hyperscaler-клиентом; чистая рента сильнее в networking.
11. **VST** — power-rent сильная, но commodity power/hedging и gas exposure делают тезис более циклическим.
12. **AMZN** — AWS-рента реальна, но AI thesis менее чистый из-за retail mix и огромного capex cycle.

**Первые 2-4 кандидата на one-pager/deep-dive:** **NVDA, TSM, ASML, GOOGL**. Если нужен меньший геополитический риск Тайваня/ASML export controls, заменить один слот на **KLAC** или **ANET**.

**Watch** (потенциал при просадке/контроле риска): TLN, MRVL, ALAB, AMAT, MU, AMD, NBIS, ORCL, VRT.

**Слабый/нечистый AI-rent тезис:** ETN, PWR, COHR, CIEN, CRWV.

**Перед сделкой вручную перепроверить:** 1) forward P/E/EV/FCF на свежей цене и консенсусе; 2) customer concentration и долю OpenAI/Stargate в ORCL RPO; 3) debt maturity/refinancing у CRWV/NBIS/ORCL; 4) China/export-control revenue exposure у ASML/AMAT/LRCX/KLAC; 5) HBM share/contract terms у MU и real take-rate в AVGO/MRVL custom ASIC.

> Следующий шаг: Quality/Risk gate по top-10 → Valuation (sector_score + valuation_vs_growth + reverse DCF) → deep-dive 2-4.
