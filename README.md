# You Science Apps 共通機能 Ver.1.1.1

## 実装済み

- 検索拡張
- 大分類・対象・単元・形式・難易度Filter
- お気に入り
- 最近使った教材（最大3件）
- 端末内データ一括消去
- 学習難易度（基本・標準・応用）
- LevelのPortal非表示
- 高校の科目分類
- 教材追加ウィザード
- Manifest Schema・Catalog Schema・Generator更新
- 既存2教材のManifest更新

## GitHub反映前

Claudeによる第三者レビューで採用・GitHub反映可と判定済みです。
レビューで必須修正がなければ、完成版として一括反映します。


## Claude初回レビュー後の修正

- 外部通信と`privacy.externalTransmission`を分離
- 外部通信先URL入力を追加
- ウィザード生成ManifestをNode.jsで実行しSchema検証
- `requirements.txt`を追加
- Catalog GeneratorとSchemaの単一正本化
- 公開CatalogからLevelを削除
- 共有端末で次の利用者に保存内容が見える可能性を明示
- `categories`と`units`の役割を文書化

## ローカル検証

```text
python -m pip install -r requirements.txt
python run-tests.py
```

ウィザード検証にはNode.jsが必要です。
