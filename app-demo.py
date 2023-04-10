
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
    instrument = False
    # render de template home.html
    form = InfoForm()
    # haal de data voor instrumenten uit het formulier
    if form.validate_on_submit():
        instrument = form.instrument.data
        form.instrument.data = ''
    return render_template("index.html", form=form, instrument=instrument) 

@app.route("/informatie")
def info():
    #render de template informatie
    return "<h1>Dit hebben we jou te bieden</h1>"

@app.route("/random_pagina/<naam>")
def random_pagina(naam):
    return f"gebruiker: {naam}" + f"<h1> Dit is de pagina van {naam}"

@app.route("/cursist/<naam>")
def cursist(naam):
    form = InfoForm()
    test = ["voetbal", "Dansen", "tennis"]
    return render_template("index.html", naam=naam, test=test)

if __name__ == "__main__":
    app.run(debug=True)
# form gedeelte werkt nog niet!