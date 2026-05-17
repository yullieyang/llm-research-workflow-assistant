# Sample Research Brief Review (Illustrative AI-Assisted Output)

> **Note:** This is an illustrative AI-assisted review of a short fictional research brief. The brief and the review are both for demonstration. They do not describe a real episode and should not be cited.

## Brief under review (fictional excerpt)

> "Over the past several months, the U.S. trade deficit has widened sharply. This was driven by a stronger dollar and lower oil prices, which together reduced the value of exports. Industrial production has also weakened, suggesting that the trade picture will continue to deteriorate in the coming quarters."

## Source notes available to the reviewer

- A monthly panel containing `exports`, `imports`, `net_exports`, `industrial_production`, `wti_crude_oil`, and `trade_weighted_usd_index` (illustrative; see [sample_data_dictionary.md](sample_data_dictionary.md)).
- A note describing data coverage and known documentation gaps (see [sample_research_notes.md](sample_research_notes.md)).
- No external citations are provided.

## Review

### 1. Claim-by-claim source check

- **"The U.S. trade deficit has widened sharply."** Partially supported. The panel contains `net_exports`, but the brief does not specify the time window, the magnitude, or the comparison period. Recommend stating the exact window and magnitude.
- **"This was driven by a stronger dollar and lower oil prices."** Not supported by the source notes. The panel shows correlations among `trade_weighted_usd_index`, `wti_crude_oil`, and the trade balance, but no causal decomposition is provided.
- **"...which together reduced the value of exports."** Not supported. The brief asserts a mechanism that the panel cannot demonstrate.
- **"Industrial production has also weakened."** Possibly supported by the `industrial_production` series, but the brief does not cite a time window or a magnitude.
- **"...suggesting that the trade picture will continue to deteriorate in the coming quarters."** Forward-looking. Not supported by the source notes, which do not include a forecast model.

### 2. Facts vs. interpretation

- The brief mixes description ("trade deficit has widened") with causal interpretation ("driven by a stronger dollar and lower oil prices") in the same sentence. Recommend splitting these into two sentences: one describing the data, one offering a more cautious interpretation.

### 3. Uncertainty

- The brief uses confident language ("driven by," "will continue to deteriorate") that the available source notes do not support.
- Suggested replacements:
  - "is consistent with"
  - "appears to coincide with"
  - "without a separate decomposition, the drivers cannot be confirmed"
  - "preliminary; subject to revision"

### 4. Overstated conclusions

- The causal claim about the dollar and oil prices should be removed or softened.
- The forward-looking statement should be removed unless a forecast model is cited.

### 5. Recommended wording (illustrative)

> "Over the past several months, the U.S. trade deficit has widened. This period also saw a stronger trade-weighted dollar and lower oil prices, though the relative contribution of each is not separately identified here. Industrial production has softened over the same window. These movements are descriptive; a forward-looking assessment would require a separate model and is outside the scope of this brief."

### 6. Human-reviewer checklist

- Confirm the exact time window for each claim.
- Confirm the magnitude of the change in `net_exports`.
- Remove or soften causal language.
- Remove forward-looking language unless a forecast source is added.
- Confirm that the brief is labeled as illustrative or as a research-support draft, not as an official view.

## Reminder

This review is a draft. A human reviewer must verify the data, edit the wording, and approve before the brief is shared.
