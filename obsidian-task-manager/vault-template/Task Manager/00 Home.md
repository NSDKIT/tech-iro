---
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
