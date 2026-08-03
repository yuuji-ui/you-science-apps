# You Science Apps Platform
# Architecture Specification Ver.1.1.5 RC

## 文書管理情報

| 項目 | 内容 |
|---|---|
| 文書名 | You Science Apps Platform Architecture Specification |
| 文書ID | YSA-ARCH-001 |
| バージョン | 1.1.5 |
| 状態 | Release Candidate / Draft |
| 前バージョン | 1.1.4 |
| 対象Platform | You Science Apps Platform Ver.1.0 |
| 対応Requirements | YSA-REQ-001 Ver.1.2.3 RC |
| 対応Governance | YSA-GOV-001 Ver.1.1.2 RC |
| 作成日 | 2026-08-03 |
| 文書責任者 | Project Owner |
| 設計担当 | ChatGPT |
| 第三者レビュー | Claude（未実施） |
| 参照検証状態 | Requirements参照自動検証済み |
| 改訂区分 | PATCH / Review修正 |

---

## 1. 本書の目的

本書はYou Science Apps Platformの技術構造、責任分界、依存関係、
公開方式、配布方式、データ配置、検証境界および移行可能性を定義する。

主な決定対象は次のとおりである。

1. GitHubリポジトリ構成
2. GitHub Pagesへの公開方式
3. 公開領域と管理文書領域の分離
4. Platform Coreと個別教材の境界
5. 教材データと教材ロジックの境界
6. Manifest、Catalog、Schemaの関係
7. 教材間および共通機能間の依存規則
8. Hosted、Portable、Standaloneの配布方式
9. 自動検証、Review Package、公開処理
10. 障害の局所化と長期移行

対応要求：
REQ-GOV-002、REQ-GOV-004、REQ-GOV-005、REQ-NFR-004、REQ-NFR-008、REQ-OPS-007

---

## 2. 訂正履歴

Architecture Ver.1.0の文書管理情報はRequirements Ver.1.0を参照すると記載しながら、
本文では後にVer.1.1で追加された要求IDを参照していた。

この不整合は文書管理情報の誤りであり、過去を遡及的に正当化しない。
Ver.1.1.1で訂正声明を記録し、本版でも履歴を保持する。

対応要求：
REQ-DOC-011、REQ-DOC-015、REQ-DOC-016

---

## 3. 意思決定の優先順位

Architecture上の判断が競合する場合はRequirementsの優先順位に従う。

1. 生徒の安全
2. Privacy
3. 科学的正確性
4. 教育効果
5. Accessibility
6. 操作性
7. 長期保守性
8. 可読性
9. 互換性
10. 拡張性
11. 性能
12. 開発効率
13. 見た目
14. 機能数
15. 新規性

対応要求：
REQ-GOV-001、REQ-GOV-002、REQ-EDU-011、REQ-PRI-001、REQ-ACC-001

---

## 4. Architecture基本原則

### 4.1 教材独立

各教材を独立Directoryに配置し、教材Aが教材BのJavaScriptや教材データを
直接読み込む構造を禁止する。

対応要求：
REQ-GOV-005、REQ-MNT-001、REQ-NFR-004

### 4.2 静的Web優先

HTML、CSS、JavaScript、SVG、Canvas、静的データを基本とし、
標準教材ではServer、Database、Login、常時通信を必要としない。

対応要求：
REQ-FUN-001、REQ-PRI-002、REQ-OFF-001、REQ-OPS-002

### 4.3 ブラウザ標準優先

標準Web APIで実現可能な場合は外部Libraryより優先する。

対応要求：
REQ-CMP-005、REQ-DEV-005、REQ-DEV-007

### 4.4 過剰共通化の禁止

共通化によって教材単体動作、教育設計、理解容易性、交換可能性が損なわれる場合は共通化しない。

対応要求：
REQ-GOV-002、REQ-GOV-003、REQ-MNT-002、REQ-NFR-006

### 4.5 段階的共通化

共通化は、長期保守性、教材独立性、運用負荷の観点から段階的に判断する。

「2〜3教材以上での再利用確認」は、Architecture上の**推奨判断基準**であり、
Requirements上の一律なMUST条件ではない。
教材間で明確に共通する要件、重大なAccessibility修正、Security修正等では、
1教材段階でもPlatform Core候補として検討してよい。

採用判断はADRまたは設計Reviewへ記録する。

