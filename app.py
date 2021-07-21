from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from database.models import Actor, Movie, setup_db, cast
from auth import *
from routes import actors
# from routes.movies import movies

app = Flask(__name__)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    # setup_db(app)

    app.register_blueprint(actors.bp)
    # app.register_blueprint(movies.bp)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, DELETE')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    @app.route('/', methods=['GET'])
    def health():
        return jsonify('healthy')
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
