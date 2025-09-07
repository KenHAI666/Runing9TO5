from flask import Flask, render_template, request, redirect, url_for
import subprocess
from web2jekyll import create_post

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new_post():
    title = request.form["title"]
    category = request.form["category"]
    content = request.form["content"]

    filename = create_post(title, category, content)

    # 自動提交到 GitHub
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"新增文章：{title}"])
    subprocess.run(["git", "push", "origin", "main"])

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
