#!/usr/bin/env python3
from pathlib import Path
import tempfile, subprocess, json, sys
validator=Path(__file__).with_name('validate-review-package.py')
with tempfile.TemporaryDirectory() as td:
 r=Path(td); req=r/'req.md'; arch=r/'arch.md'; gov=r/'gov.md'; adr=r/'adr.md'; report=r/'report.json'
 req.write_text('| 文書ID | YSA-REQ-001 |\n| バージョン | 1.2.3 |\n| 対応Architecture | YSA-ARCH-001 Ver.1.1.5 RC |\n| 対応Governance | YSA-GOV-001 Ver.1.1.2 RC |',encoding='utf-8')
 arch.write_text('| 文書ID | YSA-ARCH-001 |\n| バージョン | 1.1.5 |\n| 対応Requirements | YSA-REQ-001 Ver.1.2.3 RC |\n| 対応Governance | YSA-GOV-001 Ver.1.1.2 RC |\nADR-0011 教材Level客観判定',encoding='utf-8')
 gov.write_text('| 文書ID | YSA-GOV-001 |\n| バージョン | 1.1.2 |\n| 対応Requirements | YSA-REQ-001 Ver.1.2.3 RC |\n| 対応Architecture | YSA-ARCH-001 Ver.1.1.5 RC |\nADR-0011 教材Level客観判定',encoding='utf-8')
 adr.write_text('ADR-0011 教材Level客観判定\n0〜8点\n9〜16点\n17〜24点\n強制Level C条件',encoding='utf-8')
 cmd=[sys.executable,str(validator),str(req),str(arch),str(gov),str(adr),str(report)]
 ok=subprocess.run(cmd,capture_output=True,text=True); assert ok.returncode==0,ok.stdout+ok.stderr
 req.write_text(req.read_text(encoding='utf-8').replace('Ver.1.1.5','Ver.1.1.4'),encoding='utf-8')
 bad=subprocess.run(cmd,capture_output=True,text=True); assert bad.returncode==1
 print('PASS: valid package accepted and stale cross-version rejected')
