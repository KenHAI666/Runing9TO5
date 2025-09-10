import os
import re
from datetime import datetime
import subprocess

# -------------------------------
# Notion 文章資料範例
# -------------------------------
notion_pages = [
    {
        "title": "Threads 等級 KPI 表",
        "categories": ["Threads"],
        "content": """
        粉絲 × 流量 × 爆文

| 等級 | 粉絲數 | 流量指標 | 爆文加分 | 定位說明 |
| --- | --- | --- | --- | --- |
| 🐣 初心者 | **300 以下** | 平均流量 ≈ 粉絲數 | 無 | 建立人設，練習穩定發文（每天 ≥ 5 則） |
| ⚔️ 轉職 | **300–1000** | 平均流量 ≥ 粉絲數 **3 倍** | 若單篇 ≥ 5 倍粉絲 → ⭐ | 開始觸及陌生人，測試內容題材 |
| 🏹 高手 | **1000–3000** | 平均流量 ≥ 粉絲數 **5 倍** | 若單篇 ≥ 10 倍粉絲 → ⭐⭐ | 內容進入穩定爆發期，能持續帶新粉 |
| 👑 大師 | **3000+** | 平均流量 ≥ 粉絲數 **5–8 倍** | 每月 ≥ 1 篇爆文（≥ 10 倍粉絲）→ ⭐⭐⭐ | 帳號進入品牌化，粉絲月成長率 ≥ 15% |
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
# 解析 Notion 內容：標題 / 表格 / 分隔線 / 段落
# -------------------------------
def parse_notion_content(md_content):
    lines = md_content.split("\n")
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 標題
        if line.startswith("### "):
            new_lines.append(f"<h3>{line[4:]}</h3>")
            i += 1
            continue
        elif line.startswith("## "):
            new_lines.append(f"<h2>{line[3:]}</h2>")
            i += 1
            continue
        elif line.startswith("# "):
            new_lines.append(f"<h1>{line[2:]}</h1>")
            i += 1
            continue
        elif line == "---":
            new_lines.append("<hr>")
            i += 1
            continue

        # 表格識別（至少兩個欄位，Tab 或多空格分隔）
        if re.search(r"\t+|\s{2,}", line):
            table_rows = []
            while i < len(lines) and re.search(r"\t+|\s{2,}", lines[i]):
                row = re.split(r"\t+|\s{2,}", lines[i].strip())
                table_rows.append(row)
                i += 1
            # Markdown 表格
            header = "| " + " | ".join(table_rows[0]) + " |"
            divider = "| " + " | ".join(["---"]*len(table_rows[0])) + " |"
            rows = ["| " + " | ".join(r) + " |" for r in table_rows[1:]]
            new_lines.append("\n".join([header, divider] + rows))
            continue

        # 普通段落
        new_lines.append(line)
        i += 1

    return "\n".join(new_lines)

# -------------------------------
# 生成 Markdown 檔案
# -------------------------------
for page in notion_pages:
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"_posts/{today}-{slugify(page['title'])}.md"

    # 解析內容
    content_parsed = parse_notion_content(page['content'])

    description = generate_description(content_parsed)
    tags = generate_tags(content_parsed)
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

    # 組成完整文章
    full_content = f'''
{content_parsed}

<p><strong>分類:</strong> {page['categories'][0]}</p>
<p><strong>標籤:</strong> {', '.join(tags)}</p>
'''

    # 寫入 Markdown 檔案
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + full_content)

    print(f"生成文章：{filename}")

    # Git commit & push（改成手動提示）
    print(f"請手動 git add / commit / push {filename}")

print("完成！")
