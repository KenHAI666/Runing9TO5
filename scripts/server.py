import os
import re
from datetime import datetime
import subprocess
from flask import Flask, render_template, request, redirect

# Flask 設定 templates 路徑
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../templates")
)


# -------------------------------
# 工具函數
# -------------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

def parse_content(md_content):
    """將簡單 Markdown 轉 HTML"""
    lines = md_content.split("\n")
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("### "):
            new_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("## "):
            new_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("# "):
            new_lines.append(f"<h1>{line[2:]}</h1>")
        elif line == "---":
            new_lines.append("<hr>")
        elif "|" in line:
            table_rows = []
            while i < len(lines) and "|" in lines[i]:
                row = [cell.strip() for cell in lines[i].split("|")[1:-1]]
                table_rows.append(row)
                i += 1
            table_html = ['<table class="table-card">']
            table_html.append("<thead><tr>" + "".join(f"<th>{h}</th>" for h in table_rows[0]) + "</tr></thead>")
            table_html.append("<tbody>")
            for r in table_rows[1:]:
                table_html.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
            table_html.append("</tbody></table>")
            new_lines.append("\n".join(table_html))
            continue
        elif line:
            new_lines.append(f"<p>{line}</p>")
        i += 1
    return "\n".join(new_lines)

def generate_tags(content):
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    return list(dict.fromkeys(words))[:5]

# -------------------------------
# 後台首頁（編輯 + 預覽）
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    preview_html = ""
    title = ""
    category = ""
    content = ""
    if request.method == "POST":
        title = request.form.get("title", "")
        category = request.form.get("category", "")
        content = request.form.get("content", "")
        html_content = parse_content(content)
        preview_html = f'''
<section class="card-section" style="background:#f7f7f7;">
<h2>{title}</h2>
{html_content}
<p><strong>分類:</strong> {category}</p>
<p><strong>標籤:</strong> {', '.join(generate_tags(content))}</p>

'''
    return render_template("editor.html", preview_html=preview_html, title=title, category=category, content=content)

# -------------------------------
# 發佈文章
# -------------------------------
@app.route("/publish", methods=["POST"])
def publish():
    title = request.form.get("title", "")
    category = request.form.get("category", "")
    content = request.form.get("content", "")
    date_str = datetime.today().strftime("%Y-%m-%d")
    filename = f"_posts/{date_str}-{slugify(title)}.md"

    md_html = parse_content(content)
    tags = generate_tags(content)

    front_matter = f"""---
layout: default
title: "[{category}] {title}"
date: {date_str}
categories: [{category}]
tags: {tags}
description: "{content[:100]}..."
---
"""

    full_content = f'''
<section class="card-section" style="background:#f7f7f7;">
<h2>{title}</h2>
{md_html}
<p><strong>分類:</strong> {category}</p>
<p><strong>標籤:</strong> {', '.join(tags)}</p>

'''

    if not os.path.exists("_posts"):
        os.makedirs("_posts")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + full_content)

    # Git 自動提交
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"新增文章：{title}"])
    subprocess.run(["git", "push", "origin", "main"])

    return redirect("/")

# -------------------------------
# 啟動 Flask
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
