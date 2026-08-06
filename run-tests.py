#!/usr/bin/env python3
from pathlib import Path
import importlib.util
import subprocess
import sys

ROOT=Path(__file__).resolve().parent

if importlib.util.find_spec("jsonschema") is None:
    print("必要なPython依存関係がありません。")
    print("次を実行してください:")
    print("  python -m pip install -r requirements.txt")
    raise SystemExit(2)

tests=[
    ROOT/"platform/manifest/tests/test-manifest-schema.py",
    ROOT/"platform/catalog/tests/test-catalog-generator.py",
    ROOT/"platform/portal/tests/test-portal.py",
    ROOT/"platform/tools/app-registration-wizard/tests/test-wizard.py",
    ROOT/"platform/tools/app-update-wizard/tests/test-update-wizard.py",
    ROOT/"platform/tools/classification-editor/tests/test-classification-editor.py",
]

failed=[]
for test in tests:
    print(f"\n=== {test.relative_to(ROOT)} ===")
    proc=subprocess.run([sys.executable,str(test)],cwd=ROOT)
    if proc.returncode!=0:
        failed.append(str(test.relative_to(ROOT)))

if failed:
    print("\nFAILED:")
    for item in failed:
        print("-",item)
    raise SystemExit(1)

print("\nALL TESTS PASS")
