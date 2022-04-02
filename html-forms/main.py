from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def submit():
    if request.method=="POST":
        print(request.form.get("username"))
        print(request.form.get("pwd"))
        user = request.form.get("username")
        pwd = request.form.get("pwd")
    return "<h1>Username: " + user + " password: " + pwd + "</h1>"


if __name__=="__main__":
    app.run(debug=True)