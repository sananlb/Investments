# Russia

Российский рынок: ставки ЦБ РФ, облигации, локальные акции, валютные риски и ликвидность.

## Ключевые компании

- [SBER](SBER.md) - Сбербанк: крупнейший банк и proxy на экономику РФ.
- [LKOH](LKOH.md) - Лукойл: крупная нефтяная компания.
- [GAZP](GAZP.md) - Газпром: газовый сектор и экспортный риск.
- [NVTK](NVTK.md) - Новатэк: LNG and gas growth exposure.
- [GMKN](GMKN.md) - Норникель: никель, палладий, copper.
- [YDEX](YDEX.md) - Яндекс: локальный technology/internet leader.
- [OZON](OZON.md) - Ozon: e-commerce growth.
- [TCSG](TCSG.md) - Т-Технологии: fintech/banking.

## Данные для sector_score графика

Обновлено: 2026-05-31.

В текущую версию `sector_valuation_dashboard.html` сектор `RUSSIA` не добавлен. Причина: российский рынок нельзя корректно считать той же быстрой формулой, что и US/global sectors через StockAnalysis ratios и ETF-proxy.

Для отдельной модели нужны:

- локальные мультипликаторы по MOEX/эмитентам: `P/E`, `P/B`, `EV/EBITDA`, dividend yield;
- ставка ЦБ РФ, OFZ yield curve и equity risk premium;
- валютный риск и ликвидность;
- санкционные/дивидендные ограничения;
- отдельные веса по банкам, нефти/газу, металлам и локальному tech/e-commerce.

Рабочее правило: не добавлять `RUSSIA` в общий sector_score, пока не собрана отдельная российская методика. В обзоре рынка ограничение записано в `02_MARKET_DASHBOARD.md`.

## Компании и инструменты

- [GAZP](GAZP.md)
- [GMKN](GMKN.md)
- [LKOH](LKOH.md)
- [NVTK](NVTK.md)
- [OZON](OZON.md)
- [SBER](SBER.md)
- [TCSG](TCSG.md)
- [YDEX](YDEX.md)
