from flask import jsonify

from waf import db
from waf.database.models import Payload
from waf.database.schemas import PayloadSchema


def create(payload):
    db.session.add(payload)
    db.session.commit()
    return payload


def read_by_anomaly_status(status):
    request_schema = PayloadSchema(many=True)
    return jsonify(request_schema.dump(obj=Payload.query.filter_by(anomaly_status=status.value)))


def set_anomaly_type(payload, status):
    payload.anomaly_status = status.value
    db.session.commit()
    return payload
