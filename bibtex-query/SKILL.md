---
name: bibtex-query
description: Query and search BibTeX bibliography files by citation keys, fields, or keywords. Use when working with .bib files for academic research, literature management, or citation extraction. Supports batch queries (multiple keys), field-specific queries (e.g., --field abstract), listing all entries/fields, and full-text search across entries. Ideal for extracting specific information from bibliography databases, finding missing fields, or searching for papers by keyword.
---

# BibTeX Query Tool

Query BibTeX bibliography files efficiently by citation keys, fields, or keywords.

## Core Features

**Query by Citation Key**
- Single entry: Full bibliographic information
- Batch queries: Multiple citation keys in one command
- Field filtering: Extract specific fields only

**Discovery and Search**
- List all citation keys in a BibTeX file
- List all fields in a specific entry
- Full-text search across entries

**Error Handling**
- Clear messages when entries or fields not found
- Warnings for missing requested fields
- UTF-8 encoding support (Windows compatible)

## Usage

### Basic Query

Query complete entry:
```bash
python scripts/query_bib.py kai2026 references.bib
```

Output:
```
Entry: @article{kai2026}
  author: Kai Zhang and John Doe
  title: Machine Learning Applications
  journal: Journal of AI Research
  year: 2026
  abstract: ...
```

### Field-Specific Query

Extract only specific fields:
```bash
python scripts/query_bib.py kai2026 references.bib --field abstract
```

Query multiple fields:
```bash
python scripts/query_bib.py kai2026 references.bib --field title --field abstract
```

### Batch Queries

Query multiple citation keys at once:
```bash
python scripts/query_bib.py kai2026,zhang2025,johnson2024 references.bib
```

Combine batch with field queries:
```bash
python scripts/query_bib.py kai2026,zhang2025 references.bib --field abstract --field title
```

### List Operations

List all citation keys:
```bash
python scripts/query_bib.py --list-keys references.bib
```

List all fields in an entry:
```bash
python scripts/query_bib.py kai2026 references.bib --list-fields
```

### Search

Search for entries containing keywords:
```bash
python scripts/query_bib.py --search "machine learning" references.bib
```

Output shows which field matched:
```
Found 2 entries matching 'machine learning':
  • kai2026 (@article) - matched in: title
  • zhang2025 (@inproceedings) - matched in: abstract
```

## Common Workflows

### Extract Abstracts for Literature Review

```bash
# Get abstracts from multiple papers
python scripts/query_bib.py paper1,paper2,paper3 refs.bib --field abstract > abstracts.txt
```

### Check for Missing Fields

```bash
# Query required fields - warnings show what's missing
python scripts/query_bib.py * refs.bib --field doi --field url
```

### Find Papers by Topic

```bash
# Search for related work
python scripts/query_bib.py --search "neural network" refs.bib
```

### Inventory Your Bibliography

```bash
# List all available citations
python scripts/query_bib.py --list-keys refs.bib
```

## Error Messages

**Entry not found**:
```
❌ Entry 'nonexistent' not found in BibTeX file.
```

**Missing field**:
```
⚠️  Entry 'johnson2024' found, but missing fields: abstract
Entry: @book{johnson2024}
  abstract: [NOT FOUND]
```

**No matches**:
```
No entries found matching 'quantum computing'.
```

## Implementation Notes

The script uses Python's `re` module with carefully crafted regex patterns to parse BibTeX files:
- Entry pattern: Captures `@type{key, ...}` structures
- Field pattern: Handles both `field = {value}` and `field = "value"` formats
- Case-insensitive field matching for flexibility
- Windows encoding compatibility via UTF-8 wrapper

For Claude: When users request BibTeX queries, use this script directly rather than manually parsing .bib files. The script handles edge cases (malformed entries, encoding issues, nested braces) that regex-based manual parsing often misses.
