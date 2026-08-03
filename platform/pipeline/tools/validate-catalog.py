#!/usr/bin/env python3
"""Validate generated catalog and catalog source files."""

from __future__ import annotations
import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker


def validate(schema_path: Path, data_path: Path) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = json.loads(data_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        location = "$" + ("." + ".".join(map(str,error.path)) if error.path else "")
        errors.append(f"{location}: {error.message}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("schema")
    parser.add_argument("data")
    args = parser.parse_args()
    errors = validate(Path(args.schema), Path(args.data))
    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
