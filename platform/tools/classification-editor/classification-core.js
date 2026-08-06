(function(root,factory){
const api=factory();if(typeof module==="object"&&module.exports)module.exports=api;else root.YSAClassCore=api;
})(typeof globalThis!=="undefined"?globalThis:this,function(){
"use strict";
function csv(value){return String(value||"").split(",").map(v=>v.trim()).filter(Boolean)}
function parse(text){try{const m=JSON.parse(text);return {ok:true,manifest:m}}catch{return {ok:false,errors:["JSONを読み込めません。"]}}}
function apply(manifest,input){
 const m=JSON.parse(JSON.stringify(manifest));
 if(!m.education)return {ok:false,errors:["educationがありません。"]};
 m.education.portalGroups=csv(input.portalGroups);
 m.education.audiences=csv(input.audiences);
 m.education.categories=csv(input.categories);
 m.education.tags=csv(input.tags);
 return {ok:true,manifest:m};
}
return {csv,parse,apply};
});