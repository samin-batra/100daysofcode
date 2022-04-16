from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3



app = Flask(__name__)


# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250),unique = True, nullable = False)
    author = db.Column(db.String(250),nullable = False)
    rating = db.Column(db.Integer, nullable = False)


db.create_all()


all_books = []


@app.route('/')
def home():
    all = db.session.query(Book).all()
    print(all)
    return render_template("index.html",books=all)
    # pass


@app.route('/edit/<id>', methods = ["GET","POST"])
def edit(id):
    if request.method=="GET":
        return render_template("edit.html")
    elif request.method=="POST":
        print(type(id))
        book = Book.query.get(int(id))
        book.rating = request.form.get('rating')
        db.session.commit()
        return redirect("/")


@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method=="GET":
        return render_template("add.html")
    elif request.method=="POST":
        print(request.form)
        book = Book(title = request.form.get("book_name"), author = request.form.get("author"), rating = request.form.get("rating"))
        # all_books.append(request.form)
        db.session.add(book)
        db.session.commit()
        # print(all_books)
        return redirect("/")


@app.route("/delete/<id>", methods = ["GET","POST"])
def delete(id):
    to_delete = Book.query.get(id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)

