# You Science Apps Platform
# Architecture Migration Plan
# Ver.1.1.1 → Ver.1.1.2 RC

## 文書管理情報

| 項目 | 内容 |
|---|---|
| 文書ID | YSA-ARCH-MIG-001 |
| 状態 | Draft |
| 移行元 | YSA-ARCH-001 Ver.1.1.1 Draft |
| 移行先 | YSA-ARCH-001 Ver.1.1.2 RC |
| 対応Requirements | YSA-REQ-001 Ver.1.2.2 RC |
| 作成日 | 2026-08-03 |
| 作成担当 | ChatGPT |
| 第三者レビュー | Claude（Architecture RC完成後） |

## 1. 目的

Requirements統合作業で発生した情報欠落をArchitectureで繰り返さないため、
Ver.1.1.1の章・判断・ADR候補を棚卸ししてからVer.1.1.2 RCへ移行する。

## 2. 移行原則

1. Ver.1.1.1の設計判断を、理由なく削除しない。
2. Requirements Ver.1.2.2 RCを唯一の要求参照元とする。
3. 要求IDは機械検証し、存在しないIDを本文へ残さない。
4. 教材形式別要求（CALC／SIM／DRAG／EXP／VIS）をArchitectureへ反映する。
5. 生成物と手動編集データの責任を分離する。
6. Hosted／Portable／Standaloneを明確に区別する。
7. 教員が開発環境を操作しなくても利用できる配布経路を維持する。
8. Ver.1.1.1で訂正した文書来歴を保持する。

## 3. 章単位の移行表

| Ver.1.1.1の内容 | Ver.1.1.2での扱い | 主な変更 |
|---|---|---|
| 文書管理情報 | 継承・更新 | Requirements Ver.1.2.2 RCへ固定 |
| 訂正声明 | 継承 | Ver.1.0の参照版誤記を履歴として保持 |
| 基本原則 | 継承 | 教材形式別要求との対応を追加 |
| 7層構造 | 継承 | Distribution／Reference Implementationを明示 |
| リポジトリ構成 | 修正 | review-packages、reference-implementations、catalog-source、distを追加 |
| GitHub Pages公開 | 継承 | sourceと公開成果物の分離を明確化 |
| Platform Core | 継承・修正 | shared／vendored／standaloneを正式化 |
| 教材Level | 継承 | 判定結果をManifestへ記録 |
| Catalog | 継承・修正 | Manifest＋override＋groups→生成Catalog |
| パス設計 | 継承 | YSA_BASE置換とPortable相対パスを分離 |
| Portable | 継承・拡張 | file://制約、成果物識別、検証を追加 |
| Standalone参照実装 | 継承・拡張 | Version履歴をMUSTとして追跡 |
| Validator | 修正 | 可変階層要求IDへ対応 |
| 要求トレーサビリティ | 全面更新 | Requirements Ver.1.2.2 RCの正式IDに統一 |
| 完了条件 | 更新 | 自動参照検証とClaudeレビューを追加 |

## 4. 新設する章

- 教材形式別Architecture
- Distribution Architecture
- Reference Implementation Architecture
- 文書・要求参照Architecture
- Tooling Quality Architecture
- Review Package Architecture
- 運営主体移管を支える技術的可搬性

## 5. 削除しない重要判断

- `site/`と`project-docs/`の分離
- 単一リポジトリ
- 教材独立ディレクトリ
- 過剰共通化の禁止
- Platform Core複数Versionの併存
- Service Workerの標準非採用
- 外部CDN原則禁止
- Catalog生成成果物の直接編集禁止
- GitHub Actionsから検証ロジックを分離
- Project Siteに対応するbasePath解決
- Standalone教材向け参照実装
- Hosted／Portable／Standaloneの分離

## 6. 検証計画

1. Architecture本文から要求IDを抽出する。
2. 範囲表記を個別IDへ展開する。
3. Requirements Ver.1.2.2 RCの`requirement-index.json`と照合する。
4. 存在しないIDをERRORとする。
5. 文書管理情報の参照Versionを確認する。
6. Validator自己テストを実施する。
7. ERROR 0件の状態でClaudeへ提出する。

## 7. Claudeへ渡すタイミング

Architecture Ver.1.1.2 RC完成後に、次の2文書を同時に渡す。

- Requirements Specification Ver.1.2.2 RC
- Architecture Specification Ver.1.1.2 RC

この段階のClaudeレビューは、RequirementsとArchitectureの二文書整合レビューとする。
GovernanceはArchitecture修正後に追加し、最後に三文書合同レビューを行う。


## 8. Ver.1.1.3追加修正

Claude二文書レビューを受け、次を追加した。

1. 2〜3教材基準をMUSTではなく推奨判断基準へ修正
2. Dependency ModeとDistributionの整合表を追加
3. Portable成果物のshared依存を禁止
4. Source依存方式と成果物依存方式を分離
5. dist/の責任、生成主体、Git管理方針を定義
6. MAN-004、CAT-002、CAT-006の明示参照を追加


## 9. Ver.1.1.4同期修正

Claude再確認レビューを受け、次を修正した。

1. 第12章をSource／Distribution Dependency Mode分離モデルへ更新
2. 第27.4章をDependency Mode整合規則の正本として参照
3. 依存方式名`standalone`を`self-contained`へ統一する方針を反映
4. 第6章の構成図へ`dist/hosted/`を追加
5. 自動検証結果とManual Review結果を分離
6. Schema禁則は設計済み・実装未了であることを明記
