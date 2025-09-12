# server.py
from flask import Flask, render_template, request, redirect, url_for, flash
import os
import re
from datetime import datetime
import subprocess
import markdown

app = Flask(__name__)
app.secret_key = 'replace_with_a_secure_key'

# -------------------------------
# 確認 _posts 資料夾
# -------------------------------
if not os.path.exists("_posts"):
    os.makedirs("_posts")

# -------------------------------
# Markdown 解析 + 卡片套用
# -------------------------------
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
                row = [c.strip() for c in lines[i].split("|")[1:-1]]
                table_rows.append(row)
                i += 1
            i -= 1  # 因為外層 loop 會 +1
            table_html = ['<table class="table-card">']
            table_html.append("<thead>")
            table_html.append("<tr>" + "".join(f"<th>{h}</th>" for h in table_rows[0]) + "</tr>")
            table_html.append("</thead>")
            table_html.append("<tbody>")
            for r in table_rows[1:]:
                table_html.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
            table_html.append("</tbody>")
            table_html.append("</table>")
            new_lines.append("\n".join(table_html))
        # 段落
        elif line:
            new_lines.append(f"<p>{line}</p>")
        i += 1
    content_html = "\n".join(new_lines)
    # 套卡片
    return f'<div class="card-section-1">\n{content_html}\n</div>'

# -------------------------------
# Slug & SEO / tags
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
    tags = list(dict.fromkeys(words))
    return tags[:5]

# -------------------------------
# 後台首頁 / 新增文章
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        categories = request.form.get("categories", "一般").strip()
        tags_input = request.form.get("tags", "").strip()
        content_md = request.form.get("content", "").strip()

        if not title or not content_md:
            flash("標題與內文不可空白")
            return redirect(url_for("index"))

        content_html = parse_content(content_md)
        description = generate_description(content_html)
        tags = tags_input.split(",") if tags_input else generate_tags(content_html)
        today = datetime.today().strftime("%Y-%m-%d")
        slug = slugify(title)
        filename = f"_posts/{today}-{slug}.md"

        front_matter = f"""---
layout: default
title: "[{categories}] {title}"
date: {today}
categories: [{categories}]
tags: {tags}
description: "{description}"
---
"""

        full_content = f"{front_matter}\n{content_html}\n<p><strong>分類:</strong> {categories}</p>\n<p><strong>標籤:</strong> {', '.join(tags)}</p>"

        # 寫入檔案
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_content)

        # Git commit & push
        subprocess.run(["git", "add", filename])
        subprocess.run(["git", "commit", "-m", f"新增文章：{title}"])
        subprocess.run(["git", "push", "origin", "main"])

        flash(f"文章已發佈到網站：{filename}")
        return redirect(url_for("index"))

    return render_template("index.html")

# -------------------------------
# 預覽文章 HTML
# -------------------------------
@app.route("/preview", methods=["POST"])
def preview():
    content_md = request.form.get("content", "")
    content_html = parse_content(content_md)
    return render_template("preview.html", content=content_html)

# -------------------------------
# 啟動
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
