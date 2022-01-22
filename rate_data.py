from app.models import Rate
from app import db  
rates=[]
A=Rate(letter='A')
rates.append(A)
B=Rate(letter='B')
rates.append(B)
C=Rate(letter='C')
rates.append(C)
D=Rate(letter='D')
rates.append(D)

for rate in rates:
    db.session.add(rate)
db.session.commit()