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

        # 表格識別（Markdown 標準表格）
        if "|" in line:
            table_rows = []
            while i < len(lines) and "|" in lines[i]:
                row = [cell.strip() for cell in lines[i].split("|")[1:-1]]  # 去掉首尾空格/空單元
                table_rows.append(row)
                i += 1
            # 組成 <table class="table-card">
            table_html = ['<table class="table-card">']
            # 表頭
            table_html.append("<thead>")
            table_html.append("<tr>" + "".join(f"<th>{h}</th>" for h in table_rows[0]) + "</tr>")
            table_html.append("</thead>")
            # 表身
            table_html.append("<tbody>")
            for r in table_rows[1:]:
                table_html.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
            table_html.append("</tbody>")
            table_html.append("</table>")
            new_lines.append("\n".join(table_html))
            continue

        # 普通段落
        if line:
            new_lines.append(f"<p>{line}</p>")
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

    # 組成完整文章（套文章卡片）
    full_content = f'''
<div class="card-section-1">
{content_parsed}

<p><strong>分類:</strong> {page['categories'][0]}</p>
<p><strong>標籤:</strong> {', '.join(tags)}</p>
</div>
'''

    # 寫入 Markdown 檔案
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + full_content)

    print(f"生成文章：{filename}")

    # Git 自動 commit & push
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"新增文章：{page['title']}"])
    subprocess.run(["git", "push", "origin", "main"])

print("完成！")
