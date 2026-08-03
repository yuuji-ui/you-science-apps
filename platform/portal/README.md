# You Science Apps Portal Ver.1.0

Catalog Generatorが出力した`catalog.json`を読み込み、教材一覧を表示するPortal初版です。

## 機能

- キーワード検索
- 学年・教科・教材形式の絞り込み
- featured表示
- active／maintenance／deprecated表示
- hidden教材除外
- Keyboard操作
- reduced-motion・Dark mode対応
- 広告・解析・Cookieなし

## ローカル確認

```bash
python -m http.server 8000 --directory site
```

ブラウザで`http://localhost:8000/`を開きます。

## 配置

`site/index.html`と`site/catalog/catalog.json`をGitHub Pages公開対象へ配置します。
