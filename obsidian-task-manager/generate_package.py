from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "vault-template"

FILES = {
    "Task Manager/00 Home.md": '''---
cssclasses:
  - task-manager-dashboard
tags:
  - task-manager/home
---

# Task Manager

> 今日やることを決め、終わったらチェックするためのホーム画面です。

## ナビゲーション

| 確認する内容 | 開く画面 |
| --- | --- |
| 思いついたことを記録する | [[Task Manager/01 Inbox/Inbox|受信箱]] |
| 今日やることを決める | [[Task Manager/02 Views/Today|今日]] |
| 1週間の予定を確認する | [[Task Manager/02 Views/This Week|今週]] |
| 最近終えたことを振り返る | [[Task Manager/02 Views/Completed|完了履歴]] |
| プロジェクトを進める | [[Task Manager/03 Projects/Projects|プロジェクト一覧]] |

## 期限切れ

```tasks
not done
due before today
sort by due
sort by priority
limit 12
short mode
```

## 今日が期限

```tasks
not done
due today
sort by priority
sort by path
short mode
```

## すばやく記録

新しいタスクは、まず[[Task Manager/01 Inbox/Inbox|受信箱]]へ次の形式で追加します。

```markdown
- [ ] 次に行う具体的な行動
```

期限が決まっている場合は、Tasksの「Create or edit task」コマンドを使うと、日付や優先度を選択できます。
''',
    "Task Manager/01 Inbox/Inbox.md": '''---
cssclasses:
  - task-manager-view
tags:
  - task-manager/inbox
---

# 受信箱

> 思いついたことを一度ここへ集めます。整理時に期限、優先度、プロジェクトを付けます。

## 未整理タスク

- [ ] サンプル：最初のタスクをTasksコマンドで編集する #task/inbox
- [ ] サンプル：不要ならこのタスクを削除する #task/inbox

## 受信箱に残っているタスク

```tasks
not done
path includes Task Manager/01 Inbox
sort by priority
sort by description
short mode
```

## 整理の判断

| 状態 | 行うこと |
| --- | --- |
| 不要 | 削除する |
| すぐ終わる | その場で完了する |
| 日付が決まっている | 期限または開始日を設定する |
| 複数の行動が必要 | `03 Projects`にプロジェクトノートを作る |
| いつか行いたい | 期限を付けず、適切なプロジェクトへ移す |
''',
    "Task Manager/02 Views/Today.md": '''---
cssclasses:
  - task-manager-view
tags:
  - task-manager/today
---

# 今日

[[Task Manager/00 Home|ホームへ戻る]]

## 期限切れ

```tasks
not done
due before today
sort by due
sort by priority
short mode
```

## 今日が期限

```tasks
not done
due today
sort by priority
sort by path
short mode
```

## 今日の予定

```tasks
not done
scheduled today
sort by priority
sort by path
short mode
```

## 今日完了したタスク

```tasks
done today
sort by done reverse
short mode
```
''',
    "Task Manager/02 Views/This Week.md": '''---
cssclasses:
  - task-manager-view
tags:
  - task-manager/week
---

# 今週

[[Task Manager/00 Home|ホームへ戻る]]

## 7日以内の期限

```tasks
not done
due after today
due before in one week
sort by due
sort by priority
group by due
short mode
```

## 期限未設定

期限を付ける必要があるタスクだけを確認し、不要な日付は無理に設定しません。

```tasks
not done
no due date
path does not include Task Manager/99 Templates
sort by priority
sort by path
limit 30
short mode
```

## 週次レビュー

- [ ] 受信箱を空にする #task/review
- [ ] 期限切れタスクを再判断する #task/review
- [ ] 各プロジェクトに次の行動があるか確認する #task/review
- [ ] 完了履歴を振り返る #task/review
''',
    "Task Manager/02 Views/Completed.md": '''---
cssclasses:
  - task-manager-view
tags:
  - task-manager/completed
---

# 完了履歴

[[Task Manager/00 Home|ホームへ戻る]]

## 直近7日間

```tasks
done after 7 days ago
sort by done reverse
group by done
short mode
```

## 今月

```tasks
done this month
sort by done reverse
group by done
short mode
```
''',
    "Task Manager/03 Projects/Projects.md": '''---
cssclasses:
  - task-manager-view
tags:
  - task-manager/projects
---

# プロジェクト一覧

[[Task Manager/00 Home|ホームへ戻る]]

## プロジェクトノート

```dataview
TABLE WITHOUT ID file.link AS "プロジェクト", status AS "状態", target_date AS "目標日"
FROM "Task Manager/03 Projects"
WHERE type = "project" AND file.name != "Projects"
SORT target_date ASC
```

> 上の一覧表示にはDataviewが必要です。Dataviewを使わない場合も、下のリンクから各ノートを開けます。

- [[Task Manager/03 Projects/Sample Project|サンプルプロジェクト]]

## プロジェクト内の未完了タスク

```tasks
not done
path includes Task Manager/03 Projects
path does not include Projects.md
sort by priority
sort by due
group by filename
short mode
```
''',
    "Task Manager/03 Projects/Sample Project.md": '''---
type: project
status: active
target_date: 2026-08-31
cssclasses:
  - task-manager-project
tags:
  - task-manager/project
---

# サンプルプロジェクト

> **完了条件:** タスク管理環境を自分の運用に合わせて設定し、1週間利用する。

## 次のアクション

- [ ] Tasksプラグインをインストールする 🔼 #task/setup
- [ ] コアプラグインのTemplatesを有効化する #task/setup
- [ ] `99 Templates`をテンプレートフォルダに指定する #task/setup
- [ ] ホーム画面をブックマークする #task/setup

## 待機中

- [ ] サンプル：確認結果を待つ #task/waiting

## メモ

プロジェクトは、複数の行動を完了して初めて達成できる成果を管理する単位です。完了したら`status`を`done`へ変更し、ノートを`90 Archive`へ移動します。
''',
    "Task Manager/90 Archive/README.md": '''# アーカイブ

完了したプロジェクトや、参照頻度が下がったノートを保存する場所です。タスクを残したまま移動すると各ビューへ表示されるため、移動前に未完了タスクを確認します。
''',
    "Task Manager/99 Templates/Project.md": '''---
type: project
status: active
target_date:
cssclasses:
  - task-manager-project
tags:
  - task-manager/project
created: "{{date:YYYY-MM-DD}}"
---

# {{title}}

> **完了条件:** 

## 次のアクション

- [ ] 

## 待機中

- [ ] 

## メモ

''',
    "Task Manager/99 Templates/Daily Note.md": '''---
type: daily
date: "{{date:YYYY-MM-DD}}"
tags:
  - task-manager/daily
---

# {{date:YYYY-MM-DD}}

## 今日の焦点

1. 
2. 
3. 

## 今日のタスク

```tasks
not done
due today
sort by priority
short mode
```

## メモ


## 完了

```tasks
done today
sort by done reverse
short mode
```
''',
    "Task Manager/99 Templates/Task Capture.md": '''- [ ] {{time:HH:mm}} 
''',
    ".obsidian/snippets/task-manager.css": '''/* Obsidian Task Manager — optional visual polish */
.task-manager-dashboard,
.task-manager-view,
.task-manager-project {
  --tm-accent: var(--interactive-accent);
  --tm-panel: var(--background-secondary);
}

.task-manager-dashboard h1,
.task-manager-view h1,
.task-manager-project h1 {
  margin-bottom: 0.35rem;
  letter-spacing: -0.02em;
}

.task-manager-dashboard blockquote,
.task-manager-view blockquote,
.task-manager-project blockquote {
  border-left: 4px solid var(--tm-accent);
  background: var(--tm-panel);
  border-radius: 0 8px 8px 0;
  padding: 0.7rem 1rem;
}

.task-manager-dashboard table,
.task-manager-view table {
  width: 100%;
}

.task-manager-dashboard .tasks-list-text,
.task-manager-view .tasks-list-text,
.task-manager-project .tasks-list-text {
  line-height: 1.55;
}

.task-manager-dashboard .callout,
.task-manager-view .callout {
  border-radius: 10px;
}
''',
    ".obsidian/community-plugins.json": '''[
  "obsidian-tasks-plugin",
  "dataview"
]
''',
    ".obsidian/core-plugins.json": '''[
  "file-explorer",
  "global-search",
  "switcher",
  "graph",
  "backlink",
  "canvas",
  "outgoing-link",
  "tag-pane",
  "properties",
  "page-preview",
  "daily-notes",
  "templates",
  "note-composer",
  "command-palette",
  "bookmarks",
  "outline",
  "word-count",
  "file-recovery"
]
''',
}

for relative_path, content in FILES.items():
    destination = VAULT / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")

print(f"Generated {len(FILES)} files in {VAULT}")
