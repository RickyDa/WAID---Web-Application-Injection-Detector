import waf.dal.payload_dao as dao
from waf.database.models import AnomalyStatus


def create_payload_request(payload):
    dao.create(payload)


def create_payload_response(payload):
    dao.create(payload)


def get_unchecked():
    return dao.read_by_anomaly_status(AnomalyStatus.UNCHECKED)


def set_anomaly_type(payload, status):
    return dao.set_anomaly_type(payload, status)
