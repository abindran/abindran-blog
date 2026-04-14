#!/bin/bash
# Sync blog posts from Obsidian vault to the repo.
# Usage: ./sync.sh

OBSIDIAN_DIR="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Sync/Blogs"
CONTENT_DIR="$(dirname "$0")/src/content/posts"

if [ ! -d "$OBSIDIAN_DIR" ]; then
  echo "Error: Obsidian folder not found at $OBSIDIAN_DIR"
  exit 1
fi

rsync -av --delete --include="*.md" --exclude="*" "$OBSIDIAN_DIR/" "$CONTENT_DIR/"

echo "Synced posts from Obsidian to $CONTENT_DIR"
