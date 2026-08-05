#!/usr/bin/env python3
"""Compatibility wrapper.

The canonical Catalog Generator lives at:
platform/catalog/tools/generate-catalog.py

This wrapper prevents old pipeline references from duplicating implementation.
"""

from __future__ import annotations
import runpy
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
CANONICAL = REPOSITORY_ROOT / "platform" / "catalog" / "tools" / "generate-catalog.py"

if not CANONICAL.exists():
    raise SystemExit(f"Canonical generator not found: {CANONICAL}")

runpy.run_path(str(CANONICAL), run_name="__main__")
