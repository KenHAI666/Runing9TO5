from flask import Flask, render_template, request, redirect
from datetime import datetime
import os
import re
import subprocess

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "../templates"))

# -------------------------------
# 工具函數
# -------------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

def generate_description(content):
    plain = re.sub(r"<[^>]+>", "", content)
    plain = re.sub(r"\s+", " ", plain)
    return plain[:100] + "..." if len(plain) > 100 else plain

def generate_tags(content):
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    return list(dict.fromkeys(words))[:5]

def parse_content(md_content):
    lines = md_content.split("\n")
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # 標題
        if line.startswith("### "):
            new_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("## "):
            new_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("# "):
            new_lines.append(f"<h1>{line[2:]}</h1>")
        elif line == "---":
            new_lines.append("<hr>")
        # 表格
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
        # 普通段落
        elif line:
            new_lines.append(f"<p>{line}</p>")
        i += 1
    return "\n".join(new_lines)

# -------------------------------
# 後台首頁（輸入 + 預覽）
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
        parsed = parse_content(content)
        preview_html = f'''
<div class="card-section-1">
<h2>{title}</h2>
{parsed}
<p><strong>分類:</strong> {category}</p>
<p><strong>標籤:</strong> {', '.join(generate_tags(content))}</p>
</div>
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

    parsed = parse_content(content)
    tags = generate_tags(content)
    description = generate_description(parsed)
    front_matter = f"""---
layout: default
title: "[{category}] {title}"
date: {date_str}
categories: [{category}]
tags: {tags}
description: "{description}"
---
"""

    full_content = f'''
<div class="card-section-1">
<h2>{title}</h2>
{parsed}
<p><strong>分類:</strong> {category}</p>
<p><strong>標籤:</strong> {', '.join(tags)}</p>
</div>
'''

    if not os.path.exists("_posts"):
        os.makedirs("_posts")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + full_content)

    # Git commit & push
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"新增文章：{title}"])
    subprocess.run(["git", "push", "origin", "main"])

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
