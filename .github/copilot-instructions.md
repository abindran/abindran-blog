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
- `src/pages/og/[slug].png.ts` — auto-generated OG image endpoint (satori + @resvg/resvg-js, 1200×630 PNG)
- `src/pages/rss.xml.ts` — RSS feed endpoint via @astrojs/rss

## Content Model

Blog posts use YAML frontmatter:
```yaml
title: "Post Title"
description: "Optional summary"
date: "YYYY-MM-DD"
```

Posts use Astro content collections. Pages load posts via `getPublishedPosts()` from `src/lib/posts.ts`, which wraps `getCollection("posts")` and filters out future-dated posts. Schema is defined in `src/content.config.ts`.

## Open Graph

Each post gets an auto-generated OG image at `/og/{slug}.png`. BaseLayout includes Open Graph and Twitter Card meta tags. PostLayout passes the OG image path automatically. Images are 1200×630 PNGs rendered with satori (Inter font) and @resvg/resvg-js.

## RSS

An RSS feed is generated at `/rss.xml` using `@astrojs/rss`. BaseLayout includes an RSS autodiscovery `<link>` tag.

## SEO

Sitemap is auto-generated via `@astrojs/sitemap` (configured in `astro.config.mjs` with `site: 'https://abindran.com'`). `public/robots.txt` allows all crawlers and references the sitemap. BaseLayout emits Schema.org JSON-LD structured data (`BlogPosting`) for article pages.

## Styling

CSS variables in BaseLayout `:root`: `--text` (#1a1a1a), `--text-muted` (#666), `--bg` (#fdfdfd), `--border` (#e5e5e5), `--accent` (#2563eb). Max width: 640px. System font stack. Scoped styles per component.

## Guidelines

- Do not add client-side JavaScript
- Do not add CSS frameworks or external fonts
- Use scoped styles in Astro components
- Place new posts in `src/content/posts/` with required frontmatter
- Keep the design minimal and content-focused
