from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'

class InfoForm(FlaskForm):
    instrument = StringField("Welk instrument wil je graag leren bespelen?")
    Submit = SubmitField("verzend")
    naam = "Abraham"

@app.route("/", methods=['GET', 'POST'])
def index():
    # render de template home.html
    form = InfoForm()
    # haal de data voor instrumenten uit het formulier
    if form.validate_on_submit():
        instrument = form.instrument.data
        form.instrument.data = ''
    return render_template("index.html", form=form, instrument=instrument) 