対応要求：
REQ-GOV-002、REQ-GOV-017、REQ-GOV-018、REQ-MNT-002、REQ-NFR-008、
REQ-ACC-001、REQ-ACC-005、REQ-SEC-001

### 4.6 交換可能性

外部Library、CI、Hosting、保存方式はAdapterまたは独立Toolを介し、
教材固有Domain Logicへ直接依存させない。

対応要求：
REQ-DEV-006、REQ-TST-013、REQ-OFF-002

---

## 5. システム全体の層構造

Platformを次の8層に分ける。

1. Portal
2. App Shell
3. Platform Core
4. App Type Support
5. App Module
6. Content Data
7. Distribution
8. Governance and Tooling

依存方向は原則として上位の利用層から下位の支援層への一方向とする。
Platform Coreから個別教材への逆依存を禁止する。

対応要求：
REQ-MNT-002、REQ-DAT-001、REQ-NFR-008

---

## 6. 標準リポジトリ構成

```text
you-science-apps/
├─ README.md
├─ LICENSE
├─ AGENTS.md
├─ CONTRIBUTING.md
├─ site/
│  ├─ index.html
│  ├─ assets/
│  ├─ platform/
│  │  ├─ core/
│  │  ├─ app-types/
│  │  ├─ components/
│  │  ├─ utilities/
│  │  └─ adapters/
│  ├─ apps/
│  │  ├─ junior-high/
│  │  └─ senior-high/
│  └─ catalog/
│     ├─ catalog.json
│     └─ archived-apps.json
├─ catalog-source/
│  ├─ catalog.override.json
│  └─ catalog-groups.json
├─ project-docs/
│  ├─ requirements/
│  ├─ architecture/
│  ├─ governance/
│  ├─ adr/
│  ├─ review-packages/
│  ├─ developer-guide/
│  ├─ teacher-guide/
│  ├─ privacy/
│  ├─ accessibility/
│  ├─ licensing/
│  ├─ deprecated/
│  └─ handover/
├─ reference-implementations/
├─ schemas/
├─ curriculum/
├─ tools/
├─ tests/
├─ dist/
│  ├─ hosted/
│  └─ portable/
├─ archive/
└─ .github/
   └─ workflows/
```

対応要求：
REQ-OPS-001、REQ-OPS-008、REQ-OPS-009、REQ-DOC-013、REQ-MNT-001

---

## 7. GitHub Pages公開方式

### 7.1 採用方式

`site/`を公開原本とし、GitHub Actions等でGitHub Pagesの公開成果物へ配置する。

### 7.2 採用理由

- 設計文書と公開物を分離できる
- Schema、Tool、Testを公開対象外にできる
- 公開前検証を挟める
- Hosting交換時の移行範囲を限定できる

### 7.3 非採用方式

`docs/`を設計文書領域と公開元の双方に使用しない。
Repository root全体の公開も標準方式としない。

対応要求：
REQ-OPS-002、REQ-OPS-008、REQ-OPS-009、REQ-OPS-010、REQ-TST-012

---

## 8. 公開パイプライン

```text
Source change
→ Requirements／Schema／Manifest validation
→ Catalog generation
→ Path resolution
→ Hosted build
→ Accessibility basic checks
→ Link checks
→ Release approval
→ GitHub Pages deployment
```

MUST関連ERRORが1件でもあれば公開を停止する。

検証ロジックは`tools/`へ保持し、GitHub Actionsは実行環境として扱う。

対応要求：
REQ-TST-009、REQ-TST-010、REQ-TST-012、REQ-TST-013、REQ-REL-001

---

## 9. Portal Architecture

Portalの責任：

- 教材一覧
- 学年・教科・単元・形式による検索
- status表示
- Deprecated・後継教材案内
- 教材URLへの導線

Portalが持たない責任：

- 生徒Login
- 個人学習履歴
- 行動分析
- Ranking
- 個人別推薦
- 教材固有Domain Logic

Portalは生成済み`catalog.json`を参照する。

対応要求：
REQ-CAT-001、REQ-CAT-004、REQ-CAT-005、REQ-GOV-003、REQ-PRI-001

---

## 10. App Shell Architecture

App Shellは教材名、対象、操作説明、戻る、Reset、Help、Version、
保存データ削除、Error表示等の共通構造を提供できる。

同一のRuntime Code共有は必須ではない。
Standalone教材は参照実装をCopyしてよい。

