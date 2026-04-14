# abindran-blog

Minimalistic personal blog built with Astro. Static-only, zero JavaScript shipped to users.

## Tech Stack

- **Astro 6** — static site generator with file-based routing
- **TypeScript** — strict mode via `astro/tsconfigs/strict`
- **CSS** — custom styles with CSS variables, no framework
- **Markdown** — blog posts written in `.md` with YAML frontmatter
- **Cloudflare Pages** — deployment target (project name: `abindran-blog`)

## Commands

```bash
npm run dev       # Start dev server at localhost:4321
npm run build     # Build to dist/
npm run preview   # Preview production build locally
npx wrangler pages deploy dist/ --project-name abindran-blog --commit-dirty=true  # Deploy to Cloudflare
```

## Project Structure

```
src/
  layouts/
    BaseLayout.astro      # Root layout — header, nav, footer, global styles
    PostLayout.astro       # Wraps individual blog posts (extends BaseLayout)
  pages/
    index.astro            # Home page — hero + 3 most recent posts
    blog.astro             # Blog listing — all posts sorted by date desc
    posts/*.md             # Blog posts — each file becomes a route
public/
  favicon.svg              # Simple serif "A" favicon
```

## Conventions

### Adding a new blog post

Create a `.md` file in `src/pages/posts/` with this frontmatter:

```yaml
---
layout: "../../layouts/PostLayout.astro"
title: "Post Title"
description: "One-line summary"
date: "YYYY-MM-DD"
---
```

The post automatically appears on the home page (if recent) and the blog listing page. No other files need editing.

### Styling

- All colors defined as CSS variables in `BaseLayout.astro` under `:root`
- Max content width: 640px
- System font stack — no external font dependencies
- Scoped styles per component; global styles only in BaseLayout
- Palette: `--text: #1a1a1a`, `--text-muted: #666`, `--bg: #fdfdfd`, `--accent: #2563eb`

### Content fetching

Posts are loaded via `import.meta.glob("./posts/*.md", { eager: true })` in both `index.astro` and `blog.astro`. The Post interface expects:

```ts
interface Post {
  url: string;
  frontmatter: { title: string; description?: string; date: string };
}
```

### Design philosophy

- No JavaScript shipped to the browser
- No analytics, comments, or dark mode — keep it simple
- Add features incrementally only when needed
- System fonts, minimal CSS, fast page loads
