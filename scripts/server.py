from flask import Flask, render_template, request
import web2jekyll

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        # 從表單取得字串，然後用逗號分隔成列表
        categories_str = request.form["categories"]
        categories = [c.strip() for c in categories_str.split(',')]
        content = request.form["content"]
        
        # 呼叫 web2jekyll 中的 create_post 函式
        filename = web2jekyll.create_post(title, categories, content)
        
        return f"文章已儲存: {filename}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
