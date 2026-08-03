\
#!/usr/bin/env python3
import re
ID_PATTERN = re.compile(r"\bREQ-(?:[A-Z]+-)+\d{3}\b")
RANGE_PATTERN = re.compile(r"\b(REQ-(?:[A-Z]+-)+)(\d{3})[〜~-](\d{3})\b")
def expand(text):
    refs=set(ID_PATTERN.findall(text))
    for prefix,a,b in RANGE_PATTERN.findall(text):
        a,b=int(a),int(b)
        refs.update(f"{prefix}{n:03d}" for n in range(min(a,b),max(a,b)+1))
    return refs
sample="REQ-GOV-006〜016 REQ-CAT-008 REQ-EDU-SIM-001〜005"
actual=expand(sample)
assert "REQ-GOV-006" in actual and "REQ-GOV-016" in actual
assert "REQ-CAT-008" in actual
assert "REQ-EDU-SIM-001" in actual and "REQ-EDU-SIM-005" in actual
print("PASS: hierarchical and range references")
