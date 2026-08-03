#!/usr/bin/env python3
from pathlib import Path
import re, json, sys

ROOT=Path(__file__).resolve().parent
MD=ROOT/'requirements-v1.2.2-RC.md'
IDX=ROOT/'requirement-index.json'
ID_RE=re.compile(r'^####\s+(REQ-[A-Z]+(?:-[A-Z]+)*-\d{3}|REQ-GOV-EXC-\d{3})\b',re.M)
REQUIRED_GROUPS={
 'REQ-EDU-CALC':4,
 'REQ-EDU-SIM':5,
 'REQ-EDU-DRAG':3,
 'REQ-EDU-EXP':4,
 'REQ-EDU-VIS':4,
}
text=MD.read_text(encoding='utf-8')
index=json.loads(IDX.read_text(encoding='utf-8'))
md_ids=ID_RE.findall(text)
idx_ids=[x['id'] for x in index['requirements']]
errors=[]; warnings=[]
if len(md_ids)!=len(set(md_ids)):
 errors.append('Duplicate requirement IDs in Markdown')
if len(idx_ids)!=len(set(idx_ids)):
 errors.append('Duplicate requirement IDs in index')
if set(md_ids)!=set(idx_ids):
 errors.append(f'Markdown/index mismatch: only-md={sorted(set(md_ids)-set(idx_ids))}, only-index={sorted(set(idx_ids)-set(md_ids))}')
if index.get('requirementCount')!=len(idx_ids):
 errors.append('requirementCount does not match index length')
for prefix,count in REQUIRED_GROUPS.items():
 found=[x for x in md_ids if x.startswith(prefix+'-')]
 if len(found)!=count:
  errors.append(f'Missing hierarchical group {prefix}: expected {count}, found {len(found)}')
# Check ordinary category continuity and hierarchical group continuity.
groups={}
for rid in md_ids:
 m=re.match(r'^(REQ-(?:[A-Z]+-)+)(\d{3})$',rid)
 if not m: continue
 groups.setdefault(m.group(1),[]).append(int(m.group(2)))
for prefix,nums in groups.items():
 nums=sorted(nums)
 missing=sorted(set(range(min(nums),max(nums)+1))-set(nums))
 if missing:
  errors.append(f'Gap in {prefix}: {missing}')
# Provenance field completeness.
for row in index['requirements']:
 for key in ['introducedIn','source','status','priority','verification']:
  if key not in row or row[key] in ('',None):
   errors.append(f'Missing provenance field {key}: {row.get("id")}')
report={
 'documentId':index['documentId'],'documentVersion':index['documentVersion'],
 'validatorVersion':'1.0.0','checkedFiles':[MD.name,IDX.name],
 'markdownRequirementCount':len(md_ids),'indexRequirementCount':len(idx_ids),
 'errors':errors,'warnings':warnings,'result':'PASS' if not errors else 'FAIL'
}
(ROOT/'validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
