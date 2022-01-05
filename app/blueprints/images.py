from flask import Blueprint,send_from_directory
from flask_login import login_required
from config import Config

images_router=Blueprint('images',__name__)
@images_router.route('/<image>')
def return_image(image):
    return send_from_directory(Config.UPLOAD_FOLDER,image)
