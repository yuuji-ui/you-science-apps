# You Science Apps Platform
# Requirements Specification Ver.1.2.2 — Release Candidate

## 文書管理情報

| 項目 | 内容 |
|---|---|
| 文書名 | You Science Apps Platform Requirements Specification |
| 文書ID | YSA-REQ-001 |
| バージョン | 1.2.2 |
| 状態 | Release Candidate / Draft |
| 前バージョン | 1.2.1 |
| 対象Platform | You Science Apps Platform Ver.1.0 |
| 対応Architecture | YSA-ARCH-001 Ver.1.1.1 Draft（Ver.1.1.2へ更新予定） |
| 対応Governance | YSA-GOV-001 Ver.1.1.0 Draft |
| 文書責任者 | Project Owner |
| 設計・統合作業 | ChatGPT |
| 第三者レビュー | Claude |
| 作成日 | 2026-08-03 |
| 最終更新日 | 2026-08-03 |
| 改訂区分 | PATCH / Consolidation correction |
| 正本区分 | Consolidated Specification |
| 参照検証状態 | Requirements内部自動検証済み・Architecture/Governance照合未実施 |

## 1. 目的

本書は、You Science Apps Platformおよび個別教材が満たすべき要求を、一つの統合正本として定義する。差分資料ではなく、全active要求を収録し、Architecture、Governance、Developer Guide、Teacher Guide、AGENTS.mdおよび個別教材仕様の一次参照先とする。

## 2. 適用範囲

### 2.1 対象システム

- You Science Appsの教材Portal
- Platform Coreおよび共通部品
- 個別教育用Webアプリ
- Manifest、Catalog、Schema、検証・公開ツール
- 設計・運用・引き継ぎ文書

### 2.2 対象教科

- 中学校理科
- 高校化学
- 将来的な高校物理・生物・地学

### 2.3 対象利用者

- 中学生・高校生
- 授業・家庭学習で利用する教員
- 教材開発者・保守担当者
- Platformの承認・レビュー・引き継ぎ担当者

### 2.4 対象利用場面

- 授業導入、演習、実験前後、可視化、宿題、家庭学習、定期考査対策
- Chromebook、iPad、Windows、Mac上の対応ブラウザ

## 3. 用語と必須度

| 表記 | 意味 |
|---|---|
| MUST | 必須。未達時は原則公開不可。 |
| SHOULD | 原則として満たす。未達時は理由と代替策を記録する。 |
| MAY | 任意。教育上・運用上の必要性に応じて採用できる。 |
| MUST NOT | 禁止。 |
| SHOULD NOT | 原則禁止。採用時は理由を記録する。 |

### 3.1 検証方法

| 方法 | 意味 |
|---|---|
| Review | 内容・設計・判断を専門的に確認する。 |
| Inspection | ファイル、記述、設定、構造の存在と整合を確認する。 |
| Test | 実際に実行し、期待結果と比較する。 |
| Demonstration | 手順や復旧等を実演して確認する。 |
| Analysis | 影響、負荷、性能、依存関係等を分析する。 |
| Pilot | 教員または生徒による試験運用で確認する。 |

## 4. 判断の優先順位

要求や設計判断が競合する場合、原則として次の順序を使用する。

1. 生徒の安全
2. プライバシー
3. 科学的正確性
4. 教育効果
5. アクセシビリティ
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

下位の利益を理由に上位の原則を犠牲にしてはならない。Governance Specificationはこの優先順位を参照し、独自の異なる順位を正本として持たない。

## 5. 要求記述・ID運用規則

- ID形式は `REQ-<名前空間>-<3桁番号>` とし、名前空間は複数階層を許可する。
- 例：`REQ-TST-018`、`REQ-EDU-CALC-001`。
- 廃止IDを別の意味に再利用しない。
- 範囲参照は範囲内の全IDが存在する場合に限る。
- 正式レビューでは本文と `requirement-index.json` の一致を検査する。
- 要求追加時は100教材規模の運用負荷を評価する。

## 6. 要求一覧

### 6.1 ガバナンス要求

#### REQ-GOV-001　教育効果優先

**必須度：MUST**  
**検証方法：Review**

新機能は、面白さや新規性ではなく教育効果を根拠として採用する。

#### REQ-GOV-002　長期保守優先

**必須度：MUST**  
**検証方法：Review / Inspection**

短期的な開発速度より長期保守性、可読性、交換可能性、修正容易性を優先する。

#### REQ-GOV-003　過剰機能の抑制

**必須度：MUST**  
**検証方法：Review**

学習目標に直接寄与しないランキング、バッジ、SNS共有、演出等は原則実装しない。

#### REQ-GOV-004　教材資産としての管理

**必須度：MUST**  
**検証方法：Review / Inspection**

各教材を更新・改善・移行・廃止を前提とした教材資産として管理する。

#### REQ-GOV-005　教材障害の局所化

**必須度：MUST**  
**検証方法：Analysis / Test**

個別教材の障害が他教材の動作を妨げない構造とする。

#### REQ-GOV-006　責任者の定義

**必須度：MUST**  
**検証方法：Inspection**

各正式教材には保守責任者または管理主体を定義する。 責任者はREQ-GOV-011の役割と個人の分離原則に従って定義する。

#### REQ-GOV-007　公開承認

**必須度：MUST**  
**検証方法：Review**

正式公開はProject Ownerまたは委任された担当者が承認する。

#### REQ-GOV-008　重大変更の承認

**必須度：MUST**  
**検証方法：Review**

構造、Schema、通信、個人情報、ログイン、ライセンス等の重大変更にはADRとレビューを必要とする。

#### REQ-GOV-009　例外管理

**必須度：MUST**  
**検証方法：Inspection**

要求を満たせない例外は、理由、影響、代替策、期限、承認者を記録する。

#### REQ-GOV-010　定期レビュー

**必須度：MUST**  
**検証方法：Review**

Platform全体を少なくとも年1回レビューする。

#### REQ-GOV-011　役割と個人の分離

**必須度：MUST**  
**検証方法：Review**

Project Owner等を特定個人ではなく意思決定権限を持つ役割として定義する。

#### REQ-GOV-012　副責任者

**必須度：MUST**  
**検証方法：Inspection**

Project Owner不在に備えてDeputy Ownerまたは暫定承認者を定義する。

#### REQ-GOV-013　引き継ぎ文書

**必須度：MUST**  
**検証方法：Inspection**

責任者交代に備え、公開状況、権限、バックアップ、未解決課題、主要ADR等を含む引き継ぎ文書を維持する。

#### REQ-GOV-014　権限継承確認

**必須度：MUST**  
**検証方法：Demonstration**

責任者交代時にGitHub、Pages、バックアップ、ライセンス記録等の権限移管を確認する。

#### REQ-GOV-015　責任者不在時の制限

**必須度：MUST**  
**検証方法：Review**

Project Ownerと代理者が不在の場合、MAJOR更新、Privacy緩和、ライセンス変更等を行わない。

#### REQ-GOV-016　年次継承確認

**必須度：SHOULD**  
**検証方法：Review**

年次レビューで責任者、代理者、アクセス権限、復旧可能性を確認する。

#### REQ-GOV-017　要求追加時の負荷評価

**必須度：MUST**  
**検証方法：Review**

新しいMUST要求追加時は、100教材規模での年間負荷と自動化可能性を評価する。

#### REQ-GOV-018　形骸化要求の見直し

**必須度：MUST**  
**検証方法：Review**

年次レビューで未運用・重複・過大な要求を特定し、自動化、統合、緩和、廃止等を検討する。

#### REQ-GOV-019　教材Level分類

**必須度：MUST**  
**検証方法：Review**

