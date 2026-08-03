# You Science Apps Manifest Ver.1.0

教材ごとの情報を、Catalog生成・公開判定・配布生成・保守に利用するための
`app.manifest.json` Schemaと検証ツールです。

## 収録内容

- `schemas/app-manifest.schema.json`
- `examples/valid/app.manifest.json`
- `examples/invalid/`
- `tools/validate-manifest.py`
- `tests/test-manifest-schema.py`

## 必要環境

- Python 3.10以上
- `jsonschema`

インストール：

```bash
python -m pip install jsonschema
```

## 単体検証

```bash
python tools/validate-manifest.py   schemas/app-manifest.schema.json   examples/valid/app.manifest.json
```

## 回帰テスト

```bash
python tests/test-manifest-schema.py
```

## Ver.1.0で保証する主な規則

- appIdは小文字英数字とハイフン
- VersionはSemantic Versioning形式
- 個人情報、解析、Cookie、外部送信はfalse固定
- Portable成果物の`shared`依存を禁止
- Standalone packageの`shared`依存を禁止
- Source Dependency ModeとDistribution Dependency Modeを分離
- 保存・通信が無効な場合は詳細配列を空にする
- 教育対象・単元・教材形式・学習目標を必須化

## 未確定

- Licenseの正式な値
- Curriculum unitId一覧
- Level採点結果のManifest内詳細形式
- Catalog Schemaとの接続
