from flask import Blueprint,url_for,redirect,render_template,request,jsonify
from flask_login.utils import current_user,login_user,login_required,logout_user
from app.models import User,Profile,Plan,Language
from app import db

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/',methods=['GET','POST'])
def log_in():
    if current_user.is_active:
        return redirect(url_for('home'))
    if request.method == 'GET':
        return render_template('outside/login.html',title="LOGIN")
    if request.method == 'POST':
        body=request.get_json()
        if body['username'] != '':
            user=User.query.filter_by(username=body['username']).first()
            if user is None or not user.check_password(body['password']): #if user exists
                return jsonify({'message':'Wrong data'}),404
            login_user(user,remember=False)
            return jsonify({'message':'All ok'}),200
        return jsonify({'message':'You must provide an username'}),404

@auth_bp.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method == 'GET':
        plans=Plan.query.all()
        languages=Language.query.all()
        return render_template('outside/sign_up.html',title="SIGNUP",
            plans=plans, languages=languages)
    if request.method == 'POST':
        body=request.get_json()
        username=body['username']
        if User.query.filter_by(username=username).first() is None:
            email=body['email']
            password=body['password']
            plan_id=body['plan']
            new_user=User(username=username,email=email,plan_id=plan_id)
            new_user.set_password(password=password)
            db.session.add(new_user)
            db.session.commit()
            new_profile=Profile(user_id=new_user.id,profile_name=username,
                language_id=body['language'],rate_id=1)
            db.session.add(new_profile)
            db.session.commit()
            return jsonify({'message':'User created'}),201
        return jsonify({'message':'Username already taken'}),200

@auth_bp.route('/log_out')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('auth.log_in'))