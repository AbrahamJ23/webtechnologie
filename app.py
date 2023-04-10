from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'


class InfoForm(FlaskForm):
    check_in = StringField()
    instrument = StringField("Welk instrument wil je graag leren bespelen?")
    Submit = SubmitField("verzend")
    naam = "Abraham"

@app.route("/", methods=['GET', 'POST'])
def index():
    instrument = False
    # render de template home.html
    form = InfoForm()
    # haal de data voor instrumenten uit het formulier
    if form.validate_on_submit():
        instrument = form.instrument.data
        form.instrument.data = ''
    return render_template("index.html", form=form, instrument=instrument) 

@app.route("/test", methods=['GET', 'POST'])
def test():
    check_in=False
    if request.method == "POST":
        check_in = request.form.get("checkin")
    return render_template("hotel-html-template/index.html", check_in=check_in)



if __name__ == "__main__":
    app.run(debug=True)
