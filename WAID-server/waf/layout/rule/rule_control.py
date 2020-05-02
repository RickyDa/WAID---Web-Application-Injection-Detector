##################################################
from flask import request, jsonify, Response
##################################################
from flask_jwt_extended import jwt_required

from waf import app, log
from waf.layout.rule.rule_boundary import RulePayload, parse_rule
from waf.logic import rule_service

##################################################


@app.route('/rule/addrule', methods=['POST'])
@jwt_required
def create_rule():
    log.info(f"Adding Rule - {request} ")
    rv = rule_service.create(parse_rule(request))
    return jsonify(RulePayload(rv.id, rv.rule, rv.type, rv.action).serialize())


@app.route('/rule/getall', methods=['GET'])
@jwt_required
def get_all_rules():
    return jsonify(rule_service.get_all_rules())


@app.route('/rule/delete/<rule_id>', methods=['DELETE'])
@jwt_required
def delete_rule_by_id(rule_id):
    is_deleted = rule_service.delete_rule_by_id(rule_id)
    if is_deleted:
        return Response(status=200)
    else:
        return Response(status=500)


@app.route('/rule/update/<rule_id>', methods=['PUT'])
@jwt_required
def update_rule_by_id(rule_id):
    is_updated = rule_service.update_rule_by_id(rule_id, request.get_json())
    if is_updated:
        return Response(status=200)
    else:
        return Response(status=500)


