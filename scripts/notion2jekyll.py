import os
import datetime
import re

# -------------------------------
# Notion 文章範例資料
# -------------------------------
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
# 確認專案根目錄 _posts 資料夾
# -------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
POSTS_DIR = os.path.join(ROOT_DIR, "_posts")

if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)
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
    filename = os.path.join(POSTS_DIR, f"{page['date']}-{slugify(page['title'])}.md")
    
    # 自動抓 SEO description，如果沒有就取文章前 100 個字
    description = page.get("description", "")
    if not description:
        description = page["content"][:100].replace("\n", " ").strip()
    
    # 前置資料（Front Matter）
    front_matter = f"""---
layout: post
title: "{page['title']}"
date: {page['date']}
categories: {page.get('categories', [])}
tags: {page.get('tags', [])}
description: "{description}"
---
"""
    # 寫入檔案
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + "\n" + page['content'])
    
    print(f"生成文章：{filename}")

print("完成！")
