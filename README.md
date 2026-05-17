# llm-research-workflow-assistant

A responsible research workflow prototype for QA, documentation, and human-in-the-loop review. It packages the recurring shape of research-support work — data QA, code review, documentation drafting, brief review, and reviewer sign-off — into reusable templates and worked examples, with explicit rules for where AI coding tools may support the workflow and where they may not.

## Project overview

This repository is a workflow prototype, not a production system. It contains reusable prompt templates, illustrative examples, a small Python utility for generating blank review files, and responsible-use documentation. The prompts and checklists are analyst-owned; AI coding tools may produce draft review comments or documentation, but the workflow logic, source validation, and final review remain human-owned.

The project intentionally stays small and realistic. It does not automate research, replace analyst judgment, or validate live data.

## Why this matters for research-support workflows

Research-support work in economics and policy contexts is heavy on recurring tasks: pulling and cleaning data, checking units and frequencies, reviewing transformations, drafting documentation, and reviewing short briefs before they are shared. These tasks reward consistency, traceability, and careful human review.

LLM-assisted tooling can help by:

- producing structured first-pass reviews against an explicit checklist,
- surfacing missing documentation, mixed frequencies, or unit inconsistencies,
- drafting documentation that a reviewer can edit instead of writing from scratch,
- flagging unsupported claims in early-stage research briefs.

The goal is not to remove the analyst from the loop. It is to make the loop faster and more reviewable.

## What this project demonstrates

- **Reusable prompt templates** for data QA, code review, brief review, and documentation drafting.
- **Worked examples** showing the kind of output an AI tool might produce, with caveats and follow-up questions for a human reviewer.
- **Responsible-use guidance** covering source validation, uncertainty, reproducibility, and the limits of AI-generated review comments.
- **A simple Python utility** that generates a blank review template so reviews stay consistent across projects.
- **A `CLAUDE.md` configuration** that defines how Claude Code should behave in this repository.

## Repository structure

```
llm-research-workflow-assistant/
├── README.md
├── CLAUDE.md
├── .gitignore
├── prompts/
│   ├── data_qa_review.md
│   ├── code_review_checklist.md
│   ├── research_brief_review.md
│   └── documentation_generator.md
├── examples/
│   ├── sample_data_dictionary.md
│   ├── sample_research_notes.md
│   ├── sample_qc_report.md
│   ├── sample_research_brief_review.md
│   └── sample_code_review.md
├── scripts/
│   └── generate_review_template.py
└── docs/
    ├── responsible_ai_guidelines.md
    ├── human_in_the_loop_review.md
    └── limitations.md
```

- [prompts/data_qa_review.md](prompts/data_qa_review.md)
- [prompts/code_review_checklist.md](prompts/code_review_checklist.md)
- [prompts/research_brief_review.md](prompts/research_brief_review.md)
- [prompts/documentation_generator.md](prompts/documentation_generator.md)
- [examples/sample_data_dictionary.md](examples/sample_data_dictionary.md)
- [examples/sample_research_notes.md](examples/sample_research_notes.md)
- [examples/sample_qc_report.md](examples/sample_qc_report.md)
- [examples/sample_research_brief_review.md](examples/sample_research_brief_review.md)
- [examples/sample_code_review.md](examples/sample_code_review.md)
- [scripts/generate_review_template.py](scripts/generate_review_template.py)
- [docs/responsible_ai_guidelines.md](docs/responsible_ai_guidelines.md)
- [docs/human_in_the_loop_review.md](docs/human_in_the_loop_review.md)
- [docs/limitations.md](docs/limitations.md)

## Example use cases

- An analyst preparing a recurring trade-flow data refresh wants a structured QA pass before running downstream code.
- A research assistant has drafted a short brief and wants an AI-assisted check for unsupported claims before a senior reviewer sees it.
- A team wants a consistent code-review checklist for research scripts that handle paths, outputs, and assumptions in a reproducible way.
- A workflow owner wants a draft README or methodology section that they can edit, instead of writing documentation from a blank page.

## Example workflow

1. The analyst prepares the inputs: a data dictionary, a short research note, or a script.
2. The analyst opens the relevant prompt template in `prompts/` and provides the input to the AI tool (e.g., Claude Code).
3. The AI tool returns a structured first-pass review: observations, flags, follow-up questions.
4. The analyst runs `scripts/generate_review_template.py` to create a blank review file in `outputs/`.
5. The analyst fills in the review template, treating the AI output as a draft to verify, edit, or reject.
6. The analyst confirms the human-review checklist in [docs/human_in_the_loop_review.md](docs/human_in_the_loop_review.md) before the output is shared.

## Responsible AI approach

This project treats AI-generated output as a draft, not a conclusion. Key principles:

- Source validation is required. The AI tool does not have access to authoritative data.
- Uncertainty must be explicit. Outputs should separate facts, assumptions, and interpretation.
- No confidential or proprietary data is used in this repository. All examples are illustrative.
- Reproducibility and version control are preferred over one-off, untracked runs.
- Human review is required before any output is shared or acted on.

See [docs/responsible_ai_guidelines.md](docs/responsible_ai_guidelines.md) for the full guidance.

## Human-in-the-loop review process

Every workflow in this repository assumes a human reviewer. The review steps are:

1. Confirm source inputs.
2. Verify calculations and transformations.
3. Review generated text against source notes.
4. Check for unsupported claims.
5. Confirm limitations are documented.
6. Approve or revise the output before sharing.

The full checklist lives in [docs/human_in_the_loop_review.md](docs/human_in_the_loop_review.md).

## Limitations

- This is a workflow prototype, not a production system.
- It does not validate live data or connect to any authoritative source.
- It does not replace analysts, economists, or reviewers.
- It does not make policy conclusions.
- It does not guarantee the correctness of AI-generated review comments.
- All example data is fictional and illustrative.

See [docs/limitations.md](docs/limitations.md).

## Portfolio Context

This project translates recurring patterns from research-support work —
data QA, code review, brief review, documentation drafting, and
human-in-the-loop validation — into a public portfolio prototype. The
sample inputs and examples are fictional, and the prototype emphasizes
analyst-owned logic with AI coding tools positioned as drafting and
consistency support. AI coding tools may support scaffolding,
documentation review, and consistency checks, but the workflow logic,
assumptions, validation criteria, and final outputs remain
human-reviewed. The goal is to demonstrate reproducible, reviewable
workflow design.

## Future improvements

- Add a small evaluation harness that scores AI review outputs against hand-graded reference reviews.
- Add language-specific code review prompts (R and Python) with separate checklists.
- Add a lightweight logging utility so each AI-assisted review is timestamped and reproducible.
- Extend the template script to accept a project name and reviewer name from the command line.
- Add a short tutorial notebook showing one end-to-end workflow with a fictional dataset.

## How to run the template script

The script uses only the Python standard library.

```bash
python scripts/generate_review_template.py
```

This creates an `outputs/` folder (if it does not already exist) and writes `outputs/research_workflow_review_template.md`, a blank review template a human reviewer can fill in.

The `outputs/` folder is gitignored so generated review files are not committed by default.
