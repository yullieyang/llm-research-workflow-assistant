# Limitations

This document states the limits of this repository so that no one — author, reviewer, or reader — overestimates what it does.

## What this is

A small workflow prototype that shows how AI coding tools and LLM-assisted workflows can support recurring research-support tasks: data QA, code review, documentation drafting, and research brief review.

## What this is not

- **Not a production system.** Nothing here is hardened, monitored, or maintained on a release schedule.
- **Not a live data validator.** The repository does not connect to any data source. All examples are illustrative.
- **Not a substitute for analysts, economists, or reviewers.** AI-assisted outputs are drafts that a human reviewer must verify.
- **Not a policy tool.** The repository does not draw policy conclusions and is not a source of an official view.
- **Not a guarantee of correctness.** AI-generated review comments can be incomplete, misleading, or wrong. Human review is required.
- **Not a chat product.** The prompts and templates here are checklists and scaffolding, not a conversational assistant.

## Specific limitations to keep in mind

1. **Sample data is fictional.** The data dictionary, research notes, QC report, brief review, and code review examples are illustrative. Do not cite them.
2. **No automated validation.** The Python script in `scripts/` generates a blank review template. It does not check data, code, or text.
3. **No model evaluation.** This repository does not benchmark AI outputs against a reference. A future improvement would add a small evaluation harness.
4. **No integration with internal systems.** This repository is standalone. It does not represent any internal data feed, dashboard, or workflow.
5. **Prompt-template drift.** Prompts can be updated. Each update should be versioned through Git so reviewers can see what was asked of the AI tool at the time of an output.

## How to use this honestly

- Describe the repository as a **workflow prototype**.
- Describe AI outputs as **drafts for human review**.
- Describe results as **illustrative**, not validated.
- Keep the "what this does NOT do" framing visible in any derived workflow or write-up.
