#!/usr/bin/env python3
from pathlib import Path
import runpy

ROOT=Path(__file__).resolve().parents[3]
CANONICAL=ROOT/"platform/catalog/tools/generate-catalog.py"
if not CANONICAL.exists():
    raise SystemExit(f"Canonical generator not found: {CANONICAL}")
runpy.run_path(str(CANONICAL),run_name="__main__")
