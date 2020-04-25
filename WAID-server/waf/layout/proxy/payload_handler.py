import json

from waf.database.models import Payload
from waf.database.enums import PayloadType, AnomalyStatus


def parse_payload(payload):
    headers = str(payload.headers)
    url = payload.url
    body = decode(payload.data)
    payload_type = PayloadType.REQUEST_GET if payload.method == 'GET' else PayloadType.REQUEST_POST

    if payload.method == 'POST':
        value_to_inspect = {"form": list(payload.form.to_dict().values()), "data": decode(payload.data)}
    else:  # "GET"
        value_to_inspect = {"url": f'{payload.path}?{decode(payload.query_string)}'}
    return Payload(headers=headers,
                   url=url,
                   body=body,
                   inspected_value=value_to_inspect,
                   anomaly_status=AnomalyStatus.NORM.value,
                   payload_type=payload_type.value)


def decode(input_):
    return input_.decode("utf8")
