# CI同期完成版 Ver.1.2：GitHub反映手順

## 方針

今回はファイルの中身をGitHub上で手作業編集しません。
完成版のファイルを、同じ場所へアップロードして置き換えます。

## 作業回数

原則として次の4回です。

1. `.github`を置き換える
2. `platform`を置き換える
3. `site`と`catalog-source`を置き換える
4. リポジトリ直下の4ファイルを置き換える

---

## Step 1　ZIPを展開

`you_science_apps_ci_sync_v1_2.zip`を右クリックし、
「すべて展開」を選びます。

フォルダ構成は変更しません。

---

## Step 2　重複Schemaを削除

GitHubで次の2ファイルが存在する場合だけ削除します。

```text
platform/pipeline/tools/app-manifest.schema.json
platform/pipeline/tools/catalog.schema.json
```

削除用Commit:

```text
Remove obsolete pipeline schema copies
```

存在しなければ何もしません。

---

## Step 3　.githubを置き換える

GitHubリポジトリのトップで`.github`を開き、
`workflows`を開きます。

完成版の次の2ファイルをアップロードします。

```text
.github/workflows/deploy-pages.yml
.github/workflows/validate-platform.yml
```

同名ファイルは置き換えられます。

Commit:

```text
Synchronize GitHub Actions Ver.1.2
```

---

## Step 4　platformをまとめて置き換える

GitHubリポジトリのトップで`platform`を開きます。

完成版の`platform`フォルダ内にある次のフォルダを、
対応する同名フォルダへアップロードします。

```text
platform/manifest/
platform/catalog/
platform/portal/
platform/pipeline/
platform/automation/
platform/tools/
```

重要:

- ファイルの中身をコピーして編集しません。
- 完成版のファイルを同じパスへUploadします。
- 同名ファイルは更新、新しいファイルは追加になります。

Commit:

```text
Replace synchronized platform CI files Ver.1.2
```

---

## Step 5　siteとcatalog-sourceを置き換える

リポジトリトップから次を同じ場所へアップロードします。

```text
site/
catalog-source/
```

既存の教材HTMLは完成版ZIPには含めていないため、
電流マスターや中和シミュレーターのHTMLは削除されません。

置き換える主なもの:

- `site/index.html`
- `site/catalog/catalog.json`
- 既存2教材の`app.manifest.json`
- `catalog-source`の2ファイル

Commit:

```text
Update Portal catalog and app manifests Ver.1.2
```

---

## Step 6　トップ階層の4ファイルを置き換える

GitHubリポジトリの最初の画面へ戻ります。

完成版の次をアップロードします。

```text
requirements.txt
run-tests.py
README.md
CHANGELOG.md
```

Commit:

```text
Update root validation files Ver.1.2
```

`GITHUB-REPLACEMENT-STEPS.md`などの作業用資料は、GitHubへ入れなくても構いません。

---

## Step 7　Actionsを確認

最後のアップロード後にGitHub上部の`Actions`を開きます。

最新の次の2種類を確認します。

```text
Validate Platform
Validate and Deploy Pages
```

両方が緑になることを確認します。

Pages側では次が緑になります。

```text
build
deploy
```

---

## Step 8　失敗した場合

今回は、個別ファイルをその場で修正しません。

赤いWorkflowを開き、
`Validate platform and generate catalog`の最後のエラー部分を送ってください。

完成版との差分を特定し、次も置換用ファイルとして返します。
