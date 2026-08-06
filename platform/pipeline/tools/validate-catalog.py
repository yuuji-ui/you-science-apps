#!/usr/bin/env python3
"""Compatibility wrapper for the canonical Catalog Validator."""
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[3]
CANONICAL=ROOT/"platform/catalog/tools/validate-catalog.py"
if not CANONICAL.exists():
    raise SystemExit(f"Canonical validator not found: {CANONICAL}")
runpy.run_path(str(CANONICAL),run_name="__main__")
