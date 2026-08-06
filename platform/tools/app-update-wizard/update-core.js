(function(root,factory){
  const api=factory();
  if(typeof module==="object"&&module.exports)module.exports=api;
  else root.YSAUpdateCore=api;
})(typeof globalThis!=="undefined"?globalThis:this,function(){
"use strict";
function csv(value){return String(value||"").split(",").map(v=>v.trim()).filter(Boolean)}
function lines(value){return String(value||"").split(/\r?\n/).map(v=>v.trim()).filter(Boolean)}
function parseManifest(text){
  try{
    const value=JSON.parse(text);
    if(!value||typeof value!=="object"||Array.isArray(value))throw new Error();
    return {ok:true,manifest:value};
  }catch{
    return {ok:false,errors:["Manifest JSONを読み込めません。"]}
  }
}
function updateManifest(original,input){
  const manifest=JSON.parse(JSON.stringify(original));
  const errors=[];
  if(!manifest.appId)errors.push("appIdがありません。");
  if(!input.version.trim())errors.push("Versionを入力してください。");
  if(!/^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$/.test(input.version.trim())){
    errors.push("Versionは1.2.3の形式で入力してください。");
  }
  if(!input.updatedOn)errors.push("更新日を入力してください。");
  if(errors.length)return {ok:false,errors};

  manifest.version=input.version.trim();
  manifest.updatedOn=input.updatedOn;
  manifest.status=input.status;
  manifest.education.learningDifficulty=Number(input.learningDifficulty);
  manifest.education.portalGroups=csv(input.portalGroups);
  manifest.education.audiences=csv(input.audiences);
  manifest.education.categories=csv(input.categories);
  manifest.education.tags=csv(input.tags);
  manifest.education.learningGoals=lines(input.learningGoals);
  manifest.education.modelLimitations=lines(input.modelLimitations);
  return {ok:true,manifest};
}
function overridePatch(appId,input){
  return {
    [appId]:{
      featured:Boolean(input.featured),
      hidden:Boolean(input.hidden),
      sortOrder:Number(input.sortOrder),
      labels:csv(input.labels),
      deprecatedMessage:input.deprecatedMessage.trim()||null
    }
  };
}
return {csv,lines,parseManifest,updateManifest,overridePatch};
});