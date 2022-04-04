from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField(label = 'Email', validators=[DataRequired(),Email(message="Email is required!")])
    password = PasswordField(label = 'Password', validators=[DataRequired(),Length(min = 8, message = "Password must be at least 8 characters.")])
    submitField = SubmitField(label='Log In', validators = [])


app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login",methods = ["GET","POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        if form.email.data=="admin@email.com" and form.password.data=="12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html",form=form)


if __name__ == '__main__':
    app.run(debug=True)