対応要求：
REQ-FUN-002、REQ-FUN-003、REQ-FUN-004、REQ-PRI-008、REQ-VER-003

---

## 11. Platform Core Architecture

Platform Coreへ含める候補：

- Design Token
- Button、Input、Dialog、Tab
- Focus制御
- Keyboard支援
- 設定保存Adapter
- Error表示
- reduced-motion対応
- Print補助

含めないもの：

- 特定教科の計算
- 問題生成
- 個別教材の進行
- 教科固有図
- 個別データ

公開APIと内部APIを区別し、破壊的変更はMAJOR更新とする。

対応要求：
REQ-MNT-002、REQ-MNT-003、REQ-MNT-004、REQ-VER-004

---

## 12. Core Dependency Mode

Dependency Modeは、**Source時点**と**配布成果物時点**を分離して管理する。

### 12.1 Source Dependency Mode

教材Sourceは次の3方式を選択できる。

- `shared`：公開Platform Coreを参照する
- `vendored`：特定Core Versionを教材内へ同梱する
- `self-contained`：Runtime共有依存を持たない

旧称`standalone`はDistribution名との混同を避けるため、
Manifest Schema策定時に`self-contained`へ統一する。

### 12.2 Distribution Dependency Mode

Hosted、Portable等の各配布成果物は、
Sourceとは別に成果物時点のDependency Modeを持つ。

例：

- Source=`shared`、Hosted=`shared`
- Source=`shared`、Portable=`vendored`
- Source=`self-contained`、Hosted=`self-contained`

Portable成果物が`shared`のままになる構成は許可しない。

### 12.3 Manifest記録

Manifestは少なくとも次を区別して記録する。

- Source Dependency Mode
- Core Version
- Distributionごとの有効・無効
- Distribution成果物ごとのDependency Mode

詳細な許容組み合わせとSchema禁則は第27.4章を正本とする。

対応要求：
REQ-MAN-005、REQ-MAN-006、REQ-MNT-003、REQ-OFF-005、REQ-OFF-007、
REQ-DAT-007、REQ-TST-016、REQ-TST-017

---

## 13. App Type Support Architecture

教材形式ごとの汎用支援を`site/platform/app-types/`に配置できる。

```text
calculation/
simulation/
drag-and-drop/
experiment/
visualization/
```

ただし巨大な教材Engineは作らない。
複数教材で安定した必要性が確認されるまで個別教材内に保持する。

対応要求：
REQ-EDU-CALC-001、REQ-EDU-SIM-001、REQ-EDU-DRAG-001、REQ-EDU-EXP-001、REQ-EDU-VIS-001

---

## 14. 計算教材Architecture

計算教材はDomain LogicをDOMから分離し、
単位、許容誤差、丸め、有効数字を明示的に扱う。

Data層に問題文、正解、解説、数値条件を配置し、
途中過程や誤答診断に必要な情報を保持できる構造とする。

対応要求：
REQ-EDU-CALC-001、REQ-EDU-CALC-002、REQ-EDU-CALC-003、REQ-EDU-CALC-004、
REQ-DAT-005、REQ-DAT-006、REQ-TST-002

---

## 15. Simulation教材Architecture

Simulationは変更可能条件、固定条件、初期条件、表示状態を分離して管理する。
科学Modelの限界と実験との差をUIから確認できるようにする。

危険操作をSimulation上で扱う場合は、
実際に安全であるとの誤解を生まないWarning構造を持つ。

対応要求：
REQ-EDU-SIM-001、REQ-EDU-SIM-002、REQ-EDU-SIM-003、REQ-EDU-SIM-004、
REQ-EDU-SIM-005、REQ-EDU-012、REQ-EDU-013

---

## 16. Drag教材Architecture

Drag操作はPointer Event等で実装しても、
Button、Tap選択、Keyboard等の代替経路を必ず用意する。

Drag中の座標状態と学習上の判定状態を分離し、
誤操作から再試行できるようにする。

対応要求：
REQ-EDU-DRAG-001、REQ-EDU-DRAG-002、REQ-EDU-DRAG-003、
REQ-ACC-005、REQ-EDU-007

---

## 17. Experiment教材Architecture

実験支援教材は安全条件、使用物質、操作順、観察項目、廃棄注意を
Content Dataとして編集可能にする。

Simulationまたは画面上の操作だけで、
実物実験の安全確認を代替しない。

