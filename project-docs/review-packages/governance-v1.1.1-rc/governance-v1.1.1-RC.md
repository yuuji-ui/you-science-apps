# You Science Apps Platform
# Governance Specification Ver.1.1.1 RC

## 文書管理情報

| 項目 | 内容 |
|---|---|
| 文書名 | You Science Apps Platform Governance Specification |
| 文書ID | YSA-GOV-001 |
| バージョン | 1.1.1 |
| 状態 | Release Candidate / Draft |
| 前バージョン | 1.1 |
| 対象Platform | You Science Apps Platform Ver.1.0 |
| 対応Requirements | YSA-REQ-001 Ver.1.2.2 RC |
| 対応Architecture | YSA-ARCH-001 Ver.1.1.4 RC |
| 作成日 | 2026-08-03 |
| 文書責任者 | Project Owner |
| 設計担当 | ChatGPT |
| 第三者レビュー | Claude（未実施） |
| 参照検証状態 | Requirements参照自動検証済み |
| 改訂区分 | MINOR / 三文書整合版 |

---

## 1. 本書の目的

本書はYou Science Apps Platformにおける意思決定、役割、権限、承認、
公開、例外、Incident、廃止、引き継ぎ、組織所有および文書合同承認を定義する。

対応要求：
REQ-GOV-006、REQ-GOV-007、REQ-GOV-008、REQ-GOV-009、REQ-GOV-010、
REQ-GOV-011、REQ-GOV-012、REQ-GOV-013、REQ-GOV-014、REQ-GOV-015

---

## 2. ガバナンス原則

### 2.1 優先順位

判断が競合する場合はRequirementsの優先順位に従う。

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

### 2.2 役割と個人の分離

責任は個人名ではなく役割として定義し、担当者交代時も権限と記録を継承する。

対応要求：
REQ-GOV-011、REQ-GOV-013、REQ-MNT-009

### 2.3 単独判断の抑制

重大変更、正式公開、Privacy変更、License変更、Schema破壊的変更を
1人または1つのAIだけで決定しない。

対応要求：
REQ-GOV-008、REQ-GOV-024、REQ-AI-004、REQ-AI-005

### 2.4 記録優先

重要判断はADR、Pull Request、Issue、CHANGELOG、Review Report、
Exception Record、Incident Report、Handover Documentへ記録する。

対応要求：
REQ-DOC-002、REQ-DOC-005、REQ-DOC-016、REQ-GOV-013

### 2.5 最小権限

各役割には担当業務に必要な権限のみを与える。

対応要求：
REQ-GOV-021、REQ-GOV-022、REQ-OPS-012、REQ-OPS-013

### 2.6 可逆性

重大変更はRollback可能な状態で実施する。

対応要求：
REQ-REL-005、REQ-OPS-005

### 2.7 例外の期限管理

例外は恒久免除として扱わず、期限、代替策、解消条件を持たせる。

対応要求：
REQ-GOV-009、REQ-GOV-EXC-001

---

## 3. 役割

| 役割 | 主な責任 |
|---|---|
| Project Owner | 最終意思決定、正式文書・公開・重大変更承認 |
| Deputy Owner | 不在時の限定代理 |
| Platform Architect | 技術構造、依存、ADR、Migration |
| Requirements Maintainer | 要求ID、正本、Traceability |
| Governance Maintainer | 承認制度、例外、Incident、引き継ぎ |
| App Owner | 個別教材の教育・保守責任 |
| App Developer | 設計・実装・修正 |
| Subject Reviewer | 科学的正確性・学年相応性 |
| Accessibility Reviewer | Accessibility確認 |
| Technical Reviewer | Code・Browser・Tool・Build確認 |
| Portal Maintainer | Catalog override、groups、Portal運用 |
| Release Manager | Release、Tag、Deploy、Rollback |
| Incident Coordinator | 重大Incident対応 |
| Archive Maintainer | Deprecated／Retired／Archived管理 |
| AI Design Lead | ChatGPTによる設計・開発支援 |
| AI Independent Reviewer | Claudeによる第三者Review |

少人数運営では兼任できるが、正式公開の自己承認は禁止する。

対応要求：
REQ-GOV-006、REQ-GOV-011、REQ-GOV-024、REQ-GOV-025

---

## 4. Project Owner

Project Ownerは次を承認する。

