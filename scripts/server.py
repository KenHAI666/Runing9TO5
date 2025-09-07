from scripts import web2jekyll

filename = web2jekyll.create_markdown(title, category, content)

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        categories = request.form.getlist("categories")  # 可多選
        content = request.form["content"]
        
        filename = web2jekyll.create_markdown(title, categories, content)
        return f"文章已儲存: {filename}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
