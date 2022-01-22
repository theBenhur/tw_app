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

class Movie(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    movie_name=db.Column(db.String(64),unique=True)
    length=db.Column(db.String(32))
    movie_img_path=db.Column(db.String(128))
    rate_id=db.Column(db.Integer,db.ForeignKey('rate.id'))
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id':self.id,
           'movie_name':self.movie_name,
           'legth':self.length,
           'movie_img_path':self.movie_img_path,
           'rate_id':self.rate_id
       }
class Serie(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    serie_name=db.Column(db.String(64),unique=True)
    length=db.Column(db.String(32))
    chapter_number=db.Column(db.Integer)
    serie_img_path=db.Column(db.String(128))
    id_rate=db.Column(db.Integer,db.ForeignKey('rate.id'))
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id':self.id,
           'serie_name':self.serie_name,
           'legth':self.length,
           'serie_img_path':self.serie_img_path,
           'rate_id':self.id_rate,
           'chapter_number':self.chapter_number
       }
class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    profile_name=db.Column(db.String(64),unique=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    language_id=db.Column(db.Integer,db.ForeignKey('language.id'))
    rate_id=db.Column(db.Integer,db.ForeignKey('rate.id'))
    img_path=db.Column(db.String(128),default='default.jpg')
    def __repr__(self) -> str:
        return '{} - {}'.format(self.user_id,self.profile_name)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))