#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from uuid import uuid4
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["SECRET_KEY"] = str(uuid4())
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*/": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('API_HOST')
    port = environ.get('API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, debug=True, threaded=True)
