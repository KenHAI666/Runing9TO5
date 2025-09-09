import os
import re
from datetime import datetime
import subprocess

# -------------------------------
# Notion 文章資料範例
# -------------------------------
notion_pages = [
    {
        "title": "Threads 各行業經營指南",
        "categories": ["教學"],
        "content": """# Threads 各行業經營指南

## 發文時間指南

| 時段 | 適合內容類型 | 發文目的 | 範例方向 |
| --- | --- | --- | --- |
| **上午 07:00–09:00** | 輕鬆廢文、觀察文、情緒短句 | 快速吸睛，輕度互動 | 厭世上班族、上班前心情、生活側寫 |

---

這是一段文字示例。
"""
    },
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
# 簡單生成 SEO description
# -------------------------------
def generate_description(content):
    plain = re.sub(r"<[^>]+>", "", content)
    plain = re.sub(r"\s+", " ", plain)
    return plain[:100] + "..." if len(plain) > 100 else plain

# -------------------------------
# 簡單自動生成 tags
# -------------------------------
def generate_tags(content):
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    tags = list(dict.fromkeys(words))
    return tags[:5]

# -------------------------------
# Markdown -> HTML 保留標題與分隔線
# -------------------------------
def markdown_to_html_keep_headers(md_content):
    html_lines = []
    for line in md_content.split("\n"):
        line = line.strip()
        if line.startswith("### "):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line == "---":
            html_lines.append("<hr>")
        else:
            html_lines.append(line)  # 保留原 Markdown（表格或段落）
    return "\n".join(html_lines)

# -------------------------------
# 生成 Markdown 檔案
# -------------------------------
for page in notion_pages:
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"_posts/{today}-{slugify(page['title'])}.md"

    description = generate_description(page['content'])
    tags = generate_tags(page['content'])
    title_with_category = f"[{page['categories'][0].capitalize()}] {page['title']}"

    # Front matter
    front_matter = f"""---
layout: default
title: "{title_with_category}"
date: {today}
categories: {page.get('categories', [])}
tags: {tags}
description: "{description}"
---
"""

    # 內容轉 HTML / 保留 Markdown 表格
    content_html = markdown_to_html_keep_headers(page['content'])

    # 組成完整文章
    full_content = f'''
{content_html}

<p><strong>分類:</strong> {page['categories'][0]}</p>
<p><strong>標籤:</strong> {', '.join(tags)}</p>
'''

    # 寫入 Markdown 檔案
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + full_content)

    print(f"生成文章：{filename}")

    # Git commit & push
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"新增文章：{page['title']}"])
    subprocess.run(["git", "push", "origin", "main"])

print("完成！")
