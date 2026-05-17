"""Generate a blank Markdown review template for a research-support workflow.

This script writes a single Markdown file that a human reviewer fills in
when running an AI-assisted review of a workflow (data QA, code, brief,
or documentation). The template keeps reviews consistent across projects.

Usage:
    python scripts/generate_review_template.py

The script uses only the Python standard library and avoids external
dependencies on purpose, so it runs in any environment that has Python 3.
"""

from datetime import date
from pathlib import Path


# Resolve the project root from this script's location so the output
# folder always lands inside the repo, regardless of where the script
# is invoked from.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_FILE = OUTPUT_DIR / "research_workflow_review_template.md"


# The template is kept as a single string so it is easy to read and edit.
# Sections match the human-in-the-loop review process documented in
# docs/human_in_the_loop_review.md.
TEMPLATE = """# Research Workflow Review Template

> Draft for human review. AI-assisted suggestions in this template must be
> verified against the original sources before any output is shared.

## Project / Workflow Name

_Fill in the workflow name (e.g., `macro-trade-commodity-monitor`)._

## Date

{today}

## Source Inputs

- Data dictionary or summary:
- Research notes:
- Scripts reviewed:
- Brief or memo reviewed:
- Other source materials:

## Data QA Checks

- Missing values / coverage:
- Mixed frequencies:
- Unit consistency:
- Transformation logic:
- Derived variables:
- Documentation gaps:

## Code Review Checks

- Path handling and reproducibility:
- Modularity:
- Output handling:
- Documented assumptions:
- Error handling:
- Git-reviewability:
- Truthfulness of outputs (do messages overstate what the code does?):

## Documentation Review

- Project scope clearly stated:
- Data sources listed with units and frequency:
- Transformations and assumptions documented:
- Outputs listed with file names:
- Limitations section present:
- "What this does NOT do" section present:

## Claims and Evidence

For each substantive claim in the workflow output or brief, list:

- Claim:
- Source(s) that support it:
- Whether the source(s) fully support, partially support, or do not address the claim:
- Suggested wording change (if any):

## Assumptions

- Units, frequencies, base years:
- Missing-value handling:
- Alignment of mixed-frequency series:
- Seasonal-adjustment status:
- Other:

## Limitations

- This review is a draft, not a validation.
- AI-assisted comments may be incomplete or incorrect.
- Source data has not been independently verified inside this template.
- Add any workflow-specific limitations here.

## Human Review Checklist

- [ ] Source inputs confirmed
- [ ] Calculations and transformations verified
- [ ] Generated text checked against source notes
- [ ] Unsupported or overstated claims removed or softened
- [ ] Limitations documented
- [ ] Approved or revised before sharing

## Final Reviewer Notes

_Reviewer name, date of sign-off, and any remaining open items._
"""


def main() -> None:
    """Create the outputs folder if needed and write the review template."""
    # mkdir with parents and exist_ok keeps the script idempotent: it can
    # be re-run safely without erroring if the folder already exists.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    rendered = TEMPLATE.format(today=date.today().isoformat())
    OUTPUT_FILE.write_text(rendered, encoding="utf-8")

    print(f"Wrote review template to {OUTPUT_FILE.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