各教材は開発開始時にLevel A、B、Cのいずれかへ分類する。

#### REQ-GOV-020　要求の比例適用

**必須度：MUST**  
**検証方法：Review**

規模・リスクに応じて文書・レビュー負荷を調整するが、安全、Privacy、科学的正確性、Accessibility、Licenseは軽減しない。

#### REQ-GOV-021　正式リポジトリの組織所有

**必須度：MUST**  
**検証方法：Inspection**

正式リポジトリはGitHub Organization等の複数管理者を設定できる組織単位で所有する。

#### REQ-GOV-022　複数管理者

**必須度：MUST**  
**検証方法：Inspection / Demonstration**

正式公開基盤には少なくとも2名の管理可能な責任者を設定する。

#### REQ-GOV-023　暫定個人運営

**必須度：SHOULD NOT**  
**検証方法：Review**

個人アカウントでの暫定運営は移行期限、代理権限、外部バックアップ、移行手順を持ち、原則90日以内に組織所有へ移行する。

#### REQ-GOV-024　自己承認禁止

**必須度：MUST NOT**  
**検証方法：Review**

教材、Platform文書、公開成果物の作成者が単独で正式公開を承認してはならない。

#### REQ-GOV-025　Level A独立レビュー

**必須度：MUST**  
**検証方法：Review**

Level AでもDeveloperとOwnerが同一なら独立Reviewerを追加し、科学内容は人間のSubject Reviewを必要とする。

#### REQ-GOV-026　運営主体の評価

**必須度：MUST**  
**検証方法：Review**

運営主体を明示し、規模拡大時に学校、教育委員会、団体、法人等への移管必要性を評価する。

#### REQ-GOV-027　運営主体移管

**必須度：MUST**  
**検証方法：Review / Inspection**

運営主体変更時はリポジトリ、ドメイン、著作権、ライセンス、問い合わせ窓口、再移管方法等を確認する。

#### REQ-GOV-EXC-001　例外記録

**必須度：MUST**  
**検証方法：Inspection**

MUST要求を満たせない場合は要求ID、理由、影響、代替策、期限、解消条件、承認者を記録する。

### 教育要求

### 6.2 共通教育要求

#### REQ-EDU-001　学習目標の明示

**必須度：MUST**  
**検証方法：Review**

各教材は1〜3項目程度の具体的な到達目標を定義する。

#### REQ-EDU-002　対象学年・単元の明示

**必須度：MUST**  
**検証方法：Inspection**

対象学年、教科、分野、単元を明示する。

#### REQ-EDU-003　利用場面の明示

**必須度：MUST**  
**検証方法：Inspection**

授業導入、演習、実験前後、家庭学習等の推奨利用場面を明示する。

#### REQ-EDU-004　操作と学習内容の一致

**必須度：MUST**  
**検証方法：Review / Pilot**

生徒の操作を学習目標と直接関係させる。

#### REQ-EDU-005　思考を伴う設計

**必須度：MUST**  
**検証方法：Review**

予想、計算、比較、条件変更、観察、説明、修正、振り返りのいずれかを含める。

#### REQ-EDU-006　単純四択への依存抑制

**必須度：SHOULD**  
**検証方法：Review**

四択のみを避け、採用時は誤概念診断や理由説明等の教育的意味を持たせる。

#### REQ-EDU-007　試行錯誤の許容

**必須度：SHOULD**  
**検証方法：Demonstration / Pilot**

操作型教材では誤操作を即終了扱いにせず再試行できるようにする。

#### REQ-EDU-008　誤答から学べること

**必須度：MUST**  
**検証方法：Review / Demonstration**

不正解のみで終えず、誤りの観点、ヒント、再試行方法等を示す。

#### REQ-EDU-009　答えの即時提示抑制

**必須度：SHOULD**  
**検証方法：Review**

初回誤答直後の正解提示を避け、段階的支援を行う。

#### REQ-EDU-010　誤概念への対応

**必須度：SHOULD**  
**検証方法：Review / Pilot**

典型的誤答や誤概念を整理し、必要に応じて個別フィードバックを用意する。

#### REQ-EDU-011　科学的内容の正確性

**必須度：MUST**  
**検証方法：Review / Test**

用語、数値、図、現象、計算、単位、化学式、モデルを科学的に正確にする。

#### REQ-EDU-012　モデルの限界表示

**必須度：MUST**  
**検証方法：Review**

模式図や理想化シミュレーションの限界を必要に応じて示す。

#### REQ-EDU-013　実験代替の誤認防止

**必須度：MUST**  
**検証方法：Review**

シミュレーションを実物実験と同一視させず、違い、誤差、再現しない条件を説明する。

#### REQ-EDU-014　図の科学的整合性

**必須度：MUST**  
**検証方法：Review / Test**

力、粒子、電流、光線、地層等の図を教材内容と整合させる。

#### REQ-EDU-015　難易度の定義

**必須度：MUST**  
**検証方法：Review**

複数難易度は認知的な違いとして定義し、数値拡大だけにしない。

#### REQ-EDU-016　段階的支援

**必須度：SHOULD**  
**検証方法：Review / Demonstration**

初学者向け教材では支援を段階的に減らせる構成を用意する。

#### REQ-EDU-017　発展内容の分離

**必須度：SHOULD**  
**検証方法：Inspection**

対象学年を超える発展内容を標準内容と明確に分離する。

### 機能要求

### 6.3 計算練習型教材の追加要求

#### REQ-EDU-CALC-001　計算過程の学習支援

**必須度：MUST**  
**検証方法：Review / Demonstration**

計算練習型教材は、最終解答だけでなく、式、代入、単位変換、途中結果等の学習過程を必要に応じて確認・支援できるようにする。

#### REQ-EDU-CALC-002　単位・有効数字の判定

**必須度：MUST**  
**検証方法：Test / Review**

単位、有効数字、指数表記、丸めが学習目標に含まれる場合、数値の正誤と区別して判定し、誤りの種類を示す。

#### REQ-EDU-CALC-003　数値条件の教育的妥当性

**必須度：MUST**  
**検証方法：Review / Test**

出題値は対象学年と学習目標に適した計算量とし、意図しない端数や不自然な数値が生じないよう設計する。端数を扱う場合は丸め規則を明示する。

#### REQ-EDU-CALC-004　誤答原因の区別

**必須度：SHOULD**  
**検証方法：Review / Test**

可能な場合、公式選択、代入、演算、単位変換、有効数字等の誤答原因を区別し、原因に対応した支援を行う。

### 6.4 シミュレーション型教材の追加要求

#### REQ-EDU-SIM-001　変更可能条件と固定条件

**必須度：MUST**  
**検証方法：Inspection / Pilot**

シミュレーション型教材は、利用者が変更できる条件と固定された条件を明確に区別して表示する。

#### REQ-EDU-SIM-002　条件変更と結果の対応

**必須度：MUST**  
**検証方法：Review / Test**

条件変更に対する表示・数値・グラフ・モデルの変化は、科学的関係と一貫し、同一条件では再現可能な結果を示す。

#### REQ-EDU-SIM-003　シミュレーションモデルの限界

**必須度：MUST**  
**検証方法：Review**

省略した要因、理想化、適用範囲、実物との違いを教材内または教員向け情報で明示する。

#### REQ-EDU-SIM-004　実験との関係

**必須度：MUST**  
**検証方法：Review / Pilot**

実験を扱うシミュレーションは、実物実験を完全に代替するものと誤認させず、観察、測定誤差、安全操作等の違いを示す。

#### REQ-EDU-SIM-005　危険条件の誤学習防止

**必須度：MUST**  
**検証方法：Review / Test**

