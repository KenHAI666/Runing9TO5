from flask import Flask, render_template, request, redirect, url_for
from scripts.web2jekyll import create_post

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        categories = request.form.get("categories").split(",")  # 可輸入多個分類
        content = request.form.get("content")

        filename = create_post(title, categories, content)
        return f"文章已生成
