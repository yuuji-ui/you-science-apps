#!/usr/bin/env python3
import re

ID_PATTERN = re.compile(r"\bREQ-(?:[A-Z]+-)+\d{3}\b")
RANGE_PATTERN = re.compile(r"\b(REQ-(?:[A-Z]+-)+)(\d{3})[〜~-](\d{3})\b")

def expand(text):
    refs = set(ID_PATTERN.findall(text))
    for prefix, start, end in RANGE_PATTERN.findall(text):
        a, b = int(start), int(end)
        refs.update(f"{prefix}{n:03d}" for n in range(min(a,b), max(a,b)+1))
    return refs

sample = "REQ-TST-018 REQ-EDU-CALC-001〜004 REQ-EDU-SIM-003"
expected = {
    "REQ-TST-018",
    "REQ-EDU-CALC-001", "REQ-EDU-CALC-002",
    "REQ-EDU-CALC-003", "REQ-EDU-CALC-004",
    "REQ-EDU-SIM-003",
}
assert expand(sample) == expected
print("PASS: hierarchical IDs and ranges")