現実には危険または不適切な条件を操作可能にする場合、危険性を明示し、安全な実験手順として受け取られない表現にする。

### 6.5 ドラッグ操作型教材の追加要求

#### REQ-EDU-DRAG-001　ドラッグ操作の代替

**必須度：MUST**  
**検証方法：Test**

ドラッグ操作型教材は、タップ選択、ボタン、キーボード等による代替操作を提供する。

#### REQ-EDU-DRAG-002　配置状態と判定の明示

**必須度：MUST**  
**検証方法：Test / Pilot**

移動可能な対象、配置可能な場所、現在の選択状態、判定を行うタイミングを利用者が理解できるようにする。

#### REQ-EDU-DRAG-003　誤配置からの回復

**必須度：MUST**  
**検証方法：Test / Pilot**

誤った配置を即座に取り返しのつかない失敗とせず、移動、取り消し、再試行、初期化のいずれかを可能にする。

### 6.6 実験型教材の追加要求

#### REQ-EDU-EXP-001　安全情報の優先表示

**必須度：MUST**  
**検証方法：Review / Inspection**

実験型教材は、薬品、加熱、電気、ガラス器具、生物試料等に関する安全上の注意を、操作前に確認できる形で示す。

#### REQ-EDU-EXP-002　実験条件と観察項目

**必須度：MUST**  
**検証方法：Review / Pilot**

操作する条件、揃える条件、測定・観察する項目を区別し、比較実験として妥当な構成にする。

#### REQ-EDU-EXP-003　実験結果の確定表現抑制

**必須度：MUST**  
**検証方法：Review**

実験結果にはばらつきや誤差が生じることを踏まえ、必ず同一結果になると誤認させる断定表現を避ける。

#### REQ-EDU-EXP-004　実物実験への接続

**必須度：SHOULD**  
**検証方法：Review / Pilot**

実験型教材は、予想、手順確認、結果整理、考察等のどの段階を支援するかを明示し、実物実験との接続を示す。

### 6.7 可視化教材の追加要求

#### REQ-EDU-VIS-001　可視化対象と凡例

**必須度：MUST**  
**検証方法：Inspection / Pilot**

可視化教材は、色、矢印、粒子、線、記号、グラフ等が何を表すかを凡例または説明で示す。

#### REQ-EDU-VIS-002　尺度と誇張の明示

**必須度：MUST**  
**検証方法：Review**

大きさ、距離、時間、個数、速度等を実際と異なる尺度で示す場合、模式化・誇張・縮尺非対応であることを明示する。

#### REQ-EDU-VIS-003　視点・表示切替の一貫性

**必須度：SHOULD**  
**検証方法：Test / Pilot**

拡大縮小、表示切替、視点変更を行う場合、対象の同一性と変化の意味を見失わない表示にする。

#### REQ-EDU-VIS-004　可視化による誤概念防止

**必須度：MUST**  
**検証方法：Review / Pilot**

不可視の粒子、力、電流、場等の可視化を実体そのものと誤認させないよう、表現の意味と限界を示す。

### 6.8 機能要求

#### REQ-FUN-001　教材開始

**必須度：MUST**  
**検証方法：Test**

URLを開いた後、登録・ログインなしで開始できる。

#### REQ-FUN-002　操作説明

**必須度：MUST**  
**検証方法：Inspection / Demonstration**

主要操作を開始前または画面内で確認できる。

#### REQ-FUN-003　初期状態への復帰

**必須度：MUST**  
**検証方法：Test**

利用者が教材を初期状態へ戻せる。

#### REQ-FUN-004　前画面への復帰

**必須度：MUST**  
**検証方法：Test**

複数画面教材では主要画面やメニューへ戻れる。

#### REQ-FUN-005　再試行

**必須度：MUST**  
**検証方法：Test**

演習型教材では再回答または新しい問題へ進める。

#### REQ-FUN-006　状態表示

**必須度：MUST**  
**検証方法：Inspection**

問題番号、段階、条件、進行状況等の現在状態を表示する。

#### REQ-FUN-007　処理結果の説明

**必須度：MUST**  
**検証方法：Review / Demonstration**

計算・判定結果を意味の理解できる形で表示する。

#### REQ-FUN-008　設定の必要性

**必須度：MUST**  
**検証方法：Review**

設定項目は教育上またはAccessibility上の必要性がある場合に限る。

#### REQ-FUN-009　設定初期値

**必須度：MUST**  
**検証方法：Review / Test**

設定初期値を安全で標準的な値にする。

#### REQ-FUN-010　設定の初期化

**必須度：SHOULD**  
**検証方法：Test**

保存設定を初期値に戻せるようにする。

#### REQ-FUN-011　保存機能の限定

**必須度：MUST**  
**検証方法：Review / Inspection**

保存機能は必要な場合のみ使用し、保存対象、場所、期間、削除方法を明示する。

#### REQ-FUN-012　共有端末への配慮

**必須度：MUST**  
**検証方法：Review / Test**

共有端末で他利用者に見られると問題になる情報を保存しない。

#### REQ-FUN-013　印刷対応

**必須度：MAY**  
**検証方法：Test**

教育効果がある場合は印刷機能を提供してよい。

### UI・操作要求

### 6.9 UI・操作要求

#### REQ-UI-001　タッチ操作

**必須度：MUST**  
**検証方法：Test**

主要機能をタッチ操作だけで利用できる。

#### REQ-UI-002　主要文字サイズ

**必須度：MUST**  
**検証方法：Inspection**

本文・主要操作文字は原則16px未満にしない。

#### REQ-UI-003　タップ領域

**必須度：MUST**  
**検証方法：Inspection / Test**

主要操作領域を概ね44×44 CSS px以上とする。

#### REQ-UI-004　ホバー非依存

**必須度：MUST**  
**検証方法：Inspection**

ホバーだけで操作や説明を提供しない。

#### REQ-UI-005　画面内操作説明

**必須度：MUST**  
**検証方法：Inspection / Pilot**

別文書を読まなくても主要操作を理解できる。

#### REQ-UI-006　一貫した配置

**必須度：SHOULD**  
**検証方法：Review**

戻る、リセット、設定、ヘルプ等の共通操作を教材間で一貫させる。

#### REQ-UI-007　危険操作の確認

**必須度：SHOULD**  
**検証方法：Test**

入力や記録を消す操作に確認または取り消し手段を設ける。

#### REQ-UI-008　過剰な画面遷移の抑制

**必須度：SHOULD**  
**検証方法：Pilot**

学習活動に不要な画面遷移を要求しない。

#### REQ-UI-009　情報量の調整

**必須度：MUST**  
**検証方法：Review / Pilot**

一画面に情報を詰め込みすぎず、重要情報を優先する。

#### REQ-UI-010　端末回転

**必須度：SHOULD**  
**検証方法：Test**

縦向き・横向きの双方へ配慮し、推奨方向があれば明示する。

### アクセシビリティ要求

### 6.10 アクセシビリティ要求

#### REQ-ACC-001　色以外の情報伝達

**必須度：MUST**  
**検証方法：Inspection / Test**

正誤、選択、警告等を色だけで示さない。

#### REQ-ACC-002　キーボード操作

**必須度：MUST**  
**検証方法：Test**

主要機能を可能な範囲でキーボードだけでも操作できる。

#### REQ-ACC-003　フォーカス表示

**必須度：MUST**  
**検証方法：Test**

キーボードフォーカスを視覚表示する。

#### REQ-ACC-004　読み上げラベル

**必須度：MUST**  
**検証方法：Inspection**

入力、ボタン、アイコン、図表に識別可能なラベルまたは代替テキストを付ける。

#### REQ-ACC-005　ドラッグ代替

**必須度：MUST**  
**検証方法：Test**

