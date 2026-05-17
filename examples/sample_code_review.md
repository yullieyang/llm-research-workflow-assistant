# Sample Code Review (Illustrative AI-Assisted Output)

> **Note:** This is an illustrative AI-assisted code review of a short fictional research-support script. The script and review are for demonstration. The review is a draft for human review.

## Script under review (fictional excerpt)

```python
import pandas as pd

df = pd.read_csv("/Users/analyst/Desktop/macro_panel.csv")
df["net_exports"] = df["exports"] - df["imports"]
df.to_csv("output.csv")
print("Validated panel written to output.csv")
```

## Review

### 1. Path handling
- The input path `/Users/analyst/Desktop/macro_panel.csv` is a local hardcoded path and will not run on another machine.
- The output path `output.csv` is relative to the working directory at run time, which makes the location of the file unpredictable.
- Recommendation: move both paths to a small config block at the top of the script (or a `config.yaml`), and use a project-relative `data/` and `outputs/` folder.

### 2. Modularity
- The script does three things — load, transform, write — in a single top-level block.
- Recommendation: wrap each step in a small function (`load_panel`, `compute_net_exports`, `write_output`) so each step can be tested and reused.

### 3. Output naming
- `output.csv` is a generic name that will be silently overwritten on every run.
- Recommendation: name the file in a way that reflects what it contains (e.g., `outputs/macro_panel_with_net_exports.csv`). Add a timestamp suffix only if multiple runs per day are expected.

### 4. Assumptions
- The script assumes `exports` and `imports` exist, are in the same units, and use the same seasonal-adjustment status. None of this is checked or documented.
- Recommendation: add a short header comment stating the assumed units and adjustment status, and add an explicit column check before the subtraction.

### 5. Reproducibility
- There is no pinned environment (no `requirements.txt`, no `renv.lock`), no random seed (not needed here, but worth confirming), and no clear way for another analyst to rerun the script.
- Recommendation: add a `requirements.txt` and a short "How to run" section in the README.

### 6. Reviewability via Git
- A small, single-file change like this is reviewable, but the script writes to a path that could be inside the working directory and committed by accident.
- Recommendation: ensure `outputs/` is gitignored and add a `.gitignore` entry if not present.

### 7. Truthfulness of outputs
- The print statement says "Validated panel written to output.csv". The script does no validation. The wording overstates what the code does.
- Recommendation: change the message to something accurate, e.g., `"Wrote outputs/macro_panel_with_net_exports.csv (no validation performed)"`.

### 8. Error handling
- `read_csv` is unguarded. If the file is missing or has unexpected columns, the script will fail with a low-context error.
- Recommendation: wrap the read in a `try/except` and emit a clear message; add a column-presence check before the subtraction.

## Follow-up questions for the author

1. What is the expected sign convention for `net_exports` downstream?
2. Are `exports` and `imports` always provided in matching units and seasonal-adjustment status?
3. Should the output overwrite the previous run or be versioned?
4. Should this script be the place where `net_exports` is computed, or should it live in a shared transformation module?

## Reminder

This review is a draft. A human reviewer must read the script, run it against a representative input, and confirm the recommendations before merging.