- Platform正式文書
- Level C教材の正式公開
- MAJOR変更
- Privacy／License方針
- Schema破壊的変更
- Platform Core公開API破壊的変更
- Repository分割・Hosting移行
- Deprecated／Retired
- 緊急公開停止解除
- 運営主体移管

単独Reviewなしに上記を決定してはならない。

対応要求：
REQ-GOV-007、REQ-GOV-008、REQ-GOV-024、REQ-GOV-027

---

## 5. Deputy Owner

Deputy OwnerはProject Owner不在時に通常公開、緊急停止、緊急修正を代理できる。

原則として延期する事項：

- Platform MAJOR更新
- Privacy緩和
- License全面変更
- Repository全面移行
- 大量教材Retired
- 運営主体変更

生徒安全、Privacy、Security上の緊急対応は例外とする。

対応要求：
REQ-GOV-012、REQ-GOV-015、REQ-GOV-022

---

## 6. Organization所有と権限

正式RepositoryはGitHub Organization等の組織単位で所有する。

最低条件：

- Organization Ownerを2名以上
- Project OwnerとDeputy Ownerが管理可能
- 個人の私的Mailだけへ復旧を依存しない
- 2FAと復旧手段を確認
- 権限を年1回点検
- 退職・異動者を速やかに除外

暫定個人運営は原則90日以内とし、移行期限、代理権限、外部Backupを持つ。

対応要求：
REQ-GOV-021、REQ-GOV-022、REQ-GOV-023、REQ-OPS-012、REQ-OPS-013

---

## 7. App Owner

各active教材はApp Ownerを持つ。

責任：

- 学習目標
- 科学的正確性
- Manifest
- README、CHANGELOG、Teacher Notes
- 年次点検
- 不具合対応
- Deprecated候補
- 後継教材案内

App Owner不在時は新担当指名、暫定管理、maintenance、deprecatedの順で検討する。

対応要求：
REQ-GOV-006、REQ-MNT-006、REQ-MNT-008、REQ-MNT-009、REQ-DEP-001

---

## 8. Portal Maintainer

Portal Maintainerが編集できるもの：

- catalog.override.json
- catalog-groups.json
- 表示順
- 特集
- Portal固有Label
- 一時非表示

編集してはならないもの：

- 教材の科学内容
- Manifest管理情報
- 教材Version
- status
- Privacy
- License
- 学習目標

教材開発者が自分の教材を独断でfeaturedへ設定してはならない。

対応要求：
REQ-CAT-007、REQ-CAT-008、REQ-CAT-009、REQ-GOV-003

---

## 9. AI開発体制

標準Flow：

```text
ChatGPT設計・作成
→ GitHub保存
→ Claude第三者Review
→ ChatGPT修正
→ GitHub更新
→ 人間承認
```

重要変更では実装AIとReview AIを分ける。
AI出力を未確認で正式公開しない。

対応要求：
REQ-AI-001、REQ-AI-002、REQ-AI-003、REQ-AI-004、REQ-AI-005、REQ-AI-006

---

## 10. 教材Level

各教材をLevel A、B、Cへ分類する。

- Level A：小規模・低依存・低Risk
- Level B：標準的教材
- Level C：複雑・高依存・高Risk・Core変更等

Level判定の客観基準はArchitecture Specificationを正本とする。

対応要求：
REQ-GOV-019、REQ-GOV-020

---

## 11. Level別承認

| Level | Design承認 | Release承認 |
|---|---|---|
| A | App OwnerまたはReviewer | App Owner＋独立Reviewer |
| B | App Owner＋Subject＋Technical | App Owner＋Release Manager |
| C | App Owner＋Subject＋Technical＋Architect | 上記＋Project OwnerまたはDeputy |

Developer＝Ownerの場合は別のReviewerを必須とする。
科学内容を含む教材は人間のSubject Reviewを省略しない。

対応要求：
REQ-GOV-024、REQ-GOV-025、REQ-TST-003

---

## 12. 教材Life Cycle

```text
proposal
→ design
→ development
→ review
→ pilot
→ active
→ maintenance
→ deprecated
→ retired
→ archived
```

対応要求：
REQ-CAT-004、REQ-DEP-001、REQ-DEP-004、REQ-DEP-005

---

## 13. Gate 0 Proposal

必須事項：

- 教材名
- 対象学年・単元
- 学習課題
- 学習目標
- 利用場面
- Webアプリ化の理由
- 既存教材との差
- 教材形式
- 暫定Level
- App Owner