ドラッグ必須操作にはタップ、ボタン、キーボード等の代替を用意する。

#### REQ-ACC-006　拡大表示

**必須度：MUST**  
**検証方法：Test**

200%程度の拡大でも主要機能を利用できる。

#### REQ-ACC-007　アニメーション制御

**必須度：MUST**  
**検証方法：Review / Test**

不要な自動アニメーションを避け、必要時は停止等を用意する。

#### REQ-ACC-008　点滅抑制

**必須度：MUST NOT**  
**検証方法：Inspection**

強い点滅や短時間の反復点滅を使用しない。

#### REQ-ACC-009　音声非依存

**必須度：MUST**  
**検証方法：Test**

音声を聞かなければ学習できない構成にしない。

#### REQ-ACC-010　音量初期値

**必須度：MUST**  
**検証方法：Test**

音声を突然大音量で再生せず、学校環境では原則消音または控えめにする。

#### REQ-ACC-011　制限時間への配慮

**必須度：SHOULD**  
**検証方法：Review**

制限時間の教育目的を明示し、通常学習には時間なしの選択肢を検討する。

### プライバシー要求

### 6.11 プライバシー要求

#### REQ-PRI-001　個人情報非収集

**必須度：MUST**  
**検証方法：Review / Inspection**

氏名、学籍番号、メール等の個人識別情報を収集しない。

#### REQ-PRI-002　ログイン不要

**必須度：MUST**  
**検証方法：Test**

標準教材はログインなしで利用できる。

#### REQ-PRI-003　アクセス解析禁止

**必須度：MUST NOT**  
**検証方法：Inspection**

Google Analytics等のアクセス解析を導入しない。

#### REQ-PRI-004　広告禁止

**必須度：MUST NOT**  
**検証方法：Inspection**

広告、アフィリエイト、追跡型コンテンツを表示しない。

#### REQ-PRI-005　不要なCookie禁止

**必須度：MUST NOT**  
**検証方法：Inspection**

標準教材はCookieを使用しない。例外はADR、Privacy文書、Manifestへ記載する。

#### REQ-PRI-006　外部送信禁止

**必須度：MUST**  
**検証方法：Inspection / Test**

利用状況、解答、端末情報を外部送信しない。

#### REQ-PRI-007　端末内保存の明示

**必須度：MUST**  
**検証方法：Inspection**

localStorage等の保存内容をREADMEとManifestに記載する。

#### REQ-PRI-008　保存データ削除

**必須度：MUST**  
**検証方法：Test**

端末内保存データを利用者が削除できる。

### 安全・セキュリティ要求

### 6.12 安全・セキュリティ要求

#### REQ-SEC-001　不要な外部コード禁止

**必須度：MUST NOT**  
**検証方法：Inspection**

用途不明の外部スクリプト、追跡コード、埋め込みを使用しない。

#### REQ-SEC-002　入力値検証

**必須度：MUST**  
**検証方法：Test**

利用者入力の型、範囲、形式を検証する。

#### REQ-SEC-003　HTML直接挿入の抑制

**必須度：MUST**  
**検証方法：Inspection**

利用者入力を未処理でinnerHTML等へ挿入しない。

#### REQ-SEC-004　秘密情報の非保持

**必須度：MUST NOT**  
**検証方法：Inspection**

APIキー、パスワード、秘密鍵等を公開コードへ保存しない。

#### REQ-SEC-005　外部リンク

**必須度：SHOULD**  
**検証方法：Review**

外部リンクを必要最小限にし、教育目的等が明確な場合に限る。

#### REQ-SEC-006　エラー情報

**必須度：MUST**  
**検証方法：Test**

利用者向けエラーへ内部構造や機密情報を不必要に表示しない。

### 非機能要求

### 6.13 非機能要求

#### REQ-NFR-001　初期表示性能

**必須度：SHOULD**  
**検証方法：Test**

REQ-CMP-008で定義する基準環境において、キャッシュなしの初回アクセスから主要画面を概ね3秒以内に利用可能とする。超過時は読込表示、軽量化、遅延読込または合理的理由の記録を行う。

#### REQ-NFR-002　操作応答

**必須度：MUST**  
**検証方法：Test**

通常操作で長時間の無反応状態を生じさせない。

#### REQ-NFR-003　アニメーション性能

**必須度：SHOULD**  
**検証方法：Test**

一般的なChromebook・iPadで実用的な速度で動作する。

#### REQ-NFR-004　単一教材障害

**必須度：MUST**  
**検証方法：Analysis**

1教材の不具合が他教材を停止させない。

#### REQ-NFR-005　外部サービス障害

**必須度：MUST**  
**検証方法：Analysis / Test**

外部サービス停止時も主要学習機能を維持する。

#### REQ-NFR-006　コード可読性

**必須度：MUST**  
**検証方法：Inspection**

意味の分かる変数名、関数名、ファイル名を使用する。

#### REQ-NFR-007　過剰な圧縮禁止

**必須度：MUST NOT**  
**検証方法：Inspection**

保守対象コードを難読化状態のみで保存しない。

#### REQ-NFR-008　教材追加

**必須度：MUST**  
**検証方法：Analysis**

既存教材コードを変更せず新教材を追加できる。

#### REQ-NFR-009　教科追加

**必須度：SHOULD**  
**検証方法：Analysis**

高校物理・生物・地学追加時にPlatform全体の再構築を必要としない。

#### REQ-NFR-010　教材容量目安

**必須度：SHOULD**  
**検証方法：Analysis / Test**

標準教材の初期読込容量は圧縮後5MB以下を目標とする。

### 互換性要求

### 6.14 互換性要求

#### REQ-CMP-001　Chromebook対応

**必須度：MUST**  
**検証方法：Test**

一般的なChromebookで主要機能を利用できる。

#### REQ-CMP-002　iPad対応

**必須度：MUST**  
**検証方法：Test**

Safariを使用する一般的なiPadで主要機能を利用できる。

#### REQ-CMP-003　Windows対応

**必須度：MUST**  
**検証方法：Test**

WindowsのChromeまたはEdgeで主要機能を利用できる。

#### REQ-CMP-004　Mac対応

**必須度：MUST**  
**検証方法：Test**

MacのSafariまたはChromeで主要機能を利用できる。

#### REQ-CMP-005　ブラウザ標準優先

**必須度：MUST**  
**検証方法：Inspection**

特定ブラウザ独自機能を避け、標準Web APIを優先する。

#### REQ-CMP-006　最低画面幅

**必須度：MUST**  
**検証方法：Test**

320 CSS px程度でも主要機能が致命的に崩れない。

#### REQ-CMP-007　スマートフォン配慮

**必須度：SHOULD**  
**検証方法：Test**

主対象外でも閲覧・操作不能にならない範囲で配慮する。

#### REQ-CMP-008　基準端末プロファイル

**必須度：MUST**  
**検証方法：Inspection**

supported-environments.mdで端末、OS、ブラウザ、画面、確認日、制約を定義する。

#### REQ-CMP-009　特定機種への固定禁止

**必須度：MUST**  
**検証方法：Review**

性能基準を特定配備機種だけに固定せず、性能区分とブラウザ環境で定義する。

### オフライン・配布要求

### 6.15 オフライン・配布要求

#### REQ-OFF-001　主要機能の通信非依存

**必須度：MUST**  
**検証方法：Test**

主要学習機能を外部APIや常時通信に依存させない。

#### REQ-OFF-002　CDN非依存

**必須度：SHOULD**  
**検証方法：Inspection**

必要ファイルを原則リポジトリ内に保持する。

#### REQ-OFF-003　保存可能な配布成果物

