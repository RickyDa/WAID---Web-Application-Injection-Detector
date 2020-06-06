##################################################
from flask import request, jsonify, Response
##################################################
from flask_jwt_extended import jwt_required
import json
from waf import app, log
from waf.layout.rule.rule_boundary import RulePayload, parse_rule
from waf.logic import rule_service

import boto3
from botocore.exceptions import ClientError


##################################################


@app.route('/rule/addrule', methods=['POST'])
def create_rule():
    log.info(f"Adding Rule - {request} ")
    rv = rule_service.create(parse_rule(request))
    return jsonify(RulePayload(rv.id, rv.rule, rv.type, rv.action).serialize())


@app.route('/rule/getall', methods=['GET'])
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


@app.route('/rule/upload', methods=['POST'])
def upload_db():
    s3_client = boto3.client(
        's3',
        # TODO: add to config file the aws credtials and give the user the option to edit it.
        aws_access_key_id='AKIAJ72EHZL77N3Q2JTQ',
        aws_secret_access_key='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')
    try:
        # TODO: Add to config the path of the db file to be uploaded
        s3_client.upload_file(
            'C:/Users/ricky/Desktop/WAID/WAID---Web-Application-Injection-Detector/WAID-server/waf/logic/models/waid-model.h5',
            'waid-db', 'waid-model.h5')
        # TODO: Log the status after the uploading a file
        return Response(status=200)
    except ClientError as e:
        # TODO: Log the status after the uploading a file
        print(e)
        return Response(status=500)


@app.route('/rule/collect', methods=['POST'])
def collect_rules():
    rules = rule_service.add_rules(request.json)
    return Response(status=200)
