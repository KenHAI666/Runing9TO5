from flask import Flask, render_template, request, redirect, url_for, flash
import os, re
from datetime import datetime
import markdown2

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 預設 session key

# -------------------------------
# Helpers
# -------------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

def generate_tags(content):
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    tags = list(dict.fromkeys(words))
    return tags[:5]

def generate_description(content):
    plain = re.sub(r"<[^>]+>", "", content)
    return plain[:100] + "..." if len(plain) > 100 else plain

def markdown_to_html(content):
    return markdown2.markdown(content)

# -------------------------------
# Routes
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    preview_html = None
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        category = request.form.get("category", "").strip()
        content = request.form.get("content", "").strip()

        if not title or not content or not category:
            flash("請完整填寫標題、分類與內容")
        else:
            # Markdown -> HTML
            html_content = markdown_to_html(content)
            tags = generate_tags(content)
            description = generate_description(content)

            preview_html = f'''
<div class="card-section-1">
    <h1>{title}</h1>
    {html_content}
    <p><strong>分類:</strong> {category}</p>
    <p><strong>標籤:</strong> {', '.join(tags)}</p>
</div>
'''

            # 儲存 Markdown 到 _posts
            if not os.path.exists("_posts"):
                os.makedirs("_posts")

            today = datetime.today().strftime("%Y-%m-%d")
            filename = f"_posts/{today}-{slugify(title)}.md"

            front_matter = f"""---
layout: default
title: "[{category}] {title}"
date: {today}
categories: ["{category}"]
tags: {tags}
description: "{description}"
---
"""

            with open(filename, "w", encoding="utf-8") as f:
                f.write(front_matter + content)

            flash(f"文章已儲存至 {filename}")

    return render_template("index.html", preview_html=preview_html)

if __name__ == "__main__":
    app.run(debug=True)
