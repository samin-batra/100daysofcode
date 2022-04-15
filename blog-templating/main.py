from flask import Flask, render_template
from post import Post

app = Flask(__name__)
p = Post()


@app.route('/')
def home():
    posts = p.get_all()
    return render_template("index.html",posts = posts)

@app.route('/post/<index>')
def read_blog(index):
    b = p.get_blog_post(int(index))
    if b is not None:
        return render_template("post.html",post = b)
    return render_template("post.html",post = {"title":"","body":""})


if __name__ == "__main__":
    app.run(debug=True)
