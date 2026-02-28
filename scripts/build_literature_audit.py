#!/usr/bin/env python3
"""Build an auditable literature table and generated TeX citation blocks."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


TIME_START = 2024
TIME_END = 2026

# Papers explicitly excluded by this survey (out-of-scope domain mismatch).
# Keep this list small and auditable (see content/appendix_b_exclusion_audit.tex).
MANUAL_EXCLUDE_KEYS = {
    # Entries previously excluded have been removed from both bib files.
    # This set is kept as a placeholder for future manual exclusions.
}


EMBODIED_TERMS = (
    "embodied",
    "robot",
    "robotic",
    "manipulation",
    "navigation",
    "locomotion",
    "autonomous driving",
    "driving",
    "vla",
    "vision-language-action",
    "policy",
    "planning",
    "control",
    "action",
    "sim2real",
    "real-world",
    "physical",
    "agent",
)

WORLD_MODEL_TERMS = (
    "world model",
    "world models",
    "latent dynamics",
    "dynamics model",
    "predictive model",
    "video prediction",
)


def find_matching_brace(text: str, open_idx: int) -> int:
    depth = 0
    i = open_idx
    while i < len(text):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


@dataclass
class BibEntry:
    entry_type: str
    cite_key: str
    fields: dict[str, str]


def parse_value(body: str, idx: int) -> tuple[str, int]:
    while idx < len(body) and body[idx].isspace():
        idx += 1
    if idx >= len(body):
        return "", idx

    if body[idx] == "{":
        end = find_matching_brace(body, idx)
        if end == -1:
            return body[idx + 1 :].strip(), len(body)
        return body[idx + 1 : end].strip(), end + 1
    if body[idx] == '"':
        idx += 1
        start = idx
        while idx < len(body):
            if body[idx] == '"' and body[idx - 1] != "\\":
                return body[start:idx].strip(), idx + 1
            idx += 1
        return body[start:].strip(), len(body)

    start = idx
    while idx < len(body) and body[idx] not in ",\n":
        idx += 1
    return body[start:idx].strip(), idx


def parse_bibtex(path: Path) -> list[BibEntry]:
    text = path.read_text(encoding="utf-8", errors="replace")
    entries: list[BibEntry] = []
    i = 0
    while i < len(text):
        at = text.find("@", i)
        if at == -1:
            break
        m = re.match(r"@([A-Za-z]+)\s*\{", text[at:])
        if not m:
            i = at + 1
            continue
        entry_type = m.group(1).lower()
        brace_open = at + m.end() - 1
        brace_close = find_matching_brace(text, brace_open)
        if brace_close == -1:
            break

        raw = text[brace_open + 1 : brace_close].strip()
        comma = raw.find(",")
        if comma == -1:
            i = brace_close + 1
            continue
        cite_key = raw[:comma].strip()
        body = raw[comma + 1 :]

        fields: dict[str, str] = {}
        j = 0
        while j < len(body):
            while j < len(body) and body[j] in " \t\r\n,":
                j += 1
            if j >= len(body):
                break
            fm = re.match(r"([A-Za-z][A-Za-z0-9_-]*)\s*=", body[j:])
            if not fm:
                j += 1
                continue
            field_name = fm.group(1).lower()
            j += fm.end()
            value, j = parse_value(body, j)
            fields[field_name] = value
            while j < len(body) and body[j] != ",":
                if body[j].isspace():
                    j += 1
                else:
                    break
            if j < len(body) and body[j] == ",":
                j += 1

        entries.append(BibEntry(entry_type=entry_type, cite_key=cite_key, fields=fields))
        i = brace_close + 1
    return entries


def normalize(s: str) -> str:
    s = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", s)
    s = s.replace("{", " ").replace("}", " ")
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


def first_pdf_path(file_field: str) -> str:
    if not file_field:
        return ""
    parts = [p.strip() for p in file_field.split(";") if p.strip()]
    for part in parts:
        m = re.search(r":([A-Za-z]:\\[^:]+\.pdf):application/pdf", part)
        if m:
            return m.group(1)
        m = re.search(r"([A-Za-z]:\\[^:]+\.pdf)", part)
        if m:
            return m.group(1)
    return ""


def in_window(year: int | None) -> bool:
    return year is not None and TIME_START <= year <= TIME_END


def chunked(keys: list[str], n: int = 18) -> list[list[str]]:
    return [keys[i : i + n] for i in range(0, len(keys), n)]


def latex_escape(text: str) -> str:
    return text.replace("_", "\\_")


def to_int_year(raw: str) -> int | None:
    if not raw:
        return None
    m = re.search(r"(19|20)\d{2}", raw)
    if not m:
        return None
    return int(m.group(0))


def assign_bucket(text: str, title: str, is_world_model: bool) -> str:
    title_l = title.lower()
    if "survey" in title_l or "comprehensive" in title_l:
        return "survey-meta"
    if any(k in text for k in ("benchmark", "dataset", "evaluation", "metric", "worldbench")):
        return "data-benchmark-eval"
    if is_world_model:
        return "world-model-core"
    if any(k in text for k in ("planning", "planner", "reasoning", "search")):
        return "planning-reasoning"
    if any(k in text for k in ("reinforcement learning", "imitation learning", "fine-tuning", "alignment")):
        return "policy-learning"
    if any(k in text for k in ("vla", "vision-language-action", "vlm", "llm", "transformer")):
        return "agent-architecture"
    return "foundation-definition"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bib", default="references-full.bib")
    parser.add_argument("--audit_csv", default="ref/paper_audit.csv")
    parser.add_argument("--appendix_in_scope_tex", default="content/generated/in_scope_citations.tex")
    parser.add_argument("--appendix_exclusion_tex", default="content/generated/exclusion_audit.tex")
    parser.add_argument("--stats_txt", default="ref/paper_audit_stats.txt")
    args = parser.parse_args()

    entries = parse_bibtex(Path(args.bib))

    rows: list[dict[str, str]] = []
    in_scope_keys_by_bucket_year: dict[str, dict[int, list[str]]] = defaultdict(lambda: defaultdict(list))
    excluded_by_reason: dict[str, list[str]] = defaultdict(list)

    for e in entries:
        title = e.fields.get("title", "").strip()
        abstract = e.fields.get("abstract", "").strip()
        keywords = e.fields.get("keywords", "").strip()
        year_raw = e.fields.get("year", "").strip()
        year = to_int_year(year_raw)
        text = normalize(" ".join([title, abstract, keywords]))
        is_embodied = any(term in text for term in EMBODIED_TERMS)
        is_world_model = any(term in text for term in WORLD_MODEL_TERMS)
        window_ok = in_window(year)
        embodied_support = any(term in text for term in ("embodied", "robot", "driving", "vla", "manipulation"))

        if e.cite_key in MANUAL_EXCLUDE_KEYS:
            is_in_scope = False
            exclude_reason = "manual_excluded"
        else:
            is_in_scope = window_ok and (is_embodied or (is_world_model and embodied_support))
            if year is None:
                exclude_reason = "missing_year"
            elif not window_ok:
                exclude_reason = "out_of_window"
            elif is_in_scope:
                exclude_reason = ""
            elif is_world_model:
                exclude_reason = "world_model_not_embodied"
            else:
                exclude_reason = "not_embodied_related"

        section_bucket = assign_bucket(text=text, title=title, is_world_model=is_world_model)
        priority_tier = "core" if ("survey" in title.lower() or is_world_model) else "supporting"

        row = {
            "cite_key": e.cite_key,
            "title": title,
            "year": str(year) if year is not None else "",
            "is_embodied": str(is_embodied).lower(),
            "is_world_model": str(is_world_model).lower(),
            "is_in_scope": str(is_in_scope).lower(),
            "time_in_scope": str(window_ok).lower(),
            "section_bucket": section_bucket,
            "priority_tier": priority_tier,
            "exclude_reason": exclude_reason,
            "source_pdf_path": first_pdf_path(e.fields.get("file", "")),
            "notes": "",
        }
        rows.append(row)

        if is_in_scope and year is not None:
            in_scope_keys_by_bucket_year[section_bucket][year].append(e.cite_key)
        elif exclude_reason:
            excluded_by_reason[exclude_reason].append(e.cite_key)

    rows.sort(key=lambda r: (r["year"] or "0000", r["cite_key"]))

    csv_path = Path(args.audit_csv)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "cite_key",
                "title",
                "year",
                "is_embodied",
                "is_world_model",
                "is_in_scope",
                "time_in_scope",
                "section_bucket",
                "priority_tier",
                "exclude_reason",
                "source_pdf_path",
                "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    in_scope_tex = Path(args.appendix_in_scope_tex)
    in_scope_tex.parent.mkdir(parents=True, exist_ok=True)
    with in_scope_tex.open("w", encoding="utf-8") as f:
        f.write("% Auto-generated by scripts/build_literature_audit.py\n")
        f.write("\\subsection{In-Scope Citation Coverage (2024--2026)}\n")
        f.write(
            "This appendix groups all in-scope references by survey bucket and publication year to make coverage auditable.\n\n"
        )
        for bucket in sorted(in_scope_keys_by_bucket_year):
            f.write(f"\\subsection{{{bucket}}}\n")
            years = sorted(in_scope_keys_by_bucket_year[bucket].keys(), reverse=True)
            for year in years:
                keys = sorted(set(in_scope_keys_by_bucket_year[bucket][year]))
                f.write(f"\\paragraph{{{year}}}\n")
                for batch in chunked(keys):
                    f.write("\\cite{" + ",".join(batch) + "}.\n")
                f.write("\n")

    ex_tex = Path(args.appendix_exclusion_tex)
    ex_tex.parent.mkdir(parents=True, exist_ok=True)
    with ex_tex.open("w", encoding="utf-8") as f:
        f.write("% Auto-generated by scripts/build_literature_audit.py\n")
        f.write("\\subsection{Exclusion Audit}\n")
        f.write(
            "Entries excluded from the main in-scope set are listed by reason. Full row-level details are in \\texttt{ref/paper\\_audit.csv}.\n\n"
        )
        for reason in sorted(excluded_by_reason):
            keys = sorted(set(excluded_by_reason[reason]))
            f.write(f"\\subsection{{{latex_escape(reason)}}}\n")
            for batch in chunked(keys):
                f.write("\\cite{" + ",".join(batch) + "}.\n")
            f.write("\n")

    counts = Counter(r["exclude_reason"] or "in_scope" for r in rows)
    in_scope_total = sum(1 for r in rows if r["is_in_scope"] == "true")
    stats_path = Path(args.stats_txt)
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    with stats_path.open("w", encoding="utf-8") as f:
        f.write(f"total_entries={len(rows)}\n")
        f.write(f"in_scope_total={in_scope_total}\n")
        f.write(f"time_window={TIME_START}-{TIME_END}\n")
        for reason, cnt in sorted(counts.items()):
            f.write(f"{reason}={cnt}\n")


if __name__ == "__main__":
    main()
