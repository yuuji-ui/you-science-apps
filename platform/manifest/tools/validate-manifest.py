#!/usr/bin/env python3
"""Validate a You Science Apps app.manifest.json file."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    print("ERROR: jsonschema is not installed.")
    print("Install with: python -m pip install jsonschema")
    raise SystemExit(2)


def validate_manifest(schema_path: Path, manifest_path: Path) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(manifest), key=lambda e: list(e.path)):
        location = "$"
        if error.path:
            location += "." + ".".join(str(part) for part in error.path)
        errors.append(f"{location}: {error.message}")
    return errors


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: validate-manifest.py SCHEMA.json app.manifest.json")
        return 2

    schema_path = Path(sys.argv[1])
    manifest_path = Path(sys.argv[2])

    try:
        errors = validate_manifest(schema_path, manifest_path)
    except FileNotFoundError as exc:
        print(f"ERROR: file not found: {exc.filename}")
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}")
        return 2

    if errors:
        print(f"FAIL: {manifest_path}")
        for item in errors:
            print(f"- {item}")
        return 1

    print(f"PASS: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
