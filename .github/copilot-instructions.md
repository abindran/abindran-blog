This is a minimalistic Astro 6 personal blog. It ships zero JavaScript — static HTML and CSS only.

## Architecture

- `src/layouts/BaseLayout.astro` — root layout with header navigation (Home, Blog), footer, and all global styles via CSS variables
- `src/layouts/PostLayout.astro` — blog post layout extending BaseLayout; renders title, date, description, content, and back-link
- `src/pages/index.astro` — home page showing a hero section and the 3 most recent posts
- `src/pages/blog.astro` — lists all posts sorted by date descending
- `src/pages/posts/*.md` — each Markdown file is a blog post with file-based routing

## Content Model

Blog posts use YAML frontmatter:
```yaml
layout: "../../layouts/PostLayout.astro"
title: "Post Title"
description: "Optional summary"
date: "YYYY-MM-DD"
```

Posts are fetched in pages via `import.meta.glob("./posts/*.md", { eager: true })`.

## Styling

CSS variables in BaseLayout `:root`: `--text` (#1a1a1a), `--text-muted` (#666), `--bg` (#fdfdfd), `--border` (#e5e5e5), `--accent` (#2563eb). Max width: 640px. System font stack. Scoped styles per component.

## Guidelines

- Do not add client-side JavaScript
- Do not add CSS frameworks or external fonts
- Use scoped styles in Astro components
- Place new posts in `src/pages/posts/` with required frontmatter
- Keep the design minimal and content-focused
