from enum import unique
from app import db,login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
        
class Language(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    language=db.Column(db.String(64),unique=True)
    def __repr__(self) -> str:
        return '{} - {}'.format(self.id,self.language)
class Rate(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    letter=db.Column(db.String(32),unique=True)
    def __repr__(self) -> str:
        return '{} - {}'.format(self.id,self.letter)
class Plan(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    plan_name=db.Column(db.String(64),unique=True)
    def __repr__(self) -> str:
        return '{} - {}'.format(self.id,self.plan_name)

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(64),unique=True)
    password=db.Column(db.String(128))
    plan_id=db.Column(db.Integer,db.ForeignKey('plan.id'))
    def set_password(self,password):
        self.password=generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password,password) 
    def __repr__(self) -> str:
        return '{} - {}'.format(self.id,self.username)
        
class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    profile_name=db.Column(db.String(64),unique=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    language_id=db.Column(db.Integer,db.ForeignKey('language.id'))
    img_path=db.Column(db.String(128),default='/img_profile/default.jpg')
    def __repr__(self) -> str:
        return '{} - {}'.format(self.user_id,self.profile_name)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))