**必須度：SHOULD**  
**検証方法：Test**

小規模教材または必要性の高い教材は、検証済みPortableまたはStandalone成果物を保存利用できるようにする。

#### REQ-OFF-004　ネットワーク要求表示

**必須度：MUST**  
**検証方法：Inspection**

外部通信が必要な機能は利用前に明示する。

#### REQ-OFF-005　配布形態の明示

**必須度：MUST**  
**検証方法：Inspection**

Hosted、Portable、Standaloneの対応状況を明示する。

#### REQ-OFF-006　Hosted版

**必須度：MUST**  
**検証方法：Test**

Hosted版は承認済み公開基盤で動作し、未解決パスを含まずCatalog URLと一致する。

#### REQ-OFF-007　Portable版

**必須度：SHOULD**  
**検証方法：Test / Inspection**

必要な教材は実行時依存を同梱し、外部CDNや未解決パスを含まないPortable版を提供する。

#### REQ-OFF-008　直接ファイル起動

**必須度：MUST**  
**検証方法：Test**

file://対応を表明するPortable版は実際にネットワーク切断状態で直接起動テストする。

#### REQ-OFF-009　開発ソースと配布物の区別

**必須度：MUST**  
**検証方法：Inspection**

開発用ソースと正式Portable配布物を明確に区別しREADMEへ記載する。

### データ要求

### 6.16 データ要求

#### REQ-DAT-001　データとロジックの分離

**必須度：MUST**  
**検証方法：Inspection**

問題文、正解、解説、物質情報等を可能な限り処理ロジックから分離する。

#### REQ-DAT-002　編集箇所の集約

**必須度：MUST**  
**検証方法：Inspection**

教員が編集するデータを専用領域へ集約する。

#### REQ-DAT-003　データID

**必須度：MUST**  
**検証方法：Inspection**

管理対象データへ一意で安定したIDを付与する。

#### REQ-DAT-004　ID再利用禁止

**必須度：MUST NOT**  
**検証方法：Inspection**

廃止IDを別の意味で再利用しない。

#### REQ-DAT-005　単位の分離

**必須度：SHOULD**  
**検証方法：Inspection**

数値と単位を分離して管理する。

#### REQ-DAT-006　数値精度

**必須度：MUST**  
**検証方法：Review / Test**

丸め、許容誤差、有効数字、表示桁数を明示的に管理する。

#### REQ-DAT-007　データSchema

**必須度：MUST**  
**検証方法：Inspection / Test**

共通データ形式にJSON Schema等のSchemaを用意する。

#### REQ-DAT-008　Schemaバージョン

**必須度：MUST**  
**検証方法：Inspection**

データ形式にSchema Versionを記録する。

#### REQ-DAT-009　Schemaファイルの同梱

**必須度：MUST**  
**検証方法：Inspection**

検証対象データ形式のSchemaファイルをリポジトリ内に保持する。

#### REQ-DAT-010　Schemaを機械判定の正本とする

**必須度：MUST**  
**検証方法：Review / Test**

Manifest・Catalog構造の機械判定ではSchemaを正本とする。

#### REQ-DAT-011　Schema変更手順

**必須度：MUST**  
**検証方法：Review**

Schema変更時に互換性、移行、テスト、CHANGELOG等を更新する。

#### REQ-DAT-012　Schema例示データ

**必須度：MUST**  
**検証方法：Test**

主要Schemaに正常例・異常例を用意し、期待どおり検証されることを確認する。

### Manifest要求

### 6.17 Manifest要求

#### REQ-MAN-001　Manifest必須

**必須度：MUST**  
**検証方法：Inspection**

正式公開教材はapp.manifest.jsonを持つ。

#### REQ-MAN-002　Manifest検証

**必須度：MUST**  
**検証方法：Test**

Manifestを対応Schemaで公開前に検証する。

#### REQ-MAN-003　基本情報

**必須度：MUST**  
**検証方法：Inspection**

ManifestにID、title、version、status、教育情報、Privacy、License等を含める。

#### REQ-MAN-004　状態の正確性

**必須度：MUST**  
**検証方法：Test / Inspection**

Manifest statusをCatalogと実際の公開状態に一致させる。

#### REQ-MAN-005　依存情報

**必須度：MUST**  
**検証方法：Inspection**

外部ライブラリ、通信、Platform Core依存をManifestへ記録する。

#### REQ-MAN-006　配布情報

**必須度：MUST**  
**検証方法：Inspection / Test**

Hosted、Portable、Standalone等の配布情報をManifestへ記録する。

#### REQ-MAN-007　参照実装履歴

**必須度：MUST**  
**検証方法：Inspection**

公式参照実装の名称、Version、コピー日、改変有無をManifestへ記録する。

#### REQ-MAN-008　参照実装履歴の保持

**必須度：MUST**  
**検証方法：Inspection / Test**

大幅改変後も参照元履歴を保持し、影響教材を抽出可能にする。

### Catalog要求

### 6.18 Catalog要求

#### REQ-CAT-001　公式台帳

**必須度：MUST**  
**検証方法：Inspection**

Catalogを教材の公式横断台帳として管理する。

#### REQ-CAT-002　教材登録

**必須度：MUST**  
**検証方法：Test**

正式公開教材をCatalogへ登録する。

#### REQ-CAT-003　Manifestとの整合

**必須度：MUST**  
**検証方法：Test**

Catalog情報を各Manifestと矛盾させない。

#### REQ-CAT-004　状態管理

**必須度：MUST**  
**検証方法：Inspection**

proposalからarchivedまでの教材状態を識別できるようにする。

#### REQ-CAT-005　検索分類

**必須度：SHOULD**  
**検証方法：Inspection**

学校段階、学年、教科、単元、形式、利用場面等の検索情報を持つ。

#### REQ-CAT-006　廃止履歴

**必須度：MUST**  
**検証方法：Inspection**

廃止教材もCatalogまたは台帳へ履歴を残す。

#### REQ-CAT-007　Catalog情報の責任分離

**必須度：MUST**  
**検証方法：Review / Test**

Manifest管理情報とPortal運用情報を分離する。

#### REQ-CAT-008　Catalog運用情報の編集権限

**必須度：MUST**  
**検証方法：Review / Inspection**

Portal運用情報は権限を付与されたPortal Maintainer等のみが変更する。

#### REQ-CAT-009　生成成果物の直接編集禁止

**必須度：MUST NOT**  
**検証方法：Inspection / Test**

自動生成catalog.jsonを直接編集しない。

#### REQ-CAT-010　Catalog生成整合性

**必須度：MUST**  
**検証方法：Test**

参照、重複、上書き、status組合せ、Schema適合を検証し、失敗時は公開停止する。

### 学習指導要領対応要求

### 6.19 学習指導要領対応要求

#### REQ-CUR-001　単元IDによる対応

**必須度：MUST**  
**検証方法：Inspection**

教材と指導要領を安定した単元IDで対応付ける。

#### REQ-CUR-002　年度別管理

**必須度：MUST**  
**検証方法：Inspection**

指導要領対応情報を改訂年度・版ごとに管理する。

#### REQ-CUR-003　旧版保持

**必須度：MUST**  
**検証方法：Inspection**

旧指導要領対応データを理由なく上書き・削除しない。

#### REQ-CUR-004　変更影響判定

**必須度：MUST**  
**検証方法：Analysis**

指導要領変更時に修正不要、要確認、軽微修正、重大修正、廃止候補へ分類できる。

#### REQ-CUR-005　教科書依存の抑制

**必須度：SHOULD**  
**検証方法：Review**

特定教科書会社固有のページ番号や図版を教材中核へ使用しない。

### 保守要求

### 6.20 保守要求

