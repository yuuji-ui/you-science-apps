# You Science Apps Integration Pipeline Ver.1.0

ManifestからPortal用Catalogを生成する統合パイプラインです。

## 処理順

1. すべての`app.manifest.json`を検証
2. Catalog Generatorを実行
3. 生成した`catalog.json`をSchema検証
4. ReportをJSONで保存

## 実行例

```bash
python tools/run-platform-pipeline.py   --apps-dir examples/apps   --manifest-schema tools/app-manifest.schema.json   --catalog-generator tools/generate-catalog.py   --catalog-validator tools/validate-catalog.py   --catalog-schema tools/catalog.schema.json   --override examples/catalog-source/catalog.override.json   --groups examples/catalog-source/catalog-groups.json   --output site/catalog/catalog.json   --report reports/pipeline-report.json
```

## テスト

```bash
python tests/test-platform-pipeline.py
```

## 公開停止条件

- Manifestが1件でも不正
- Catalog生成失敗
- 生成CatalogがSchema不適合

いずれかで終了コード1を返します。

## Manifest Schema補足

`links.hostedUrl`は絶対URLに加え、GitHub Pages用の`./`・`../`・`/`で始まる相対URLを許可します。
