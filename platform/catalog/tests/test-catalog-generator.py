#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, sys, tempfile
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]

with tempfile.TemporaryDirectory() as td:
 out=Path(td)/"catalog.json"
 p=subprocess.run([
   sys.executable,str(ROOT/"tools/generate-catalog.py"),
   "--apps-dir",str(ROOT/"examples/apps"),
   "--override",str(ROOT/"examples/catalog-source/catalog.override.json"),
   "--groups",str(ROOT/"examples/catalog-source/catalog-groups.json"),
   "--output",str(out)
 ],text=True,capture_output=True)
 print(p.stdout,p.stderr)
 assert p.returncode==0,p.stderr
 catalog=json.loads(out.read_text(encoding="utf-8"))
 assert catalog["schemaVersion"]=="1.1.0"
 assert len(catalog["apps"])==2
 assert all("learningDifficulty" in app for app in catalog["apps"])
 assert all("portalGroups" in app for app in catalog["apps"])
 assert all("level" not in app for app in catalog["apps"])
 schema=json.loads((ROOT/"schemas/catalog.schema.json").read_text(encoding="utf-8"))
 errors=list(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(catalog))
 for error in errors: print(error.message)
 assert not errors

print("ALL TESTS PASS")
