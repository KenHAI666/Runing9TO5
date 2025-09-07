from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys

# 將 scripts 加入 path
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))
from web2jekyll import create_article

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Flash message 用

# 首頁 / 新增文章頁
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        category = request.form.get("category")
        content = request.form.get("content")

        if not title or not content:
            flash("標題與內容不可空白！")
            return redirect(url_for("index"))

        path = create_article(title, category, content)
        flash(f"✅ 已建立文章: {path}")
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
