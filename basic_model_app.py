import os
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

with app.app_context():
    print(current_app.name)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
        
class Gasten(db.Model):
    # __tablename__ = 'gasten'
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.Text)
    username = db.Column(db.Text, unique=True)
    # password = db.Column(db.Text)

    def __init__(self, naam, username):
        self.naam = naam
        self.username = username
        
    
    def __repr__(self):
        return f"Gast {self.naam} heeft de username {self.username}"
    
        

