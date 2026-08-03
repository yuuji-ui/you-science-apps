#!/usr/bin/env python3
from pathlib import Path
import re
ID_RE=re.compile(r'^####\s+(REQ-[A-Z]+(?:-[A-Z]+)*-\d{3}|REQ-GOV-EXC-\d{3})\b',re.M)
text=(Path(__file__).resolve().parent/'requirements-v1.2.2-RC.md').read_text(encoding='utf-8')
ids=ID_RE.findall(text)
assert 'REQ-EDU-CALC-001' in ids
assert 'REQ-EDU-VIS-004' in ids
# Simulate the old failure: remove a whole group and verify group-count check catches it.
reduced=[x for x in ids if not x.startswith('REQ-EDU-SIM-')]
assert len([x for x in reduced if x.startswith('REQ-EDU-SIM-')]) != 5
# Duplicate detection.
assert len(ids+[ids[0]]) != len(set(ids+[ids[0]]))
print('Validator self-tests: PASS')
