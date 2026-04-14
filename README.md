# abindran-blog

A minimalistic personal blog built with [Astro](https://astro.build). Ships zero JavaScript — just static HTML and CSS.

## Quick Start

```bash
npm install
npm run dev
```

Open [localhost:4321](http://localhost:4321).

## Writing a Post

Create a Markdown file in `src/pages/posts/`:

```markdown
---
layout: "../../layouts/PostLayout.astro"
title: "Your Post Title"
description: "A brief summary"
date: "2026-04-14"
---

Your content here.
```

It will appear automatically on the home page and blog listing.

## Project Structure

```
src/
  layouts/
    BaseLayout.astro       — shared layout (nav, footer, global styles)
    PostLayout.astro       — blog post wrapper
  pages/
    index.astro            — home page
    blog.astro             — blog listing
    posts/*.md             — blog posts (file-based routing)
public/
  favicon.svg
```

## Deployment

Built for Cloudflare Pages:

```bash
npm run build
npx wrangler pages deploy dist/ --project-name abindran-blog
```

## AI Context Files

This repo includes context files for AI-assisted development:

| File | Tool |
|------|------|
| `CLAUDE.md` | [Claude Code](https://claude.com/claude-code) |
| `.cursorrules` | [Cursor](https://cursor.com) |
| `.github/copilot-instructions.md` | [GitHub Copilot](https://github.com/features/copilot) |

Run `/update-context` in Claude Code after making structural changes to keep these files in sync.
