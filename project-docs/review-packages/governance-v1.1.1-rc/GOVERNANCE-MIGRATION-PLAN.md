# You Science Apps Platform
# Governance Migration Plan
# Ver.1.1 → Ver.1.1.1 RC

## 文書管理情報

| 項目 | 内容 |
|---|---|
| 文書ID | YSA-GOV-MIG-001 |
| 状態 | Draft |
| 移行元 | YSA-GOV-001 Ver.1.1 Draft |
| 移行先 | YSA-GOV-001 Ver.1.1.1 RC |
| 対応Requirements | YSA-REQ-001 Ver.1.2.2 RC |
| 対応Architecture | YSA-ARCH-001 Ver.1.1.4 RC |
| 作成日 | 2026-08-03 |
| 作成担当 | ChatGPT |
| 第三者レビュー | Claude（三文書合同レビュー前） |

## 1. 目的

Requirements Ver.1.2.2 RCおよびArchitecture Ver.1.1.4 RCに合わせて、
Governanceの役割、承認、例外、公開、引き継ぎ、組織所有、文書合同承認を整合させる。

## 2. 主な移行内容

1. Requirementsの正式IDへ全面統一
2. GitHub Organization所有と複数OwnerをMUST運用へ反映
3. Level A自己承認防止を明確化
4. Catalog override編集権限をPortal Maintainerへ限定
5. Review Packageによる三文書合同承認を制度化
6. 自動検証とManual Reviewの役割を分離
7. Portable／Hosted／Standalone成果物の承認責任を追加
8. Tooling変更、Schema変更、Distribution変更の承認境界を明確化
9. Project Owner不在時の制限とDeputy Ownerの代理権限を整理
10. 組織移管、著作権、Domain、Repositoryの引き継ぎを制度化

## 3. 削除しない重要判断

- 生徒安全を最優先とする優先順位
- Privacy例外は原則承認不可
- AI生成物の独立Review
- 例外の期限管理
- Incident時の公開停止とRollback
- Deprecated→Retired→Archivedの段階移行
- 年次・3年・10年レビュー
- Project OwnerとDeputy Owner
- Catalogの利益相反防止
- 文書版の遡及的書き換え禁止

## 4. 検証計画

- Governance本文のRequirements参照を機械照合
- Requirements Version表記を確認
- Architecture Version表記を確認
- 必須役割、承認Gate、例外期限、Organization所有、自己承認防止の存在を自動確認
- 意味的整合はManual Reviewとして分離
