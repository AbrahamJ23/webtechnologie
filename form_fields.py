from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                                  RadioField, SelectField, TextField,
                                  TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'

class InfoForm(FlaskForm):

    naam = StringField('Wat is je naam?',validators=[DataRequired()])
    vrouw  = BooleanField("Ben je een vrouw?")
    instrument = RadioField('Welk instrument wil je leren bespelen?',   choices=[('ins_een','Gitaar'),('ins_twee','Drums')])
    plaats = SelectField(u'Welke locatie heeft de voorkeur?',
             choices=[('as', 'Assen'), ('dr', 'Drachten'), ('gr', 'Groningen')])
    feedback = TextAreaField()
    submit = SubmitField('Verzend')

@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():

        session['naam'] = form.naam.data
        session['vrouw'] = form.vrouw.data
        session['instrument'] = form.instrument.data
        session['plaats'] = form.plaats.data
        session['feedback'] = form.feedback.data

        return redirect(url_for("bedankt"))


    return render_template('home1.html', form=form)

@app.route('/bedankt')
def bedankt():
    return render_template('bedankt.html')

if __name__ == '__main__':
    app.run(debug=True)