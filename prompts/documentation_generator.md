# Prompt: Documentation Generator

Use this prompt when you want an AI tool to draft a README or methodology section from a short workflow summary. The output is a draft for human review and editing.

## Instructions to the AI tool

You are drafting documentation for a research-support workflow. Use only the workflow summary and any notes the user provides. Do not invent data sources, transformations, or outputs that are not described in the input.

Produce a draft Markdown document that includes the following sections, in order. If the input does not cover a section, leave a clearly-marked placeholder rather than guessing.

### 1. Project scope
- One short paragraph describing what the workflow does and who it is for.
- Avoid promotional language. Do not call the workflow "automated," "production-grade," or "validated" unless the input explicitly supports that.

### 2. Data sources
- List each input source with name, frequency, units, and where it comes from.
- If a source is not specified, mark it `TBD — confirm with analyst`.

### 3. Transformations
- List the key transformations in the order they are applied (e.g., aggregation, deflation, indexing, seasonal adjustment).
- For each transformation, state the assumption it relies on (e.g., base year, deflator).

### 4. Outputs
- List the files or artifacts the workflow produces, with file names and a one-line description of each.

### 5. Assumptions
- List the assumptions the workflow depends on (units, frequencies, base year, missing-value handling, alignment of mixed-frequency series).

### 6. Limitations
- State what the workflow does NOT do. This section is required.
- Examples: does not validate live data, does not adjust for revisions, does not draw causal conclusions.

### 7. Reproducibility steps
- A short numbered list a new team member could follow to reproduce the workflow end to end.

### 8. What this project does NOT do
- A short, explicit list. This is separate from "Limitations" and is meant to prevent over-reading the workflow's scope.

## Tone and style

- Plain language. Short sentences.
- No marketing tone.
- No claims that the input does not support.
- Mark anything uncertain with `TBD` so a human reviewer can fill it in.

## Reminder

This draft is for human review. A reviewer must edit, confirm sources, and remove placeholders before this documentation is published or shared.
