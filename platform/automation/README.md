# You Science Apps GitHub Actions Ver.1.0

Manifest検証、Catalog生成、Portal検証、GitHub Pages公開を自動化します。

- `validate-platform.yml`: Pull Requestとmain Pushの検証
- `deploy-pages.yml`: main Push後の検証・Pages公開
- `run-ci.py`: Bootstrap／Production両対応の統合検証

`site/apps/`にManifestがない間は既存Catalogを検証するBootstrap mode、
Manifestが追加された後はCatalogを再生成するProduction modeで動作します。
