# ADR-0011 教材Level客観判定

## 文書管理情報

| 項目 | 内容 |
|---|---|
| ADR ID | ADR-0011 |
| 状態 | Accepted for RC |
| 決定日 | 2026-08-03 |
| 対応Architecture | YSA-ARCH-001 Ver.1.1.5 RC |
| 対応Requirements | REQ-GOV-019、REQ-GOV-020 |

## 1. 背景

教材Level A／B／Cは、文書量、Review、Test、承認Gateを比例適用するための開発・保守・公開Risk分類であり、教育的重要度の優劣ではない。

## 2. 判定方法

各指標を0〜2点で採点する。

| No. | 指標 | 0点 | 1点 | 2点 |
|---:|---|---|---|---|
| 1 | 主要画面数 | 1画面 | 2〜3画面 | 4画面以上 |
| 2 | 状態管理 | ほぼなし | 複数状態 | 複雑な遷移・履歴 |
| 3 | 教材データ量 | 少量 | 分離Data 1種 | 複数Data・大量問題 |
| 4 | 科学計算・判定 | 単純 | 複数式・許容誤差 | 複雑Model・連続計算 |
| 5 | 可視化 | 静的 | 単純Canvas/SVG | 動的・複数View |
| 6 | 操作方式 | Button/Input中心 | Drag等1種 | 複数高度操作 |
| 7 | Platform Core依存 | なし | shared/vendored | Core変更・新API |
| 8 | 配布形態 | 1形態 | 2形態 | 3形態 |
| 9 | 保存・通信 | なし | 端末内保存 | 外部通信・同期候補 |
| 10 | 外部Library | なし | 交換可能な1個 | 複数・高依存 |
| 11 | 教員編集機能 | なし | Data編集 | 画面Editor・Import/Export |
| 12 | 公開・運用Risk | 低い | 標準 | 高い・多数利用・主要授業 |

## 3. 閾値

- 0〜8点：Level A
- 9〜16点：Level B
- 17〜24点：Level C
- 境界で迷う場合は高いLevelを選ぶ。

## 4. 強制Level C条件

- Platform Core公開APIの新設・破壊的変更
- 個人情報、Login、外部送信を扱う提案
- Ranking、Class共有、外部Database等を扱う提案
- 教員向け画面Editorが教材Dataを生成・変更
- 複数教材へ影響するSchema変更
- 安全性に関わる実験手順・危険操作が主要機能
- 大規模外部Library・3D Engineへの強い依存
- Portal、Catalog Generator、Builder、Validator自体の変更

Privacy・安全方針に反する提案はLevel Cにすれば許可されるものではない。

## 5. 記録

各指標点、合計、強制条件、最終Level、判定日、判定者、再判定理由を記録する。

## 6. 再判定

保存・通信、外部Library、Distribution、Core、Schema、Editor、画面・状態・Data量が変化した場合に再判定する。

## 7. 正本

このADRを教材Level判定の正本とし、Architecture本文は概要と参照のみを持つ。
