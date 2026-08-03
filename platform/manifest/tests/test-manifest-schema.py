#!/usr/bin/env python3
"""Regression tests for the app manifest schema."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "validate-manifest.py"
SCHEMA = ROOT / "schemas" / "app-manifest.schema.json"


def run(path: Path) -> int:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(SCHEMA), str(path)],
        text=True,
        capture_output=True,
    )
    print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    return result.returncode


def main() -> int:
    valid = ROOT / "examples" / "valid" / "app.manifest.json"
    invalid_files = sorted((ROOT / "examples" / "invalid").glob("*.json"))

    if run(valid) != 0:
        print("TEST FAIL: valid example was rejected.")
        return 1

    for path in invalid_files:
        if run(path) == 0:
            print(f"TEST FAIL: invalid example was accepted: {path.name}")
            return 1

    print("ALL TESTS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
