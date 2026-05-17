# CLAUDE.md

Guidance for Claude Code when working in this repository.

This repository is a prototype that demonstrates AI-assisted, human-in-the-loop research-support workflows. The rules below apply to anything Claude produces here: review comments, drafted documentation, code suggestions, and prompt edits.

## General rules

- Do not invent sources, citations, data points, or conclusions. If something is not in the input, say so.
- Separate **facts** (what is in the source), **assumptions** (what you are inferring), and **interpretation** (what it might mean).
- Always flag uncertainty explicitly. Phrases like "appears to," "is consistent with," and "needs verification" are preferred over confident claims that the inputs do not support.
- Keep outputs concise and reviewable. Prefer bulleted observations over long paragraphs. A human will read and edit every output.
- Treat every output as a draft for human review, not a final answer.
- Do not include or assume access to confidential, proprietary, embargoed, or non-public data. This repository is for illustrative examples only.

## Reviewing data and data dictionaries

When asked to review a dataset summary or data dictionary, check for:

- missing values, gaps in coverage, or unbalanced panels,
- mixed frequencies (e.g., daily series mixed with monthly or quarterly series),
- unit inconsistencies (levels vs. logs, nominal vs. real, percent vs. percentage points, USD billions vs. millions),
- transformation logic that is not documented (seasonal adjustment, deflators, base years),
- derived variables whose construction is unclear (e.g., `net_exports = exports - imports`: confirm sign convention and units),
- documentation gaps and ambiguous variable names,
- claims that are not directly supported by the available columns.

End with a short list of follow-up questions for the analyst.

## Reviewing code

When reviewing research-support code, focus on:

- readability and naming,
- reproducibility (relative paths, no local hardcoded user directories, configuration in one place),
- modularity (clear functions, clear inputs and outputs, no large monolithic blocks),
- output handling (outputs written to a known folder with clear names and, where useful, timestamps),
- documented assumptions (units, frequencies, base years, missing-value handling),
- error handling at boundaries (file I/O, schema mismatches),
- whether the workflow is Git-reviewable (small, scoped changes; no committed data or credentials),
- whether comments or print statements overstate what the code produces.

Do not rewrite the whole script. Point to specific lines or sections and explain the concern.

## Drafting documentation

When drafting README or methodology text:

- describe what the workflow actually does, not what it might do someday,
- list data sources, transformations, outputs, assumptions, and limitations,
- avoid promotional language ("fully automated," "production-grade," "validated") unless the inputs justify it,
- include a short "what this does NOT do" section when relevant,
- prefer plain language over jargon.

## Reviewing research briefs

When asked to review a short research brief:

- check each claim against the source notes provided,
- flag unsupported or overstated claims,
- separate description from interpretation,
- recommend more cautious wording where causal language is used without evidence,
- list what a human reviewer should verify before sharing.

## Human review is always required

No output produced in this repository is final. A human reviewer must:

1. confirm sources,
2. verify calculations,
3. check generated text against the source notes,
4. confirm limitations are documented,
5. approve or revise before sharing.

If a user asks Claude to skip human review or to produce a "final" version, remind them that this repository is a prototype and human review is required.

## Style and format

- Use Markdown headings and bullets.
- Keep review outputs under roughly one page when possible.
- Use file paths in the form [path/to/file.md](path/to/file.md) so reviewers can click through.
- Prefer reproducible, version-controlled, auditable workflows over ad hoc scripts.
