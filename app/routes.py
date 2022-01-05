from flask_login.utils import login_required,login_user,logout_user,current_user
from flask_migrate import current
from werkzeug.utils import redirect
from app import app,db
from flask import request,url_for,Response,jsonify
from app.models import Plan, User,Profile,Rate,Language
from flask.templating import render_template

@app.route('/log_in',methods=['GET','POST'])
def log_in():
    if current_user.is_active:
        return redirect(url_for('home'))
    if request.method == 'GET':
        return render_template('outside/login.html',title="LOGIN")
    if request.method == 'POST':
        user=request.get_json()
        if user['username'] != '':
            user=User.query.filter_by(username=user['username']).first()
            if user is None or not user.check_password(user['password']): #if user exists
                return jsonify({'message':'Wrong data'}),404
            login_user(user,remember=False)
            return redirect(url_for('home'))
        return jsonify({'message':'You must provide an username'}),404

@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method == 'GET':
        plans=Plan.query.all()
        languages=Language.query.all()
        return render_template('sign_up.html',title="SIGNUP",
            plans=plans, languages=languages)
    if request.method == 'POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        plan_id=request.form['plan']
        new_user=User(username=username,email=email,plan_id=plan_id)
        new_user.set_password(password=password)
        db.session.add(new_user)
        db.session.commit()
        new_profile=Profile(user_id=new_user.id,profile_name=username,
            language_id=request.form['language'])
        db.session.add(new_profile)
        db.session.commit()
        return redirect(url_for('log_in'))

@app.route('/home')
@login_required
def home():
    profile=request.args.get('profile')
    # profiles=None
    # current_profile_info=None
    if profile is None:
        profiles=Profile.query.filter_by(user_id=current_user.id)
        current_profile=profiles[0]
        print('None {}'.format(current_profile))
    if not profile is None:
        profiles=Profile.query.filter_by(user_id=current_user.id)
        current_profile=Profile.query.filter_by(profile_name=profile).filter(Profile.user_id == current_user.id).first()
        print('Not None {}'.format(current_profile))

    return render_template('inside/home.html',title='HOME',current_profile=current_profile,profiles=profiles)
    
# @app.route('/profiles/create',methods=['GET','POST'])
# def create_profile():
#     if request.method == 'GET':
#         return render_template('create_profile.html',title='CREATE A NEW PROFILE')
#     if request.method == 'POST':
#         profile_name=request.form['profile_name']
#         new_profile=Profile(user_id=current_user.id,profile_name=profile_name)
#         db.session.add(new_profile)
#         db.session.commit()
#         return redirect(url_for('profiles'))

# @app.route('/profiles')
# def profiles():
#     profiles=Profile.query.filter_by(user_id=current_user.id)
#     return render_template('profiles_list.html',title="HOME",profiles=profiles)

# @app.route('/profiles/<int id>')
# def profile_by_id():
#     return render_template('profile_by_id.html',title="PROFILE BY ID")

@app.route('/log_out')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('log_in'))