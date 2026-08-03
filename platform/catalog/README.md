# You Science Apps Catalog Generator Ver.1.0

`app.manifest.json`を集約し、Portalで利用する`catalog.json`を生成します。

## 構成

- `schemas/catalog.schema.json`
- `schemas/catalog-override.schema.json`
- `schemas/catalog-groups.schema.json`
- `tools/generate-catalog.py`
- `tools/validate-catalog.py`
- `tests/test-catalog-generator.py`
- `examples/`

## 生成ルール

- `active`・`maintenance`・`deprecated`のみ公開候補
- `appId`重複はERROR
- overrideは表示順・featured・非表示・label等のみ変更可能
- Manifest管理情報をoverrideで上書きできない
- unknown appIdのoverrideはERROR
- groupがunknown appIdを参照した場合はERROR
- hidden教材は標準出力から除外
- sortOrder→featured→title→appIdの順で並べる

## 実行

```bash
python tools/generate-catalog.py   --apps-dir examples/apps   --override examples/catalog-source/catalog.override.json   --groups examples/catalog-source/catalog-groups.json   --output examples/expected/catalog.json   --report docs/generation-report.json
```

## 検証

```bash
python tools/validate-catalog.py   schemas/catalog.schema.json   examples/expected/catalog.json
```

## テスト

```bash
python tests/test-catalog-generator.py
```
