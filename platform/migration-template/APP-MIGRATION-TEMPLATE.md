教材Platform移植テンプレート Ver.1.0
元教材確認
[ ] index.html単体で起動
[ ] 外部CDN
[ ] fetch／API
[ ] localStorage／IndexedDB
[ ] 個人情報入力
[ ] Analytics・広告・Cookie
[ ] 教育上維持すべき機能
標準配置
```text
site/apps/<school-stage>/<field>/<app-id>/
├─ index.html
└─ app.manifest.json
```
Catalog
Manifestには教材情報、catalog.override.jsonにはPortal表示情報だけを書く。
検証
[ ] Manifest Schema PASS
[ ] Catalog生成 PASS
[ ] Catalog Schema PASS
[ ] GitHub Actions PASS
[ ] Portal表示
[ ] 教材起動
[ ] Chromebook/iPad
[ ] Privacy宣言と実装が一致

Portalへの戻り導線（必須）
すべてのHosted教材には、画面上部の分かりやすい位置に
「← 教材一覧へ戻る」リンクを設置する。
最低要件
[ ] 文言だけで戻り先が分かる
[ ] タップ領域は高さ48px以上
[ ] Keyboardで選択・実行できる
[ ] 色だけでLinkを区別しない
[ ] 学習操作を隠さない位置に置く
[ ] GitHub Pagesの階層に合う相対Pathを使う
[ ] Portable版では、戻り先が存在しない場合の扱いを別途定義する
標準HTML
```html
<div class="portal-return-bar">
  <a class="portal-return-link"
     href="../../../../"
     aria-label="You Science Appsの教材一覧へ戻る">
    ← 教材一覧へ戻る
  </a>
</div>
```
相対Pathは教材の配置階層に応じて調整する。
