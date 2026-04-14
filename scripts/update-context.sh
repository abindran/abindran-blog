#!/usr/bin/env bash
#
# update-context.sh
#
# Checks if source files changed in the last commit and, if so,
# invokes Claude Code to update the AI context files.
#
# Usage:
#   ./scripts/update-context.sh          # Run manually
#   Called automatically via git post-commit hook

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"

# Files/dirs whose changes should trigger a context update
WATCH_PATHS=(
  "src/"
  "package.json"
  "astro.config.mjs"
  "tsconfig.json"
  "public/"
)

# Context files that get updated (skip if ONLY these changed)
CONTEXT_FILES=(
  "CLAUDE.md"
  "README.md"
  ".cursorrules"
  ".github/copilot-instructions.md"
)

# Check if any watched paths changed in the last commit
changed_files=$(git diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null || true)

if [ -z "$changed_files" ]; then
  exit 0
fi

source_changed=false
for watch_path in "${WATCH_PATHS[@]}"; do
  if echo "$changed_files" | grep -q "^${watch_path}"; then
    source_changed=true
    break
  fi
done

if [ "$source_changed" = false ]; then
  exit 0
fi

# Check if ONLY context files changed (avoid infinite loop)
non_context_changes=false
while IFS= read -r file; do
  is_context=false
  for ctx in "${CONTEXT_FILES[@]}"; do
    if [ "$file" = "$ctx" ]; then
      is_context=true
      break
    fi
  done
  if [ "$is_context" = false ]; then
    non_context_changes=true
    break
  fi
done <<< "$changed_files"

if [ "$non_context_changes" = false ]; then
  exit 0
fi

# Check if claude CLI is available
if ! command -v claude &>/dev/null; then
  echo "[update-context] claude CLI not found, skipping context update"
  exit 0
fi

echo "[update-context] Source files changed — updating AI context files..."

cd "$REPO_ROOT"
claude --print "Run the /update-context command. Update all AI context files (CLAUDE.md, README.md, .cursorrules, .github/copilot-instructions.md) to reflect the current state of the codebase. Only change what is actually out of date." --allowedTools "Read,Write,Edit,Glob,Grep,Bash" 2>/dev/null || {
  echo "[update-context] Claude context update failed (non-fatal)"
}

echo "[update-context] Done."
