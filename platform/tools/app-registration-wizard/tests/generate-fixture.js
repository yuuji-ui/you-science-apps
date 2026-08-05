#!/usr/bin/env node
const fs=require("fs");
const path=require("path");
const core=require(path.resolve(__dirname,"../wizard-core.js"));

const mode=process.argv[2]||"offline";

const base={
  appId:"test-science-app",
  title:"テスト教材",
  version:"1.0.0",
  updatedOn:"2026-08-05",
  level:"B",
  learningDifficulty:3,
  group:"junior-high-science",
  audience:"JH2",
  categories:"電流と回路",
  tags:"電流, テスト",
  appType:"simulation",
  unit:"JH2.PHYS.TEST",
  learningGoals:"学習目標を確認する。",
  folderField:"physics",
  featured:false,
  sortOrder:100,
  labels:"中2",
  storageEnabled:false
};

if(mode==="offline"){
  base.networkRequired=false;
  base.externalEndpoints="";
}
if(mode==="network"){
  base.networkRequired=true;
  base.externalEndpoints="https://api.example.org/data";
}
if(mode==="network-missing-endpoint"){
  base.networkRequired=true;
  base.externalEndpoints="";
}

const result=core.generateRegistration(base);
process.stdout.write(JSON.stringify(result,null,2));