対応要求：
REQ-EDU-EXP-001、REQ-EDU-EXP-002、REQ-EDU-EXP-003、REQ-EDU-EXP-004、
REQ-EDU-013

---

## 18. Visualization教材Architecture

凡例、尺度、向き、色以外の区別、簡略化内容を表示する。
Zoomや切替がある場合も、図の意味が変化したと誤認させない。

対応要求：
REQ-EDU-VIS-001、REQ-EDU-VIS-002、REQ-EDU-VIS-003、REQ-EDU-VIS-004、
REQ-ACC-001、REQ-EDU-014

---

## 19. 教材Level判定と標準構成

教材Levelの客観判定は`ADR-0011 教材Level客観判定`を正本とする。

- 12指標を0〜2点で採点
- 0〜8点：Level A
- 9〜16点：Level B
- 17〜24点：Level C
- 強制Level C条件を適用
- 設計変更時に再判定

Levelは教育的重要度ではなく、開発・保守・公開Riskを示す。

対応要求：
REQ-GOV-019、REQ-GOV-020、REQ-DOC-005

### 19.1 個別教材の標準構成

Level A最小構成：

```text
app-id/
├─ index.html
├─ app.manifest.json
├─ README.md
└─ CHANGELOG.md
```

Level B標準構成：

```text
app-id/
├─ index.html
├─ app.manifest.json
├─ README.md
├─ CHANGELOG.md
├─ teacher-notes.md
├─ css/
├─ js/
├─ data/
└─ assets/
```

Level Cはdesign、tests、migration、ADR参照を追加する。

対応要求：
REQ-GOV-019、REQ-GOV-020、REQ-DOC-001、REQ-DOC-002、REQ-DOC-003

---

## 20. 教材内の責任分離

- Domain：科学計算・正誤判定
- State：現在条件・進行状態
- UI：表示・操作
- Data：問題・解説・設定・物質情報
- App：各Moduleの接続

Domainは原則DOMを直接操作しない。
Dataは実行Logicを持たない。

対応要求：
REQ-DAT-001、REQ-DAT-002、REQ-MNT-002、REQ-NFR-006

---

## 21. 依存規則

許可：

```text
UI → State
UI → Domain
State → Domain
App → Platform Core
App → App Type Support
App → App Data
Portal → Catalog
Generator → Manifest
Validator → Schema
```

禁止：

```text
Platform Core → Individual App
App A → App B
Data → DOM
Catalog → App JavaScript
Domain → Portal
```

循環依存は禁止し、上位CoordinatorがModuleを接続する。

対応要求：
REQ-GOV-005、REQ-MNT-002、REQ-NFR-004

---

## 22. Manifest Architecture

Manifestを教材固有メタデータの正本とする。

最低限の責任：

- appId
- title
- version
- status
- 教育情報
- Platform依存
- Distribution
- 保存・通信
- Privacy
- License
- Reference Implementation履歴

Manifestは教材Directory内へ置き、Schemaで検証する。

対応要求：
REQ-MAN-001、REQ-MAN-002、REQ-MAN-003、REQ-MAN-004、REQ-MAN-005、REQ-MAN-006、
REQ-MAN-007、REQ-MAN-008

---

## 23. Catalog Architecture

Catalogは次を統合して生成する。

```text
App Manifests
+ catalog.override.json
+ catalog-groups.json
→ Catalog Generator
→ site/catalog/catalog.json
```

Manifest管理情報をoverrideから上書きしてはならない。
生成済みCatalogは直接編集しない。

対応要求：
REQ-CAT-002、REQ-CAT-003、REQ-CAT-006、REQ-CAT-007、REQ-CAT-008、
REQ-CAT-009、REQ-CAT-010、REQ-MAN-004

---

## 24. Schema Architecture

Schemaを機械判定の正本とする。

主要Schema：

- app-manifest.schema.json
- catalog.schema.json
- catalog-override.schema.json
- catalog-groups.schema.json
- curriculum-map.schema.json
- 必要に応じてquestion-data.schema.json

正常例・異常例を保持し、Schema変更時は移行と回帰Testを行う。

対応要求：
REQ-DAT-007、REQ-DAT-008、REQ-DAT-009、REQ-DAT-010、REQ-DAT-011、REQ-DAT-012

---

## 25. Curriculum Architecture

教材Manifestは安定したunitIdを参照し、
年度別のcurriculum-mapへ対応付ける。

