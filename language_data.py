from app.models import Language
from app import db
languages=[]
s=Language(language='ESPAÑOL')
languages.append(s)
s=Language(language='INGLES')
languages.append(s)
s=Language(language='ALEMAN')
languages.append(s)
s=Language(language='JAPONES')
languages.append(s)

for l in languages:
    db.session.add(l)
db.session.commit()