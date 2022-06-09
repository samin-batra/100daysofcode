from random import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    cafes = db.session.query(Cafe).all()
    cafe_list = [cafe.to_dict() for cafe in cafes]
    print(cafe_list)

    return render_template("index.html",cafes=cafe_list)


@app.route("/random")
def random_record():

    cafes = db.session.query(Cafe).all()
    rand_cafe = random.choice(cafes)
    return jsonify(id = rand_cafe.id, name = rand_cafe.name, url = rand_cafe.map_url,
                   img_url = rand_cafe.img_url, loc = rand_cafe.location,
                   seats = rand_cafe.seats, has_toilet = rand_cafe.has_toilet,
                   has_wifi = rand_cafe.has_wifi, sockets = rand_cafe.has_sockets,
                   calls = rand_cafe.can_take_calls, price = rand_cafe.coffee_price)


@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    cafe_list = [cafe.to_dict() for cafe in cafes]
    print(cafe_list)
    return jsonify(cafe_list)


@app.route("/search")
def search_cafe():
    loc = request.args.get("location")
    cafes = db.session.query(Cafe).filter_by(location=loc)
    cafe_list = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafe_list)




@app.route("/add", methods = ["GET","POST"])
def add_cafe():
    if request.method=="GET":
        return render_template("add.html")
    if request.method=="POST":
        print(request.form)
        try:
            cafe = Cafe(name=request.form.get('name'), map_url=request.form.get('map_url'),img_url= request.form.get('img_url'),
                        location=request.form.get('location'),seats= request.form.get('seats'),
                        has_toilet = bool(request.form.get('has_toilet')),
                        has_wifi = bool(request.form.get('has_wifi')), has_sockets = bool(request.form.get('has_sockets')),
                        can_take_calls = bool(request.form.get('can_take_calls')), coffee_price = request.form.get('coffee_price'))
            db.session.add(cafe)
            db.session.commit()
            return "Record has been added successfully."
        except:
            return "Sorry, there was an error! Please try again later"


@app.route("/update_cafe/<id>",methods = ["PATCH"])
def update_cafe(id):
    try:
        price = request.args.get("new_price")
        print(price)
        cafe = db.session.query(Cafe).filter_by(id=id).first()
        print(cafe.name)
        cafe.coffee_price = price
        db.session.commit()
        return jsonify(response = {"Success":"Request is successful!"}), 200
    except AttributeError:
        return jsonify(error={"Not Found":"Request was not successful as the cafe does not exist."}), 404




## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record
@app.route("/delete_cafe/<cafe_id>",methods = ["DELETE"])
def delete_cafe(cafe_id):
    print(cafe_id)
    if request.args.get("api-key")=="TOPSECRETAPIKEY":
        try:
            cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response = {"Success": "The cafe has been deleted successfully."}), 200
        except AttributeError:
            return jsonify(error = {"Not found": "The cafe does not exist."}), 404
    else:
        return jsonify(error={"Unauthorized": "You're not authorized to make this request."}), 403


if __name__ == '__main__':
    app.run(debug=True)
