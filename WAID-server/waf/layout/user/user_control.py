##################################################
from flask import request, jsonify, Response
##################################################
from waf.layout.user.user_boundary import parse_user, UserPayload
from waf.logic import user_service
from waf import app, log


##################################################


@app.route('/user/adduser', methods=['POST'])
def add_user():
    log.info(f"adding new user- {request.get_json().values()}")
    user = user_service.create(parse_user(request))
    if user:
        return jsonify(UserPayload(id=user.id, username=user.username, role=user.role).serialize())
    else:
        return Response(status=409, response="User already exist")


@app.route('/user/getall', methods=['GET'])
def get_all_users():
    return jsonify(user_service.get_all())


@app.route('/user/delete/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    is_deleted = user_service.delete_user_by_id(user_id)
    if is_deleted:
        return Response(status=200)
    else:
        return Response(status=500)


@app.route('/user/update/<user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    is_updated = user_service.update_user_by_id(user_id, request.get_json())
    if is_updated:
        return Response(status=200)
    else:
        return Response(status=500)


@app.route('/user/login', methods=['POST'])
def login():
    is_auth, user = user_service.login(request.get_json())
    if is_auth:
        return jsonify(UserPayload(id=user.id, mail=user.mail, username=user.username, role=user.role).serialize())
    else:
        return Response(status=500)
