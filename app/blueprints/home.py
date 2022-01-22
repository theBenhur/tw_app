from app.models import Movie,Profile,Serie
from flask import Blueprint,request,render_template
from flask_login.utils import current_user,login_required

home_bp=Blueprint('home',__name__)

@home_bp.route('/')
@login_required
def home():
    profile=request.args.get('profile')
    profiles=Profile.query.filter_by(user_id=current_user.id)
    current_profile=profiles[0] if profile is None \
        else Profile.query.filter_by(profile_name=profile).filter(Profile.user_id == current_user.id).first()
    
    if current_profile is None:
        return render_template('inside/profile_not_found.html',title='HOME',profiles=profiles)

    movies=Movie.query.filter_by(rate_id=current_profile.rate_id)
    series=Serie.query.filter_by(id_rate=current_profile.rate_id)

    return render_template('inside/home.html',
        title='HOME',
        current_profile=current_profile,
        profiles=profiles,
        movies=movies,
        series=series)