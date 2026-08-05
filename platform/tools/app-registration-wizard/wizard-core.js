(function(root,factory){
  const api=factory();
  if(typeof module==="object" && module.exports){
    module.exports=api;
  }else{
    root.YSAWizardCore=api;
  }
})(typeof globalThis!=="undefined"?globalThis:this,function(){
  "use strict";

  function csv(value){
    return String(value||"").split(",").map(v=>v.trim()).filter(Boolean);
  }

  function lines(value){
    return String(value||"").split(/\r?\n/).map(v=>v.trim()).filter(Boolean);
  }

  function normalizeEndpoints(value){
    return String(value||"")
      .split(/[\n,]/)
      .map(v=>v.trim())
      .filter(Boolean);
  }

  function validateInput(input){
    const errors=[];
    if(!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(input.appId||"")){
      errors.push("appIdは小文字英数字とハイフンで入力してください。");
    }
    if(!String(input.title||"").trim()){
      errors.push("教材名を入力してください。");
    }

    const endpoints=normalizeEndpoints(input.externalEndpoints);
    if(input.networkRequired && endpoints.length===0){
      errors.push("外部通信が必要な場合は、通信先URLを1件以上入力してください。");
    }
    if(!input.networkRequired && endpoints.length>0){
      errors.push("外部通信を使用しない場合は、通信先URLを空欄にしてください。");
    }

    for(const endpoint of endpoints){
      try{
        const url=new URL(endpoint);
        if(!["https:","http:"].includes(url.protocol)){
          errors.push(`通信先URLはhttpまたはhttpsを使用してください: ${endpoint}`);
        }
      }catch{
        errors.push(`通信先URLの形式が正しくありません: ${endpoint}`);
      }
    }

    return {errors,endpoints};
  }

  function generateRegistration(input){
    const checked=validateInput(input);
    if(checked.errors.length){
      return {ok:false,errors:checked.errors};
    }

    const audience=input.audience;
    const group=input.group;
    const difficulty=Number(input.learningDifficulty);
    const schoolStage=audience.startsWith("JH")?"junior-high":"senior-high";
    const subjectMap={
      "senior-high-physics":"physics",
      "senior-high-chemistry":"chemistry",
      "senior-high-biology":"biology",
      "senior-high-earth-science":"earth-science",
      "junior-high-science":"science",
      "other":"science"
    };
    const grade=audience.startsWith("JH")?audience:"other";
    const folder=`site/apps/${schoolStage}/${input.folderField}/${input.appId}/`;

    const manifest={
      schemaVersion:"1.0.0",
      appId:input.appId,
      title:input.title.trim(),
      version:input.version.trim(),
      updatedOn:input.updatedOn,
      status:"active",
      level:input.level,
      education:{
        schoolStage,
        subjects:[subjectMap[group]],
        grades:[grade],
        portalGroups:[group],
        audiences:[audience],
        categories:csv(input.categories),
        tags:csv(input.tags),
        learningDifficulty:difficulty,
        units:[input.unit.trim()],
        appTypes:[input.appType],
        learningGoals:lines(input.learningGoals),
        useCases:["lesson-practice","home-study"],
        modelLimitations:[
          "教材固有のモデル上の限界を確認し、必要に応じて編集してください。"
        ]
      },
      platform:{
        sourceDependencyMode:"self-contained",
        coreVersion:null,
        referenceImplementations:[]
      },
      distribution:{
        hosted:{enabled:true,dependencyMode:"self-contained"},
        portable:{
          enabled:true,
          dependencyMode:"self-contained",
          directFileOpen:true
        },
        standalonePackage:{
          enabled:true,
          dependencyMode:"self-contained"
        }
      },
      storage:{
        enabled:Boolean(input.storageEnabled),
        types:input.storageEnabled?["localStorage"]:[],
        deletionMethod:input.storageEnabled
          ?"教材内の消去機能またはブラウザ設定から削除する。"
          :"保存データはありません。"
      },
      network:{
        required:Boolean(input.networkRequired),
        externalEndpoints:checked.endpoints
      },
      privacy:{
        collectsPersonalData:false,
        usesAnalytics:false,
        usesCookies:false,
        externalTransmission:false
      },
      accessibility:{
        keyboardSupported:true,
        dragAlternativeProvided:true,
        colorIndependentFeedback:true,
        reducedMotionSupported:true
      },
      license:{
        code:"TBD",
        content:"TBD",
        thirdPartyNotices:[]
      },
      owners:{
        appOwnerRole:`${input.title.trim()} App Owner`,
        maintainerRole:"You Science Apps Platform Maintainer"
      },
      links:{
        hostedUrl:`./apps/${schoolStage}/${input.folderField}/${input.appId}/`,
        repositoryPath:folder.replace(/\/$/,"")
      }
    };

    const override={
      [input.appId]:{
        featured:Boolean(input.featured),
        hidden:false,
        sortOrder:Number(input.sortOrder),
        labels:csv(input.labels),
        deprecatedMessage:null
      }
    };

    const groupItem={
      groupId:`${input.appId}-group`,
      title:csv(input.categories)[0]||input.title.trim(),
      description:`${input.title.trim()}に関連する教材`,
      appIds:[input.appId],
      sortOrder:Number(input.sortOrder)
    };

    return {
      ok:true,
      folder,
      manifest,
      override,
      groupItem
    };
  }

  function difficultyLabel(score){
    if(score<=2)return "基本";
    if(score<=4)return "標準";
    return "応用";
  }

  return {
    csv,
    lines,
    normalizeEndpoints,
    validateInput,
    generateRegistration,
    difficultyLabel
  };
});
