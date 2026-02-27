#!/usr/bin/env python3
"""
BibTeX Query Tool

Query BibTeX files by citation keys and fields.

Usage:
    # Query single entry (full)
    python query_bib.py kai2026 references.bib

    # Query specific field
    python query_bib.py kai2026 references.bib --field abstract

    # Query multiple fields
    python query_bib.py kai2026 references.bib --field abstract --field title

    # Query multiple keys
    python query_bib.py kai2026,zhang2025 references.bib

    # List all citation keys
    python query_bib.py --list-keys references.bib

    # List fields for a specific entry
    python query_bib.py kai2026 references.bib --list-fields

    # Search by keyword
    python query_bib.py --search "machine learning" references.bib
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")


class BibEntry:
    """Represents a single BibTeX entry."""

    def __init__(self, entry_type: str, cite_key: str, fields: Dict[str, str]):
        self.entry_type = entry_type
        self.cite_key = cite_key
        self.fields = fields

    def get_field(self, field_name: str) -> Optional[str]:
        for key, value in self.fields.items():
            if key.lower() == field_name.lower():
                return value
        return None

    def has_field(self, field_name: str) -> bool:
        return self.get_field(field_name) is not None

    def to_bibtex(self) -> str:
        lines = [f"@{self.entry_type}{{{self.cite_key},"]
        for field, value in self.fields.items():
            lines.append(f"  {field} = {{{value}}},")
        lines.append("}")
        return "\n".join(lines)

    def to_formatted(self, fields: Optional[List[str]] = None) -> str:
        if fields:
            return self._format_specific_fields(fields)
        return self._format_all_fields()

    def _format_specific_fields(self, fields: List[str]) -> str:
        output = [f"Entry: @{self.entry_type}{{{self.cite_key}}}"]
        for field in fields:
            value = self.get_field(field)
            display_value = value if value is not None else "[NOT FOUND]"
            output.append(f"  {field}: {display_value}")
        return "\n".join(output)

    def _format_all_fields(self) -> str:
        output = [f"Entry: @{self.entry_type}{{{self.cite_key}}}"]
        for field, value in self.fields.items():
            output.append(f"  {field}: {value}")
        return "\n".join(output)


class BibParser:
    """Parse BibTeX files."""

    # Regex pattern: @type{key, field=value, ...}
    ENTRY_PATTERN = re.compile(
        r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\s*\}", re.DOTALL | re.IGNORECASE
    )

    # Regex pattern: field = {value} or field = "value"
    FIELD_PATTERN = re.compile(r'(\w+)\s*=\s*[{"]([^}"]*)[}"]', re.DOTALL)

    # Regex pattern: field = {value} or field = "value"
    FIELD_PATTERN = re.compile(r'(\w+)\s*=\s*[{"]([^}"]*)[}"]', re.DOTALL)

    @staticmethod
    def parse_file(filepath: Path) -> Dict[str, BibEntry]:
        if not filepath.exists():
            raise FileNotFoundError(f"BibTeX file not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        entries = {}
        for match in BibParser.ENTRY_PATTERN.finditer(content):
            entry_type = match.group(1)
            cite_key = match.group(2).strip()
            fields_text = match.group(3)

            fields = BibParser._parse_fields(fields_text)
            entries[cite_key] = BibEntry(entry_type, cite_key, fields)

        return entries

    @staticmethod
    def _parse_fields(fields_text: str) -> Dict[str, str]:
        fields = {}
        for match in BibParser.FIELD_PATTERN.finditer(fields_text):
            field_name = match.group(1).strip()
            field_value = match.group(2).strip()
            fields[field_name] = field_value
        return fields


def query_entries(
    entries: Dict[str, BibEntry],
    cite_keys: List[str],
    fields: Optional[List[str]] = None,
) -> str:
    output = []

    for cite_key in cite_keys:
        if cite_key not in entries:
            output.append(f"❌ Entry '{cite_key}' not found in BibTeX file.")
            continue

        entry = entries[cite_key]

        if fields:
            missing_fields = [f for f in fields if not entry.has_field(f)]
            if missing_fields:
                output.append(
                    f"⚠️  Entry '{cite_key}' found, but missing fields: {', '.join(missing_fields)}"
                )
            output.append(entry.to_formatted(fields))
        else:
            output.append(entry.to_formatted())

        output.append("")

    return "\n".join(output)


def list_keys(entries: Dict[str, BibEntry]) -> str:
    if not entries:
        return "No entries found in BibTeX file."

    output = [f"Found {len(entries)} entries:\n"]
    for cite_key, entry in sorted(entries.items()):
        output.append(f"  • {cite_key} (@{entry.entry_type})")

    return "\n".join(output)


def list_fields(entry: BibEntry) -> str:
    output = [f"Fields in entry '{entry.cite_key}' (@{entry.entry_type}):\n"]
    for field in sorted(entry.fields.keys()):
        output.append(f"  • {field}")
    return "\n".join(output)


def search_entries(entries: Dict[str, BibEntry], query: str) -> str:
    query_lower = query.lower()
    matches = []

    for cite_key, entry in entries.items():
        if query_lower in cite_key.lower():
            matches.append((cite_key, entry, "cite_key"))
            continue

        for field, value in entry.fields.items():
            if query_lower in value.lower():
                matches.append((cite_key, entry, field))
                break

    if not matches:
        return f"No entries found matching '{query}'."

    output = [f"Found {len(matches)} entries matching '{query}':\n"]
    for cite_key, entry, match_field in matches:
        output.append(
            f"  • {cite_key} (@{entry.entry_type}) - matched in: {match_field}"
        )

    return "\n".join(output)


def list_fields(entry: BibEntry) -> str:
    output = [f"Fields in entry '{entry.cite_key}' (@{entry.entry_type}):\n"]
    for field in sorted(entry.fields.keys()):
        output.append(f"  • {field}")
    return "\n".join(output)


def search_entries(entries: Dict[str, BibEntry], query: str) -> str:
    query_lower = query.lower()
    matches = []

    for cite_key, entry in entries.items():
        if query_lower in cite_key.lower():
            matches.append((cite_key, entry, "cite_key"))
            continue

        for field, value in entry.fields.items():
            if query_lower in value.lower():
                matches.append((cite_key, entry, field))
                break

    if not matches:
        return f"No entries found matching '{query}'."

    output = [f"Found {len(matches)} entries matching '{query}':\n"]
    for cite_key, entry, match_field in matches:
        output.append(
            f"  • {cite_key} (@{entry.entry_type}) - matched in: {match_field}"
        )

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Query BibTeX files by citation keys and fields.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s kai2026 references.bib
  %(prog)s kai2026 references.bib --field abstract
  %(prog)s kai2026,zhang2025 references.bib
  %(prog)s --list-keys references.bib
  %(prog)s kai2026 references.bib --list-fields
  %(prog)s --search "machine learning" references.bib
        """,
    )

    parser.add_argument(
        "cite_keys",
        nargs="?",
        help="Citation key(s) to query (comma-separated for multiple)",
    )
    parser.add_argument("bib_file", type=Path, help="Path to BibTeX file")
    parser.add_argument(
        "--field",
        action="append",
        dest="fields",
        help="Specific field(s) to query (can be used multiple times)",
    )
    parser.add_argument(
        "--list-keys", action="store_true", help="List all citation keys in the file"
    )
    parser.add_argument(
        "--list-fields",
        action="store_true",
        help="List all fields in the specified entry",
    )
    parser.add_argument(
        "--search", type=str, help="Search for entries containing the query string"
    )

    args = parser.parse_args()

    try:
        entries = BibParser.parse_file(args.bib_file)

        if not entries:
            print("⚠️  No entries found in BibTeX file.", file=sys.stderr)
            sys.exit(1)

        if args.list_keys:
            print(list_keys(entries))
        elif args.search:
            print(search_entries(entries, args.search))
        elif args.cite_keys:
            cite_keys = [k.strip() for k in args.cite_keys.split(",")]

            if args.list_fields:
                if cite_keys[0] not in entries:
                    print(f"❌ Entry '{cite_keys[0]}' not found.", file=sys.stderr)
                    sys.exit(1)
                print(list_fields(entries[cite_keys[0]]))
            else:
                print(query_entries(entries, cite_keys, args.fields))
        else:
            parser.print_help()
            sys.exit(1)

    except FileNotFoundError as e:
        print(f"❌ {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

        if args.list_keys:
            print(list_keys(entries))
        elif args.search:
            print(search_entries(entries, args.search))
        elif args.cite_keys:
            cite_keys = [k.strip() for k in args.cite_keys.split(",")]

            if args.list_fields:
                if cite_keys[0] not in entries:
                    print(f"❌ Entry '{cite_keys[0]}' not found.", file=sys.stderr)
                    sys.exit(1)
                print(list_fields(entries[cite_keys[0]]))
            else:
                print(query_entries(entries, cite_keys, args.fields))
        else:
            parser.print_help()
            sys.exit(1)

        # Handle different operations
        if args.list_keys:
            print(list_keys(entries))

        elif args.search:
            print(search_entries(entries, args.search))

        elif args.cite_keys:
            cite_keys = [k.strip() for k in args.cite_keys.split(",")]

            if args.list_fields:
                # List fields for the first cite_key
                if cite_keys[0] not in entries:
                    print(f"❌ Entry '{cite_keys[0]}' not found.", file=sys.stderr)
                    sys.exit(1)
                print(list_fields(entries[cite_keys[0]]))
            else:
                # Query entries
                print(query_entries(entries, cite_keys, args.fields))

        else:
            parser.print_help()
            sys.exit(1)

    except FileNotFoundError as e:
        print(f"❌ {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
