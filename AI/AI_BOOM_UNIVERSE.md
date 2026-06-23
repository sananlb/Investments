# AI-boom Universe — кандидаты на покупку (Фаза 1)

- Обновлено: 2026-06-24
- Назначение: единый universe бенефициаров бума ИИ с rent/quality-тегами для отбора 2-4 акций. См. методологию в [AI_BOOM_PLAN.md](AI_BOOM_PLAN.md).
- Статус: **ревизия Фазы 1 после fact-check 2026-06-23 и расширения 2026-06-24**. Проверены только материальные свежие цифры по последним кварталам/релизам и крупным контрактам; forward-мультипликаторы в этом файле считать грубыми оценками и перед сделкой перепроверять в терминале/модели.
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

---

# Quality / Risk gate — top-10 в Valuation (Фаза 3)

Прогон rent-owners через жёсткие quality/risk-критерии (pricing power, маржа, FCF, баланс, концентрация клиентов/входов, capex, моат, bubble-test). Все 12 имён из shortlist проходят базовый порог (нет круговое-финансирование-фейлов — те уже в watch/drop: CRWV, ORCL, NBIS). Поэтому gate не отсеивает «насмерть», а **ранжирует чистоту и помечает доминирующий риск**, отбирая top-10 в оценку.

| # | Ticker | Слой | Verdict | Сильная сторона качества | Доминирующий риск-флаг | Bubble/circular? |
|---|---|---|---|---|---|---|
| 1 | **NVDA** | Compute | **PASS** | GM ~75%, огромный FCF, net-cash, CUDA-моат | Длительность capex-цикла + потеря Китая | Нет |
| 2 | **TSM** | Compute | **PASS** | Foundry-монополия leading-edge, GM 67%, рента со всего слоя | Тайвань binary гео-риск; H-capex | Нет |
| 3 | **ASML** | Equipment | **PASS** | 100% EUV/High-NA монополия, net-cash, длиннейший моат | Export-controls/China; near-term WFE orders | Нет |
| 4 | **GOOGL** | Cloud | **PASS** | Search-кэш-машина + свой TPU (мин. NVDA-завис.), net-cash | ROIC на огромном capex | Нет |
| 5 | **KLAC** | Equipment | **PASS-flag** | Квази-монополия process control, GM ~60%, software-like маржа | China ~39% выручки | Нет |
| 6 | **MSFT** | Cloud | **PASS** | Софт-рента (Office/Azure lock-in), GM 69%, net-cash | Прозрачность OpenAI/Azure capex-economics | Нет |
| 7 | **ANET** | Networking | **PASS-flag** | EOS софт-lock-in, GM 62%, net-cash | **Концентрация: MSFT+Meta ~48% выручки** | Нет |
| 8 | **GEV** | Power | **PASS-flag** | Олигополия газ-турбин, слоты до 2030, net-cash | Низкая Power-маржа ~25%; execution/valuation жёсткие | Нет |
| 9 | **CEG** | Power | **PASS-flag** | Невоспроизводимый нукл. baseload, 20-летние PPA | **Левередж после Calpine** + co-location регуляторика | Нет |
| 10 | **AVGO** | Compute/Net | **PASS-flag** | Networking-монополия + sticky co-design, GM ~69% | **Закредитован (VMware)** + custom-ASIC рента делится с клиентом + конц. H | Частично (custom-ASIC завязан на capex клиентов) |
| — | VST | Power | **bench** | Нукл.+gas в дефиц. сетях, hedge-видимость | Более циклична (commodity power/hedging, gas) | Нет |
| — | AMZN | Cloud | **bench** | AWS-рента, net-cash | Retail-микс размывает AI-тезис; гигантский capex | Нет |

**В Valuation идут 10:** NVDA, TSM, ASML, GOOGL, KLAC, MSFT, ANET, GEV, CEG, AVGO.
**На скамейке (вернуть при просадке/смене веса):** VST (энергия, но циклична), AMZN (нечистый AI-тезис).
**Энергия в top-10:** GEV + CEG (2 имени) — слой сохранён, несмотря на понижение Codex.

**Что gate НЕ решает (это работа Valuation):** все 10 — отличные бизнесы, но «отличный бизнес ≠ отличная покупка». Дальше нужно отделить *cheap-and-improving* от *priced-for-perfection* через `valuation_vs_history` (sector_score) + `valuation_vs_growth` + reverse-DCF + revision-score. Только после этого — 2-4 на deep-dive.

> Для Valuation нужны свежие мультипликаторы по всем 10 + их 5Y-нормы. Локально частично есть в [README.md](README.md) (NVDA/TSM/AVGO/GOOG/MSFT/AMZN на 2026-05-30, ~3.5 нед. давности); недостают ASML, KLAC, ANET, GEV, CEG → требуется дата-пул.

