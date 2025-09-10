import os
import re
from datetime import datetime
import subprocess

# -------------------------------
# Notion 文章資料範例
# -------------------------------
notion_pages = [
    {
        "title": "帶著任務的勇者",
        "categories": ["電子報"],
        "content": """
📌 你經營帳號的目的，是什麼​
​
最近讀到一篇文章
大意是說 帳號分成兩種“任務型”跟“勇者型”
任務型=你打開他的頁面，就是滿滿的賣東西/賣課程，你很清楚他的任務是什麼
勇者型=頁面裡什麼都有，你可以認識這個人喜歡什麼，簡單說就是個人IP
​
我蠻認同這個二分法THREADS上也很容易看出來這兩類人
不過 我希望大家可以是帶著任務的勇者​
​
​你可以是一個分享觀察、日常與想法的人，但同時心中有個任務存在
你想讓更多人認識你的服務、你正在做的產品、副業項目
甚至是一間你努力經營的實體店​
​在做個人IP時也是可以戴著任務的
​讓你的觀眾透過認識你進而信任你再來跟你消費​
​​
個人品牌不是只有「做自己」
也可以「做自己+傳遞價值」
因為有任務，內容會更有方向
因為像勇者，分享才有溫度，觀眾才會信任你
​
這也是我常在說的 先交友再交易
先拿出你能幫們解決那些問題的能力
讓大家信任你有這個能力
你才容易交易
​
但
還有一種狀況是不會賣​
有人氣 有產品 但不敢賣
如同我一年前一樣，如何銷售，我們找時間再來寫
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
