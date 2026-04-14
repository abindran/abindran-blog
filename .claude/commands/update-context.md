Review the current state of the repository and update all AI context files to reflect the latest project structure, conventions, and patterns.

## Steps

1. Read every source file under `src/` to understand the current project structure, components, pages, content, and patterns.
2. Check `package.json` for any dependency or script changes.
3. Check `astro.config.mjs` for any configuration changes.
4. Review recent git history with `git log --oneline -10` and `git diff HEAD~1 --stat` to understand what changed recently.

## Files to update

Update each of these files so they accurately reflect the **current** state of the codebase:

### CLAUDE.md
- Project structure (add/remove files and directories as needed)
- Tech stack and dependencies
- Commands (dev, build, deploy)
- Conventions (how to add posts, styling patterns, content fetching)
- Design philosophy

### README.md
- Project description
- Quick start instructions
- Project structure tree
- Deployment instructions

### .cursorrules
- Tech stack summary
- Project layout
- Key patterns
- Rules for AI assistants

### .github/copilot-instructions.md
- Architecture overview
- Content model
- Styling details
- Guidelines

## Rules

- Only update information that has actually changed. Do not rewrite files that are already accurate.
- Preserve the existing format and style of each file.
- Do not add speculative or aspirational content — only document what exists now.
- If a new page, layout, component, or integration was added, make sure it appears in all four files.
- If something was removed, make sure it is removed from all four files.
- After updating, run `npm run build` to verify the project still builds cleanly.