旧指導要領Mappingを履歴として保持し、
改訂時に修正不要・要確認・軽微修正・重大修正・廃止候補へ分類する。

対応要求：
REQ-CUR-001、REQ-CUR-002、REQ-CUR-003、REQ-CUR-004

---

## 26. Storage Architecture

標準教材は個人情報を保存しない。
保存する場合は端末内に限定し、Adapterを介する。

Key形式：

```text
ysa:<appId>:<dataName>:<schemaVersion>
```

保存内容と削除方法を明示する。

対応要求：
REQ-PRI-001、REQ-PRI-007、REQ-PRI-008、REQ-FUN-011、REQ-FUN-012

---

## 27. Distribution Architecture

### 27.1 Hosted

GitHub Pages等で提供する標準版。
共有CoreとbasePath解決を利用できる。

### 27.2 Portable

必要なCore、Data、Assetを教材Directoryへ同梱した保存・移管用成果物。

### 27.3 Standalone

最初からRuntime共有依存を持たない教材。

配布形態をManifestとREADMEへ記録する。

対応要求：
REQ-OFF-005、REQ-OFF-006、REQ-OFF-007、REQ-OFF-009、REQ-MAN-006

### 27.4 Dependency ModeとDistributionの整合規則

Dependency ModeとDistributionは別の軸として管理する。

- Dependency Mode：実行時にCoreへどう依存するか
- Distribution：利用者へどの形で配布するか

用語の混同を避けるため、Dependency Modeの`standalone`は
**`self-contained`へ名称変更することをManifest Schema策定時に優先検討する。**

許容組み合わせは次のとおりとする。

| Distribution | shared | vendored | self-contained |
|---|---:|---:|---:|
| Hosted | 可 | 可 | 可 |
| Portable | 不可 | 可 | 可 |
| Standalone package | 不可 | 条件付き | 可 |

補足：

- Portable成果物は、生成後の実行時に共有Coreへ依存してはならない。
- Source教材が`shared`でも、Portable BuilderがCoreを同梱して成果物を`vendored`へ変換する場合は許容する。
- `distribution.portable = true`かつ**成果物側**`dependencyMode = shared`はSchemaまたはBuild検証でERRORとする。
- Standalone packageは原則`self-contained`とする。
- `vendored`をStandalone packageとして扱う場合は、教材Directory内ですべての依存が完結することを検証する。
- ManifestはSource時点の依存方式とDistribution成果物の依存方式を区別して記録できる構造とする。

想定Manifest構造：

```json
{
  "platform": {
    "sourceDependencyMode": "shared",
    "coreVersion": "1.2.0"
  },
  "distribution": {
    "hosted": {
      "enabled": true,
      "dependencyMode": "shared"
    },
    "portable": {
      "enabled": true,
      "dependencyMode": "vendored",
      "directFileOpen": true
    }
  }
}
```

この整合規則は`app-manifest.schema.json`の条件分岐、
Portable Builderの最終検証、Integration Testの三箇所で検証する。

本版はArchitecture設計を定義する段階であり、
`app-manifest.schema.json`実体と正常例・異常例Testは未実装である。
Manifest Schema Specification工程で実装・検証する。

対応要求：
REQ-MAN-005、REQ-MAN-006、REQ-OFF-005、REQ-OFF-007、REQ-OFF-008、
REQ-DAT-007、REQ-TST-016、REQ-TST-017、REQ-TST-020

---

## 28. Portable Builder

Portable Builderは次を行う。

1. Core Version固定
2. 必要FileのCopy
3. basePathの相対Path変換
4. 必要に応じたJSONのJavaScript化
5. 外部URL検査
6. 未解決Placeholder検査
7. VERSION.json生成
8. Offline Test対象の生成

`file://`対応を表明する場合は実際に直接起動Testを行う。

対応要求：
REQ-OFF-008、REQ-TST-017、REQ-OPS-014、REQ-DEV-010

### 28.1 `dist/`の責任と管理方針

`dist/`はBuild Toolが生成する**一時的またはRelease用成果物領域**とする。

標準構成：

```text
dist/
├─ hosted/
└─ portable/
```

- `dist/hosted/`：Pages公開前の検証用Hosted成果物
- `dist/portable/<appId>/`：教材別Portable成果物

管理方針：

