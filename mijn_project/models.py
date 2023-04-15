import os
from flask import Flask
from mijn_project.authentication import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Koppelt de Flask-applicatie met database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

 

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.Text)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, email, naam, username, password):
        self.email = email
        self.naam = naam
        self.username = username
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
    def __repr__(self):
        return f"Gast {self.naam} heeft de username {self.username}"
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
class Huisjes(db.Model):
    __tablename__ = 'huisjes'

    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.Text, unique=True, nullable=False)
    type = db.Column(db.Integer, nullable=False)

    def __init__(self, naam, type):
        self.naam = naam
        self.type = type


class Reservering(db.Model):
    __tablename__ = 'reservering'

    id = db.Column(db.Integer, primary_key=True)
    huisje_id = db.Column(db.Integer, db.ForeignKey('huisjes.id'))
    username_id = db.Column(db.Text, db.ForeignKey('users.id'))
    checkin = db.Column(db.DateTime)
    checkout = db.Column(db.DateTime)


    def __init__(self, huisje_id, username_id, checkin, checkout):
        self.huisje_id = huisje_id
        self.username_id = username_id
        self.checkin = checkin
        self.checkout = checkout


with app.app_context():
    db.create_all()