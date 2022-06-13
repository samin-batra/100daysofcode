from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, IntegerField, validators
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
Bootstrap(app)
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class MovieEditForm(FlaskForm):
    rating = IntegerField('Rating', [validators.DataRequired()])
    review = StringField('Review', [validators.DataRequired()])
    submit = SubmitField('Submit')


class MovieAddForm(FlaskForm):
    title = StringField('Movie Title', [validators.DataRequired()])
    submit = SubmitField("Add Movie")

db.create_all()

movie = Movie(title="Rush",year = 2013, description = "This movie is about the rivalry between James Hunt and Niki Lauda and revolves around the 1976 F1 World Championship.", rating = 5, ranking = 100, review = "Great movie!", img_url = "")
# db.session.add(movie)
# db.session.commit()


@app.route("/")
def home():
    movie = db.session.query(Movie).all()

    return render_template("index.html", movies = movie)


@app.route("/edit/<id>", methods = ["GET","POST"])
def edit(id):
    movieEdit = MovieEditForm()
    if movieEdit.validate_on_submit():
        movie = Movie.query.get(int(id))
        movie.rating = movieEdit.rating.data
        movie.review = movieEdit.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form = movieEdit)


@app.route('/delete/<id>', methods = ["GET"])
def delete(id):
    movie_delete = Movie.query.get(id)
    db.session.delete(movie_delete)
    db.session.commit()
    return redirect("/")


@app.route('/add', methods = ["GET","POST"])
def add():
    form = MovieAddForm()
    return render_template("add.html", form = form)


if __name__ == '__main__':
    app.run(debug=True)