---

# Quality/Risk gate — новые имена (расширение)

- Обновлено: 2026-06-24.
- Статус: точечный fact-check по 9 именам, которые доступны пользователю через Interactive Brokers. Это **не valuation** и не рекомендация к сделке: цель — понять, есть ли право на AI-ренту до расчета цены.
- Основные источники свежих данных: [SK hynix 1Q26](https://www.prnewswire.com/news-releases/sk-hynix-announces-1q26-financial-results-302750959.html), [Credo FQ4/FY26](https://investors.credosemi.com/news-events/news/news-details/2026/Credo-Technology-Group-Holding-Ltd-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Financial-Results/default.aspx) + [Credo FY26 10-K](https://www.sec.gov/Archives/edgar/data/1807794/000162828026043303/crdo-20260502.htm), [Camtek 1Q26](https://www.camtek.com/news-and-events/camtek-announces-results-for-the-first-quarter-of-2026/), [Besi 1Q26](https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q1-26-results/), [Arm FQ4/FY26 6-K](https://www.sec.gov/Archives/edgar/data/1973239/000197323926000062/exhibit992fye26q431-marx26.htm), [BWXT 1Q26](https://investors.bwxt.com/news-releases/news-release-details/bwx-technologies-reports-first-quarter-2026-results/), [Siemens Energy Q2 FY26](https://www.siemens-energy.com/us/en/home/press-releases/earnings-release-q2-fy-2026.html), [NEXTDC 1H26](https://www.nextdc.com/news/asx-release-1h26-record-results) + [May 2026 funding update](https://www.nextdc.com/news/nextdc-bolsters-liquidity-to-a8.4-billion-to-accelerate-ai-infrastructure-rollout), [GDS 1Q26](https://investors.gds-services.com/news-releases/news-release-details/gds-holdings-limited-reports-first-quarter-2026-results).

| Ticker | Слой / рынок | Fact-check свежих цифр | Баланс / концентрация / контрактность | Verdict | Сильная сторона качества | Доминирующий риск-флаг | Bubble/circular? |
|---|---|---|---|---|---|---|---|
| **000660.KS / SK Hynix** | Memory / KR | Q1'26 revenue **KRW 52.6T** (+60% QoQ, +198% YoY), operating margin **72%**; gross margin не раскрыт в релизе; рост прямо привязан к HBM, high-capacity server DRAM и eSSD для AI | Cash **KRW 54.3T**, interest-bearing debt **KRW 19.3T**, net cash **KRW 35T**; customer concentration по HBM не раскрыта; контрактность HBM н.д., но компания пишет, что спрос превышает supply capacity | **PASS-flag** | Лучший публичный чистый HBM-лидер, сильнее MU по качеству текущей AI-позиции | Memory cycle + NVDA/HBM customer concentration + капекс-ответ отрасли | N |
| **CRDO / Credo** | Networking / US | FQ4'26 revenue **$437M** (+7.4% QoQ, +157% YoY), non-GAAP GM **68.3%**; FY26 revenue **>$1.3B**, более чем утроилась; FQ1'27 guide **$465-475M**, non-GAAP GM **67-69%** | Cash/ST investments **~$1.43B**; долг материально не виден; FY26 top-10 customers **~90%** revenue, 2 customers >10%; 10-K прямо говорит, что long-term purchase commitments в основном нет | **PASS-flag** | SerDes/AEC/connectivity IP с софтверно-системной ценностью и очень высокой GM для small/mid-cap | Концентрация клиентов, cancellable orders, конкуренция Broadcom/Marvell, valuation priced-for-perfection | N |
| **CAMT / Camtek** | Equipment / US+IL | Q1'26 revenue **$121.7M** (+2.5% YoY), non-GAAP GM **51.0%**; Q2 guide **$129-131M**; менеджмент ждет 2H26 revenue **>25% выше** 1H26 на strong demand | Cash/deposits/securities **$849.7M**; Q1 OCF **$3.1M**; backlog/order momentum качественно подтвержден, но backlog value не раскрыт; customer concentration н.д. | **PASS-flag** | Узкий inspection/metrology tollgate для advanced packaging/HBM с малой базой | Lumpy equipment cycle, customer concentration н.д., Israel risk, valuation spike | N |
| **BESI.AS / Besi** | Equipment / EU | Q1'26 revenue **EUR 184.9M** (+28.3% YoY), GM **63.5%**; orders **EUR 269.7M** (+104.5% YoY), сила в hybrid bonding; Q2 guide revenue **+30-40% QoQ**, GM **64-66%** | Баланс в кратком HTML-релизе: н.д. / проверить full PDF; customer concentration н.д.; China/export-control exposure н.д., но WFE/advanced packaging equipment риск релевантен | **PASS-flag** | Hybrid bonding niche leader: более узкий bottleneck, чем broad WFE | Adoption timing hybrid bonding + WFE-cycle + valuation | N |
| **ARM / Arm Holdings ADS** | Compute IP / US ADR | FQ4'26 revenue **$1.49B** (+20% YoY), FY26 revenue **$4.92B** (+23%); non-GAAP GM **98.3%**; data-center royalty more than doubled YoY; Arm AGI CPU customer demand **>$2B** across FY27-FY28, Meta lead partner | Cash/ST investments **$3.6B**; net-cash likely, debt н.д. в quick check; FY25 top-5 customers incl. Arm China **~56%** revenue, Arm China **17%**; FY26 concentration н.д. | **PASS** | CPU/IP tollgate с почти software gross margin и royalty flywheel | Valuation, RISC-V, Arm China/governance/licensing risk, silicon strategy execution | N |
| **BWXT / BWX Technologies** | Nuclear supply chain / US | Q1'26 revenue **$860.2M** (+26% YoY), adjusted EBITDA **$148M** (~17.2% margin), FCF **$50.1M**; FY26 guide raised: adj. EBITDA **$650-665M**, FCF **$315-330M**; gross margin н.д. | Cash **$512M**, long-term debt **$2.02B**; backlog **$8.65B** (Government **$6.93B**, Commercial **$1.72B**); AI/DC mix н.д., связь с AI пока через nuclear/SMR option | **PASS-flag** | Редкая ядерная производственная база и контрактный backlog | AI-связь косвенная, government budget/customer concentration, долг выше cash | N |
| **ENR.DE / Siemens Energy** | Power: gas turbines + grid / EU | Q2 FY26 revenue **EUR 10.3B** (+8.9% comparable), orders **EUR 17.7B**, backlog **EUR 154B**, book-to-bill **1.72**; FY26 guide raised: growth **14-16%**, profit margin before special items **10-12%**, FCF pre-tax **~EUR 8B**; gross margin н.д. | Net debt/cash: н.д. / проверить в full Q2 PDF; customer concentration низкая; exact AI/DC mix н.д., но demand сильнее в Gas Services/Grid Technologies | **PASS-flag** | Non-US аналог GEV: олигополия gas turbines + grid bottleneck | Siemens Gamesa/wind execution, project risk, already repriced | N |
| **NXT.AX / NEXTDC** | Data centers / AU | 1H26 net revenue **A$189.2M** (+13%), underlying EBITDA **A$115.3M** (+9%), net loss **A$39.4M**; contracted utilisation **416.6MW** (+137%), forward order book **296.8MW** to FY29; May update: pro-forma contracted utilisation **667MW**, forward order book **544MW** | Liquidity: A$4.2B at 31.12.25; May funding lifts pro-forma liquidity to **~A$8.4B** via debt/equity/hybrids; FY25 two customers **29%** and **18%** of revenue; gross margin н.д. | **PASS-flag** | Scarce powered APAC campuses + network ecosystem, smaller base than US cloud incumbents | Heavy capex, funding/dilution, lease-up timing, tenant concentration | N |
| **GDS / GDS Holdings ADR** | Data centers / China/SEA | Q1'26 revenue **RMB 3.37B** (+23.6% YoY), but normalized ex one-time only **+7.9%**; gross margin **33.6%** / **23.9% ex one-time**; adjusted GP margin **58.0%** / **51.8% ex one-time** | Cash **RMB 14.8B**, short-term debt **RMB 9.37B**, long-term debt **RMB 36.53B**; area committed/pre-committed **725k sqm**, utilization **77.3%**, pre-commitment under construction **84.4%**; China/VIE + hyperscaler bargaining | **drop-weak** | Real Tier-1 China DC footprint and SEA/DayOne optionality | Levered China DC buildout, weak normalized organic growth, refinancing/VIE/geopolitical risk | N |

## Асимметрия новых имен

**Выше upside, чем у инкумбентов, но выше риск:** **CRDO, CAMT, BESI, NXT.AX**. Причина не в лучшем качестве, а в меньшей базе и более узком bottleneck: SerDes/AEC, HBM/advanced-packaging inspection, hybrid bonding, powered APAC campuses. Цена риска — customer concentration, lumpy orders, funding/dilution или adoption timing.

**Лучшее сочетание качества и AI-релевантности среди новых:** **SK Hynix**. Это не small-cap асимметрия, но как HBM-лидер он ближе к фактической AI-ренте, чем MU. Главный минус — это всё еще memory cycle, где текущая маржа может быть пиком, а не нормой.

**Качественный, но менее асимметричный tollgate:** **ARM**. Рента почти чистая через IP/royalty, но valuation и Arm China/RISC-V делают его кандидатом только после жесткого reverse-DCF.

**Энергослой:** **ENR.DE** выглядит ближе к GEV, чем BWXT к CEG/VST. **BWXT** интересен как nuclear supply-chain option, но AI/DC monetization пока не доказана цифрами.

**Отсев:** **GDS** не проходит gate: это не owner-rent уровня top-10, а levered China DC buildout с высокой долговой нагрузкой, нормализованной органикой <10% и VIE/geopolitical risk.

---

# Финальный объединённый shortlist

Ранжирование ниже — по **уверенности в праве на AI-ренту**, а не по цене акции. `High-asymmetry` означает не «лучше бизнес», а «больше потенциальный upside при подтверждении thesis из-за меньшей базы / более узкого bottleneck».

| # | Ticker | Слой | Тип | Market | Почему здесь | Главный риск |
|---|---|---|---|---|---|---|
| 1 | **NVDA** | Compute | incumbent | US | CUDA + full-stack accelerator rent, максимальная видимость AI spend | Capex-cycle duration, China loss |
| 2 | **ASML** | Equipment | incumbent | EU | 100% EUV/High-NA monopoly, длиннейший технологический moat | Export controls / WFE timing |
| 3 | **TSM** | Foundry | incumbent | US ADR/TW | Leading-edge foundry tollgate для всего AI compute | Taiwan binary risk, capex intensity |
| 4 | **KLAC** | Equipment | incumbent | US | Process-control quasi-monopoly, software-like margins | China exposure |
| 5 | **ARM** | Compute IP | high-asymmetry / IP tollgate | US ADR | 98% GM royalty/IP tollgate; AI data-center CPU demand только начинает раскрываться | Valuation, RISC-V, Arm China |
| 6 | **GOOGL** | Cloud/TPU | incumbent | US | Search cash engine + TPU stack снижает зависимость от NVDA | ROIC огромного capex |
| 7 | **MSFT** | Cloud/software | incumbent | US | Software rent + Azure distribution | OpenAI/Azure capex transparency |
| 8 | **ANET** | Networking | incumbent | US | EOS/software lock-in в AI Ethernet | MSFT+Meta concentration |
| 9 | **000660.KS / SK Hynix** | Memory/HBM | high-asymmetry | KR | HBM leader с net-cash и текущей AI-рентой | Memory cycle, NVDA/customer concentration |
| 10 | **BESI.AS** | Advanced packaging equipment | high-asymmetry | EU | Hybrid bonding bottleneck, orders +104.5% YoY | Adoption timing, WFE cycle |
| 11 | **GEV** | Power | energy-слой | US | Gas turbines/grid slots, net-cash, backlog quality | Execution/valuation |
| 12 | **ENR.DE** | Power | energy-слой | EU | Gas Services + Grid Technologies, EUR 154B backlog | Wind execution, project risk |
| 13 | **CEG** | Power/nuclear | energy-слой | US | Невоспроизводимый nuclear baseload и long PPA | Leverage after Calpine, regulation |
| 14 | **AVGO** | Compute/networking | incumbent | US | Networking + custom ASIC co-design | VMware debt, hyperscaler bargaining |
| 15 | **CRDO** | Networking/connectivity | high-asymmetry | US | SerDes/AEC bottleneck, 68% GM, revenue >3x | Top-10 customers ~90%, no firm long-term commitments |
| 16 | **CAMT** | Advanced packaging inspection | high-asymmetry | US/IL | Small-base inspection tollgate for HBM/advanced packaging | Lumpy orders, Israel/customer risk |
| 17 | **NXT.AX** | Data centers | high-asymmetry | AU | Scarce powered APAC campuses; 544MW pro-forma forward order book | Funding/dilution, lease-up, tenant concentration |
| 18 | **BWXT** | Nuclear supply chain | energy-слой | US | Rare nuclear manufacturing base + $8.65B backlog | AI-link indirect, government concentration, debt |

**Первые новые кандидаты на deep-dive:** **SK Hynix, BESI, CRDO, CAMT**.

- **SK Hynix** — проверять как core HBM candidate против MU/TSM/NVDA chain: контрактность HBM4/HBM4E, долю NVIDIA, durability 72% operating margin.
- **BESI** — проверять, не является ли hybrid bonding следующим узким местом advanced packaging с рентой выше broad WFE.
- **CRDO** — проверять design-win quality и customer concentration: upside выше ANET/MRVL, но thesis может сломаться одним hyperscaler order cut.
- **CAMT** — проверять, насколько 2H26 acceleration подтвержден заказами, а не только pipeline; это high-beta вариант на HBM/advanced packaging inspection.

**NXT.AX** — отдельный deep-dive только если нужен APAC data-center/power слой. **ARM** — не первый deep-dive, потому что право на ренту очевидно; вопрос почти полностью в valuation/reverse-DCF. **GDS** не включать в shortlist без экстремально дешевой оценки и отдельной China/debt risk-premium модели.

---

# Расширение: мелкие и неамериканские кандидаты (raw, до gate)

- Обновлено: 2026-06-24.
- Статус: **СЫРОЙ список, не прошёл полный fact-check / quality-gate / valuation**. Часть имен уже перенесена в gate выше: 000660.KS, CRDO, CAMT, BESI.AS, ARM, BWXT, ENR.DE, NXT.AX, GDS. Остальные строки остаются raw.
- Метод: тот же rent-owner-тест — компания должна владеть дефицитным ресурсом звена или иметь шанс на сверхнормальную прибыль. Если тезис больше похож на commodity/storytelling, это помечено прямо.
- Точечная проверка листинга/бизнеса сделана экономно: Siemens Energy data centers / IR, Hammond Power data centers, Alchip, SK hynix, Applied Materials-Besi hybrid bonding, Camtek investors, Keppel DC REIT, IREN, а также Yahoo Finance / биржевые страницы по тикерам. Мультипликаторы, текущие цены и свежие квартальные цифры **не проверялись**.

## Корзина 1 — Power bottleneck

В power-слое чистых small-cap rent owners мало: большинство маленьких имён — это pre-revenue SMR, fuel-cell или battery stories. В таблицу попали только те, у кого есть физический дефицитный ресурс: турбины, nuclear manufacturing, transformers, grid/power equipment.

| Ticker / биржа / страна | Звено | Дефицитный ресурс | Rent owner? | Ключевой риск | Предв. тег | Тип |
|---|---|---|---|---|---|---|
| **ENR.DE / Xetra / Германия** | Power: turbines + grid | Gas turbines, HVDC/grid equipment, service backlog | **Y/partial — турбины+grid slots scarce** | Execution в wind, уже сильная переоценка, project risk | **keep** | non-US |
| **7011.T / Tokyo / Япония** | Power: gas turbines + nuclear | Large gas turbines, nuclear engineering, power plants | **Y — олигополия больших турбин** | Длинные циклы заказов, project execution, FX | **keep/watch** | non-US |
| **BWXT / NYSE / США** | Power: nuclear supply chain | Nuclear components, fuel/services, reactor manufacturing know-how | **Y/partial — ядерная производственная база** | Зависимость от government contracts, SMR timing slow | **watch** | small/mid-cap |
| **HPS.A.TO / TSX / Канада** | Power: transformers | Dry-type / distribution transformers for electrification and DCs | **N/partial — дефицитно, но копируемо** | Нормализация transformer-маржи, capacity cycle | **watch** | small/mid-cap; non-US |

**Сырые выводы:** ENR.DE и 7011.T — наиболее близкие non-US аналоги GEV по дефициту больших турбин/grid, но уже не дешёвые «неоткрытые» истории. BWXT интереснее как асимметрия: если nuclear/SMR переходит из опциональности в реальные DC PPA, operating leverage выше, чем у CEG/GEV; пока это `watch`, потому что AI-связь косвенная. HPS.A.TO — хороший transformer bottleneck, но rent слабее: это скорее supply-chain shortage, чем технологическая монополия.

## Корзина 2 — Networking / optics

Здесь много commodity optical-module поставщиков. Rent-owner-тест проходят только те, у кого есть SerDes/DSP/IP, масштаб 800G/1.6T или доказанная скорость ramp у гиперскейлеров.

| Ticker / биржа / страна | Звено | Дефицитный ресурс | Rent owner? | Ключевой риск | Предв. тег | Тип |
|---|---|---|---|---|---|---|
| **CRDO / Nasdaq / США** | Networking: high-speed connectivity | SerDes/DSP, active electrical cables, AI-cluster connectivity | **Y/partial — SerDes IP + design wins** | Customer concentration, конкуренция Broadcom/Marvell, valuation | **keep** | small/mid-cap |
| **LITE / Nasdaq / США** | Optics: lasers/components | Lasers / photonic components for high-speed optics | **N/partial — лазеры нужны, рента спорна** | Telecom cycle, debt, price pressure, China exposure | **watch** | small/mid-cap |
| **300308.SZ / Shenzhen / Китай** | Optics: transceivers | Scale in 800G/1.6T optical modules | **Y/partial — масштаб, но price pressure** | Export controls, China listing risk, ASP compression | **keep/watch** | non-US |
| **300502.SZ / Shenzhen / Китай** | Optics: transceivers | High-speed optical modules for AI/data centers | **partial — быстрый optical-module ramp** | Конкуренция модулей, customer concentration, China risk | **watch** | non-US |

**Сырые выводы:** CRDO — самый чистый small/mid-cap кандидат в этой корзине: если AEC/SerDes становится новым узким местом AI-scale networking, upside выше, чем у ANET/MRVL, потому что база меньше. Китайские 300308/300502 дают non-US доступ к тому же 800G/1.6T дефициту, но рента менее чистая: optical modules быстро превращаются в ценовую войну. LITE оставить как `watch`, не как rent-owner.

## Корзина 3 — Memory / equipment

Здесь лучшие новые кандидаты не small-cap, а non-US владельцы технологической ренты вокруг HBM и advanced packaging. Это ближе к качеству ASML/KLAC, чем к commodity memory beta.

| Ticker / биржа / страна | Звено | Дефицитный ресурс | Rent owner? | Ключевой риск | Предв. тег | Тип |
|---|---|---|---|---|---|---|
| **000660.KS / Korea Exchange / Корея** | Memory: HBM | HBM leadership, packaging/process know-how, NVIDIA qualification | **Y/partial — HBM лидер, но цикл** | Memory cycle, NVDA/customer concentration, capex response | **keep** | non-US |
| **BESI.AS / Euronext Amsterdam / Нидерланды** | Equipment: advanced packaging | Hybrid bonding / die attach equipment | **Y/partial — hybrid bonding niche leader** | Adoption timing, cyclic WFE, high valuation | **keep** | non-US |
| **ASM.AS / Euronext Amsterdam / Нидерланды** | Equipment: ALD/epi | Atomic layer deposition / materials precision for advanced nodes | **Y — ALD process leadership** | WFE cycle, China/export controls, order timing | **keep** | non-US |
| **CAMT / Nasdaq+TASE / Израиль** | Equipment: inspection | Inspection/metrology for advanced packaging and HBM | **Y/partial — inspection niche, high beta** | Customer concentration, Israel risk, valuation spike | **keep/watch** | small/mid-cap; non-US |

**Сырые выводы:** SK Hynix — очевидный пропуск текущего файла: как HBM-лидер он ближе к реальному rent owner, чем MU, хотя цикличность памяти никуда не исчезает. BESI и CAMT дают более высокую асимметрию, чем ASML/KLAC: меньше база и более узкий advanced-packaging bottleneck, но выше риск timing/valuation. ASM.AS — качественный non-US кандидат, но, вероятно, с меньшей асимметрией, чем BESI/CAMT.

## Корзина 4 — Compute / silicon

В compute small-cap публичных чистых winners почти нет: лучшие частные или уже в NVDA/AVGO/TSM ecosystem. Смысл поиска — найти tollgate/IP или design-service узкие места для custom ASIC и sovereign/non-US compute.

| Ticker / биржа / страна | Звено | Дефицитный ресурс | Rent owner? | Ключевой риск | Предв. тег | Тип |
|---|---|---|---|---|---|---|
| **ARM / Nasdaq / UK/Japan** | Compute: IP | CPU/IP licensing tollgate for AI servers and custom SoCs | **Y — CPU/IP licensing tollgate** | Valuation, RISC-V, China licensing risk | **keep** | non-US |
| **3661.TW / TWSE / Тайвань** | Compute: custom ASIC | Advanced-node ASIC design + TSMC proximity | **Y/partial — TSMC-linked ASIC capacity** | Customer concentration, export controls, lumpy programs | **keep/watch** | non-US |
| **6526.T / Tokyo / Япония** | Compute: custom SoC | ASIC/SoC design services for high-end compute | **partial — ASIC capacity, less moat** | Project lumpiness, customer mix, margin volatility | **watch** | non-US |
| **688256.SS / Shanghai STAR / Китай** | Compute: AI accelerator | Domestic Chinese AI accelerator supply under sanctions | **N/partial — China scarcity, weak ecosystem** | Sanctions, CUDA gap, valuation, profitability | **watch/drop-weak** | non-US |

**Сырые выводы:** ARM — чистый tollgate, но уже большой и дорогой. На асимметрию интереснее Alchip (3661.TW): если custom ASIC забирает часть роста у NVDA/AVGO, маленькая дизайн-платформа с TSMC proximity может дать больший upside. Socionext похож, но rent слабее. Cambricon — не quality-rent, а China-policy option: высокий upside возможен, но это `watch/drop-weak` до проверки экономики и software moat.

## Корзина 5 — Cloud / data-center operators

У небольших DC-операторов главный риск — они не владельцы ренты, а levered buildout stories. Настоящая рента возникает только если компания владеет редкой площадкой с power, разрешениями, network ecosystem и кредитоспособными клиентами.

| Ticker / биржа / страна | Звено | Дефицитный ресурс | Rent owner? | Ключевой риск | Предв. тег | Тип |
|---|---|---|---|---|---|---|
| **NXT.AX / ASX / Австралия** | Data centers: colocation | Scarce powered campuses + network ecosystem in APAC | **Y/partial — scarce powered APAC campuses** | High capex, funding cost, lease-up risk | **keep/watch** | non-US |
| **9698.HK / HKEX; GDS / Nasdaq / Китай** | Data centers: China/SEA | Tier-1 China sites + Southeast Asia expansion | **partial — Tier-1 sites, leverage heavy** | China risk, debt, utilization, hyperscaler bargaining | **watch** | non-US |
| **AJBU.SI / SGX / Сингапур** | Data-center REIT | Pure-play DC real estate portfolio in Asia/Europe | **N/partial — assets scarce, REIT capped** | Rates, tenant concentration, limited growth without issuance | **watch** | non-US |
| **IREN / Nasdaq / Australia/US sites** | AI DC / power sites | Secured power, land, owned data-center sites | **N/partial — secured power, execution unproved** | Bitcoin legacy, financing, customer concentration, GPU debt | **watch** | small/mid-cap |

**Сырые выводы:** NXT.AX — самый чистый non-US DC-кандидат: power/campus scarcity в Австралии/APAC может быть реальной локальной рентой. IREN даёт самую высокую асимметрию, но rent слабый: пока это pivot из bitcoin/power-site owner в AI infrastructure, а не доказанный cloud rent owner. GDS и Keppel DC REIT — полезны для карты non-US DC слоя, но не выглядят сильнее top-10 без дешёвой оценки.

## Самые интересные новые имена по асимметрии

1. **CRDO** — small/mid-cap bottleneck в SerDes/AEC для AI networking; база намного меньше ANET/MRVL, поэтому upside выше при подтверждении design wins.
2. **3661.TW / Alchip** — чистый рычаг на custom ASIC вне NVDA; если hyperscalers ускоряют собственные XPUs, маленькая ASIC-design платформа может расти быстрее AVGO.
3. **CAMT** — inspection для HBM/advanced packaging; маленький поставщик на физическом bottleneck, потенциально выше asymmetry, чем у KLAC, но выше customer/valuation risk.
4. **BESI.AS** — опцион на hybrid bonding как следующий packaging bottleneck; более узкий и высокобета-инструмент, чем ASML/AMAT/LRCX.
5. **IREN** — самый высокий upside, но самый слабый rent-quality: power-secured AI DC pivot может переоцениться резко, однако это финансируемая buildout story, не доказанный rent owner.

**Предварительный next-step:** в fact-check/quality-gate первыми проверить **CRDO, Alchip, CAMT, BESI, SK Hynix, NXT.AX, BWXT**. IREN держать отдельно как high-risk asymmetric option, а не как core candidate.

---

# Valuation-скрин (Фаза 4) — цена, не качество

- Обновлено: 2026-06-24. Прогнан весь shortlist из 18 (3 саб-агента, данные StockAnalysis/Yahoo, ~24.06.2026).
- Все 18 УЖЕ прошли rent/quality-gate. Здесь отделяем «отличный бизнес» от «отличной ПОКУПКИ»: сравнение с собственной 5Y-нормой + рост + forward + reverse-DCF → ОДИН ТИП.
- Мультипликаторы и 2027E — частью оценки агентов, перед сделкой перепроверять в терминале. Где данные ненадёжны — помечено.

**Ключевой вывод: valuation переворачивает рейтинг по «качеству».** Рынок в 2026 распродал мегакап-AI на страхах перед capex, а энергослой и мелкие имена разогнал. В итоге **самые дешёвые к своей истории — крупнейшие «очевидные» имена**, а любимый энергослой — преимущественно priced-for-perfection.

| Ticker | ТИП оценки | Fwd P/E | vs своя 5Y-норма | Рост выр. | Вердикт по цене |
|---|---|---|---|---|---|
| **NVDA** | 🟢 cheap-and-improving | ~21 | дешевле ~55-60% | +71% | Лучший risk/reward: дёшево к истории И к росту, revisions вверх |
| **MSFT** | 🟢 cheap-and-improving | ~20 | дешевле ~30-35% | +18% | Редкий случай MSFT ниже своей нормы — качество за норм. цену |
| **CRDO** | 🟢 cheap-and-improving* | ~44 (fwd '27 ~25-30) | дешевле своей корот. истории | +206%→+80% fwd | Дорого на TTM, дёшево на forward; ставка на исполнение +80% |
| **GOOGL** | 🟡 expensive-but-justified | ~28 | дороже ~15-25% | +22% | Самый «адекватно дорогой» мегакап |
| **TSM** | 🟡 expensive-but-justified | ~24-28 | дороже ~10-20% | +38% | Премия оправдана монополией; лучший buy&hold после NVDA |
| **ASML** | 🟡 expensive-but-justified | ~38-42 | дороже ~15-25% | +12-24% | EUV-монополия; добирать на China-просадках |
| **ENR.DE** | 🟡 expensive-but-justified | ~31 | дороже (recovery) | +14-16% | Реальный turnaround, P/FCF 23x вменяем; наименее «рентный» в энергослое |
| **ANET** | 🟡 expensive-but-justified | ~46 | ~у нормы (+5-10%) | +30-35% | Справедливо; апсайд от мультипликатора исчерпан |
| **CAMT** | 🟡 expensive-but-justified | ~30 | дороже ~55-60% | +25%+ | Качество+TAM, но вход на коррекции к ~22-24x EBITDA |
| **CEG** | 🟡→🔴 exp.-but-justified / риск | ~23 | дороже ~15-20% | +64% (M&A) | Рынок капитализирует power как ренту; ждать просадку |
| **KLAC** | 🔴 cheap-for-a-reason→perfection | ~35 | дороже ~40% к 3Y | +13% (тормозит) | Рост тормозит, мультипл на максимуме; ждать просадку |
| **SK Hynix** | 🔴 cheap-for-a-reason (cyclical trap) | ~6.7 | дешевле ~40-50% | +50% | Низкий P/E на ПИКОВОЙ марже (op 72%); не value, а ставка на цикл |
| **AVGO** | 🔴 priced-for-perfection | ~33 | дороже ~150-200% к медиане | +32% | Весь AI-custom-silicon уже в цене |
| **GEV** | 🔴 priced-for-perfection | ~56 | история <2 лет | +20-24% | Заложен безупречный margin-ramp + вечная рента |
| **BESI** | 🔴 priced-for-perfection | ~57-65 | дороже ~70-90% | дно цикла | Заложен идеальный hybrid-bonding super-cycle |
| **NXT.AX** | 🔴 priced-for-perfection | н.д. (убыток) | на верхах P/S | +14%→+26% | Pre-FCF опцион, полная конверсия backlog уже в цене |
| **ARM** | 🔴 priced-for-perfection | ~150-180 | «дорого всегда» | +23% (тормозит) | Оценка оторвана от фундамента |
| **BWXT** | 🔴 priced-for-perfection | ~44 | дороже ~70-90% | +13-18% | Самый яркий разрыв мультипл/рост в слое |

\* CRDO — cheap только с поправкой на рост (PEG ~0.35); по TTM-мультипликаторам дорогой.

**Синтез для отбора:**
- 🟢 **Дёшево + качество есть:** NVDA, MSFT (оба мегакапы, дешевле своей истории), CRDO (growth-adjusted, выше риск).
- 🟡 **Разумно, держать/добирать на коррекции:** GOOGL, TSM, ASML, ENR.DE.
- 🔴 **Хороший бизнес, но цена без margin of safety → ждать просадку:** энергослой (GEV, CEG, BWXT), AVGO, ARM, BESI, NXT.AX, KLAC.
- ⚠️ **Ловушка:** SK Hynix — оптически дёшев, но это peak-earnings P/E памяти; не покупать «как value».

## Финалисты на deep-dive (Фаза 5)

Пересечение (rent owner) ∩ (cheap/разумно) ∩ (переживает bubble-тест):

1. **NVDA** — топ-рента + cheap-and-improving. Главный кандидат.
2. **MSFT** — сильная рента + cheap-and-improving. Самый «безопасный» вход.
3. **GOOGL** или **TSM** — сильная рента, разумная цена (third core).
4. **CRDO** — high-asymmetry опцион (cheap-on-forward), но с риском концентрации/исполнения.

> Энергослой (любимый GEV/CEG) сознательно НЕ в финалистах: тезис верный, но цена уже его отражает — держать в watch-листе на просадку 15-25%.
