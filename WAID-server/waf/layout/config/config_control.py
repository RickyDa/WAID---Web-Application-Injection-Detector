from flask_jwt_extended import jwt_required

from waf import app
from waf import config
from flask import jsonify, Response, request


@app.route('/conf/get_all', methods=['GET'])
@jwt_required
def get_config():
    return jsonify(config.get_all_web())


@app.route('/conf/setall', methods=['POST'])
@jwt_required
def set_all_conf():
    return config.set_all_conf(request.get_json())
