import os
from flask import Blueprint, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from models import Actor, Movie, setup_db, cast
from auth import *

bp = Blueprint('movies', __name__)

@bp.route('/movies')
# @requires_auth('get:movies')
def get_movies(token=''):
    # selection = Movie.query.order_by(Movie.id).all()
    # current_movies = paginate_items(request, selection, Movie)

    # if (len(current_movies) == 0):
    #     abort(404)

    # return jsonify({
    #     'success': True,
    #     'movies': current_movies,
    #     'total_movies': len(selection),
    # })
    return 'movies'

# @app.route('/movies', methods=['POST'])
# @requires_auth('post:movies')
# def create_movie(token):
#     body = request.get_json()
#     new_name = body.get('name', None)
#     new_release = body.get('release_date', None)
#     new_actors = body.get('actors', None)
#     actor_list = []

#     for actor in new_actors:
#         new = Actor.query.filter(Actor.name == actor).first()
#         if new is None:
#             abort(404)
#         actor_list.append(new)

#     try:
#         entry = Movie(name=new_name, release_date=new_release,
#                         actors=actor_list)
#         entry.insert()

#         return jsonify({
#             'success': True,
#             'created': entry.id,
#             'total_actors': len(Movie.query.all())
#         })

#     except Exception as ex:
#         print(ex)
#         abort(422)

# @app.route('/movies/<int:movie_id>', methods=['DELETE'])
# @requires_auth('delete:movie')
# def delete_movie(token, movie_id):
#     try:
#         # Later, add feature to warn user about deleting permanently
#         movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
#         movie.actors = []
#         db.session.commit()

#         if movie is None:
#             # print('error')
#             abort(404)

#         movie.delete()

#         return jsonify({
#             'success': True,
#             'deleted': movie_id,
#             'total_movies': len(Movie.query.all())
#         })

#     except Exception as ex:
#         # print(ex)
#         abort(422)

# @app.route('/movies/<int:movie_id>', methods=['PATCH'])
# @requires_auth('patch:movie')
# def edit_movie(token, movie_id):
#     body = request.get_json()
#     new_actors = body.get('actors')
#     try:
#         movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
#         if movie is None:
#             abort(404)

#         if 'name' in body:
#             movie.name = body.get('name')
#         if 'actors' in body:
#             current_actors = []
#         for instance in new_actors:
#             a = Actor.query.filter(Actor.name == instance).first()
#             current_actors.append(a)

#         movie.actors = current_actors

#         if 'release_date' in body:
#             movie.release_date = int(body.get('release_date'))
#         movie.update()

#         return jsonify({
#             'success': True,
#             'edited': movie_id,
#                         'total_movies': len(Movie.query.all())
#         })

#     except Exception as ex:
#         print(ex)
#         abort(422)
