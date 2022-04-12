from flask import Flask, render_template
from datetime import date
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    d = date.today()
    year = d.year

    return render_template("index.html",year = year)

@app.route("/guess/<name>")
def guess(name):
    age_res = requests.get("https://api.agify.io/?name="+name)
    age = json.loads(age_res.text)
    print(age)

    gender_res = requests.get("https://api.genderize.io/?name="+name)
    gender = json.loads(gender_res.text)
    print(gender)
    print(gender)
    d = date.today()
    year = d.year

    return render_template("index.html",name=name,gender=gender['gender'],age=age['age'],year=year)


@app.route("/blog")
def get_blog():
    api_endpoint = "https://api.npoint.io/e99299dc2a4450416132"
    res = requests.get(api_endpoint)
    # print(res.text)
    all_posts = res.json()
    print(all_posts)
    return render_template("blog.html",blog = all_posts)


if __name__ == "__main__":
    app.run(debug = True)