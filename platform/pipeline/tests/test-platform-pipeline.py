#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]

def command(output,report):
 return [
   sys.executable,str(ROOT/"tools/run-platform-pipeline.py"),
   "--apps-dir",str(ROOT/"examples/apps"),
   "--manifest-schema",str(REPO/"platform/manifest/schemas/app-manifest.schema.json"),
   "--catalog-generator",str(REPO/"platform/catalog/tools/generate-catalog.py"),
   "--catalog-validator",str(REPO/"platform/catalog/tools/validate-catalog.py"),
   "--catalog-schema",str(REPO/"platform/catalog/schemas/catalog.schema.json"),
   "--override",str(ROOT/"examples/catalog-source/catalog.override.json"),
   "--groups",str(ROOT/"examples/catalog-source/catalog-groups.json"),
   "--output",str(output),
   "--report",str(report),
 ]

def main():
 with tempfile.TemporaryDirectory() as td:
  td=Path(td)
  out=td/"catalog.json"
  report=td/"report.json"
  cmd=command(out,report)
  p=subprocess.run(cmd,text=True,capture_output=True)
  print(p.stdout,end="")
  assert p.returncode==0,p.stderr
  data=json.loads(report.read_text(encoding="utf-8"))
  assert data["result"]=="PASS"
  catalog=json.loads(out.read_text(encoding="utf-8"))
  assert len(catalog["apps"])==2
  assert all("level" not in app for app in catalog["apps"])

  bad_path=ROOT/"examples/apps/mole-calculation/app.manifest.json"
  original=bad_path.read_text(encoding="utf-8")
  bad=json.loads(original)
  bad["privacy"]["usesAnalytics"]=True
  bad_path.write_text(json.dumps(bad,ensure_ascii=False,indent=2),encoding="utf-8")
  try:
   p=subprocess.run(cmd,text=True,capture_output=True)
   assert p.returncode==1
   data=json.loads(report.read_text(encoding="utf-8"))
   assert data["result"]=="FAIL"
   assert any("Manifest validation failed" in x for x in data["errors"])
  finally:
   bad_path.write_text(original,encoding="utf-8")

 print("ALL TESTS PASS")
 return 0

if __name__=="__main__":
 raise SystemExit(main())