却下・保留条件：

- 学習目標不明
- Web化の必然性なし
- 既存教材と実質重複
- 保守担当不在
- 個人情報収集が前提
- 外部有料Serviceが必須
- 娯楽性が教育効果より中心

対応要求：
REQ-EDU-001、REQ-EDU-002、REQ-EDU-003、REQ-DEV-001、REQ-GOV-003

---

## 14. Gate 1 Design

必須成果物：

- 学習目標
- 対象生徒
- 使用時間
- 画面構成
- 操作方法
- 必要／不要機能
- Data構造
- 誤答・誤概念
- Accessibility
- Privacy
- Test観点
- 教員編集箇所
- Distribution方針
- Dependency Mode
- Level判定

対応要求：
REQ-DEV-001、REQ-EDU-010、REQ-ACC-001、REQ-PRI-001、REQ-MNT-005、
REQ-OFF-005、REQ-MAN-005

---

## 15. Gate 2 Design Review

確認項目：

- 学習目標と操作の一致
- 科学的正確性
- 過剰機能なし
- 誤答支援
- Model限界
- 実験との差
- 教材形式別要求
- Core共通化妥当性
- Distribution／Dependency整合
- Level妥当性

対応要求：
REQ-DEV-002、REQ-EDU-004、REQ-EDU-008、REQ-EDU-012、REQ-EDU-013、
REQ-GOV-019、REQ-GOV-020

---

## 16. Gate 3 Development

実装中に管理するもの：

- Manifest
- README
- CHANGELOG
- Teacher Notes
- Data／Logic分離
- Test
- Reference Implementation履歴
- 外部Library
- 既知制約
- Distribution成果物識別

再Review条件：

- Level変更
- 外部Library追加
- 保存・通信追加
- Core変更
- Schema変更
- Distribution変更
- 学習目標・対象学年変更

対応要求：
REQ-MAN-001、REQ-DOC-001、REQ-DOC-002、REQ-DOC-003、REQ-DAT-001、
REQ-MAN-007、REQ-DEV-005、REQ-OPS-014

---

## 17. Gate 4 Technical Review

確認項目：

- 自動検証
- Manifest／Schema
- Catalog整合
- JavaScript重大Error
- Browser／端末
- Touch／Keyboard
- Reset
- Error処理
- 保存削除
- 外部通信
- Hosted／Portable／Standalone
- Dependency Mode整合
- Reference Implementation追跡
- Regression Test

対応要求：
REQ-TST-001、REQ-TST-004、REQ-TST-005、REQ-TST-006、REQ-TST-008、
REQ-TST-009、REQ-TST-010、REQ-TST-017

---

## 18. Gate 5 Educational Review

確認項目：

- 科学的正確性
- 学年相応性
- 用語・単位・有効数字
- 図
- 誤概念
- Hint
- 答え提示
- 実験との差
- 教材形式別教育要求
- 授業時間
- 教員介入量

対応要求：
REQ-EDU-006、REQ-EDU-008、REQ-EDU-009、REQ-EDU-010、REQ-EDU-011、
REQ-EDU-013、REQ-EDU-014、REQ-TST-003、REQ-TST-014

---

## 19. Gate 6 Pilot

Level B／Cは原則Pilotを行う。
個人情報やアクセス解析を使わず、操作つまずき、誤答、表示、時間、端末差を観察する。

判定：

- active候補
- 軽微修正
- 再Pilot
- Design差戻し
- 中止

対応要求：
REQ-TST-007、REQ-PRI-001、REQ-PRI-003

---

## 20. Gate 7 Release

公開条件：

- 自動検証PASS
- Technical／Educational Review
- 必要なPilot
- Manifest、Catalog、README、CHANGELOG、Teacher Notes
- License
- Rollback可能
- Release Tag
- 承認記録

対応要求：
REQ-REL-001、REQ-REL-002、REQ-REL-003、REQ-REL-005、REQ-LIC-001

---

## 21. Distribution成果物の承認

### Hosted

- 公開URL
- basePath
- Catalog URL
- `dist/hosted/`検証
- Pages Deploy結果

### Portable

- Shared Runtime依存なし
- Asset／Data同梱
- 未解決Placeholderなし
- `file://`対応表明時の実地Test
- VERSION.json
- Source Commit追跡

### Standalone package

- 実行時依存が教材内で完結
- Distribution名とDependency Modeを混同しない
- Dependency Modeは`self-contained`を原則とする

