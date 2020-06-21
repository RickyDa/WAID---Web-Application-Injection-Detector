##################################################
from flask import request, jsonify, Response
##################################################
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, \
    get_jwt_identity

from waf.layout.user.user_boundary import parse_user, UserPayload
from waf.logic import user_service
from waf import app, log


##################################################


@app.route('/user/adduser', methods=['POST'])
@jwt_required
def add_user():
    log.info(f"adding new user- {request.get_json().values()}")
    user = user_service.create(parse_user(request))
    if user:
        return jsonify(UserPayload(id=user.id, username=user.username, role=user.role).serialize())
    else:
        return Response(status=409, response="User already exist")


@app.route('/user/getall', methods=['GET'])
@jwt_required
def get_all_users():
    return jsonify(user_service.get_all())


@app.route('/user/delete/<user_id>', methods=['DELETE'])
@jwt_required
def delete_user_by_id(user_id):
    is_deleted = user_service.delete_user_by_id(user_id)
    if is_deleted:
        return Response(status=200)
    else:
        return Response(status=500)


@app.route('/user/update/<user_id>', methods=['PUT'])
@jwt_required
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
        user_payload = jsonify(
            UserPayload(id=user.id, mail=user.mail, username=user.username, role=user.role).serialize())
        return user_payload
    else:
        return Response(status=500)


@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    ''' refresh token endpoint '''
    current_user = get_jwt_identity()
    ret = {
            'token': create_access_token(identity=current_user)
    }
    return jsonify({'ok': True, 'data': ret}), 200
