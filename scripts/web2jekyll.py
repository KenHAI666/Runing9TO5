import os
import re
from datetime import datetime

# -------------------------------
# 幫標題生成安全檔名
# -------------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

# -------------------------------
# 簡單生成 SEO description
# -------------------------------
def generate_description(content):
    plain = re.sub(r"<[^>]+>", "", content)
    return plain[:100] + "..." if len(plain) > 100 else plain

# -------------------------------
# 簡單自動生成 tags
# -------------------------------
def generate_tags(content):
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    tags = list(dict.fromkeys(words))
    return tags[:5]

# -------------------------------
# 生成 Markdown 並套 card-section-1 CSS
# -------------------------------
def create_post(title, categories, content):
    if not os.path.exists("_posts"):
        os.makedirs("_posts")

    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"_posts/{today}-{slugify(title)}.md"

    description = generate_description(content)
    tags = generate_tags(content)
    title_with_category = f"[{categories[0].capitalize()}] {title}"

    # Front matter
    front_matter = f"""---
layout: default
title: "{title_with_category}"
date: {today}
categories: {categories}
tags: {tags}
description: "{description}"
---
"""

    # 內容轉 HTML
    content_paragraphs = content.split('\n\n')
    content_html = ''.join(f'<p>{p.replace("\n","<br>")}</p>\n' for p in content_paragraphs)

    card_html = f'''
<div class="card-section-1">
    <h1>{title}</h1>
    {content_html}
    <p><strong>分類:</strong> {categories[0]}</p>
    <p><strong>標籤:</strong> {', '.join(tags)}</p>
</div>
'''

    # 寫入 Markdown
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + card_html)

    return filename
# scripts/web2jekyll.py
import os
from datetime import datetime

def create_markdown(title, category, content, posts_dir="../_posts"):
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"{posts_dir}/{today}-{title.replace(' ', '-')}.md"

    md_content = f"""---
layout: default
title: "{title}"
date: {today}
categories: ["{category}"]
---

{content}
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    return filename
