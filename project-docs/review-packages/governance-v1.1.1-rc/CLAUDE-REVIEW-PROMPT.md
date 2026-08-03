# Claudeレビュー依頼：Requirements／Architecture／Governance 三文書合同レビュー

You Science Apps Platform Ver.1.0の設計文書一式を第三者視点でレビューしてください。

## 添付資料

### Requirements
- Requirements Specification Ver.1.2.2 RC
- requirement-index.json
- Requirements validation files

### Architecture
- Architecture Specification Ver.1.1.4 RC
- Architecture validation files

### Governance
- Governance Specification Ver.1.1.1 RC
- Governance validation files

## 確認項目

1. 三文書間の役割分担が明確か
2. Requirementsの要求がArchitectureとGovernanceへ十分反映されているか
3. ArchitectureがGovernance上の権限を独断で定義していないか
4. GovernanceがArchitecture上の技術構造と矛盾していないか
5. Owner／Deputy／App Owner／Portal Maintainer／Reviewerの権限が妥当か
6. Level A自己承認防止が現実的か
7. Catalog override編集権限と利益相反防止が十分か
8. Hosted／Portable／StandaloneおよびDependency Modeの承認責任が明確か
9. Automated ValidationとManual Reviewの区別が一貫しているか
10. 例外、Incident、Deprecated、引き継ぎが30年運用に耐えるか
11. 100教材規模で過剰な運用負荷にならないか
12. Requirements／Architecture／GovernanceをActive化可能か

## 出力形式

1. 総合評価（100点）
2. 長所
3. 短所
4. 重大な問題点
5. 改善提案
6. 三文書整合性
7. 将来性
8. 保守性
9. 教育効果
10. Active化判断
11. 次工程へ進めるか

機械検証可能な主張は、可能な範囲で実際に再実行してください。
推測と確認済み事実を区別してください。