1. 通常の開発では`dist/`を再生成可能な成果物として扱う。
2. `dist/`全体をSourceの正本にしない。
3. 通常は`.gitignore`対象とする。
4. 正式Release成果物はGitHub Release、Archive、または承認済みArtifact保管先へ保存する。
5. Releaseへ保存するPortable成果物には`VERSION.json`とSource Commitを含める。
6. Hosted公開は`dist/hosted/`の検証済み内容をDeployする。
7. `site/`は公開Source、`dist/hosted/`は生成済み公開候補として責任を分ける。
8. CI障害時もLocal Toolから`dist/`を再生成できなければならない。

対応要求：
REQ-DEV-010、REQ-OPS-004、REQ-OPS-014、REQ-TST-013、REQ-TST-016、REQ-REL-003

---

## 29. Base Path Architecture

Hosted Sourceでは論理Placeholderを使用できる。

```html
{{YSA_BASE}}platform/core/platform.css
```

公開BuildでProject SiteまたはCustom Domainに応じて置換する。

教材自身のAssetは`./`による教材内相対Pathを使用する。
深い`../../../../`参照を標準例として使用しない。

Portable版では教材内相対Pathへ変換する。

対応要求：
REQ-NFR-008、REQ-OFF-006、REQ-OFF-009、REQ-TST-010

---

## 30. Reference Implementation Architecture

Standalone教材向けに、Runtime依存のない参照実装を提供する。

候補：

- standalone-basic
- accessible-form
- accessible-dialog
- drag-alternative
- reduced-motion
- status-feedback

利用した名称、Version、Copy日、改変有無をManifestへ記録する。
重大不具合時は影響教材を抽出する。

対応要求：
REQ-MAN-007、REQ-MAN-008、REQ-ACC-001、REQ-ACC-005、REQ-ACC-007

---

## 31. 外部Library Architecture

採用条件：

- 教育上必要
- 標準APIだけでは著しく困難
- Licenseが適切
- Offline保持可能
- Security上許容
- 交換可能
- 保守状況を確認

正式教材で外部CDNを原則使用しない。
利用時はAdapterを設ける。

対応要求：
REQ-DEV-005、REQ-DEV-006、REQ-OFF-002、REQ-LIC-002

---

## 32. Error Handling Architecture

利用者向けErrorは、何が起きたか、再試行方法、初期化方法を示す。
内部Stack Traceや秘密情報を表示しない。

科学的に誤った結果を出す可能性がある場合はFail Closedとし、
処理を継続しない。

Portal障害時も個別教材URLから起動可能にする。

対応要求：
REQ-SEC-006、REQ-FUN-003、REQ-NFR-004

---

## 33. Offline・障害戦略

主要機能は外部通信なしで動作する。
Service WorkerとPWAはVer.1.0の標準必須機能としない。

理由：

- Cache更新問題
- 古い教材残存
- Debug複雑化
- Browser差
- 保守負荷

導入時はADRを必要とする。

対応要求：
REQ-OFF-001、REQ-OFF-003、REQ-NFR-005、REQ-DOC-005

---

## 34. Version Compatibility

個別にVersion管理する。

- Platform
- Platform Core
- App
- Manifest Schema
- Catalog Schema
- Content Data Schema
- Build Tool
- Reference Implementation

Core MINORは原則後方互換を維持し、
Core 1.x、2.x、self-contained教材を一定期間併存可能とする。

対応要求：
REQ-VER-001、REQ-VER-002、REQ-VER-004、REQ-VER-005

---

## 35. Deprecated・Archive Architecture

active教材は`site/apps/`に置く。
deprecated教材は原則公開を継続し、警告と後継案内を表示する。
retired教材は公開対象から外して`archive/retired/`へ移す。
archived教材は履歴保存のみとする。

対応要求：
REQ-DEP-001、REQ-DEP-002、REQ-DEP-003、REQ-DEP-004、REQ-DEP-005、REQ-DEP-006

---

## 36. Tooling Architecture

管理対象Tool：

- Manifest Validator
- Schema Validator
- Catalog Generator
- Requirement Reference Checker
- Link Checker
- Base Path Resolver
- Portable Builder
- Release Checker
- Migration Tool
- Local Preview Tool

各ToolはREADME、Version、入出力、Error条件、Test、CHANGELOGを持つ。

対応要求：
REQ-DEV-008、REQ-DEV-009、REQ-DEV-010、REQ-DEV-011

---

## 37. Testing Architecture

