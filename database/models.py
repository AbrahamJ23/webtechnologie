import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Koppelt de Flask-applicatie met database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Gasten(db.Model):
    __tablename__ = 'gasten'

    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.Text)
    username = db.Column(db.String(14), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, naam, username, password):
        self.naam = naam
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f"Gast {self.naam} heeft de username {self.username}"
    
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
    username_id = db.Column(db.Text, db.ForeignKey('gasten.id'))
    datum = db.Column(db.DateTime)

    def __init__(self, huisje_id, username_id, datum):
        self.huisje_id = huisje_id
        self.username_id = username_id
        self.datum = datum
    


