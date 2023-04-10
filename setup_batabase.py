from basic_model_app import db, Gasten


db.create_all

abraham = Gasten("abraham", "vsvp_ambla")
emmanuel = Gasten("emmanuel", "EmmanuelJ23")

db.session.add(abraham)
db.session.commit()
