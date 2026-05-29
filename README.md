# Runing9TO5

Jekyll site for `runing9to5.com`.

## Stack

- Jekyll + GitHub Pages
- Main layouts in `_layouts/`
- Shared SEO and metadata in `_includes/head.html`
- Long-form posts in `_posts/`
- Static pages like home, articles, resources, about, contact at repo root

## Content flow

- Published articles live in `_posts/`
- Draft content lives in `_drafts/`
- `scripts/notion2jekyll.py` converts exported Notion JSON into Jekyll posts
- The script is safe by default: it does not stage, commit, or push changes

## Local workflow

1. Install Ruby / Bundler dependencies for Jekyll.
2. Run the site locally with `bundle exec jekyll serve`.
3. Open `http://127.0.0.1:4000`.

## Notion import

Dry run:

```bash
python3 scripts/notion2jekyll.py path/to/notion-export.json
```

Write posts:

```bash
python3 scripts/notion2jekyll.py path/to/notion-export.json --write
```

Expected JSON shape:

```json
[
  {
    "title": "文章標題",
    "date": "2026-06-10",
    "categories": ["content-strategy"],
    "tags": ["內容策略", "Threads"],
    "permalink": "/articles/custom-slug/",
    "content": "# 段落標題\n\n這裡是內容"
  }
]
```

## Config

- Site settings are in `_config.yml`
- Brand/social/email values should be changed there first
- Ad slots are disabled by default until real slot IDs are configured