- Unit Test：Domain計算、判定、変換、Generator
- Integration Test：UI／State／Domain／Build Pipeline
- Browser Test：Chromebook、iPad、Windows、Mac
- Human Review：科学内容、教育効果、図、学年相応性
- Pilot：実際の授業・少人数操作

対応要求：
REQ-TST-001、REQ-TST-002、REQ-TST-003、REQ-TST-004、REQ-TST-007、
REQ-TST-008、REQ-TST-014、REQ-TST-015、REQ-TST-016

---

## 38. 要求ID・文書参照Architecture

要求IDは可変階層形式を許容する。

例：

```text
REQ-TST-018
REQ-EDU-CALC-001
REQ-EDU-SIM-005
```

Validatorは次を検査する。

- 本文とrequirement-indexの一致
- 重複
- 欠番
- 必須Group欠落
- Architecture／Governanceの未定義参照
- 参照Requirements Version
- Deprecated要求
- 未付与仮ID

対応要求：
REQ-TST-018、REQ-TST-019、REQ-TST-020、REQ-DOC-012、REQ-DOC-015

---

## 39. Review Package Architecture

相互依存文書を次のPackageでレビューする。

```text
review-packages/
└─ platform-design-v1-rc/
   ├─ REVIEW-INDEX.md
   ├─ requirements/
   ├─ architecture/
   ├─ governance/
   ├─ requirement-index.json
   ├─ reference-validation-report.json
   └─ validation-summary.md
```

Requirements、Architecture、Governanceを単独でActiveにせず、
相互整合後に合同承認する。

対応要求：
REQ-DOC-014、REQ-DOC-017、REQ-TST-019

---

## 40. Security Boundary

標準教材のSecurity BoundaryはBrowser内とする。

禁止・抑制事項：

- API Key
- eval
- 動的Code実行
- 不要なiframe
- 未検証innerHTML
- 外部追跡Script
- 不正な保存Data

対応要求：
REQ-SEC-001、REQ-SEC-002、REQ-SEC-003、REQ-SEC-004、REQ-PRI-006

---

## 41. 対応環境と性能基準

対応環境は`supported-environments.md`を正本とする。

目安：

- 概ね5年以内のChromebook相当
- Memory 4GB以上
- 実効下り10Mbps以上
- Latency 100ms以下
- Cacheなしの初回起動
- 対象Browser安定版

標準教材は初期読込5MB以下、主要画面3秒以内を目標とする。

対応要求：
REQ-NFR-001、REQ-NFR-010、REQ-CMP-001、REQ-CMP-002、REQ-CMP-003、
REQ-CMP-004、REQ-CMP-008、REQ-CMP-009

---

## 42. 100教材規模への対応

人手で100教材のManifest、Link、Version、Statusを照合しない。

自動化対象：

- Catalog生成
- appId重複
- Manifest／Schema
- 必須File
- Link
- 外部依存
- Deprecated一覧
- Version一覧
- Curriculum対応
- Reference Implementation影響教材

対応要求：
REQ-OPS-007、REQ-OPS-011、REQ-GOV-017、REQ-GOV-018

---

## 43. 単一Repositoryと将来分割

Ver.1.0では単一Repositoryを採用する。

再検討条件：

- 容量増加
- 大型動画・音声
- 複数Team
- 権限分離
- CI時間超過
- 教科別Release周期の大幅差

分割にはADR、Migration Plan、Catalog継続性確認を必要とする。

対応要求：
REQ-OPS-001、REQ-DOC-005、REQ-GOV-008

---

## 44. 組織移管を支える可搬性

運営主体変更時も次を一括移管可能にする。

- Source
- site
- Schema
- Catalog Source
- Tool
- Test
- Review Package
- License Record
- Release Artifact
- Portable Artifact
- Domain設定資料

特定個人の端末やAccountだけにBuild方法を保持しない。

対応要求：
REQ-GOV-021、REQ-GOV-022、REQ-GOV-027、REQ-OPS-004、REQ-OPS-013、REQ-OPS-016

---

## 45. Architecture Decision Records

最低限次のADRを作成する。

