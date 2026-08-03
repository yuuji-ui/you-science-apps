\
#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path
P={
'document_id':re.compile(r'\| 文書ID \| ([^|]+) \|'),
'version':re.compile(r'\| バージョン \| ([^|]+) \|'),
'requirements':re.compile(r'\| 対応Requirements \| ([^|]+) \|'),
'architecture':re.compile(r'\| 対応Architecture \| ([^|]+) \|'),
'governance':re.compile(r'\| 対応Governance \| ([^|]+) \|')}
def meta(path):
 t=Path(path).read_text(encoding='utf-8'); d={'text':t}
 for k,p in P.items():
  m=p.search(t); d[k]=m.group(1).strip() if m else None
 return d
def main():
 if len(sys.argv)!=6:return 2
 req,arch,gov=map(meta,sys.argv[1:4]); adr=Path(sys.argv[4]).read_text(encoding='utf-8'); out=Path(sys.argv[5])
 checks={
 'req_version':req['version']=='1.2.3','arch_version':arch['version']=='1.1.5','gov_version':gov['version']=='1.1.2',
 'req_to_arch':req['architecture']=='YSA-ARCH-001 Ver.1.1.5 RC','req_to_gov':req['governance']=='YSA-GOV-001 Ver.1.1.2 RC',
 'arch_to_req':arch['requirements']=='YSA-REQ-001 Ver.1.2.3 RC','arch_to_gov':arch['governance']=='YSA-GOV-001 Ver.1.1.2 RC',
 'gov_to_req':gov['requirements']=='YSA-REQ-001 Ver.1.2.3 RC','gov_to_arch':gov['architecture']=='YSA-ARCH-001 Ver.1.1.5 RC',
 'adr_exists':'ADR-0011 教材Level客観判定' in adr,'arch_refers_adr':'ADR-0011 教材Level客観判定' in arch['text'],
 'gov_refers_adr':'ADR-0011 教材Level客観判定' in gov['text'],'thresholds':all(x in adr for x in ['0〜8点','9〜16点','17〜24点']),
 'forced_c':'強制Level C条件' in adr}
 errors=[k for k,v in checks.items() if not v]; report={'checks':checks,'errorItems':errors,'errors':len(errors),'warnings':0,'result':'PASS' if not errors else 'FAIL'}
 out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps(report,ensure_ascii=False,indent=2)); return 0 if not errors else 1
if __name__=='__main__':raise SystemExit(main())
