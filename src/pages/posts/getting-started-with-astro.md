---
layout: "../../layouts/PostLayout.astro"
title: "Getting Started with Astro"
description: "Why I chose Astro for my personal blog and what makes it great for content-focused sites."
date: "2026-04-10"
---

I've been looking for the right tool to build a personal blog — something fast, simple, and that lets me write in Markdown without fighting a framework. Astro checked every box.

## Why Astro?

Astro ships **zero JavaScript by default**. For a blog that's mostly text, this means pages load instantly. No hydration, no bundle overhead, just HTML and CSS.

Other things I liked:

- **File-based routing** — drop a `.md` file in `pages/posts/` and it becomes a page
- **Component islands** — if I ever need interactivity, I can add it per-component without bloating the rest
- **Familiar syntax** — `.astro` files feel like HTML with a script block at the top

## The setup

The entire blog is a handful of files:

```
src/
  layouts/
    BaseLayout.astro
    PostLayout.astro
  pages/
    index.astro
    blog.astro
    posts/
      getting-started-with-astro.md
```

Each post is a Markdown file with frontmatter for the title, date, and description. The layout handles everything else.

## What's next

I plan to keep this minimal. No analytics, no comment system, no dark mode toggle — just words on a page. If I need something later, Astro makes it easy to add incrementally.
