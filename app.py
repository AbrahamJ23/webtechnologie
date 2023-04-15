import os
from flask_login import LoginManager, login_user, login_required, logout_user
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from mijn_project.models import app, db, Reservering, User
from mijn_project.forms import LoginForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            template_folder='mijn_project/templates/',
            static_folder="mijn_project/static")

app.config['SECRET_KEY'] = 'mijngeheimesleutel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mijn_project/data.sqlite')

db.init_app(app)


class InfoForm(FlaskForm):
    check_in = DateField(render_kw={"autocomplete": "off"})
    check_out = DateField(render_kw={"autocomplete": "off"})
    huisje = SelectField(u'Welk huisje?', choices=[('Huis 1','4 personen'), ('Huis 2', '6 Personen'), ('Huis 3', '8 Personen')], render_kw={"autocomplete": "off"})
    submit = SubmitField('Verzend', render_kw={"autocomplete": "off"})

@app.route("/", methods=['POST', 'GET'])
def index():
    form = InfoForm()

    # Hier wordt gecontroleerd of er op submet is geklikt en 

    if form.validate_on_submit():
        username = "test"
        check_in = form.check_in.data
        check_out = form.check_out.data
        huisjes = form.huisje.data
        
        # Voeg de form data in database
        reservering = Reservering(huisjes, username, check_in, check_out)
        db.session.add(reservering)
        db.session.commit()
        db.create_all()
       
    return render_template("home.html", form=form) 

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Succesvol ingelogd")

    # next = request.args.get("next")
    # if next == None or not next[0] == "/":
    #     next = url_for("bedankt")
    #     return redirect(next)
    return render_template("login.html", form=form)



@app.route("/bedankt")
def bedankt():

    return render_template("bedankt.html")

@app.route("/info")
@login_required
def info():
    return render_template("contact.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Je bent uitgelogd!")
    return redirect(url_for("home.html"))


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
