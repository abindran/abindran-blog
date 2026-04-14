This is a minimalistic Astro 6 personal blog. It ships zero JavaScript — static HTML and CSS only.

## Architecture

- `src/layouts/BaseLayout.astro` — root layout with header navigation (Home, Blog), footer, and all global styles via CSS variables
- `src/layouts/PostLayout.astro` — blog post layout extending BaseLayout; renders title, date, description, content, and back-link
- `src/content/posts/*.md` — blog posts managed via Astro content collections
- `src/content.config.ts` — content collection schema definition
- `src/lib/posts.ts` — post fetching helper; filters out future-dated posts for scheduled publishing
- `src/pages/index.astro` — home page showing a hero section and the 3 most recent posts
- `src/pages/blog.astro` — lists all posts sorted by date descending
- `src/pages/posts/[slug].astro` — dynamic route rendering individual blog posts

## Content Model

Blog posts use YAML frontmatter:
```yaml
title: "Post Title"
description: "Optional summary"
date: "YYYY-MM-DD"
```

Posts use Astro content collections. Pages load posts via `getPublishedPosts()` from `src/lib/posts.ts`, which wraps `getCollection("posts")` and filters out future-dated posts. Schema is defined in `src/content.config.ts`.

## Styling

CSS variables in BaseLayout `:root`: `--text` (#1a1a1a), `--text-muted` (#666), `--bg` (#fdfdfd), `--border` (#e5e5e5), `--accent` (#2563eb). Max width: 640px. System font stack. Scoped styles per component.

## Guidelines

- Do not add client-side JavaScript
- Do not add CSS frameworks or external fonts
- Use scoped styles in Astro components
- Place new posts in `src/content/posts/` with required frontmatter
- Keep the design minimal and content-focused
