import os
from typing import TypeGuard
from config import Config
from app import db 
from app.models import Language, Plan,Profile,Rate,User
from flask_login import current_user,login_required
from flask import Blueprint,render_template,request,redirect,url_for,jsonify,abort

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
        languages=Language.query.all()
        return render_template('inside/add_profile.html',title='CREATE A NEW PROFILE',languages=languages)
    if request.method == 'POST':
        # body=request.get_json()
        profilename=request.form['profilename']
        profile=Profile.query.filter_by(profile_name=profilename).first()#.filter(Profile.user_id == current_user.id)
        if not profile is None:
            return jsonify({'message':'The profile name is already taken'}),200
        language=request.form['language']
        image=request.files['image']
        if image.filename != '':
            extension=image.filename.split('.')[1]
            if extension in ['jpg','png']:
                new_profile=Profile(profile_name=profilename,user_id=current_user.id,
                    language_id=language,img_path=image.filename)
                try:
                    image.save(os.path.join(
                        os.path.join('app',Config.UPLOAD_FOLDER),
                        image.filename
                    ))
                except FileNotFoundError:
                    print("Error")
                db.session.add(new_profile)
                db.session.commit()
                return jsonify({'message':'New profile created'}),201

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
    plan=Plan.query.get(int(User.query.get(int(current_user.id)).plan_id)).plan_name
    # rate=Rate.query.get(profile_data.rate_id).letter
    return render_template('inside/profile_data.html',profile=profile_data,
            language=language,languages=languages,plan=plan)

@router.route('/update/<id>',methods=['GET','POST','PUT'])
def update_profile(id):
    if request.method == 'GET':
        profile=Profile.query.filter_by(id=id).first()
        if profile is None:
            return abort(404)
        return jsonify({'profile_name':profile.profile_name,'language':profile.language_id}),200
    
    if request.method == 'POST':
        # body=request.get_json()
        # print(request.data)
        # print(request.get_json(force=True))
        print(request.form['profilename'])
        profilename=request.form['profilename']
        language=request.form['language']
        profile=Profile.query.filter_by(id=id).first()
        profile.profile_name=profilename
        profile.language_id=language
        image=request.files['image']
        if image.filename != '':
            name,extension=image.filename.split('.')
            if extension in ['jpg','png']:
                profile.img_path=image.filename
                try:
                    image.save(os.path.join(
                        os.path.join('app',Config.UPLOAD_FOLDER)
                        ,image.filename))
                except FileNotFoundError:
                    print(os.path.join(Config.UPLOAD_FOLDER,image.filename),'did not exists')
        db.session.commit()
        db.session.close()
        return jsonify({'message':'User updated'}),203

@router.route('/delete/<id>',methods=['DELETE'])
def delete_profile(id):
    profile=Profile.query.get(int(id))
    db.session.delete(profile)
    db.session.commit()
    return jsonify({'message':'User successfull deleted'}),200