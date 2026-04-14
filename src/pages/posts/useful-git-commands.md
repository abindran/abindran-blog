---
layout: "../../layouts/PostLayout.astro"
title: "Git Commands I Actually Use"
description: "A short reference of the git commands that come up most often in my daily workflow."
date: "2026-04-07"
---

I don't use 90% of what git can do. Here are the commands that cover the other 10% — the ones I actually reach for every day.

## The basics

```bash
git status          # what changed?
git diff            # what exactly changed?
git add -p          # stage hunks interactively
git commit -m "msg" # commit with a message
```

`git add -p` is underrated. It lets you review and stage changes hunk by hunk instead of blindly adding everything.

## Navigating history

```bash
git log --oneline -20       # recent commits, compact
git log --oneline --graph   # visual branch history
git show <commit>           # inspect a specific commit
git blame <file>            # who changed what, and when
```

`git blame` gets a bad reputation, but it's genuinely useful for understanding *why* code looks the way it does.

## Fixing mistakes

```bash
git stash              # shelve current changes
git stash pop          # bring them back
git reset HEAD~1       # undo last commit, keep changes
git checkout -- <file> # discard changes to a file
```

The one I use most is `git stash` when I realize I'm on the wrong branch.

## Working with branches

```bash
git switch -c feature  # create and switch to a branch
git rebase main        # replay commits on top of main
git cherry-pick <sha>  # grab a single commit
```

I prefer `rebase` over `merge` for keeping history linear, but either works. The important thing is consistency within a team.
