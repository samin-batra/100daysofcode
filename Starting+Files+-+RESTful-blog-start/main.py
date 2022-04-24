from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(),URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    print(posts)
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)
    # for blog_post in posts:
    #     if blog_post["id"] == index:
    #         requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods = ["GET","POST"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        try:
            post = BlogPost()
            post.date = datetime.datetime.now().strftime("%d %B, %Y")
            post.body = form.body.data
            post.title = form.title.data
            post.author = form.author.data
            post.img_url = form.img_url.data
            post.subtitle = form.subtitle.data
            db.session.add(post)
            db.session.commit()
            return redirect("/")

        except:
            return "There was an error inserting the blog post"
            return redirect("/")

    return render_template("make-post.html", form=form, is_edit = False)


@app.route("/edit-post/<int:post_id>",methods = ["GET","POST"])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    print(post.title)
    form =  CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        post.body = form.body.data
        post.subtitle = form.subtitle.data
        db.session.commit()
        return redirect("/")
    return render_template("make-post.html", form=form, is_edit = True)


@app.route("/delete-post/<int:post_id>")
def delete_post(post_id):
    try:
        blog = BlogPost.query.get(post_id)
        db.session.delete(blog)
        db.session.commit()
        return redirect("/")
    except:
        return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug = True)