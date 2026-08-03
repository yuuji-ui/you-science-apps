\
#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path

ID_PATTERN = re.compile(r"\bREQ-(?:[A-Z]+-)+\d{3}\b")
RANGE_PATTERN = re.compile(r"\b(REQ-(?:[A-Z]+-)+)(\d{3})[〜~-](\d{3})\b")

def expand(text: str) -> set[str]:
    refs=set(ID_PATTERN.findall(text))
    for prefix,a,b in RANGE_PATTERN.findall(text):
        a,b=int(a),int(b)
        refs.update(f"{prefix}{n:03d}" for n in range(min(a,b),max(a,b)+1))
    return refs

def main() -> int:
    if len(sys.argv)!=4:
        print("Usage: validate-governance.py GOVERNANCE.md requirement-index.json REPORT.json")
        return 2
    doc=Path(sys.argv[1])
    idx=Path(sys.argv[2])
    out=Path(sys.argv[3])
    text=doc.read_text(encoding="utf-8")
    data=json.loads(idx.read_text(encoding="utf-8"))
    valid={x["id"] for x in data["requirements"]}
    refs=expand(text)
    invalid=sorted(refs-valid)
    checks={
        "requirements_version_present": f"YSA-REQ-001 Ver.{data['documentVersion']}" in text,
        "organization_ownership_present": "## 6. Organization所有と権限" in text,
        "self_approval_prevention_present": "## 11. Level別承認" in text,
        "catalog_authority_present": "## 8. Portal Maintainer" in text,
        "automated_manual_separation_present": "## 23. Automated ValidationとManual Review" in text,
        "distribution_approval_present": "## 21. Distribution成果物の承認" in text,
        "joint_document_approval_present": "Requirements、Architecture、GovernanceはReview Package単位で合同承認する" in text,
    }
    errors=len(invalid)+sum(1 for v in checks.values() if not v)
    report={
        "document":doc.name,
        "referenceCount":len(refs),
        "invalidReferences":invalid,
        "checks":checks,
        "errors":errors,
        "warnings":0,
        "result":"PASS" if errors==0 else "FAIL"
    }
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if errors==0 else 1

if __name__=="__main__":
    raise SystemExit(main())
