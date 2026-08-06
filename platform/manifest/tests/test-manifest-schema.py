#!/usr/bin/env python3
from pathlib import Path
import json
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/"schemas/app-manifest.schema.json").read_text(encoding="utf-8"))
validator=Draft202012Validator(SCHEMA,format_checker=FormatChecker())

valid=ROOT/"examples/valid/app.manifest.json"
invalids=[
 ROOT/"examples/invalid/analytics-enabled.json",
 ROOT/"examples/invalid/invalid-app-id.json",
 ROOT/"examples/invalid/portable-shared.json",
]

data=json.loads(valid.read_text(encoding="utf-8"))
errors=list(validator.iter_errors(data))
print(("PASS" if not errors else "FAIL"),valid)
for error in errors: print("-",list(error.path),error.message)
if errors: raise SystemExit(1)

for path in invalids:
 data=json.loads(path.read_text(encoding="utf-8"))
 errors=list(validator.iter_errors(data))
 print(("PASS" if errors else "FAIL"),path)
 if not errors: raise SystemExit(1)

print("ALL TESTS PASS")
