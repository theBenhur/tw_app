from flask import Blueprint,request,jsonify
from flask.templating import render_template
from app.models import Movie, Rate, Serie

search_bp=Blueprint('search',__name__)

@search_bp.route('/')
def search():
    rates=Rate.query.all()
    return render_template('inside/search.html',title='SEARCH MOVIE',rates=rates)

@search_bp.route('/content')
def search_by_name():
    content_name=request.args.get('cn')
    rate=request.args.get('r')
    movies=Movie.query.filter(Movie.movie_name.like('{}%'.format(content_name))) \
        .filter(Movie.rate_id == rate)
    series=Serie.query.filter(Serie.serie_name.like('{}%'.format(content_name))) \
        .filter(Serie.id_rate == rate)
    return jsonify(movies=[m.serialize for m in movies],series=[s.serialze for s in series])