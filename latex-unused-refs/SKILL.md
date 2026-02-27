---
name: latex-unused-refs
description: Check for unused BibTeX references in LaTeX documents. Use when users need to find citations defined in .bib files but never cited in .tex files, clean up bibliography entries, or audit LaTeX document references. Triggers on phrases like "unused references", "unused citations", "clean bib file", "find uncited entries", or "check latex references".
---

# LaTeX Unused References Checker

Find BibTeX entries that are defined but never cited in LaTeX documents.

## Usage

```bash
python scripts/check_unused_refs.py <main.tex> [--output <output.txt>] [--verbose]
```

**Arguments:**
- `<main.tex>`: Main LaTeX file (required)
- `--output`: Output file path (default: stdout, one key per line)
- `--verbose`: Show detailed information including bib files found and all parsed references

**Features:**
- Automatically extracts `.bib` files from `\bibliography{}` or `\addbibresource{}` commands
- Recursively finds all `\input{}` and `\include{}` sub-files
- Detects `\cite{}`, `\citep{}`, `\citet{}`, `\parencite{}`, `\textcite{}`, `\autocite{}` and variants
- Outputs unused citation keys, one per line

## Example

```bash
# Check main.tex, output to terminal
python scripts/check_unused_refs.py paper.tex

# Save unused keys to file
python scripts/check_unused_refs.py paper.tex --output unused.txt

# Verbose mode for debugging
python scripts/check_unused_refs.py paper.tex --verbose
```
