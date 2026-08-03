# Claudeレビュー依頼：Requirements／Architecture二文書整合レビュー

You Science Apps Platformの設計文書を第三者視点でレビューしてください。

## 添付資料

### Requirements Package
- Requirements Specification Ver.1.2.2 RC
- requirement-index.json
- Requirements validation report

### Architecture Package
- Architecture Migration Plan
- Architecture Specification Ver.1.1.2 RC
- Architecture validation report

## 今回のレビュー範囲

Governanceはまだ最終整合前です。
今回はRequirementsとArchitectureの二文書だけを対象にしてください。

## 確認項目

1. Requirements Ver.1.2.2 RCの要求がArchitectureへ適切に反映されているか
2. ArchitectureがRequirementsにない方針を無断でMUST化していないか
3. 教材形式別要求
   - CALC
   - SIM
   - DRAG
   - EXP
   - VIS
   が技術構造へ正しく反映されているか
4. Hosted／Portable／Standaloneの責任分界に矛盾がないか
5. Platform Core、Standalone、Vendored方式の併存が30年保守に現実的か
6. Catalog、Manifest、Schemaの正本関係が明確か
7. `site/`、`project-docs/`、`catalog-source/`、`dist/`の構成が妥当か
8. 可変階層要求IDの検証方法に抜けがないか
9. 100教材規模で過剰な運用負荷にならないか
10. Governance作成前にArchitecture側で修正すべき点
11. Ver.1.1.2 RCを採用可能か
    - 採用
    - 一部修正
    - 大幅修正
    のいずれかで判定

## 出力形式

1. 総合評価（100点）
2. 長所
3. 短所
4. 重大な問題点
5. 改善提案
6. Requirementsとの整合性
7. 将来性
8. 保守性
9. 教育効果への影響
10. 採用判断と理由

要求IDに関する指摘は、該当する実際のIDを示してください。
不明な場合は推測せず「検証不能」と明記してください。
