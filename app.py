from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'


class InfoForm(FlaskForm):
    check_in = DateField()
    check_out = DateField()
    huisje = SelectField(u'Welk huisje?', choices=[('Huis 1','4 personen'), ('Huis 2', '6 Personen'), ('Huis 3', '8 Personen')])
    submit = SubmitField('Verzend')

@app.route("/", methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['check_in'] = form.check_in.data
        session['check_out'] = form.check_out.data
        session['huisje'] = form.huisje.data

        return redirect(url_for('bedankt'))
    
    return render_template("home.html", form=form) 

@app.route("/bedankt")
def bedankt():
    return render_template("bedankt.html")



if __name__ == "__main__":
    app.run(debug=True)





# @app.route("/", methods=['GET', 'POST'])
# def index():
#     instrument = False
#     # render de template home.html
#     form = InfoForm()
#     # haal de data voor instrumenten uit het formulier
#     if form.validate_on_submit():
#         instrument = form.instrument.data
#         form.instrument.data = ''
#     return render_template("home.html", form=form, instrument=instrument) 
