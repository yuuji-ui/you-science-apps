\
#!/usr/bin/env python3
"""Validate requirement references in an Architecture Markdown document."""

from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ID_PATTERN = re.compile(r"\bREQ-(?:[A-Z]+-)+\d{3}\b")
RANGE_PATTERN = re.compile(
    r"\b(REQ-(?:[A-Z]+-)+)(\d{3})[〜~-](\d{3})\b"
)

def expand_references(text: str) -> set[str]:
    refs = set(ID_PATTERN.findall(text))
    for prefix, start, end in RANGE_PATTERN.findall(text):
        a, b = int(start), int(end)
        if a > b:
            a, b = b, a
        refs.update(f"{prefix}{n:03d}" for n in range(a, b + 1))
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
    version_marker = f"YSA-REQ-001 Ver.{expected_version}"
    version_ok = version_marker in text

    report = {
        "document": doc_path.name,
        "requirementsDocument": index["documentId"],
        "requirementsVersion": expected_version,
        "referenceCount": len(refs),
        "invalidReferences": invalid,
        "versionReferenceValid": version_ok,
        "errors": len(invalid) + (0 if version_ok else 1),
        "warnings": 0,
        "result": "PASS" if not invalid and version_ok else "FAIL"
    }
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["result"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
