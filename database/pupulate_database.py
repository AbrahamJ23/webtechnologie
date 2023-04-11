from models import db, Gasten, Reservering, Huisjes, app

app.app_context().push()
db.create_all()
# Maak 2 gebruikers aan
abraham = Gasten('Abraham', 'vsvp.ambla', 'welkom123')
emmanuel = Gasten('Emmanuel', 'XxEmmanueljxX', 'welkom123')

db.session.add_all([abraham, emmanuel])
db.session.commit()

print(Gasten.query.all())

# add huisjes
bungelow1 = Huisjes("bungelow_1", 6)
bungelow2 = Huisjes("bungelow_2", 8)
bungelow3 = Huisjes("bungelow_3", 4)

db.session.add_all([bungelow1, bungelow2, bungelow3])
db.session.commit()