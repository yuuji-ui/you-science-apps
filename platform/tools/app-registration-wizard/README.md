# 教材追加ウィザード Ver.1.0

ブラウザ上で教材情報を入力し、以下を生成します。

- 推奨フォルダパス
- app.manifest.json
- catalog.override.jsonへ追加する項目
- catalog-groups.jsonへ追加する項目

GitHubへ自動送信しません。生成内容を確認して手動で反映します。

学習難易度の公開表示:
- 1〜2: 基本
- 3〜4: 標準
- 5: 応用

Level A/B/Cは内部管理情報であり、Portalには表示しません。


## 外部通信

- `network.required`は外部API・外部データ読込の必要性を示します。
- 外部通信を使う場合、通信先URLを1件以上入力します。
- `privacy.externalTransmission`は常に`false`です。
- 個人情報、学習結果、行動履歴の外部送信は、この標準ウィザードでは生成できません。
- そのような教材は、別途Privacy・Governanceレビューが必要です。
