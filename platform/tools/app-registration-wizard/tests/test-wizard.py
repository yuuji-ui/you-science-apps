#!/usr/bin/env python3
from pathlib import Path
import json
import shutil
import subprocess
import sys

from jsonschema import Draft202012Validator, FormatChecker

TEST_DIR=Path(__file__).resolve().parent
WIZARD_DIR=TEST_DIR.parent
REPO=WIZARD_DIR.parents[2]

NODE=shutil.which("node")
if not NODE:
    raise SystemExit(
        "Node.jsが見つかりません。教材追加ウィザードの生成ロジック検証にはNode.jsが必要です。"
    )

schema=json.loads(
    (REPO/"platform/manifest/schemas/app-manifest.schema.json").read_text(encoding="utf-8")
)
validator=Draft202012Validator(schema,format_checker=FormatChecker())

def run(mode):
    proc=subprocess.run(
        [NODE,str(TEST_DIR/"generate-fixture.js"),mode],
        capture_output=True,
        text=True
    )
    if proc.returncode!=0:
        print(proc.stdout)
        print(proc.stderr)
        raise SystemExit(1)
    return json.loads(proc.stdout)

offline=run("offline")
assert offline["ok"] is True
assert offline["manifest"]["network"]=={
    "required":False,
    "externalEndpoints":[]
}
assert offline["manifest"]["privacy"]["externalTransmission"] is False
errors=list(validator.iter_errors(offline["manifest"]))
for error in errors:
    print("OFFLINE ERROR",list(error.path),error.message)
assert not errors

network=run("network")
assert network["ok"] is True
assert network["manifest"]["network"]=={
    "required":True,
    "externalEndpoints":["https://api.example.org/data"]
}
assert network["manifest"]["privacy"]["externalTransmission"] is False
errors=list(validator.iter_errors(network["manifest"]))
for error in errors:
    print("NETWORK ERROR",list(error.path),error.message)
assert not errors

missing=run("network-missing-endpoint")
assert missing["ok"] is False
assert any("通信先URL" in message for message in missing["errors"])

html=(WIZARD_DIR/"index.html").read_text(encoding="utf-8")
assert 'src="./wizard-core.js"' in html
assert 'id="externalEndpoints"' in html

print("PASS offline manifest generation and schema validation")
print("PASS network manifest generation and schema validation")
print("PASS missing endpoint rejection")
print("ALL TESTS PASS")
