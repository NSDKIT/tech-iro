# Obsidian Task Manager

ObsidianのMarkdownをそのままタスクデータとして使う、軽量な個人向けタスク管理ツールです。**受信箱、今日、今週、プロジェクト、完了履歴**をひとつのVault内で管理できます。

> タスクは通常のMarkdownチェックボックスとして保存されます。独自クラウドや専用データベースは使用しません。

## 機能

| 機能 | 内容 | 必要なもの |
| --- | --- | --- |
| 受信箱 | 思いついたタスクを一時保管する | Tasks |
| 今日 | 期限切れ、今日が期限、今日開始を表示する | Tasks |
| 今週 | 7日以内の期限と期限未設定を表示する | Tasks |
| プロジェクト | 成果単位でタスクとメモを管理する | Tasks |
| プロジェクト一覧 | プロパティから一覧表を生成する | Dataview、任意 |
| 完了履歴 | 今日、直近7日、今月の完了を表示する | Tasks |
| テンプレート | プロジェクト、デイリーノート、簡易入力 | Obsidian標準Templates |
| 見た目の調整 | ダッシュボード用CSS | Obsidian標準CSSスニペット |

## 必要環境

Obsidianと、コミュニティプラグインの[Tasks](https://github.com/obsidian-tasks-group/obsidian-tasks)を使用します。プロジェクト一覧表を自動生成する場合だけ、[Dataview](https://github.com/blacksmithgu/obsidian-dataview)も使用します。

TasksのクエリはVault内のタスクを集約し、表示されたタスクをクエリ結果から操作できます。Obsidian標準のTemplatesは、事前定義した内容や日付変数をノートへ挿入できます。[1] [2]

## すぐ試す

`vault-template`を新しいVaultとしてObsidianで開きます。その後、次の設定を行います。

1. **設定 → コミュニティプラグイン**からTasksをインストールし、有効化します。
2. プロジェクト一覧表を使う場合はDataviewもインストールし、有効化します。
3. **設定 → コアプラグイン**でTemplatesを有効化します。
4. Templatesのフォルダを`Task Manager/99 Templates`に設定します。
5. **設定 → 外観 → CSSスニペット**で`task-manager`を有効化します。
6. `Task Manager/00 Home.md`を開きます。

## 既存Vaultへ導入する

macOSまたはLinuxでは、次のコマンドを実行します。

```bash
chmod +x install.sh
./install.sh "/path/to/your-vault"
```

インストーラーは`Task Manager`フォルダとCSSスニペットをコピーします。既存の`.obsidian`設定ファイルは変更しません。すでに`Task Manager`フォルダがある場合は停止します。

内容を確認したうえで更新する場合は、`--force`を指定します。既存フォルダは日時付きバックアップ名へ変更されます。

```bash
./install.sh "/path/to/your-vault" --force
```

Windowsでは、`vault-template/Task Manager`をVault直下へコピーし、`vault-template/.obsidian/snippets/task-manager.css`をVault内の`.obsidian/snippets`へコピーします。

## 日々の使い方

### タスクを収集する

`Task Manager/01 Inbox/Inbox.md`へ、次のように追加します。

```markdown
- [ ] 顧客へ確認事項を送る
```

### タスクを整理する

Tasksのコマンド**Create or edit task**を使い、期限、開始日、優先度、繰り返しを設定します。

```markdown
- [ ] 顧客へ確認事項を送る 📅 2026-07-17 🔼 #task/work
```

### 今日やることを確認する

`Task Manager/02 Views/Today.md`を開きます。期限切れ、今日が期限、今日開始の順に確認し、完了したら表示上のチェックボックスを選択します。

### プロジェクトを作る

1. `Task Manager/03 Projects`に新しいノートを作成します。
2. Templatesの**Insert template**コマンドで`Project`を挿入します。
3. 完了条件と次のアクションを記入します。
4. 完了後は`status: done`へ変更し、`90 Archive`へ移します。

## タスク記法

| 項目 | 記法例 | 用途 |
| --- | --- | --- |
| 期限 | `📅 2026-07-17` | 完了すべき日 |
| 開始日 | `🛫 2026-07-15` | 着手候補日 |
| 高優先度 | `⏫` | 最優先 |
| 中優先度 | `🔼` | 通常より優先 |
| 低優先度 | `🔽` | 後回し可能 |
| 繰り返し | `🔁 every Friday` | 定期タスク |
| タグ | `#task/work` | 分類と検索 |

## フォルダ構成

```text
vault-template/
├── .obsidian/
│   └── snippets/task-manager.css
└── Task Manager/
    ├── 00 Home.md
    ├── 01 Inbox/
    ├── 02 Views/
    ├── 03 Projects/
    ├── 90 Archive/
    └── 99 Templates/
```

## カスタマイズ

画面の抽出条件は、各Markdownファイルの`tasks`コードブロックを変更して調整します。仕事だけを表示する場合は、クエリへ`tags include #task/work`を追加できます。特定フォルダを除外する場合は、`path does not include フォルダ名`を追加します。

Dataviewを使用しない場合、`Projects.md`のDataviewコードブロックだけ表示されません。Tasksを使うプロジェクト別タスク一覧はそのまま利用できます。

## ファイル一覧

| ファイル | 役割 |
| --- | --- |
| `generate_package.py` | Vaultテンプレートを再生成する |
| `install.sh` | 既存Vaultへ安全にコピーする |
| `verify_package.py` | 構造、リンク、クエリを検証する |
| `DESIGN.md` | 情報設計と操作フローを説明する |
| `vault-template/` | そのまま試せるVault内容 |

## References

[1]: https://publish.obsidian.md/tasks/Queries/Examples "Tasks User Guide — Query Examples"
[2]: https://obsidian.md/help/plugins/templates "Obsidian Help — Templates"
