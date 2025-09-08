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
# 生成 Markdown 檔案
# -------------------------------
def create_post(title, categories, content):
    # 使用 os.path.join 來確保路徑正確
    posts_dir = "_posts"
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    today = datetime.today().strftime("%Y-%m-%d")
    filename = os.path.join(posts_dir, f"{today}-{slugify(title)}.md")

    description = generate_description(content)
    tags = categories # 這裡簡單地將分類作為標籤，你也可以根據內容生成更複雜的標籤

    # Front matter
    front_matter = f"""---
layout: default
title: "{title}"
date: {today}
categories: {categories}
tags: {tags}
description: "{description}"
---
"""
    # 寫入 Markdown，直接使用原始的 content 內容
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + "\n\n" + content)

    return filename
