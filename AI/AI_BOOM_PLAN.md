# План: поиск конкретных акций — бенефициаров бума ИИ

- Обновлено: 2026-06-23
- Цель: **найти 2-4 конкретные акции для покупки** среди бенефициаров бума ИИ (не «понять сектор»).
- Статус: методология зафиксирована (с правкой от Codex). Следующий шаг — Фаза 1 (Universe-таблица).
- Связанные файлы: [AI_Research_2026.md](AI_Research_2026.md) (раздел 7 «кто выигрывает»), [README.md](README.md) (корзина AI Infrastructure + sector_score), [SECTOR_PIPELINE.md](../SECTOR_PIPELINE.md).

## Принцип

Воронка сверху вниз: каждая фаза **сужает список имён**. Компанию открываем на глубокий разбор только в самом конце — когда уже известно, *почему именно она*. По-компанийный анализ с самого начала — ошибка (имён десятки, критерия отбора ещё нет).

**Ключевая правка (Codex):** оценка (`sector_score`) — НЕ первый фильтр. Сначала доказываем, что у компании есть *право на сверхнормальную прибыль от ИИ* (дефицитный ресурс / pricing power / рост без бесконечного выпуска акций и долга). Иначе `sector_score` ранжирует смесь победителей, поставщиков второго порядка и value-trap'ов и даёт ложный сигнал.

## Воронка (исправленный порядок)

| # | Фаза | Что делает | Выхлоп |
|---|---|---|---|
| 1 | **Universe с тегами** | 5 корзин «по праву на ренту» (ниже), сразу с колонками: AI-exposure (реальная, не storytelling), bottleneck-type, `rent owner? y/n` | 1 таблица |
| 2 | **Отсев слабого тезиса** | Убрать имена, где ИИ вторичен / только история | Сокращённый список |
| 3 | **Quality / Risk gate** *(до оценки)* | Колонки: pricing power, gross margin / operating leverage, FCF (генерит/жжёт), баланс (долг, maturities, потребность в equity), **концентрация клиентов**, **концентрация поставщиков** (NVIDIA-dependency, single foundry, single grid), backlog/contracted revenue quality, capex-интенсивность ($capex на $1 выручки), длина моата, EPS/revenue revisions | Прошедшие гейт |
| 4 | **Valuation как «температура»** | `sector_score` остаётся, но это **не** buy/sell. См. «Лечение 5Y-нормы» | Тип по каждому имени |
| 5 | **One-pagers → Deep-dive** | По top-10 mini one-pager (thesis / why now / valuation / key risk / what would change my mind), затем полный разбор только **2-4 финалистов** → buy / wait / pass | Вердикты |

## Лечение 5Y-нормы (главный методологический риск)

`vs own 5Y norm` ловит циклические перекосы, но ломается на структурно меняющемся бизнесе (hyper-growth ИИ): «дорого» может быть оправдано ростом TAM/маржи/ROIC, «дёшево» — ловушкой (commoditization, разводнение, замедление). 5 лет истории могут включать совсем другой бизнес.

Решение — не ломать подход, а добавить второй слой поверх `valuation_vs_history`:
- `valuation_vs_growth` — EV/Sales или EV/GP к ожидаемому росту выручки и gross profit;
- `forward_normalized` — EV/EBITDA или P/E на 2027-2028;
- `reverse DCF` — какой рост и маржа уже заложены в цену;
- `revision_score` — динамика EPS/revenue-оценок за 3-6 мес.

Итоговый вывод — не «дёшево», а **тип**:
- **cheap and improving**
- **expensive but justified**
- **cheap for a reason**
- **priced for perfection**

## Bubble-тест ≠ только P/S

Главное — **кто чей рост финансирует**. Красный флаг качества выручки: vendor/customer financing, GPU-долг, круговые сделки (NVIDIA → OpenAI → Oracle → CoreWeave), hyperscaler-обещания. Высокий P/S — лишь один из симптомов.

## Стартовые 5 корзин «по праву на ренту»

1. **Power bottleneck** — CEG, VST, TLN, GEV, VRT, ETN, PWR. *(наш недоразвитый энергослой; IEA: потребление электроэнергии ЦОД ~удваивается к 2030, ИИ — ключевой драйвер. Риск: FERC отклонил behind-the-meter co-location Amazon-Talen → деньги в front-of-meter 20-летние PPA.)*
2. **Networking / optics** — AVGO, ANET, MRVL, CIEN, COHR. *(MRVL уже в портфеле; искать реальный рост Ethernet/optics/custom silicon, не hype.)*
3. **Memory / equipment** — MU, ASML, AMAT, LRCX, KLAC. *(отделить структурный bottleneck от обычного semi-цикла.)*
4. **Compute** — NVDA, AMD, AVGO. *(оценка почти всегда «дорого» → обязателен reverse-DCF.)*
5. **Cloud / DC-операторы** — ORCL, MSFT, AMZN, GOOGL, CoreWeave-типы. *(самый жёсткий bubble-тест: долг, концентрация клиентов, circular capex, contract quality.)*

## Порядок действий (чек-лист)

1. [ ] Собрать Universe-таблицу: 5 корзин × колонки Фазы 1+3 (rent/quality), без прогона оценки.
2. [ ] Отсеять слабый/вторичный AI-тезис.
3. [ ] Прогнать Quality/Risk gate.
4. [ ] Только после этого применить `sector_score` (+ второй слой оценки).
5. [ ] One-pager по top-10.
6. [ ] Deep-dive по 2-4 финалистам → buy/wait/pass.

## Контекст-источники

- Энергослой и риск FERC — см. свежий ресёрч в истории (Meta-нуклеар-сделки, GE Vernova бэклог $163 млрд, турбинные слоты до 2030).
- Движок оценки — `scripts/update_all.py`, `scripts/compute_sector_scores.py`.
