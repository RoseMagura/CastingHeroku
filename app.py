from flask import Flask, jsonify
from routes import actors
from routes import movies

app = Flask(__name__)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(actors.bp)
    app.register_blueprint(movies.bp)

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
