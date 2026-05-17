# Responsible AI Guidelines

Practical guidance for using AI coding tools and LLM-assisted workflows in research-support contexts. These guidelines apply to anything produced with the prompts and templates in this repository.

## 1. Human review is required

Every output from an AI tool — review comments, drafted documentation, suggested code edits — is a **draft**. A human reviewer must read, verify, edit, or reject the output before it is shared or acted on. AI-assisted output that has not been reviewed should not be treated as a finding.

## 2. Treat AI outputs as drafts

- Do not paste AI output into a brief, memo, or commit message without editing.
- Do not forward AI-generated review comments without confirming each item against the source.
- Track which sections of a document were AI-assisted, especially during the prototype stage of a workflow.

## 3. Source validation is required

- AI tools used in this repository do not have access to live data or authoritative sources.
- Every numeric figure, citation, or named source in an output must be traceable to a verifiable input.
- If an AI output references a number or source not in the input, treat it as a fabrication until proven otherwise.

## 4. Uncertainty should be explicit

- Outputs should separate facts (what is in the source), assumptions (what is being inferred), and interpretation (what it might mean).
- Use hedged language where appropriate: "appears to," "is consistent with," "preliminary," "needs verification."
- Do not let confident phrasing in an AI output paper over thin evidence.

## 5. Avoid unsupported causal claims

- Correlations in the data do not establish causation.
- Forward-looking statements require a model or a source. Without one, do not let them through.
- When reviewing briefs, flag and rewrite causal language that the underlying inputs do not support.

## 6. Do not use confidential or proprietary data

- This repository is for illustrative examples only.
- Do not paste embargoed, internal, proprietary, or otherwise non-public data into AI tools as part of any workflow built on this repository, unless you have explicit authorization and an appropriate environment.
- When in doubt, use a public or synthetic example.

## 7. Maintain reproducibility and version control

- Prefer reproducible, scripted workflows over ad hoc runs.
- Keep inputs, transformations, and outputs in a structure another reviewer can follow.
- Use Git for both code and prompt templates so changes are auditable.
- Generated outputs (e.g., the contents of `outputs/`) are kept local and not committed by default.

## 8. Document assumptions and limitations

- Every workflow should state its assumptions (units, frequencies, base years, missing-value handling, alignment of mixed-frequency series).
- Every workflow should state what it does NOT do.
- A reviewer should be able to read the documentation and understand the scope without running the code.

## 9. Failure modes to watch for

- **Confident hallucination:** an AI output cites a source or number that does not exist in the input.
- **Quiet overreach:** an AI output describes the workflow as "validated," "production-grade," or "automated" when it is not.
- **Drift in prompts:** prompt templates change without version control, and review outputs become inconsistent over time.
- **Skipped review:** an AI draft is forwarded without human review because it "looked fine."

If any of these occur, treat them as bugs in the workflow, not as one-off mistakes.

## 10. When in doubt

Stop and ask a human reviewer. The cost of pausing to confirm is low. The cost of an unsupported claim or a mislabeled output is high.
