# Energy

Нефть, газ, integrated majors, E&P, oilfield services and energy infrastructure.

## Секторная карта

Обновлено: 2026-05-31.

### Что это за сектор

Energy - это несколько разных бизнес-моделей внутри одного commodity-cycle:

| Подсектор | Примеры | Главный драйвер |
|---|---|---|
| Integrated majors | `XOM`, `CVX`, `SHEL`, `TTE` | Oil/gas price, refining margins, LNG, capital discipline, buybacks |
| E&P | `COP`, `EOG` | Oil/gas production, lifting cost, shale productivity, reserve life |
| Oilfield services | `SLB` | Upstream capex cycle, rig activity, international drilling, technology/services pricing |

Главная особенность сектора: прибыль может резко меняться из-за цены нефти и газа. Поэтому низкий P/E на пике commodity-cycle не всегда означает дешевизну, а высокий P/E на дне цикла не всегда означает дороговизну.

### Данные для sector_score графика

Для первой версии графика использована выбранная energy-корзина: `XOM`, `CVX`, `COP`, `EOG`, `SHEL`, `TTE`, `SLB`. Текущие мультипликаторы сравниваются со средним значением FY2021-FY2025 по StockAnalysis.

Стартовые веса для пилота:

```text
Energy sector_score =
0.35 x EV/EBITDA coefficient
+ 0.30 x P/FCF coefficient
+ 0.20 x P/E coefficient
+ 0.15 x P/B coefficient
```

Итоговые компоненты на якорную дату 2026-05-30 (фактическое закрытие 2026-05-29):

| Метрика | Коэффициент |
|---|---:|
| EV/EBITDA | `1.371` |
| P/FCF | `1.791` |
| P/E | `1.567` |
| P/B | `1.102` |
| Итоговый sector_score | `1.50` |

Декадная динамика в `sector_valuation_dashboard.html` строится по последним 10 якорным датам: 10-е, 20-е, 30-е / конец месяца. Если якорная дата не торговая, используется закрытие последнего торгового дня до нее. Компоненты между полными фундаментальными обновлениями масштабируются по закрытию `XLE`, потому что за несколько торговых дней фундаментальные значения почти не меняются.

Ограничение: это пилотная valuation-only модель. Следующий шаг - добавить commodity price adjustment по нефти/газу, reserve life / production cost и debt discipline, чтобы отличать дорогой сектор от сектора с реально сильным commodity backdrop.

Карта источников для быстрого обновления:

| Что | Источник |
|---|---|
| ETF-proxy | [StockAnalysis: XLE history](https://stockanalysis.com/etf/xle/history/) |
| `XOM` ratios | [StockAnalysis: XOM financial ratios](https://stockanalysis.com/stocks/xom/financials/ratios/) |
| `CVX` ratios | [StockAnalysis: CVX financial ratios](https://stockanalysis.com/stocks/cvx/financials/ratios/) |
| `COP` ratios | [StockAnalysis: COP financial ratios](https://stockanalysis.com/stocks/cop/financials/ratios/) |
| `EOG` ratios | [StockAnalysis: EOG financial ratios](https://stockanalysis.com/stocks/eog/financials/ratios/) |
| `SHEL` ratios | [StockAnalysis: SHEL financial ratios](https://stockanalysis.com/stocks/shel/financials/ratios/) |
| `TTE` ratios | [StockAnalysis: TTE financial ratios](https://stockanalysis.com/stocks/tte/financials/ratios/) |
| `SLB` ratios | [StockAnalysis: SLB financial ratios](https://stockanalysis.com/stocks/slb/financials/ratios/) |

Как быстро обновлять:

1. Открыть ratios-страницы корзины `XOM`, `CVX`, `COP`, `EOG`, `SHEL`, `TTE`, `SLB`.
2. Взять текущие `EV/EBITDA`, `P/FCF`, `P/E`, `P/B`.
3. Сравнить каждую метрику со средним FY2021-FY2025.
4. Посчитать weighted score по весам выше.
5. Для якорных дат масштабировать компоненты по закрытию `XLE` на последний торговый день до якоря.
6. В финальной версии добавить отдельный commodity adjustment по oil/gas price и quality adjustment по reserve life / production cost.

## Ключевые компании

- [XOM](XOM.md) - Exxon Mobil: largest US integrated oil major.
- [CVX](CVX.md) - Chevron: US integrated oil major.
- [COP](COP.md) - ConocoPhillips: large E&P company.
- [SHEL](SHEL.md) - Shell: global integrated energy major.
- [TTE](TTE.md) - TotalEnergies: global integrated energy and LNG.
- [SLB](SLB.md) - SLB: oilfield services leader.
- [EOG](EOG.md) - EOG Resources: US shale E&P benchmark.

## Компании и инструменты

- [COP](COP.md)
- [CVX](CVX.md)
- [EOG](EOG.md)
- [SHEL](SHEL.md)
- [SLB](SLB.md)
- [TTE](TTE.md)
- [XOM](XOM.md)
