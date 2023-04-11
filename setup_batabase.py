from basic_model_app import db, Gasten, app 

app.app_context().push()

db.create_all()

abraham = Gasten("abraham", "vsvp_ambla")
emmanuel = Gasten("emmanuel", "EmmanuelJ23")

db.session.add_all([abraham, emmanuel])
db.session.commit()