#### REQ-MNT-001　教材独立ディレクトリ

**必須度：MUST**  
**検証方法：Inspection**

各教材を原則独立ディレクトリで管理する。

#### REQ-MNT-002　共通部と固有部の分離

**必須度：MUST**  
**検証方法：Review / Inspection**

共通UI、共通処理、教材固有処理、教材データの責任を区別する。

#### REQ-MNT-003　Platform Core依存の明示

**必須度：MUST**  
**検証方法：Inspection**

利用するCore Versionを明示する。

#### REQ-MNT-004　一括破壊的更新禁止

**必須度：MUST NOT**  
**検証方法：Review**

Core変更を検証なしに全教材へ強制適用しない。

#### REQ-MNT-005　教員編集箇所

**必須度：MUST**  
**検証方法：Inspection**

編集可能箇所と変更禁止箇所を明示する。

#### REQ-MNT-006　変更履歴

**必須度：MUST**  
**検証方法：Inspection**

各正式教材はCHANGELOGを持つ。

#### REQ-MNT-007　既知の制約

**必須度：MUST**  
**検証方法：Inspection**

既知の制約や未対応条件をREADME等に記載する。

#### REQ-MNT-008　年次点検

**必須度：MUST**  
**検証方法：Review / Test**

正式教材を年1回以上、起動、内容、ブラウザ、指導要領、Accessibility、License等で点検する。

#### REQ-MNT-009　無担当状態への配慮

**必須度：MUST**  
**検証方法：Review**

特定担当者だけが理解できる構造や運用にしない。

### バージョン管理要求

### 6.21 バージョン管理要求

#### REQ-VER-001　Semantic Versioning

**必須度：MUST**  
**検証方法：Inspection**

Platformと教材は原則SemVerを使用する。

#### REQ-VER-002　Platformと教材の分離

**必須度：MUST**  
**検証方法：Inspection**

Platform Versionと教材Versionを分ける。

#### REQ-VER-003　Version表示

**必須度：MUST**  
**検証方法：Inspection**

利用者・教員が教材Versionを確認できるようにする。

#### REQ-VER-004　破壊的変更

**必須度：MUST**  
**検証方法：Review**

後方互換性を壊す変更をMAJOR更新とし、移行方法を文書化する。

#### REQ-VER-005　データ互換性

**必須度：SHOULD**  
**検証方法：Test**

データ形式変更時は移行または非互換表示を用意する。

### 廃止・移行要求

### 6.22 廃止・移行要求

#### REQ-DEP-001　廃止状態

**必須度：MUST**  
**検証方法：Inspection**

正式終了前に原則deprecatedを経由する。

#### REQ-DEP-002　廃止理由

**必須度：MUST**  
**検証方法：Inspection**

廃止理由を記録する。

#### REQ-DEP-003　後継教材

**必須度：SHOULD**  
**検証方法：Inspection**

後継教材があれば案内する。

#### REQ-DEP-004　移行期間

**必須度：SHOULD**  
**検証方法：Review**

重大問題がない限りdeprecatedからretiredまで標準1年程度の移行期間を設ける。

#### REQ-DEP-005　廃止教材の保存

**必須度：MUST**  
**検証方法：Inspection**

コード、Manifest、CHANGELOG、廃止理由をArchiveする。

#### REQ-DEP-006　削除の抑制

**必須度：MUST**  
**検証方法：Review**

法的・Privacy・安全上の例外を除き履歴を残さず完全削除しない。

### 文書要求

### 6.23 文書要求

#### REQ-DOC-001　README

**必須度：MUST**  
**検証方法：Inspection**

各正式教材は対象、目標、利用方法、通信、保存、編集箇所、制約、License、Versionを含むREADMEを持つ。

#### REQ-DOC-002　CHANGELOG

**必須度：MUST**  
**検証方法：Inspection**

各正式教材はCHANGELOGを持つ。

#### REQ-DOC-003　Teacher Notes

**必須度：MUST**  
**検証方法：Inspection**

授業使用例、時間、説明、つまずき、限界、編集方法を教員向けに提供する。

#### REQ-DOC-004　文書メタデータ

**必須度：MUST**  
**検証方法：Inspection**

正式文書に状態、責任者、更新日、対象Versionを記載する。

#### REQ-DOC-005　ADR

**必須度：MUST**  
**検証方法：Inspection**

重要な設計判断をADRとして記録する。

#### REQ-DOC-006　文書状態

**必須度：MUST**  
**検証方法：Inspection**

Draft、Active、Deprecated、Archivedを使用する。

#### REQ-DOC-007　チェックリスト版の提供

**必須度：MUST**  
**検証方法：Inspection**

日常運用向けに1〜2ページ相当の簡潔なチェックリストを提供する。

#### REQ-DOC-008　詳細文書とチェックリストの対応

**必須度：MUST**  
**検証方法：Inspection**

チェックリスト各項目へ対応要求IDを記載する。

#### REQ-DOC-009　重複管理の禁止

**必須度：MUST**  
**検証方法：Review**

要求正本を詳細仕様書とし、チェックリストで意味を独自変更しない。

#### REQ-DOC-010　未完成文書への必須依存禁止

**必須度：MUST**  
**検証方法：Review**

Active文書を存在しない、または使用不能なDraftだけへ依存させない。

#### REQ-DOC-011　依存文書の状態明示

**必須度：MUST**  
**検証方法：Inspection**

参照文書ID、Version、状態を記録する。

#### REQ-DOC-012　要求仕様の統合正本

**必須度：MUST**  
**検証方法：Inspection**

正式Requirementsは全active要求を含む統合正本として提供する。

#### REQ-DOC-013　Architecture整合性確認

**必須度：MUST**  
**検証方法：Review**

公開・文書・教材・Catalog・Schema・Archive・検証配置をArchitectureと照合する。

#### REQ-DOC-014　Review Package

**必須度：MUST**  
**検証方法：Inspection**

相互依存文書をREVIEW-INDEX、本文、要求台帳、検証結果等を含むPackageでレビューする。

#### REQ-DOC-015　参照状態の明示

**必須度：MUST**  
**検証方法：Inspection**

未照合、手動照合済み・自動未実施、自動検証済みのいずれかを明示する。

#### REQ-DOC-016　訂正履歴

**必須度：MUST**  
**検証方法：Review / Inspection**

文書誤りを遡及的に正当化せず、誤り、正しい内容、影響、再発防止を記録する。

#### REQ-DOC-017　文書合同承認

**必須度：MUST**  
**検証方法：Review**

相互依存するRequirements、Architecture、GovernanceをPackage単位で合同承認する。

### 開発要求

### 6.24 開発要求

#### REQ-DEV-001　設計先行

**必須度：MUST**  
**検証方法：Review**

実装前に目標、対象、利用場面、画面、操作、機能、誤答、テスト等を定義する。

#### REQ-DEV-002　レビュー先行

**必須度：MUST**  
**検証方法：Review**

正式実装前に設計レビューを行う。

#### REQ-DEV-003　命名規則

**必須度：MUST**  
**検証方法：Inspection**

ファイル、appId、変数、関数、CSSを命名規則に従わせる。

#### REQ-DEV-004　コメント

**必須度：MUST**  
**検証方法：Inspection**

教育固有ロジック、複雑計算、編集対象、互換処理に意図を説明するコメントを付ける。

#### REQ-DEV-005　外部ライブラリ

**必須度：MUST**  
**検証方法：Review**

必要性、License、更新、容量、Offline、交換可能性、Security、代替を確認する。

#### REQ-DEV-006　ライブラリラッパー

**必須度：SHOULD**  
**検証方法：Inspection**

外部ライブラリを可能な限りAdapter経由で利用する。