対応要求：
REQ-OFF-005、REQ-OFF-006、REQ-OFF-007、REQ-OFF-008、REQ-OFF-009、
REQ-TST-017、REQ-OPS-014

---

## 22. 自動検証失敗

MUST関連ERRORがある場合は正式公開を停止する。

WARNINGは修正、影響なし、既知制約、期限付き例外、将来改善のいずれかを記録する。

検証を通すためだけにTestやCheckを無効化してはならない。

対応要求：
REQ-TST-012、REQ-GOV-009、REQ-GOV-EXC-001

---

## 23. Automated ValidationとManual Review

Automated Validation：

- ID
- Schema
- Manifest
- Catalog
- Link
- Build
- Dependency／Distribution禁則
- 必須File
- 禁止Script

Manual Review：

- 科学的正確性
- 教育効果
- 学年相応性
- 図
- Model限界
- 授業操作性
- Governance上の利益相反

両者を同一結果として表示しない。

対応要求：
REQ-TST-010、REQ-TST-014、REQ-TST-018、REQ-TST-019、REQ-TST-020

---

## 24. 例外管理

例外記録：

- 例外ID
- 対象
- 要求ID
- 内容
- 理由
- 教育必要性
- 安全・Privacy影響
- 代替策
- 承認者
- 開始日
- 期限
- 解消条件
- 状態

Privacy、安全、秘密情報に関する例外は原則承認しない。

標準期限：

- 軽微文書不足：30日
- 端末確認不足：90日
- 互換移行：1年
- Accessibility改善：Riskに応じ最長1年
- 安全・科学重大問題：例外不可または即時修正

対応要求：
REQ-GOV-009、REQ-GOV-EXC-001、REQ-PRI-001、REQ-SEC-004

---

## 25. Incident

緊急事象：

- 重大な科学的誤り
- 危険操作推奨
- 個人情報送信
- API Key公開
- 悪意あるCode
- 計算結果の重大誤り
- License違反
- 不適切外部Link

初動：

1. Portal非表示
2. 公開停止
3. Rollback
4. Incident Coordinator指定
5. 影響範囲確認
6. 記録開始
7. Owner報告

対応要求：
REQ-REL-004、REQ-REL-005、REQ-OPS-005、REQ-SEC-004

---

## 26. Deprecated／Retired／Archived

Deprecated理由：

- 指導要領不整合
- 科学的に古い
- 後継教材
- Browser非互換
- Accessibility重大問題
- 保守担当不在
- 外部依存維持不能
- 重複整理

標準移行期間は1年。
安全、Privacy、License、Security問題では短縮できる。

対応要求：
REQ-DEP-001、REQ-DEP-002、REQ-DEP-003、REQ-DEP-004、REQ-DEP-005、REQ-DEP-006

---

## 27. 文書承認

DraftからActiveへの条件：

- 参照文書同梱
- 要求ID自動照合
- 文書間矛盾確認
- 第三者Review
- 重大指摘解消
- CHANGELOG
- Project Owner承認

Requirements、Architecture、GovernanceはReview Package単位で合同承認する。

対応要求：
REQ-DOC-014、REQ-DOC-015、REQ-DOC-016、REQ-DOC-017、REQ-TST-018、REQ-TST-019

---

## 28. Pull Request

PR必須変更：

- active公開
- Manifest
- Catalog Source
- Platform Core
- Schema
- Requirements／Architecture／Governance
- Deprecated／Retired
- License
- Workflow
- Validator／Builder

PR記載：

- 目的
- 対象
- 要求ID
- 教育影響
- Privacy／安全
- Test
- 既知制約
- Rollback

対応要求：
REQ-GOV-008、REQ-DOC-005、REQ-REL-005

---

## 29. 年次レビュー

Platform：

- Requirements
- Architecture
- Governance
- Privacy
- Accessibility
- License
- AGENTS.md
- CI
- Pages
- Backup
- 権限
- 引き継ぎ

教材：

- 起動
- 科学内容
- 指導要領
- Browser
- 端末
- Accessibility
- 外部依存
- License
- App Owner
- status
- Distribution

対応要求：
REQ-GOV-010、REQ-GOV-016、REQ-MNT-008、REQ-OPS-012

---

## 30. 3年レビュー

- Core肥大化
- Level判定
- Schema複雑化
- 文書量
- 形骸化要求
- 自動化不足
- Portal分類
- Tool保守
- CI時間
- 運用負荷
- Organization体制

