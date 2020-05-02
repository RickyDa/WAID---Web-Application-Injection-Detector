from flask_jwt_extended import jwt_required

from waf import app
from waf import config
from flask import jsonify, Response, request


@app.route('/conf/get_all', methods=['GET'])
@jwt_required
def get_config():
    return jsonify(config.get_all_web())


@app.route('/conf/set_is_client', methods=['POST'])
@jwt_required
def set_is_client():
    response = config.set_value("is_client", request.get_json()["is_client"])
    return Response(status=200) if response else Response(status=500)


@app.route('/conf/set_server_ip', methods=['POST'])
@jwt_required
def set_server_ip():
    response = config.set_value("server_ip", request.get_json()["server_ip"])
    return Response(status=200) if response else Response(status=500)


@app.route('/conf/set_is_active', methods=['POST'])
@jwt_required
def set_is_waf_active():
    response = config.set_value("is_active", request.get_json()["is_active"])
    return Response(status=200) if response else Response(status=500)


@app.route('/conf/set_is_analyzer', methods=['POST'])
@jwt_required
def set_is_analyzer():
    response = config.set_value("is_analyzer", request.get_json()["is_analyzer"])
    return Response(status=200) if response else Response(status=500)


@app.route('/conf/set_is_classifier', methods=['POST'])
@jwt_required
def set_is_classifier():
    response = config.set_value("is_classifier", request.get_json()["is_classifier"])
    return Response(status=200) if response else Response(status=500)


@app.route('/conf/set_site_address', methods=['POST'])
@jwt_required
def set_site_address():
    response = config.set_value("site_address", request.get_json()["site_address"])
    return Response(status=200) if response else Response(status=500)
