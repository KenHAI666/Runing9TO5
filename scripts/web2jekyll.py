import os
import re
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

def generate_description(content):
    plain = re.sub(r"<[^>]+>", "", content)
    return plain[:100] + "..." if len(plain) > 100 else plain

def generate_tags(content):
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    tags = list(dict.fromkeys(words))
    return tags[:5]

def create_post(title, category, content):
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"_posts/{today}-{slugify(title)}.md"

    if not os.path.exists("_posts"):
        os.makedirs("_posts")

    description = generate_description(content)
    tags = generate_tags(content)

    front_matter = f"""---
layout: default
title: "[{category}] {title}"
date: {today}
categories: [{category}]
tags: {tags}
description: "{description}"
---
"""

    content_paragraphs = content.split('\n\n')
    content_html = ''.join(f'<p>{p.replace("\n","<br>")}</p>\n' for p in content_paragraphs)

    card_html = f'''
<div class="card-section-1">
    <h1>{title}</h1>
    {content_html}
    <p><strong>分類:</strong> {category}</p>
    <p><strong>標籤:</strong> {', '.join(tags)}</p>
</div>
'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + card_html)

    return filename
