# Human-in-the-Loop Review Process

This document describes the review steps that apply to any output produced with the prompts and templates in this repository. The process is intentionally short and explicit so it can be followed each time without ambiguity.

## Principles

- AI-assisted outputs are drafts.
- A human reviewer is accountable for every output that leaves the workflow.
- Each step below is required, in order. Steps cannot be skipped because an output "looks fine."

## Steps

### 1. Confirm source inputs

- Identify every input that fed the AI tool: data dictionary, code, brief text, prior notes.
- Confirm that each input is the version you intended to review (correct file, correct date).
- Confirm that no confidential or proprietary material was pasted into a tool that should not see it.

### 2. Verify calculations and transformations

- For any numeric claim in the output, trace it back to the input.
- For any derived variable, recompute at least one value by hand or with a small spot check.
- For any transformation (seasonal adjustment, deflation, indexing, aggregation), confirm the assumed base year, deflator, or aggregation rule.

### 3. Review generated text against source notes

- Read each substantive sentence in the AI output alongside the source notes.
- Confirm that the source notes support the claim, partially support it, or do not address it.
- Flag any sentence whose support is unclear.

### 4. Check for unsupported claims

- Remove or rewrite causal language that the inputs do not support.
- Remove or rewrite forward-looking statements that are not backed by a model or a cited source.
- Replace confident phrasing with hedged phrasing where the evidence is thin.

### 5. Confirm limitations are documented

- The output should state what the workflow does NOT do.
- The output should state the assumptions the workflow depends on.
- If either is missing, add it before sign-off.

### 6. Approve or revise before sharing

- Record reviewer name and date on the final review template.
- Either approve the output as-is, return it to the author with revisions, or reject it.
- Do not share an output that has not gone through steps 1–5.

## Where to record the review

- Run `python scripts/generate_review_template.py` to create a blank review file in `outputs/`.
- Fill in each section of the template.
- Keep the completed template alongside the workflow it reviewed.

## When the AI tool disagrees with the analyst

If the AI tool flags something the analyst believes is correct, the resolution is not "the AI is right" or "the analyst is right." The resolution is:

1. Identify exactly which input the AI tool is reacting to.
2. Confirm whether that input is accurate.
3. Update the input, the documentation, or the workflow as needed.
4. Note the resolution in the review template so future reviewers can see how it was handled.
