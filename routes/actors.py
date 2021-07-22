from flask import Blueprint
from CastingHeroku.auth import * 
from flask import request, abort, jsonify
# from database.models.actor import Actor
# from database.models.movie import Movie
# from database.main import db
from CastingHeroku.utilities import paginate_items

bp = Blueprint("actors", __name__)

@bp.route('/actors', methods=['GET'])
# @requires_auth('get:actors')
def get_actors(token=''):
    # selection = Actor.query.order_by(Actor.id).all()
    # current_actors = paginate_items(request, selection, Actor)

    # if (len(current_actors) == 0):
    #     abort(404)

    # return jsonify({
    #     'success': True,
    #     'actors': current_actors,
    #     'total_actors': len(selection),
    # })
    return 'actors'

# @bp.route('/actors', methods=['POST'])
# @requires_auth('post:actor')
# def create_actor(token):
#     body = request.get_json()
#     new_name = body.get('name', None)
#     new_age = body.get('age', None)
#     new_gender = body.get('gender', None)
#     new_movies = body.get('movies', None)

#     movie_list = []

#     for movie in new_movies:
#         new = Movie.query.filter(Movie.name == movie).one_or_none()
#         if new is None:
#             abort(404)
#         movie_list.append(new)

#     try:
#         entry = Actor(name=new_name, age=new_age, gender=new_gender,
#                         movies=movie_list)
#         entry.insert()

#         return jsonify({
#             'success': True,
#             'created': entry.id,
#                         'total_actors': len(Actor.query.all())
#         })

#     except Exception as ex:
#         print(ex)
#         abort(422)

# @bp.route('/actors/<int:actor_id>', methods=['DELETE'])
# @requires_auth('delete:actor')
# def delete_actor(token, actor_id):
#     try:
#         # Later, add feature to warn user about deleting permanently
#         actor = Actor.query.get(actor_id)
#         actor.movies = []
#         db.session.commit()

#         if actor is None:
#             # print('error')
#             abort(404)

#         actor.delete()

#         return jsonify({
#             'success': True,
#             'deleted': actor_id,
#                         'total_actors': len(Actor.query.all())
#         })

#     except Exception as ex:
#         # print(ex)
#         abort(422)

# @bp.route('/actors/<int:actor_id>', methods=['PATCH'])
# @requires_auth('patch:actor')
# def edit_actor(token, actor_id):
#     body = request.get_json()
#     try:
#         actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
#         new_movies = body.get('movies')
#         if actor is None:
#             abort(404)

#         if 'name' in body:
#             actor.name = body.get('name', None)
#         if 'movies' in body:
#             current_movies = []
#         for instance in new_movies:
#             m = Movie.query.filter(Movie.name == instance).first()
#             current_movies.bpend(m)

#         actor.movie = current_movies
#         if 'age' in body:
#             actor.age = int(body.get('age'))
#         actor.update()

#         return jsonify({
#             'success': True,
#             'edited': actor_id,
#             'total_actors': len(Actor.query.all())
#             })

#     except Exception as ex:
#         # print(ex)
#         abort(422)