#### REQ-DEV-007　ブラウザ標準API

**必須度：SHOULD**  
**検証方法：Review**

標準APIで十分なら外部ライブラリより優先する。

#### REQ-DEV-008　管理対象ツール

**必須度：MUST**  
**検証方法：Review**

公開・変換・検証・移行ツールを管理対象ソフトウェアとして扱う。

#### REQ-DEV-009　ツール文書

**必須度：MUST**  
**検証方法：Inspection**

主要ツールにREADME、Version、入出力、エラー、使用例、CHANGELOG、テスト手順を持たせる。

#### REQ-DEV-010　再現可能な生成

**必須度：SHOULD**  
**検証方法：Test**

同一入力と設定から同等の成果物を再生成できるようにする。

#### REQ-DEV-011　ツールの破壊的変更

**必須度：MUST**  
**検証方法：Review / Test**

主要ツールの破壊的変更にMAJOR更新、影響分析、移行、回帰テスト、ADR等を行う。

### テスト要求

### 6.25 テスト要求

#### REQ-TST-001　公開前テスト

**必須度：MUST**  
**検証方法：Review**

正式公開前に機能、内容、操作、端末、Accessibilityをテストする。

#### REQ-TST-002　計算テスト

**必須度：MUST**  
**検証方法：Test**

代表値、境界値、ゼロ、負値、不正入力、丸め、有効数字を確認する。

#### REQ-TST-003　科学内容テスト

**必須度：MUST**  
**検証方法：Review**

教科担当者または同等知識者が内容を確認する。

#### REQ-TST-004　端末テスト

**必須度：MUST**  
**検証方法：Test**

Chromebook、iPad、Windows、Macで確認し、未確認環境は明示する。

#### REQ-TST-005　入力異常

**必須度：MUST**  
**検証方法：Test**

未入力、文字、極端値、連打、回転、再読込等を確認する。

#### REQ-TST-006　Accessibilityテスト

**必須度：MUST**  
**検証方法：Test**

キーボード、フォーカス、色、拡大、タッチ、ドラッグ代替、ラベルを確認する。

#### REQ-TST-007　試験運用

**必須度：SHOULD**  
**検証方法：Pilot**

正式公開前に少人数または1クラス程度でPilotする。

#### REQ-TST-008　回帰テスト

**必須度：MUST**  
**検証方法：Test**

修正時に主要機能が壊れていないことを確認する。

#### REQ-TST-009　継続的自動検証

**必須度：MUST**  
**検証方法：Demonstration**

GitHub Actionsまたは同等手段で継続的な自動検証を実行する。

#### REQ-TST-010　自動検証の最低項目

**必須度：MUST**  
**検証方法：Test**

Manifest、Catalog、appId、Version、必須ファイル、リンク、構文、外部参照、広告・解析、Licenseを検証する。

#### REQ-TST-011　自動Accessibility検査

**必須度：SHOULD**  
**検証方法：Test / Review**

ラベル、alt、見出し、重複ID、コントラスト等を自動検査する。

#### REQ-TST-012　自動検証失敗時の公開禁止

**必須度：MUST**  
**検証方法：Inspection**

MUST関連の自動検証失敗時にactive公開しない。

#### REQ-TST-013　検証ツールの交換可能性

**必須度：MUST**  
**検証方法：Inspection / Demonstration**

検証ロジックをリポジトリ内へ保持し、CI以外でも実行可能にする。

#### REQ-TST-014　人力検証との役割分担

**必須度：MUST**  
**検証方法：Review / Pilot**

科学的正確性、教育効果、学年相応性等は自動検証だけで合格判定しない。

#### REQ-TST-015　生成ツールのUnit Test

**必須度：MUST**  
**検証方法：Test**

主要生成・検証ツールに正常・異常・境界入力のUnit Testを持たせる。

#### REQ-TST-016　生成パイプラインのIntegration Test

**必須度：MUST**  
**検証方法：Test**

Manifest収集からHosted・Portable成果物の最終検証までを統合テストする。

#### REQ-TST-017　Portable版テスト

**必須度：MUST**  
**検証方法：Test**

Portable対応教材でOffline起動、依存、素材、データ、結果、保存、Hosted一致を確認する。

#### REQ-TST-018　要求ID参照自動検査

**必須度：MUST**  
**検証方法：Test**

正式文書の要求ID、参照Version、欠番、Deprecated、仮ID、Review Package欠落を自動検査する。検査対象IDは `REQ-EDU-CALC-001` のような可変階層の名前空間を含む。

#### REQ-TST-019　要求参照検査結果

**必須度：MUST**  
**検証方法：Inspection**

対象文書、Version、Requirements、日時、ツールVersion、Commit、ERROR/WARNING、結果を記録する。

#### REQ-TST-020　検査ツール自身の検証

**必須度：MUST**  
**検証方法：Test**

検査ツールに正常例・異常例を用意し、意図したエラーを検出できることを確認する。異常例には、カテゴリ群の丸ごとの欠落、可変階層IDの欠落、重複、未解決参照を含める。

### 6.26 公開・リリース要求

#### REQ-REL-001　公開ゲート

**必須度：MUST**  
**検証方法：Review**

Proposal、Design、Review、Development、Technical、Educational、Pilot、Activeの段階を経る。

#### REQ-REL-002　公開必須物

**必須度：MUST**  
**検証方法：Inspection**

教材本体、Manifest、README、CHANGELOG、License、Teacher情報、Catalog、テスト記録を揃える。

#### REQ-REL-003　リリースタグ

**必須度：MUST**  
**検証方法：Inspection**

正式公開版へGit Tag等の識別可能な記録を付ける。

#### REQ-REL-004　緊急修正

**必須度：MUST**  
**検証方法：Review**

科学的誤り、安全、Privacy、重大障害を通常機能追加より優先する。

#### REQ-REL-005　ロールバック

**必須度：SHOULD**  
**検証方法：Demonstration**

重大不具合時に直前の安定版へ戻せるようにする。

### ライセンス要求

### 6.27 ライセンス要求

#### REQ-LIC-001　License明示

**必須度：MUST**  
**検証方法：Inspection**

コード、文章、画像、音声、データの利用条件を明示する。

#### REQ-LIC-002　第三者素材

**必須度：MUST**  
**検証方法：Inspection**

第三者素材の出典、License、改変条件を記録する。

#### REQ-LIC-003　利用条件不明素材

**必須度：MUST NOT**  
**検証方法：Review**

利用条件不明の素材を正式教材へ使用しない。

#### REQ-LIC-004　コードと教材内容の分離

**必須度：SHOULD**  
**検証方法：Review**

コードと教材文章・問題データへ異なるLicenseを適用できる構造にする。

#### REQ-LIC-005　学校固有情報

**必須度：MUST**  
**検証方法：Review**

学校名、生徒作品、校章、写真等の公開権限を確認する。

### AI開発要求

### 6.28 AI開発要求

#### REQ-AI-001　AI作業規則

**必須度：MUST**  
**検証方法：Review**

AGENTS.md完成前はCharter、Requirements、承認済みArchitecture/Governanceを作業規則とし、完成後はAGENTS.mdを入口にする。

#### REQ-AI-002　AIによる独断変更禁止

**必須度：MUST NOT**  
**検証方法：Review**

AIは承認なく構造、Schema、Privacy、License、Deprecated、Core APIを変更しない。

#### REQ-AI-003　クロスレビュー

**必須度：MUST**  
**検証方法：Review**

重要変更はChatGPT設計→Claudeレビュー→ChatGPT修正→Claude確認を原則とする。

#### REQ-AI-004　レビュー役割分離

**必須度：MUST**  
**検証方法：Review**

