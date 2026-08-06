#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, shutil

ROOT=Path(__file__).resolve().parents[1]
NODE=shutil.which("node")
if not NODE: raise SystemExit("Node.js is required")
script=r"""
const core=require(process.argv[1]);
const source={
 appId:"test-app",title:"テスト",version:"1.0.0",updatedOn:"2026-08-01",status:"active",
 education:{learningDifficulty:3,portalGroups:["junior-high-science"],audiences:["JH2"],categories:["電流"],tags:["旧"],learningGoals:["旧目標"],modelLimitations:[]}
};
const result=core.updateManifest(source,{
 version:"1.1.0",updatedOn:"2026-08-06",status:"maintenance",learningDifficulty:4,
 portalGroups:"junior-high-science",audiences:"JH2",categories:"電流, 回路",tags:"新, 更新",
 learningGoals:"新目標",modelLimitations:"近似モデル"
});
console.log(JSON.stringify(result));
"""
proc=subprocess.run([NODE,"-e",script,str(ROOT/"update-core.js")],capture_output=True,text=True)
assert proc.returncode==0,proc.stderr
data=json.loads(proc.stdout)
assert data["ok"] is True
assert data["manifest"]["version"]=="1.1.0"
assert data["manifest"]["education"]["categories"]==["電流","回路"]
print("ALL TESTS PASS")
