#!/usr/bin/env python3
"""Genera dati derivati per sito ed EPUB a partire dal corpus canonico."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    validation = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate.py")], cwd=ROOT)
    if validation.returncode:
        return validation.returncode

    entries = []
    for path in sorted((ROOT / "entries").glob("*.yaml")):
        with path.open(encoding="utf-8") as handle:
            entries.append(yaml.safe_load(handle))
    entries.sort(key=lambda item: item["term_it"].casefold())

    payload = {
        "generated_on": date.today().isoformat(),
        "source": "entries/",
        "entries": entries,
    }
    for product in ("site", "epub"):
        destination = ROOT / "build" / product
        destination.mkdir(parents=True, exist_ok=True)
        (destination / "catalog.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print(f"Build completata: {len(entries)} lemmi per site ed epub.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
