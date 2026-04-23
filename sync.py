#!/usr/bin/env python3
"""Sync blog posts and images from Obsidian vault to Astro content."""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}
POST_EXTENSIONS = IMAGE_EXTENSIONS | {".md"}
EMBED_PATTERN = re.compile(r"!\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def should_ignore(relative_path: Path) -> bool:
    return "Templates" in relative_path.parts


def collect_files(source_dir: Path, allowed_extensions: set[str]) -> set[Path]:
    results: set[Path] = set()
    for file_path in source_dir.rglob("*"):
        if not file_path.is_file():
            continue
        rel = file_path.relative_to(source_dir)
        if should_ignore(rel):
            continue
        if file_path.suffix.lower() in allowed_extensions:
            results.add(rel)
    return results


def prune_empty_dirs(root: Path) -> None:
    for directory in sorted((path for path in root.rglob("*") if path.is_dir()), reverse=True):
        if not any(directory.iterdir()):
            directory.rmdir()


def sync_tree(source_dir: Path, target_dir: Path, allowed_extensions: set[str]) -> None:
    source_files = collect_files(source_dir, allowed_extensions)
    target_files = collect_files(target_dir, allowed_extensions) if target_dir.exists() else set()

    for rel_path in sorted(target_files - source_files):
        (target_dir / rel_path).unlink(missing_ok=True)

    for rel_path in sorted(source_files):
        source_file = source_dir / rel_path
        target_file = target_dir / rel_path
        target_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, target_file)

    if target_dir.exists():
        prune_empty_dirs(target_dir)


def normalize_obsidian_embeds(content_dir: Path) -> None:
    for markdown_file in content_dir.rglob("*.md"):
        original = markdown_file.read_text(encoding="utf-8")

        def replace_embed(match: re.Match[str]) -> str:
            target = match.group(1).strip()
            alt = (match.group(2) or "").strip()
            target_path = Path(target)
            normalized_target = target_path.as_posix()

            if target_path.suffix.lower() not in IMAGE_EXTENSIONS:
                return match.group(0)

            # Resolve plain filenames from top-level Assets/Asserts folders.
            if "/" not in normalized_target:
                assets_candidate = content_dir / "Assets" / target
                asserts_candidate = content_dir / "Asserts" / target
                if assets_candidate.exists():
                    normalized_target = f"Assets/{target}"
                elif asserts_candidate.exists():
                    normalized_target = f"Asserts/{target}"

            # Numeric wiki suffixes are usually width hints, not alt text.
            if alt.isdigit():
                alt = ""
            return f"![{alt}](<{normalized_target}>)"

        updated = EMBED_PATTERN.sub(replace_embed, original)
        if updated != original:
            markdown_file.write_text(updated, encoding="utf-8")


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    obsidian_vault_dir = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Sync"
    obsidian_posts_dir = obsidian_vault_dir / "Blogs"
    content_dir = repo_root / "src/content/posts"

    if not obsidian_posts_dir.is_dir():
        print(f"Error: Obsidian posts folder not found at {obsidian_posts_dir}", file=sys.stderr)
        return 1

    content_dir.mkdir(parents=True, exist_ok=True)
    sync_tree(obsidian_posts_dir, content_dir, POST_EXTENSIONS)

    for asset_folder in ("Assets", "Asserts"):
        source_asset_dir = obsidian_vault_dir / asset_folder
        target_asset_dir = content_dir / asset_folder
        if source_asset_dir.is_dir():
            target_asset_dir.mkdir(parents=True, exist_ok=True)
            sync_tree(source_asset_dir, target_asset_dir, IMAGE_EXTENSIONS)

    normalize_obsidian_embeds(content_dir)
    print(f"Synced posts from Obsidian to {content_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
