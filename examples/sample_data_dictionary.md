# Sample Data Dictionary (Illustrative)

> **Note:** This data dictionary is fictional and illustrative. It is not based on a live data feed and should not be used for analysis. It exists only to demonstrate how the prompt templates in this repository would be applied to a realistic macro/trade workflow.

## Workflow context

- **Workflow name:** `macro-trade-commodity-monitor` (illustrative)
- **Purpose:** Track a small set of monthly U.S. macro, trade, and commodity indicators for an internal monitoring dashboard.
- **Frequency of refresh:** Monthly, with weekly checks on the daily series.
- **Notional source mix:** Public statistical releases (illustrative — not a live pull).

## Variables

| Variable                  | Type    | Frequency | Units                          | Source (illustrative)               | Notes                                                                 |
|---------------------------|---------|-----------|--------------------------------|--------------------------------------|-----------------------------------------------------------------------|
| `date`                    | date    | monthly   | YYYY-MM-DD (first of month)    | constructed                          | Aligned to month-start for all monthly series.                        |
| `exports`                 | numeric | monthly   | USD billions, nominal          | national statistics agency (illustr.) | Goods and services, seasonally adjusted.                              |
| `imports`                 | numeric | monthly   | USD billions, nominal          | national statistics agency (illustr.) | Goods and services, seasonally adjusted.                              |
| `net_exports`             | numeric | monthly   | USD billions, nominal          | derived                              | `net_exports = exports - imports`. Confirm sign convention.           |
| `real_gdp`                | numeric | quarterly | chained USD billions, SAAR     | national accounts (illustrative)     | Quarterly series; must be aligned with monthly series before merging. |
| `unemployment_rate`       | numeric | monthly   | percent                        | labor statistics (illustrative)      | Seasonally adjusted, civilian, 16+.                                   |
| `cpi`                     | numeric | monthly   | index, base year TBD           | price statistics (illustrative)      | All items. Base year must be confirmed.                               |
| `industrial_production`   | numeric | monthly   | index, base year TBD           | central bank stats (illustrative)    | Seasonally adjusted.                                                  |
| `wti_crude_oil`           | numeric | daily     | USD per barrel                 | commodity reference (illustrative)   | Spot. Daily series; aggregate to monthly mean before merging.         |
| `fed_funds_rate`          | numeric | daily     | percent                        | central bank (illustrative)          | Effective rate. Daily; aggregate to monthly mean.                     |
| `trade_weighted_usd_index`| numeric | daily     | index, base year TBD           | central bank (illustrative)          | Broad nominal. Base year must be confirmed.                           |

## Known documentation gaps

- Base years for `cpi`, `industrial_production`, and `trade_weighted_usd_index` are not yet documented.
- Seasonal-adjustment method for `exports` and `imports` is not specified.
- Missing-value handling for the daily series on holidays is not documented.
- The aggregation rule used to convert the daily series to monthly is not stated.

## Reminder

All values, sources, and labels here are illustrative. Do not use this dictionary for downstream analysis.
