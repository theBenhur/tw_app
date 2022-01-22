from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
login=LoginManager(app)
from app.blueprints.profiles import router
from app.blueprints.images import images
from app.blueprints.users import users
from app.blueprints.auth import auth_bp
from app.blueprints.home import home_bp
from app.blueprints.search import search_bp
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp,url_prefix='/home')
app.register_blueprint(router,url_prefix='/profiles')
app.register_blueprint(images,url_prefix='/images')
app.register_blueprint(users,url_prefix='/users')
app.register_blueprint(search_bp,url_prefix='/search')
from app import routes,models,router