from flask import Flask, jsonify
from .tests import test


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.register_blueprint(test, url_prefix="/")

    # @app.route('/home', methods=['GET'])
    # def home():
    #     return jsonify({'message': 'hello'}), 200

    return app
