from app.models import Plan
from app import db  
plans=[]
A=Plan(plan_name='BASIC')
plans.append(A)
B=Plan(plan_name='STANDARD')
plans.append(B)
C=Plan(plan_name='PREMIUM')

for Plan in plans:
    db.session.add(Plan)
db.session.commit()