# GitHub Upload Steps

1. `You_Science_Apps_Platform_Ver_1_3_1_Release.zip`を展開する。
2. GitHubで`you-science-apps`リポジトリのトップを開く。
3. `Add file` → `Upload files`を選ぶ。
4. 展開したReleaseフォルダの**中身すべて**を選び、アップロード画面へドラッグする。
5. パス先頭に`You_Science_Apps_Platform_Ver_1_3_1_Release/`が付いていないことを確認する。
6. Commit messageへ次を入力する。

```text
Release You Science Apps Platform Ver.1.3.1
```

7. `Commit directly to the main branch`を選び、`Commit changes`を押す。
8. `Actions`で次を確認する。
   - Validate Platform
   - Validate and Deploy Pages
9. `build`と`deploy`が緑になったら、Portalを確認する。