対応要求：
REQ-GOV-017、REQ-GOV-018、REQ-OPS-011

---

## 31. 10年レビュー

- GitHub／Pages継続性
- HTML／CSS／JavaScript
- Browser／端末
- File形式
- Hosting移行
- Organization所有
- 学校・団体・法人への移管
- 著作権
- Domain
- 費用
- 問い合わせ
- 組織終了時の再移管

対応要求：
REQ-GOV-026、REQ-GOV-027、REQ-OPS-015、REQ-OPS-016

---

## 32. Project Owner引き継ぎ

必須項目：

- 理念
- Active文書
- 教材一覧
- Issue
- GitHub権限
- Pages
- Backup
- Release／Rollback
- Catalog
- Portable生成
- Incident
- App Owner
- License
- Domain

後継者は実際にAccess、Test、Deploy、Rollback、Backup、Catalog更新を確認する。

対応要求：
REQ-GOV-013、REQ-GOV-014、REQ-OPS-004、REQ-OPS-005

---

## 33. 運営主体移管

移管時に確認する。

- Repository所有
- Pages／Hosting
- Domain／DNS
- Source著作権
- 教材文章・問題著作権
- Contributor権利
- License
- 学校名・校章
- 問い合わせ
- Backup
- 再移管

既存利用条件を説明なく不利益変更しない。

対応要求：
REQ-GOV-026、REQ-GOV-027、REQ-LIC-001、REQ-LIC-005

---

## 34. Backup

対象：

- Git Repository
- Release
- Portable成果物
- project-docs
- Review Package
- Incident
- License
- 外部素材原本

大規模Release前後、Owner交代前、Hosting移行前に取得する。
年1回は復旧Testを行う。

対応要求：
REQ-OPS-004、REQ-OPS-005

---

## 35. 意見対立

1. 対立点を文章化
2. 要求ID確認
3. 教育影響
4. 安全・Privacy
5. 長期保守
6. 代替案
7. ADR
8. Owner決定

科学内容の不確実性は断定表現にしない。

対応要求：
REQ-GOV-001、REQ-GOV-002、REQ-DOC-005、REQ-EDU-011

---

## 36. ガバナンス違反

- 承認なしactive公開
- 自動検証回避
- 未確認AI出力公開
- Manifestと実態の不一致放置
- 秘密情報Commit
- 生成Catalog直接編集
- 例外期限無視
- Incident非報告
- 理由なし削除
- 文書版の遡及的書き換え
- 個人Account単独所有
- 形式的自己承認

対応要求：
REQ-GOV-024、REQ-CAT-009、REQ-DOC-016、REQ-SEC-004

---

## 37. 要求トレーサビリティ

参照元：

```text
YSA-REQ-001 Requirements Specification Ver.1.2.2 RC
YSA-ARCH-001 Architecture Specification Ver.1.1.4 RC
```

主要対応：

| Governance領域 | Requirements |
|---|---|
| Owner／Deputy | REQ-GOV-006〜016 |
| Level | REQ-GOV-019〜020 |
| Organization | REQ-GOV-021〜023 |
| 自己承認防止 | REQ-GOV-024〜025 |
| 組織移管 | REQ-GOV-026〜027 |
| Catalog権限 | REQ-CAT-007〜009 |
| AI Review | REQ-AI-001〜006 |
| 文書合同承認 | REQ-DOC-014〜017 |
| 自動検証 | REQ-TST-009〜020 |
| Distribution | REQ-OFF-005〜009 |

---

## 38. Ver.1.1.1 RC完了条件

1. Requirements参照ERROR 0件
2. Requirements／Architecture Version表記一致
3. Organization所有・複数Ownerを収録
4. Level A自己承認防止を収録
5. Catalog編集権限を収録
6. Automated／Manual Reviewを分離
7. Distribution成果物承認を収録
8. 例外、Incident、引き継ぎを収録
9. Claudeによる三文書整合Review
10. 重大指摘解消
11. Project Owner承認

---

## 39. 結論

Governanceは承認作業を増やすためではなく、
担当者やAIが変わっても判断を再現できるようにする制度である。

```text
Roles
+ Independent Review
+ Approval Gates
+ Automated Validation
+ Time-limited Exceptions
+ Incident and Rollback
+ Organization Ownership
+ Handover
= Sustainable Governance
```
