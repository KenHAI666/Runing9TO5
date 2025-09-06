import os
import datetime
import re

# -------------------------------
# Notion 文章範例資料
# -------------------------------
# 每篇文章用 dict 表示
# page['title'] → 標題
# page['date'] → 發布日期 YYYY-MM-DD
# page['content'] → 文章內容（Markdown）
# page['tags'] → 標籤 list
# page['categories'] → 分類 list
# page['description'] → SEO description
notion_pages = [
    {
        "title": "測試文章",
        "date": "2025-09-06",
        "content": "這是從 Notion 來的文章內容。\n\n可以換行。\n\n也可以有列表。",
        "tags": ["Notion", "Jekyll", "測試"],
        "categories": ["教學"],
        "description": "這是一篇測試用文章，用來示範自動生成 Jekyll 文章。"
    },
    # 可以加入更多文章 dict
]

# -------------------------------
# 確認 _posts 資料夾
# -------------------------------
if not os.path.exists("_posts"):
    os.makedirs("_posts")
    print("已建立 _posts 資料夾")

# -------------------------------
# 幫標題生成安全檔名
# -------------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

# -------------------------------
# 生成 Markdown 檔案
# -------------------------------
for page in notion_pages:
    # 檔名：YYYY-MM-DD-標題.md
    filename = f"_posts/{page['date']}-{slugify(page['title'])}.md"
    
    # 前置資料（Front Matter）
    front_matter = f"""---
layout: post
title: "{page['title']}"
date: {page['date']}
categories: {page.get('categories', [])}
tags: {page.get('tags', [])}
description: "{page.get('description','')}"
---
"""
    # 寫入檔案
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + "\n" + page['content'])
    
    print(f"生成文章：{filename}")

print("完成！")
