# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250),unique = True, nullable = False)
    author = db.Column(db.String(250),nullable = False)
    rating = db.Column(db.Integer, nullable = False)



db.create_all()

book1 = Book(title = "Sins of the father", author = "Jeffrey Archer", rating = 4)
# db.session.add(book1)
# db.session.commit()

all = db.session.query(Book).all()

book = Book.query.filter_by(title="Sins of the father").first()

print(all)
print(book.id)