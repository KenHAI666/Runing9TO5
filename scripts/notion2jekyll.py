import os
import re
from datetime import datetime

# -------------------------------
# Notion 文章資料，只需填寫這些
# -------------------------------
notion_pages = [
    {
        "title": "Welcome",
        "content": "這是一篇範例文章，測試 Jekyll 是否正常運作。文章會自動生成 SEO 與 tags。",
        "categories": ["articles"]
    },
    {
        "title": "測試文章",
        "content": "測試文章內容，用來示範自動生成 Jekyll 文章，SEO description 與 tags 都會自動抓取。",
        "categories": ["教學"]
    }
]

# -------------------------------
# 確認 _posts 資料夾
# -------------------------------
if not os.path.exists("_posts"):
    os.makedirs("_posts")

# -------------------------------
# 幫標題生成安全檔名
# -------------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

# -------------------------------
# 簡單生成 SEO description：取前 100 個字
# -------------------------------
def generate_description(content):
    plain = re.sub(r"<[^>]+>", "", content)
    return plain[:100] + "..." if len(plain) > 100 else plain

# -------------------------------
# 簡單自動生成 tags：抓文章內容中的詞語（此處為示範，可改進）
# -------------------------------
def generate_tags(content):
    # 取中文詞語與英文單字
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    # 去重並選前 5 個
    tags = list(dict.fromkeys(words))
    return tags[:5]

# -------------------------------
# 生成 Markdown 檔案
# -------------------------------
for page in notion_pages:
    # 日期：今天
    today = datetime.today().strftime("%Y-%m-%d")
    
    # 前置資料
    title_with_category = f"[{page['categories'][0].capitalize()}] {page['title']}"
    description = generate_description(page['content'])
    tags = generate_tags(page['content'])

    filename = f"_posts/{today}-{slugify(page['title'])}.md"

    front_matter = f"""---
layout: default
title: "{title_with_category}"
date: {today}
categories: {page.get('categories', [])}
tags: {tags}
description: "{description}"
---
"""

    content = f"""
<div class="card-section" style="background:#fff6e8;">
  <h1>{page['title']}</h1>
  {page['content']}
</div>
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + content)

    print(f"生成文章：{filename}")

print("完成！")