実装AIと第三者レビューAIを分ける。

#### REQ-AI-005　未検証AI出力の公開禁止

**必須度：MUST NOT**  
**検証方法：Review**

AI生成コード、問題、解説、図、説明を独立確認なしで正式公開しない。

#### REQ-AI-006　省略防止

**必須度：MUST**  
**検証方法：Review**

AI修正依頼時に変更範囲、維持機能、更新文書を明示する。

#### REQ-AI-007　AGENTS.md完成条件

**必須度：MUST**  
**検証方法：Inspection**

Platform本格実装開始前にAGENTS.mdをActiveにする。

### 運用要求

### 6.29 運用要求

#### REQ-OPS-001　GitHub一括管理

**必須度：MUST**  
**検証方法：Inspection**

正式教材とPlatform文書を原則GitHubで一括管理する。

#### REQ-OPS-002　GitHub Pages公開

**必須度：MUST**  
**検証方法：Test**

教材をGitHub Pagesで公開可能な静的構成とする。

#### REQ-OPS-003　トップページ分離

**必須度：SHOULD**  
**検証方法：Analysis**

Google Sites等の案内と教材本体を分離し、教材URLから直接利用可能にする。

#### REQ-OPS-004　バックアップ

**必須度：MUST**  
**検証方法：Review**

GitHub以外の媒体へ定期バックアップする。

#### REQ-OPS-005　復旧手順

**必須度：MUST**  
**検証方法：Demonstration**

誤削除、公開障害、重大不具合からの復旧手順を文書化する。

#### REQ-OPS-006　リンク点検

**必須度：MUST**  
**検証方法：Test**

教材URL、Catalog、Portalリンクを定期点検する。

#### REQ-OPS-007　100教材規模

**必須度：MUST**  
**検証方法：Analysis**

Catalog、命名、検索、公開手順を100教材程度まで管理可能にする。

#### REQ-OPS-008　公開領域と管理文書領域の分離

**必須度：MUST**  
**検証方法：Inspection**

Web公開教材とPlatform管理・設計文書を論理的に分離する。

#### REQ-OPS-009　docs名称の用途限定

**必須度：MUST**  
**検証方法：Inspection**

docsをPages公開元に使う場合は設計文書保存先に使わない。

#### REQ-OPS-010　公開構成のADR化

**必須度：MUST**  
**検証方法：Review**

Pages公開元、Branch、対象DirectoryをArchitectureとADRで確定する。

#### REQ-OPS-011　100教材換算による運用評価

**必須度：SHOULD**  
**検証方法：Analysis**

運用手順を100教材へ適用した年間総作業量で評価する。

#### REQ-OPS-012　Organization権限点検

**必須度：MUST**  
**検証方法：Review**

年1回Owner、Deputy、退職者、Pages、Actions、Token、2FA、復旧手段を点検する。

#### REQ-OPS-013　外部サービスの複数管理

**必須度：MUST**  
**検証方法：Inspection**

Domain、DNS、CI、Backup、組織Mail等も可能な限り複数管理者体制にする。

#### REQ-OPS-014　配布成果物の識別

**必須度：MUST**  
**検証方法：Inspection / Test**

成果物からappId、App/Core Version、Distribution Type、Source Commit、Tool Versionを追跡可能にする。

#### REQ-OPS-015　組織化の臨時評価

**必須度：SHOULD**  
**検証方法：Review**

教材数、利用校、開発者、資金、Domain、Owner交代等の条件で組織化を臨時評価する。

#### REQ-OPS-016　10年レビューにおける主体確認

**必須度：MUST**  
**検証方法：Review**

個人運営、組織移管、著作権、Domain、責任者、費用、問い合わせ、再移管を確認する。

## 7. 要求トレーサビリティ

各個別教材仕様、Architecture、Governance、ADR、テスト、チェックリストは、関係する要求IDを明記する。機械可読台帳には、少なくとも `id`、`title`、`priority`、`verification`、`status`、`introducedIn`、`modifiedIn`、`source`、`deprecatedIn`、`replacedBy` を記録する。

過去の来歴を後から都合よく書き換えてはならない。誤りを発見した場合は、訂正内容と根拠をCHANGELOGに記録する。

## 8. 例外運用

MUSTまたはMUST NOT要求に適合できない場合は、REQ-GOV-009およびREQ-GOV-EXC-001に従い、対象要求、理由、影響、代替策、期限、承認者、解消条件を記録する。安全、Privacy、秘密情報に関する例外は原則として承認しない。

## 9. 既存教材による適用検証

最初のPlatform検証では、少なくとも次を使用する。

| 教材 | 主な適用要求 |
|---|---|
| 物質量計算教材 | EDU-CALC、数値精度、有効数字、単位、誤答支援 |
| 酸・アルカリ・中和シミュレーター | EDU-SIM、EDU-VIS、モデル限界、実験との差、安全 |
| 力学・力の向き教材 | EDU-DRAG、EDU-VIS、図の科学的整合性、代替操作 |

加えて、小規模教材を含む5〜10案へLevel分類を適用し、A・B・Cの分布と運用負荷を確認する。

## 10. Review Package

正式レビューには、次を含める。

- 本Requirements統合正本
- Architecture Specification
- Governance Specification
- requirement-index.json
- 要求参照検証レポート
- CHANGELOGまたは修正概要
- Review Package索引

## 11. 関連文書

- Project Charter
- Architecture Specification
- Governance Specification
- Privacy Policy
- Accessibility Policy
- License Policy
- Deprecated Policy
- AGENTS.md
- Developer Guide
- Teacher Guide
- ADR Collection

本書と関連文書が矛盾する場合、対象事項の一次正本と判断の優先順位を確認し、無断でどちらかを上書きせず、Review Package内で解消する。

## 12. Active移行条件

1. 本文とrequirement-index.jsonが完全一致する。
2. 重複ID、欠番、教材形式別要求群の欠落がない。
3. ArchitectureおよびGovernanceの参照ID検査がERROR 0件である。
4. WARNINGの判断と処理が記録されている。
5. Portable、Catalog、Level A承認、Organization所有を小規模検証する。
6. Claudeによる合同レビューを行う。
7. 重大指摘を解消する。
8. Project OwnerがRequirements・Architecture・Governanceを合同承認する。

## 13. CHANGELOG

### Ver.1.2.2 — 2026-08-03

#### Restored

- `REQ-EDU-CALC-001〜004`
- `REQ-EDU-SIM-001〜005`
- `REQ-EDU-DRAG-001〜003`
- `REQ-EDU-EXP-001〜004`
- `REQ-EDU-VIS-001〜004`
- 適用範囲、用語、検証方法、優先順位、関連文書、適用検証、結論相当の章

#### Corrected

- `REQ-DOC-012` の `introducedIn` を1.2.1へ訂正した。
- 可変階層IDを検査対象へ追加した。
- 教材形式別要求群の丸ごとの欠落を検出対象へ追加した。
- `REQ-NFR-001`から基準環境定義 `REQ-CMP-008` への参照を明示した。
- `REQ-GOV-006`と`REQ-GOV-011`の関係を明示した。

#### Provenance note

教材形式別20要求のID群はVer.1.0由来として復元した。Ver.1.2.1統合作業で欠落していたため、内容は既存の教育方針とレビュー記録をもとに再構成した。原文との逐語一致ではなく、意味を保持した規範要求として復元している。

## 14. 結論

You Science Apps Platformは、教材コードだけでなく、教育的安全性、配布、所有権、承認、文書、生成ツール、廃止・移行までを追跡可能な教材資産として管理する。本書を唯一の要求正本とし、実装の便利さより、生徒の安全、科学的正確性、教育効果、長期保守を優先する。
