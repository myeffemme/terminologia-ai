#!/usr/bin/env python3
"""Valida schema, tassonomia e coerenza trasversale del corpus."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
ENTRIES_DIR = ROOT / "entries"


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> int:
    schema = json.loads((ROOT / "schema" / "lemma.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    category_ids = {item["id"] for item in load_yaml(ROOT / "taxonomy" / "categories.yaml")["categories"]}
    tag_ids = set(load_yaml(ROOT / "taxonomy" / "tags.yaml")["tags"])
    paths = sorted(ENTRIES_DIR.glob("*.yaml"))
    errors: list[str] = []
    warnings: list[str] = []
    entries: dict[str, tuple[Path, dict]] = {}

    if not paths:
        errors.append("entries/: nessun lemma trovato")

    for path in paths:
        try:
            entry = load_yaml(path)
        except yaml.YAMLError as exc:
            errors.append(f"{path.relative_to(ROOT)}: YAML non valido: {exc}")
            continue
        if not isinstance(entry, dict):
            errors.append(f"{path.relative_to(ROOT)}: la radice deve essere un oggetto")
            continue
        for problem in sorted(validator.iter_errors(entry), key=lambda item: list(item.path)):
            location = ".".join(map(str, problem.path)) or "<radice>"
            errors.append(f"{path.relative_to(ROOT)}:{location}: {problem.message}")
        entry_id = entry.get("id")
        if not isinstance(entry_id, str):
            continue
        if path.stem != entry_id:
            errors.append(f"{path.relative_to(ROOT)}: il nome file deve essere {entry_id}.yaml")
        if entry_id in entries:
            errors.append(f"{path.relative_to(ROOT)}: id duplicato {entry_id!r}")
        entries[entry_id] = (path, entry)

    names: dict[str, list[str]] = defaultdict(list)
    for entry_id, (path, entry) in entries.items():
        if entry.get("category") not in category_ids:
            errors.append(f"{path.relative_to(ROOT)}: categoria sconosciuta {entry.get('category')!r}")
        for tag in entry.get("tags", []):
            if tag not in tag_ids:
                errors.append(f"{path.relative_to(ROOT)}: tag sconosciuto {tag!r}")
        for name in [entry.get("term_it"), entry.get("term_en"), *entry.get("aliases", [])]:
            if isinstance(name, str):
                names[name.casefold()].append(entry_id)
        status = entry.get("status")
        reviewed = entry.get("provenance", {}).get("human_reviewed")
        reviewed_on = entry.get("last_reviewed")
        if status in {"reviewed", "published"} and (not reviewed or reviewed_on is None):
            errors.append(f"{path.relative_to(ROOT)}: {status} richiede revisione umana e last_reviewed")
        if reviewed_on is not None:
            try:
                if date.fromisoformat(str(reviewed_on)) > date.today():
                    errors.append(f"{path.relative_to(ROOT)}: last_reviewed è nel futuro")
            except ValueError:
                pass

    for normalized, owners in names.items():
        unique_owners = sorted(set(owners))
        if len(unique_owners) > 1:
            errors.append(f"termine o alias duplicato {normalized!r}: {', '.join(unique_owners)}")

    known_ids = set(entries)
    for entry_id, (path, entry) in entries.items():
        for related_id in entry.get("related", []):
            if related_id == entry_id:
                errors.append(f"{path.relative_to(ROOT)}: un lemma non può rimandare a sé stesso")
            elif related_id not in known_ids:
                message = f"{path.relative_to(ROOT)}: related inesistente {related_id!r}"
                if entry.get("status") == "draft":
                    warnings.append(message)
                else:
                    errors.append(message)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Validazione fallita: {len(errors)} errori, {len(warnings)} avvisi.", file=sys.stderr)
        return 1
    print(f"Validazione completata: {len(entries)} lemmi, 0 errori, {len(warnings)} avvisi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
