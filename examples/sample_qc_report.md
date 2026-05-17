# Sample QC Report (Illustrative AI-Assisted Output)

> **Note:** This is an illustrative AI-assisted QC report against the sample data dictionary in [examples/sample_data_dictionary.md](sample_data_dictionary.md). The findings below are produced as a draft for human review. They do not validate live data.

## Inputs reviewed

- [examples/sample_data_dictionary.md](sample_data_dictionary.md)
- [examples/sample_research_notes.md](sample_research_notes.md)

## Summary

The dictionary mixes monthly, quarterly, and daily series, with several documentation gaps and at least one derived variable whose construction should be confirmed. The QC notes below are first-pass observations and should be verified by an analyst before downstream use.

## 1. Mixed data frequencies

- `real_gdp` is quarterly; most other series are monthly.
- `wti_crude_oil`, `fed_funds_rate`, and `trade_weighted_usd_index` are daily.
- Action: confirm the alignment rule for each pair of frequencies. The research notes mention forward-fill for the quarterly series and monthly mean for the daily series; both choices should be documented in the README and held constant across runs.

## 2. Units that need clarification

- `cpi`, `industrial_production`, and `trade_weighted_usd_index` are indexed series with no documented base year.
- Action: confirm and document base years before any year-over-year or "real" calculation is published.
- `exports` and `imports` are listed as nominal USD billions; confirm whether any downstream consumer expects real values.

## 3. Missing observations

- The data dictionary does not state how holidays or non-trading days are handled in the daily series (`wti_crude_oil`, `fed_funds_rate`, `trade_weighted_usd_index`).
- Action: document the missing-value rule (skip, forward-fill, or interpolate) before aggregating to monthly.

## 4. Derived variable checks

- `net_exports = exports - imports`. The sign convention should be confirmed against what the dashboard displays.
- Action: add a unit test or a small spot check that recomputes `net_exports` for one period and compares it to the value in the panel.

## 5. Net exports calculation

- The construction of `net_exports` is simple, but the units and seasonal-adjustment status of `exports` and `imports` must match. Mixing seasonally adjusted exports with non-seasonally adjusted imports would produce a misleading net series.
- Action: confirm both inputs use the same adjustment method and are in the same units.

## 6. Causality caution on oil prices

- The research notes flag an unusually low `wti_crude_oil` period. The QC review should not interpret this as causal of any change in other series.
- Action: in any eventual brief, avoid language that implies oil price changes cause changes in trade balance, GDP, or the dollar index without a separate, documented analysis.

## 7. Documentation gaps

- Base years missing for indexed series.
- Seasonal-adjustment method missing for trade series.
- Daily-to-monthly aggregation rule missing.
- Missing-value handling for daily series missing.

## Follow-up questions for the analyst

1. What sign convention does the dashboard expect for `net_exports`?
2. What base years apply to `cpi`, `industrial_production`, and `trade_weighted_usd_index`?
3. What aggregation rule converts daily series to monthly: mean, end-of-month, or median?
4. How is `real_gdp` aligned to monthly: forward-fill, linear interpolation, or kept quarterly?
5. What is the missing-value rule for the daily series on holidays?

## Reminder

This QC report is a draft. A human reviewer must confirm each item against the original data and documentation before it is acted on.
