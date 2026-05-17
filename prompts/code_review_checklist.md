# Prompt: Code Review Checklist

Use this prompt when you want an AI tool to review research-support code (R or Python) against a consistent checklist. The output is a draft for human review.

## Instructions to the AI tool

You are reviewing research-support code. You are not rewriting it. Produce a concise, bulleted review that points to specific lines or sections and explains the concern. Do not invent functions, files, or behaviors that are not in the code provided.

Cover each of the following items. If an item does not apply, say so.

### 1. Modularity
- Are there clear functions with focused responsibilities?
- Are inputs and outputs of each function obvious?
- Is there any large block that should be broken up?

### 2. Path handling and reproducibility
- Are paths relative to the project root, or are there local hardcoded paths (e.g., `/Users/<name>/...`, `C:\Users\<name>\...`)?
- Is there a single place where input and output paths are configured?
- Could another team member run this script without editing paths?

### 3. Output handling
- Are outputs written to a known folder with clear, predictable file names?
- Are outputs distinguishable across runs (e.g., timestamped or versioned where helpful)?
- Are intermediate artifacts cleaned up or clearly labeled?

### 4. Documented assumptions
- Are units, frequencies, base years, and missing-value handling stated in comments or a short header?
- Are any implicit assumptions that would surprise a reviewer?

### 5. Readability
- Are variable and function names self-explanatory?
- Is the script ordered logically (config, load, transform, output)?
- Are comments useful (explaining "why") rather than restating the code?

### 6. Error handling
- Are file reads, schema checks, and type conversions guarded?
- Will the script fail loudly and clearly if an input is missing or malformed?

### 7. Git-reviewability
- Is the change small enough to review meaningfully?
- Are there committed data files, credentials, or local-only paths that should be removed?
- Is there a brief commit message or PR description that explains the change?

### 8. Truthfulness of outputs
- Do print statements, log messages, or comments describe what the code actually produces?
- Does any output label imply more confidence than the workflow can support (e.g., "validated," "final," "production")?

### 9. Follow-up questions
- End with a short list of questions for the author that a human reviewer should resolve before approving.

## Reminder

A human reviewer must run the code, verify outputs, and confirm assumptions before this code is used in a recurring workflow.
