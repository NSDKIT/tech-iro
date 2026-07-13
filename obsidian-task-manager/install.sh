#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/vault-template"
TARGET_VAULT="${1:-}"
FORCE="${2:-}"

if [[ -z "$TARGET_VAULT" ]]; then
  echo "使い方: ./install.sh /path/to/ObsidianVault [--force]" >&2
  exit 1
fi

if [[ ! -d "$TARGET_VAULT" ]]; then
  echo "エラー: Vaultフォルダが見つかりません: $TARGET_VAULT" >&2
  exit 1
fi

if [[ ! -d "$TARGET_VAULT/.obsidian" ]]; then
  echo "エラー: .obsidianが見つかりません。Obsidianで一度Vaultとして開いてください。" >&2
  exit 1
fi

TASK_TARGET="$TARGET_VAULT/Task Manager"
CSS_SOURCE="$SOURCE_DIR/.obsidian/snippets/task-manager.css"
CSS_TARGET="$TARGET_VAULT/.obsidian/snippets/task-manager.css"

if [[ -e "$TASK_TARGET" && "$FORCE" != "--force" ]]; then
  echo "エラー: '$TASK_TARGET' は既に存在します。" >&2
  echo "内容を確認し、上書きする場合だけ第2引数に --force を指定してください。" >&2
  exit 1
fi

if [[ -e "$TASK_TARGET" && "$FORCE" == "--force" ]]; then
  BACKUP="$TARGET_VAULT/Task Manager.backup.$(date +%Y%m%d-%H%M%S)"
  mv "$TASK_TARGET" "$BACKUP"
  echo "既存フォルダをバックアップしました: $BACKUP"
fi

mkdir -p "$TARGET_VAULT/.obsidian/snippets"
cp -R "$SOURCE_DIR/Task Manager" "$TARGET_VAULT/"

if [[ ! -e "$CSS_TARGET" || "$FORCE" == "--force" ]]; then
  cp "$CSS_SOURCE" "$CSS_TARGET"
else
  echo "既存CSSスニペットは上書きしませんでした: $CSS_TARGET"
fi

cat <<EOF

導入が完了しました。

次にObsidianで以下を設定してください。
1. コミュニティプラグイン「Tasks」をインストールして有効化する。
2. 任意で「Dataview」をインストールして有効化する。
3. 設定 → コアプラグイン → Templates を有効化する。
4. Templatesのフォルダを「Task Manager/99 Templates」にする。
5. 設定 → 外観 → CSSスニペットで「task-manager」を有効化する。
6. 「Task Manager/00 Home.md」を開く。
EOF
