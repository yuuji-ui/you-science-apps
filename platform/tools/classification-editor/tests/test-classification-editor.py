#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, shutil
ROOT=Path(__file__).resolve().parents[1]
NODE=shutil.which("node")
if not NODE: raise SystemExit("Node.js is required")
script=r"""
const core=require(process.argv[1]);
const m={appId:"x",education:{portalGroups:["old"],audiences:["JH1"],categories:["旧"],tags:["旧"]},privacy:{externalTransmission:false}};
const r=core.apply(m,{portalGroups:"junior-high-science",audiences:"JH2",categories:"電流, 回路",tags:"計算, 可視化"});
console.log(JSON.stringify(r));
"""
proc=subprocess.run([NODE,"-e",script,str(ROOT/"classification-core.js")],capture_output=True,text=True)
assert proc.returncode==0,proc.stderr
data=json.loads(proc.stdout)
assert data["ok"] is True
assert data["manifest"]["education"]["tags"]==["計算","可視化"]
assert data["manifest"]["privacy"]["externalTransmission"] is False
print("ALL TESTS PASS")