- ADR-0001 教材独立Directory
- ADR-0002 教材単体動作
- ADR-0003 Manifest正本・Catalog生成
- ADR-0004 Core Version固定
- ADR-0005 `site/`と`project-docs/`分離
- ADR-0006 GitHub ActionsによるPages公開
- ADR-0007 検証LogicのCI非依存
- ADR-0008 Service Worker標準非採用
- ADR-0009 個人情報・Login・解析をCoreへ含めない
- ADR-0010 DataとLogicの分離
- ADR-0011 Level客観判定
- ADR-0012 Catalog Source分離
- ADR-0013 生成Catalog直接編集禁止
- ADR-0014 basePath Build解決
- ADR-0015 Standalone参照実装
- ADR-0016 文書ID・Version固定

対応要求：
REQ-DOC-005、REQ-GOV-008

---

## 46. Requirements Traceability Summary

本書の要求参照元は次に固定する。

```text
YSA-REQ-001 Requirements Specification Ver.1.2.3 RC
```

主要対応：

| Architecture領域 | Requirements |
|---|---|
| 公開領域分離 | REQ-OPS-008〜010 |
| 教材独立 | REQ-GOV-005、REQ-MNT-001 |
| Core依存 | REQ-MNT-003〜004 |
| Manifest | REQ-MAN-001〜008 |
| Catalog | REQ-CAT-001〜010 |
| Schema | REQ-DAT-007〜012 |
| Distribution | REQ-OFF-005〜009 |
| 参照実装 | REQ-MAN-007〜008 |
| 自動検証 | REQ-TST-009〜020 |
| 教材形式 | REQ-EDU-CALC-001〜004、REQ-EDU-SIM-001〜005、REQ-EDU-DRAG-001〜003、REQ-EDU-EXP-001〜004、REQ-EDU-VIS-001〜004 |
| 組織移管 | REQ-GOV-021〜027、REQ-OPS-012〜016 |

---

## 47. Ver.1.1.2 RCの完了条件

1. Requirements Ver.1.2.3 RC参照がERROR 0件
2. 文書管理情報と本文の参照Versionが一致
3. Migration PlanをReview Packageへ収録
4. 教材形式別Architectureを収録
5. Hosted／Portable／Standaloneを収録
6. Catalog Source責任分離を収録
7. Reference Implementation追跡を収録
8. Tooling Test方針を収録
9. ClaudeによるRequirements・Architecture二文書レビュー
10. 重大指摘解消
11. 第12章と第27.4章のDependency Modeモデルが一致
12. `dist/hosted/`・`dist/portable/`の構成と管理方針を確認
13. Project OwnerによるRC承認

---

## 48. Ver.1.1.3変更履歴

### Corrected

- 第4.5章の「2〜3教材」基準をRequirements上のMUSTではなくArchitecture上の推奨判断基準として明確化
- Dependency ModeとDistributionの異なる責任軸を明確化
- Portable成果物が`shared`依存のままになる無効構成を禁止
- Source Dependency Modeと成果物Dependency Modeを分離
- `dist/`の生成主体、用途、Git管理方針、Release保存方針を定義
- `REQ-MAN-004`、`REQ-CAT-002`、`REQ-CAT-006`の明示的Traceabilityを追加

### Added

- Dependency Mode／Distribution許容組み合わせ表
- Manifest Schemaの条件分岐要件
- `dist/hosted/`と`dist/portable/`の責任分離
- Portable Build後のDependency Mode検証

---

## 49. Ver.1.1.4変更履歴

### Corrected

- 第12章をSource Dependency ModeとDistribution Dependency Modeの分離モデルへ同期
- `standalone`依存方式を`self-contained`へ統一する方針を第12章へ反映
- Portable成果物の`shared`依存禁止を第12章にも明記
- 第6章のRepository構成へ`dist/hosted/`を追加
- 第4.5章へAccessibility／Security関連要求の参照を追加
- Schema禁則は設計済み・実装未了であることを明記
- 自動検証とManual Reviewの結果表示を分離

---

## 50. 結論


You Science Apps Platformは、全教材を巨大な共通Engineへ統合するものではない。

```text
Independent Apps
+ Limited and Versioned Platform Core
+ Manifest and Generated Catalog
+ Schema and Automated Validation
+ Hosted / Portable / Standalone Distribution
+ Reviewable Documents and ADR
= Long-lived Educational Asset Platform
```

30年保守の中心は、最新技術ではなく、
教材独立性、責任分界、機械検証、配布可搬性、履歴、移行可能性に置く。


## 51. Ver.1.1.5変更履歴

- ADR-0011をLevel判定の正本として追加
- 相互参照Versionを更新
- Standalone依存表現をself-containedへ統一
