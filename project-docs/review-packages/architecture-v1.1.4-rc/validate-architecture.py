#!/usr/bin/env python3
"""Validate Architecture requirement references and synchronization markers."""

from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ID_PATTERN = re.compile(r"\bREQ-(?:[A-Z]+-)+\d{3}\b")
RANGE_PATTERN = re.compile(r"\b(REQ-(?:[A-Z]+-)+)(\d{3})[〜~-](\d{3})\b")

def expand_references(text: str) -> set[str]:
    refs = set(ID_PATTERN.findall(text))
    for prefix, start, end in RANGE_PATTERN.findall(text):
        a, b = int(start), int(end)
        refs.update(f"{prefix}{n:03d}" for n in range(min(a, b), max(a, b) + 1))
    return refs

def main() -> int:
    if len(sys.argv) != 4:
        print("Usage: validate-architecture.py ARCH.md requirement-index.json REPORT.json")
        return 2

    doc_path = Path(sys.argv[1])
    index_path = Path(sys.argv[2])
    report_path = Path(sys.argv[3])

    text = doc_path.read_text(encoding="utf-8")
    index = json.loads(index_path.read_text(encoding="utf-8"))
    valid = {item["id"] for item in index["requirements"]}
    refs = expand_references(text)
    invalid = sorted(refs - valid)
    expected_version = index["documentVersion"]

    checks = {
        "requirements_references_valid": len(invalid) == 0,
        "requirements_version_valid": f"YSA-REQ-001 Ver.{expected_version}" in text,
        "section12_source_mode_present": "### 12.1 Source Dependency Mode" in text,
        "section12_distribution_mode_present": "### 12.2 Distribution Dependency Mode" in text,
        "portable_shared_forbidden_section12": "Portable成果物が`shared`のままになる構成は許可しない" in text,
        "section12_refers_27_4": "詳細な許容組み合わせとSchema禁則は第27.4章を正本とする" in text,
        "dist_hosted_in_tree": "│  ├─ hosted/" in text,
        "schema_implementation_status_clear": "Manifest Schema Specification工程で実装・検証する" in text,
    }

    errors = sum(1 for value in checks.values() if not value)
    report = {
        "document": doc_path.name,
        "requirementsVersion": expected_version,
        "automatedValidation": {
            "referenceCount": len(refs),
            "invalidReferences": invalid,
            "checks": checks,
            "errors": errors,
            "warnings": 0,
            "result": "PASS" if errors == 0 else "FAIL"
        }
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if errors == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
