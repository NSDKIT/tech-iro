---
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
