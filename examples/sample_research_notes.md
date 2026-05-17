# Sample Research Notes (Illustrative)

> **Note:** These notes are fictional and illustrative. They are written to demonstrate the kind of input a research-support analyst might bring to an AI-assisted review. They do not describe a real macroeconomic episode and should not be used for analysis.

## Context

I am reviewing a small monthly monitoring panel that mixes U.S. macro indicators, trade flows, and a few commodity and FX series. The goal is an internal monitoring dashboard, not a forecast. The notes below capture my first read of the data and a few things I want a reviewer (human or AI-assisted) to check before I extend the workflow.

## Observations (illustrative)

1. **Trade balance**
   - `exports` and `imports` look directionally reasonable over the sample, but I have not confirmed the seasonal-adjustment method.
   - `net_exports` is constructed as `exports - imports`. I need to confirm the sign convention used in the downstream dashboard.

2. **Real activity**
   - `real_gdp` is quarterly while almost everything else is monthly. The current script aligns them by forward-filling the quarterly value across the three months. This is a modeling choice and should be flagged.
   - `industrial_production` and `unemployment_rate` move broadly together in the expected direction across the illustrative sample, but I have not run any formal check.

3. **Prices**
   - `cpi` base year is not documented. Any year-over-year calculation downstream needs to confirm the base year before publication.

4. **Commodities and FX**
   - `wti_crude_oil` and `trade_weighted_usd_index` are daily. The current workflow takes a simple monthly mean. Whether this is the right aggregation depends on what the dashboard is meant to show (end-of-month snapshot vs. average level).
   - There appears to be a multi-month period where `wti_crude_oil` is unusually low. I would not interpret this as causal of anything downstream without further checks.

5. **Policy rate**
   - `fed_funds_rate` is daily and aggregated to monthly mean. The aggregation rule should be documented.

## Things I want a reviewer to verify

- Sign convention and units for `net_exports`.
- Base years for `cpi`, `industrial_production`, and `trade_weighted_usd_index`.
- Seasonal-adjustment method for `exports` and `imports`.
- Aggregation rule from daily to monthly for `wti_crude_oil`, `fed_funds_rate`, and `trade_weighted_usd_index`.
- Whether quarterly-to-monthly alignment of `real_gdp` should be forward-fill, interpolation, or kept quarterly.
- Whether any wording in the eventual brief implies causality that the data does not support.

## Reminder

These are illustrative notes. They do not describe a real episode and should not be cited.
