    # @app.errorhandler(AuthError)
    # def auth_error(e):
    #     response = jsonify(e.error)
    #     response.status_code = e.status_code
    #     return response

    # @app.errorhandler(400)
    # def bad_request(error):
    #     return jsonify({
    #         'success': False,
    #         'error': 400,
    #         'message': 'bad request'
    #     }), 400

    # @app.errorhandler(401)
    # def unauthorized(error):
    #     return jsonify({
    #         'success': False,
    #         'error': 401,
    #         'message': 'Unauthorized'
    #     }), 401

    # @app.errorhandler(403)
    # def forbidden(error):
    #     return jsonify({
    #         'success': False,
    #         'error': 403,
    #         'message': 'Forbidden'
    #     }), 403

    # @app.errorhandler(404)
    # def not_found(error):
    #     return jsonify({
    #         'success': False,
    #         'error': 404,
    #         'message': 'resource not found'
    #     }), 404

    # @app.errorhandler(405)
    # def not_allowed(error):
    #     return jsonify({
    #         'success': False,
    #         'error': 405,
    #         'message': 'method not allowed'
    #     }), 405

    # @app.errorhandler(422)
    # def unprocessable(error):
    #     return jsonify({
    #         'success': False,
    #         'message': 'unprocessable'
    #     }), 422