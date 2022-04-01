from flask import Flask, render_template
from post import Post

app = Flask(__name__)
p = Post()


@app.route("/")
def home():
    posts = p.get_all()
    return render_template("index.html", posts = posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/posts/<index>")
def get_posts(index):
    b = p.get_blog_post(int(index))
    print(b)
    if b is not None:
        return render_template("post.html", post=b)
    return render_template("post.html", post={"title": "", "body": ""})

if __name__=='__main__':
    app.run(debug=True)

