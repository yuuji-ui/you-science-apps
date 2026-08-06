# You Science Apps 共通機能 Ver.1.1.1 GitHub反映手順

## 反映後に追加される主な機能

- キーワード検索
- 大分類・対象・単元・教材形式・学習難易度による絞り込み
- お気に入り
- 最近使った教材（最大3件）
- 端末内履歴の一括消去
- 学習難易度「基本・標準・応用」
- Level A/B/CのPortal非表示
- 教材追加ウィザード
- Manifest・Catalog Schema更新
- Catalog Generator更新

---

# 作業の全体像

1. ZIPを展開
2. 不要になったSchema複製を2ファイル削除
3. 完成版ファイルをGitHubへアップロード
4. GitHub Actionsを確認
5. Portalと教材追加ウィザードを確認

---

# Step 1 ZIPを展開する

`you_science_apps_common_features_v1_1_1_FINAL.zip`を右クリックし、
「すべて展開」を選びます。

展開後のフォルダ構成を変えないでください。

---

# Step 2 GitHub上の不要ファイルを削除する

次のファイルが存在する場合だけ削除します。

```text
platform/pipeline/tools/app-manifest.schema.json
platform/pipeline/tools/catalog.schema.json
```

## 削除方法

1. GitHubで対象ファイルを開く
2. 右上の三点メニューまたはゴミ箱アイコンを押す
3. `Delete file`を選ぶ
4. Commit messageへ次を入力する

```text
Remove duplicate pipeline schemas
```

5. `Commit changes`を押す

2ファイルとも同じ操作をします。

`platform/pipeline/tools/generate-catalog.py`は削除しません。

---

# Step 3 完成版ファイルをアップロードする

最も確実なのは、GitHub DesktopまたはローカルGitを使う方法です。
ブラウザだけで行う場合は、フォルダごとではなく、対応する場所ごとにアップロードします。

## 3-1 リポジトリのトップへ移動

GitHubで`you-science-apps`リポジトリのトップを開きます。

## 3-2 既存フォルダへファイルをアップロード

展開した完成版フォルダの中身を、同じパスへ配置します。

重要な置換先:

```text
site/index.html
site/catalog/catalog.json

site/apps/junior-high/physics/electric-current-master/app.manifest.json
site/apps/junior-high/chemistry/neutralization-simulator/app.manifest.json

catalog-source/catalog.override.json
catalog-source/catalog-groups.json

platform/manifest/schemas/app-manifest.schema.json
platform/catalog/schemas/catalog.schema.json
platform/catalog/tools/generate-catalog.py
platform/pipeline/tools/generate-catalog.py
platform/portal/tests/test-portal.py
```

新規追加先:

```text
platform/tools/app-registration-wizard/
requirements.txt
run-tests.py
project-docs/implementation/COMMON-FEATURES-SPEC-v1.1.1.md
```

テストファイルも完成版に含まれているため、同じパスへ配置します。

## ブラウザでの操作

1. アップロード先のフォルダをGitHubで開く
2. `Add file`
3. `Upload files`
4. パソコン側の同じフォルダにあるファイルをドラッグ
5. Commit messageへ次を入力

```text
Release common features Ver.1.1.1
```

6. `Commit changes`を押す

同名ファイルは置き換えとして更新されます。

---

# Step 4 GitHub Actionsを確認する

1. リポジトリ上部の`Actions`を開く
2. 最新の`Validate and Deploy Pages`を開く
3. 次の両方が緑になることを確認

```text
build
deploy
```

赤くなった場合は、赤いStepを開き、ログ末尾を確認します。

---

# Step 5 Portalを確認する

次を開きます。

```text
https://yuuji-ui.github.io/you-science-apps/
```

確認項目:

- Level A/B/Cが表示されない
- 電流マスターは「難易度：標準」
- 中和シミュレーターは「難易度：標準」
- キーワード検索が動く
- 大分類・対象・単元・形式・難易度で絞り込める
- お気に入りボタンが動く
- 教材を開いた後、最近使った教材へ最大3件表示される
- 「端末内の履歴を消去」が動く
- 共有端末に関する注意が表示される
- PC・Chromebook横向きで3列
- iPad縦向き・小画面で2列

---

# Step 6 教材追加ウィザードを確認する

GitHub Pagesで直接公開される場所へ置いていないため、
まずGitHub上のファイル確認またはローカルで使用します。

配置場所:

```text
platform/tools/app-registration-wizard/index.html
```

ローカル確認:

1. リポジトリをパソコンへダウンロード
2. 上記`index.html`を開く
3. 教材情報を入力
4. `JSONを生成`を押す
5. Manifest・Catalog追記用JSONが表示されることを確認

外部通信をONにした場合は、通信先URLの入力が必須です。
個人情報や学習記録の外部送信は常に無効です。

---

# Step 7 任意のローカル検証

PythonとNode.jsが使えるパソコンでは、リポジトリのトップで次を実行します。

```text
python -m pip install -r requirements.txt
python run-tests.py
```

すべてPASSすれば完了です。
