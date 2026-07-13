from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "vault-template"

REQUIRED_FILES = [
    "Task Manager/00 Home.md",
    "Task Manager/01 Inbox/Inbox.md",
    "Task Manager/02 Views/Today.md",
    "Task Manager/02 Views/This Week.md",
    "Task Manager/02 Views/Completed.md",
    "Task Manager/03 Projects/Projects.md",
    "Task Manager/03 Projects/Sample Project.md",
    "Task Manager/99 Templates/Project.md",
    "Task Manager/99 Templates/Daily Note.md",
    ".obsidian/snippets/task-manager.css",
]

errors: list[str] = []

for relative in REQUIRED_FILES:
    path = VAULT / relative
    if not path.is_file():
        errors.append(f"必須ファイルがありません: {relative}")

markdown_files = sorted(VAULT.rglob("*.md"))
if not markdown_files:
    errors.append("Markdownファイルがありません")

wiki_link_pattern = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
absolute_path_pattern = re.compile(r"(?:/home/|/Users/|[A-Za-z]:\\\\)")

for path in markdown_files:
    text = path.read_text(encoding="utf-8")

    if text.count("```") % 2:
        errors.append(f"コードフェンスが閉じていません: {path.relative_to(VAULT)}")

    if absolute_path_pattern.search(text):
        errors.append(f"環境依存の絶対パスがあります: {path.relative_to(VAULT)}")

    for target in wiki_link_pattern.findall(text):
        target_path = VAULT / f"{target}.md"
        if not target_path.exists():
            errors.append(
                f"リンク先がありません: {path.relative_to(VAULT)} -> {target}.md"
            )

combined = "\n".join(path.read_text(encoding="utf-8") for path in markdown_files)
for required_query in ["due today", "due before today", "done today", "no due date"]:
    if required_query not in combined:
        errors.append(f"必須Tasksクエリがありません: {required_query}")

if "```tasks" not in combined:
    errors.append("Tasksコードブロックがありません")

if "```dataview" not in combined:
    errors.append("Dataviewコードブロックがありません")

if errors:
    print("検証に失敗しました。", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print(f"検証成功: {len(REQUIRED_FILES)}個の必須ファイル")
print(f"検証成功: {len(markdown_files)}個のMarkdownファイル")
print("検証成功: 内部リンク、コードフェンス、相対パス、主要クエリ")
