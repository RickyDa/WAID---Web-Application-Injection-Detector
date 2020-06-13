##################################################
from flask import request, jsonify, Response
##################################################
from flask_jwt_extended import jwt_required
from waf import app, log, config
from waf.layout.rule.rule_boundary import RulePayload, parse_rule
from waf.logic import rule_service

from pathlib import Path
import boto3
from botocore.exceptions import ClientError


##################################################


@app.route('/rule/addrule', methods=['POST'])
def create_rule():
    log.info(f"Adding Rule - {request} ")
    rv = rule_service.create(parse_rule(request))
    print(rule_service.get_rules_of_today())
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


base_path = Path(__file__).parent
db_path = (base_path / "./database/server.db")


@app.route('/rule/upload', methods=['POST'])
def upload_db():
    s3_client = boto3.client(
        's3',
        aws_access_key_id=config.get_value('aws_access_key_id', ''),
        aws_secret_access_key=config.get_value('aws_secret_access_key', ''))
    try:
        response = s3_client.upload_file(db_path, 'waid-db', 'server.db')
        log.info(f'Database uploaded{response}')
        return Response(status=200)
    except ClientError as e:
        log.debug(e)
        return Response(status=500)


@app.route('/rule/download', methods=['GET'])
def download_db():
    s3 = boto3.client(
        's3',
        aws_access_key_id=config.get_value('aws_access_key_id', ''),
        aws_secret_access_key=config.get_value('aws_secret_access_key', ''))
    try:
        response = s3.download_file('waid-db', 'server.db', db_path)
        log.info(f'Database Downloaded{response}')
        return Response(status=200)
    except ClientError as e:
        log.debug(e)
        return Response(status=500)


@app.route('/rule/collect', methods=['POST'])
def collect_rules():
    rules = rule_service.add_rules(request.json)
    log.info(f'Rules Collected -- Size: {len(request.json)} From : {request.remote_addr}')
    return Response(status=200)
