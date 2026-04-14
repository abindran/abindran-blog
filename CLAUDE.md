# abindran-blog

Minimalistic personal blog built with Astro. Static-only, zero JavaScript shipped to users.

## Tech Stack

- **Astro 6** — static site generator with file-based routing
- **TypeScript** — strict mode via `astro/tsconfigs/strict`
- **CSS** — custom styles with CSS variables, no framework
- **Markdown** — blog posts written in `.md` with YAML frontmatter
- **satori + @resvg/resvg-js** — auto-generated Open Graph images at build time
- **Cloudflare Pages** — deployment target (project name: `abindran-blog`)

## Commands

```bash
npm run dev       # Start dev server at localhost:4321
npm run build     # Build to dist/
npm run preview   # Preview production build locally
./sync.sh         # Sync posts from Obsidian vault to repo
npx wrangler pages deploy dist/ --project-name abindran-blog --commit-dirty=true  # Deploy to Cloudflare
```

## Project Structure

```
src/
  content/
    posts/*.md             # Blog posts (Astro content collections)
  content.config.ts        # Content collection schema definition
  lib/
    posts.ts               # Post fetching helper — filters out future-dated posts
  layouts/
    BaseLayout.astro       # Root layout — header, nav, footer, global styles
    PostLayout.astro        # Wraps individual blog posts (extends BaseLayout)
  pages/
    index.astro            # Home page — hero + 3 most recent posts
    blog.astro             # Blog listing — all posts sorted by date desc
    posts/[slug].astro     # Dynamic route — renders individual blog posts
    og/[slug].png.ts       # OG image endpoint — generates PNG per post at build time
public/
  favicon.svg              # Simple serif "A" favicon
.github/
  workflows/
    deploy.yml             # Manual deploy via workflow_dispatch
    scheduled-deploy.yml   # Daily cron — deploys if a post is scheduled for today
scripts/
  update-context.sh        # Auto-updates AI context files after source changes
sync.sh                    # Script to sync posts from Obsidian vault to repo
```

## Conventions

### Adding a new blog post

Create a `.md` file in `src/content/posts/` with this frontmatter:

```yaml
---
title: "Post Title"
description: "One-line summary"
date: "YYYY-MM-DD"
---
```

The post automatically appears on the home page (if recent) and the blog listing page. No other files need editing. To schedule a post for the future, set `date` to a future date — it will be excluded from the build until that date arrives.

### Styling

- All colors defined as CSS variables in `BaseLayout.astro` under `:root`
- Max content width: 640px
- System font stack — no external font dependencies
- Scoped styles per component; global styles only in BaseLayout
- Palette: `--text: #1a1a1a`, `--text-muted: #666`, `--bg: #fdfdfd`, `--border: #e5e5e5`, `--accent: #2563eb`

### Content fetching

Posts use [Astro content collections](https://docs.astro.build/en/guides/content-collections/). The schema is defined in `src/content.config.ts`:

```ts
{ title: z.string(), description: z.string().optional(), date: z.string() }
```

Pages load posts via `getPublishedPosts()` from `src/lib/posts.ts`, which wraps `getCollection("posts")` and filters out posts with a future `date`. This enables scheduled posts — set a future date and the post won't appear until the site is rebuilt on or after that date.

### Obsidian workflow

Posts are written in Obsidian. The vault is on iCloud at `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Sync/Blogs/`. The `sync.sh` script uses `rsync` to copy `.md` files from the vault into `src/content/posts/`. The flow:

1. Write/edit posts in Obsidian (syncs across devices via iCloud)
2. Run `./sync.sh` to copy posts into the repo
3. Commit and push — deploy manually via `workflow_dispatch` or wait for the daily scheduled deploy

### CI/CD

Two GitHub Actions workflows handle deployment:

- **`deploy.yml`** — manual deploy triggered via `workflow_dispatch` in the GitHub UI
- **`scheduled-deploy.yml`** — runs daily at 5am UTC; checks if any post has `date` matching today, and only deploys if one is found. This is what makes scheduled posts work — set a future date and the daily cron will publish it automatically.

Both workflows run `npm ci && npm run build` then deploy to Cloudflare Pages via `wrangler-action`.

### Open Graph images

Each blog post gets an auto-generated OG image at `/og/{slug}.png`. The endpoint (`src/pages/og/[slug].png.ts`) uses `satori` to render an HTML-like layout to SVG, then `@resvg/resvg-js` to convert it to a 1200×630 PNG. Fonts are fetched from Google Fonts (Inter). `BaseLayout.astro` includes Open Graph and Twitter Card meta tags; `PostLayout.astro` passes the OG image path automatically.

### Design philosophy

- No JavaScript shipped to the browser
- No analytics, comments, or dark mode — keep it simple
- Add features incrementally only when needed
- System fonts, minimal CSS, fast page loads
