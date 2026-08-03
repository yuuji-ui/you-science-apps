#!/usr/bin/env python3
from __future__ import annotations
import json, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT/"tools"/"generate-catalog.py"
VAL = ROOT/"tools"/"validate-catalog.py"
SCHEMA = ROOT/"schemas"/"catalog.schema.json"
APPS = ROOT/"examples"/"apps"
OVERRIDE = ROOT/"examples"/"catalog-source"/"catalog.override.json"
GROUPS = ROOT/"examples"/"catalog-source"/"catalog-groups.json"


def run(cmd):
    return subprocess.run(cmd, text=True, capture_output=True)


def main():
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        out = td/"catalog.json"
        report = td/"report.json"

        p = run([sys.executable,str(GEN),"--apps-dir",str(APPS),"--override",str(OVERRIDE),"--groups",str(GROUPS),"--output",str(out),"--report",str(report)])
        print(p.stdout,end="")
        assert p.returncode == 0, p.stderr

        data = json.loads(out.read_text(encoding="utf-8"))
        assert len(data["apps"]) == 2
        assert data["apps"][0]["appId"] == "mole-calculation"
        assert data["apps"][0]["featured"] is True

        p = run([sys.executable,str(VAL),str(SCHEMA),str(out)])
        print(p.stdout,end="")
        assert p.returncode == 0

        # duplicate appId
        dup_apps = td/"apps"
        shutil.copytree(APPS, dup_apps)
        extra = dup_apps/"duplicate"
        extra.mkdir()
        shutil.copy2(APPS/"mole-calculation"/"app.manifest.json", extra/"app.manifest.json")
        p = run([sys.executable,str(GEN),"--apps-dir",str(dup_apps),"--override",str(OVERRIDE),"--groups",str(GROUPS),"--output",str(td/"dup.json")])
        assert p.returncode == 1
        assert "Duplicate appId" in p.stdout

        # unknown override
        bad_override = json.loads(OVERRIDE.read_text(encoding="utf-8"))
        bad_override["apps"]["unknown-app"] = {"featured": True}
        bad_path = td/"bad-override.json"
        bad_path.write_text(json.dumps(bad_override),encoding="utf-8")
        p = run([sys.executable,str(GEN),"--apps-dir",str(APPS),"--override",str(bad_path),"--groups",str(GROUPS),"--output",str(td/"bad.json")])
        assert p.returncode == 1
        assert "unknown or unpublished" in p.stdout

        print("ALL TESTS PASS")
        return 0

if __name__ == "__main__":
    raise SystemExit(main())
