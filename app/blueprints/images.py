from flask import Blueprint,send_from_directory
from flask_login import login_required
from config import Config

images=Blueprint('images',__name__)
@images.route('/profile/<image>')
def profile_img(image):
    return send_from_directory(Config.UPLOAD_FOLDER,image)
@images.route('/movie/<image>')
def movie_img(image):
    return send_from_directory('{}/movies'.format(Config.IMGS_FOLDER),image)
@images.route('/serie/<image>')
def serie_img(image):
    return send_from_directory('{}/series'.format(Config.IMGS_FOLDER),image)