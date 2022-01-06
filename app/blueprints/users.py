from flask  import Blueprint,request,jsonify
from app.models import User

users=Blueprint('users',__name__)

@users.route('/<username>')
def exists_user(username):
    if User.query.filter_by(username=username).first() is None:
        return jsonify({'message':'Valid username'}),404
    return jsonify({'message':'The username is already taken'}),200