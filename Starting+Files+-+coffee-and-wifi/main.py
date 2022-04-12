from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafeLocation = StringField("Cafe Location", validators=[DataRequired(), URL()])
    openTime = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    closeTime = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffeeRating = SelectField(u"Coffee Rating", choices = [("☕","☕"),("☕☕","☕ ☕"), ("☕☕☕","☕☕☕"), ("☕☕☕☕","☕☕☕☕")], validators=[DataRequired()])
    wifiRating = SelectField(u"Wifi Strength Rating", choices = [("✘","✘"),("💪","💪"),("💪💪","💪💪"),("💪💪💪","💪💪💪"),("💪💪💪💪","💪💪💪💪")], validators=[DataRequired()])
    powerAvailability = SelectField(u"Power Socket Availability", choices = [("✘","✘"),("🔌","🔌"),("🔌🔌","🔌🔌"),("🔌🔌🔌","🔌🔌🔌"),("🔌🔌🔌🔌","🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods = ["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv","a", encoding="utf-8", newline= "") as csv_file:
            write_csv = csv.writer(csv_file, delimiter = ",")
            write_csv.writerow([form.cafe.data, form.cafeLocation.data, form.openTime.data, form.closeTime.data, form.coffeeRating.data, form.wifiRating.data, form.powerAvailability.data ])
        return render_template('add.html', form=form, formSubmitted=True)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form, formSubmitted = False)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding = 'utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        next(csv_data,None)
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
