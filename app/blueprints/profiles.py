from app import db 
from app.models import Language, Plan,Profile,Rate,User
from flask_login import current_user,login_required
from flask import Blueprint,render_template,request,redirect,url_for

router=Blueprint('profiles',__name__)

@router.route('/')
@login_required
def profiles():
    profiles=Profile.query.filter_by(user_id=current_user.id)
    return render_template('profiles_list.html',title="HOME",profiles=profiles)

@router.route('/create',methods=['GET','POST'])
@login_required
def create_profile():
    if request.method == 'GET':
        return render_template('create_profile.html',title='CREATE A NEW PROFILE')
    if request.method == 'POST':
        profile_name=request.form['profile_name']
        new_profile=Profile(user_id=current_user.id,profile_name=profile_name)
        db.session.add(new_profile)
        db.session.commit()
        return redirect(url_for('profiles.profiles'))

@router.route('/<id>',methods=['GET'])
@login_required
def profile_by_id(id):
    profile_data=Profile.query.get(int(id))
    language=Language.query.get(profile_data.language_id).language
    languages=Language.query.all()
    plan=Plan.query.get(int(User.query.get(int(current_user.id)).plan_id))
    # rate=Rate.query.get(profile_data.rate_id).letter
    return render_template('inside/profile_data.html',profile=profile_data,
            language=language,languages=languages,plan=plan)

@router.route('/add',methods=['GET','POST'])
@login_required
def add_profile():
    if request.method == 'GET':
        return render_template('inside/add_profile.html',title='ADD PROFILE')
    