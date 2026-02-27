#!/usr/bin/env python3
"""
Check for unused BibTeX references in LaTeX documents.

Finds all citation keys defined in .bib files but never cited in .tex files.
Recursively processes \input and \include directives.
"""

import argparse
import re
import sys
from pathlib import Path


BIB_PATTERNS = [
    r"\\bibliography\{([^}]+)\}",
    r"\\addbibresource\{([^}]+)\}",
]

INPUT_PATTERNS = [
    r"\\input\{([^}]+)\}",
    r"\\include\{([^}]+)\}",
]

CITE_PATTERNS = [
    r"\\cite\*?\{([^}]+)\}",
    r"\\citep\*?\{([^}]+)\}",
    r"\\citet\*?\{([^}]+)\}",
    r"\\parencite\*?\{([^}]+)\}",
    r"\\textcite\*?\{([^}]+)\}",
    r"\\autocite\*?\{([^}]+)\}",
    r"\\citeauthor\*?\{([^}]+)\}",
    r"\\citeyear\*?\{([^}]+)\}",
    r"\\citealt\*?\{([^}]+)\}",
    r"\\citealp\*?\{([^}]+)\}",
    r"\\fullcite\{([^}]+)\}",
    r"\\nocite\{([^}]+)\}",
]

# Matches @article{key, @book{key, @inproceedings{key, etc.
BIB_ENTRY_PATTERN = r"@\w+\s*\{\s*([^,\s]+)\s*,"

NOCITE_ALL_PATTERN = r"\\nocite\s*\{\s*\*\s*\}"


def read_file_content(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def find_bib_files(tex_content: str, tex_dir: Path) -> list[Path]:
    bib_files = []
    for pattern in BIB_PATTERNS:
        for match in re.finditer(pattern, tex_content):
            entries = match.group(1).split(",")
            for entry in entries:
                entry = entry.strip()
                if not entry.endswith(".bib"):
                    entry += ".bib"
                bib_path = tex_dir / entry
                if bib_path.exists():
                    bib_files.append(bib_path)
    return bib_files


def find_sub_tex_files(tex_content: str, tex_dir: Path) -> list[Path]:
    sub_files = []
    for pattern in INPUT_PATTERNS:
        for match in re.finditer(pattern, tex_content):
            filename = match.group(1).strip()
            for ext in ["", ".tex"]:
                sub_path = tex_dir / (filename + ext)
                if sub_path.exists() and sub_path.suffix == ".tex":
                    sub_files.append(sub_path)
                    break
    return sub_files


def read_tex_recursive(
    tex_path: Path, visited: set[Path] | None = None
) -> tuple[str, list[Path]]:
    if visited is None:
        visited = set()

    tex_path = tex_path.resolve()
    if tex_path in visited:
        return "", []
    visited.add(tex_path)

    content = read_file_content(tex_path)
    tex_dir = tex_path.parent
    bib_files = find_bib_files(content, tex_dir)

    combined_content = content
    for sub_file in find_sub_tex_files(content, tex_dir):
        sub_content, sub_bibs = read_tex_recursive(sub_file, visited)
        combined_content += "\n" + sub_content
        bib_files.extend(sub_bibs)

    return combined_content, bib_files


def extract_bib_keys(bib_path: Path) -> set[str]:
    content = read_file_content(bib_path)
    return set(re.findall(BIB_ENTRY_PATTERN, content))


def extract_cited_keys(tex_content: str) -> set[str]:
    if re.search(NOCITE_ALL_PATTERN, tex_content):
        return {"*"}

    cited_keys = set()
    for pattern in CITE_PATTERNS:
        for match in re.finditer(pattern, tex_content):
            keys = match.group(1).split(",")
            for key in keys:
                key = key.strip()
                if key and key != "*":
                    cited_keys.add(key)
    return cited_keys


def main():
    parser = argparse.ArgumentParser(
        description="Find unused BibTeX references in LaTeX documents."
    )
    parser.add_argument("tex_file", type=Path, help="Main .tex file to check")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output file path (default: stdout)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show detailed information"
    )

    args = parser.parse_args()

    if not args.tex_file.exists():
        print(f"Error: File not found: {args.tex_file}", file=sys.stderr)
        sys.exit(1)

    tex_content, bib_files = read_tex_recursive(args.tex_file)
    bib_files = list(set(bib_files))

    if args.verbose:
        print(f"Found {len(bib_files)} bib file(s):", file=sys.stderr)
        for bib in bib_files:
            print(f"  - {bib}", file=sys.stderr)

    if not bib_files:
        print("Warning: No .bib files found in the document.", file=sys.stderr)
        sys.exit(0)

    all_bib_keys = set()
    for bib_path in bib_files:
        keys = extract_bib_keys(bib_path)
        if args.verbose:
            print(f"{bib_path.name}: {len(keys)} entries", file=sys.stderr)
        all_bib_keys.update(keys)

    cited_keys = extract_cited_keys(tex_content)

    if args.verbose:
        print(f"\nTotal bib entries: {len(all_bib_keys)}", file=sys.stderr)
        print(f"Total citations: {len(cited_keys)}", file=sys.stderr)

    if "*" in cited_keys:
        if args.verbose:
            print(
                "\n\\nocite{*} found - all entries are considered used.",
                file=sys.stderr,
            )
        sys.exit(0)

    unused_keys = sorted(all_bib_keys - cited_keys)

    if args.verbose:
        print(f"Unused entries: {len(unused_keys)}\n", file=sys.stderr)

    output_content = "\n".join(unused_keys)
    if unused_keys:
        output_content += "\n"

    if args.output:
        args.output.write_text(output_content, encoding="utf-8")
        if args.verbose:
            print(f"Results written to: {args.output}", file=sys.stderr)
    else:
        print(output_content, end="")


if __name__ == "__main__":
    main()
