# You Science Apps CI同期完成版 Ver.1.2

## 同期対象

- Manifest Schema・Validator・正常例・異常例
- Catalog Schema・Generator・Validator・サンプル教材
- Pipeline・サンプル教材・統合テスト
- Portal・教材追加ウィザード・既存2教材Manifest
- Automation CI Runner
- GitHub Actions 2本
- requirements.txt

## 検証結果

- `python run-tests.py`: PASS
- `python platform/automation/tools/run-ci.py --repo .`: PASS
- CI mode: production
- CI steps: 11
- Node.js Wizard test: PASS
- Catalog generation: PASS
- 公開CatalogからLevel除外: PASS

## 運用変更

今後は部分修正を避け、完成版ファイルの置き換えを原則とします。
