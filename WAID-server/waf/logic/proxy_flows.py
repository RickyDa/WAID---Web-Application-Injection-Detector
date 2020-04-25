############################################################
from flask import Response
from requests import request as send_request
############################################################
from waf import log, config
from waf.database.models import AnomalyStatus
from waf.layout.proxy.payload_handler import parse_payload
from waf.logic import payloadService, analyzer


############################################################


class Flows:
    def __init__(self, classifier):
        self.classifier = classifier
        self.site_name = config.get_value('site_address', 'https://redtiger.labs.overthewire.org/')
        self.request = ''
        self.path = ''

    def main_flow(self, request, path):
        self.request = request
        self.path = path

        if not config.get_value('is_active', False) != 'False':
            return self._response()

        payload = parse_payload(self.request)

        if config.get_value('is_client', True) == 'True':
            return self._client_flow(payload)
        else:
            return self._server_flow(payload)

    def _response(self):
        data = self.request.data if self.request.content_type == 'application/json' else self.request.form
        response = send_request(self.request.method,
                                f'{self.site_name}{self.path}?{self.request.query_string.decode("utf8")}',
                                data=data)
        return Response(response.content, status=response.status_code, content_type=response.headers['content-type'])

    def _client_flow(self, payload):
        if analyzer.analyze(payload):
            return Response(status=403)
        else:
            return self._response()

    def _server_flow(self, payload):
        is_analyzer = config.get_value('is_analyzer', 'True')
        is_classifier = config.get_value('is_classifier', 'True')
        log.info(f"Server Mode, Classifier is {'ON' if is_classifier else 'OFF'} "
                 f"and Analyzer is {'ON' if is_classifier else 'OFF'}")
        if is_analyzer:
            self._use_analyzer(payload)
        if is_classifier and payload.anomaly_status != AnomalyStatus.ATTACK.value:
            self._use_classifier(payload)

        payloadService.create_payload_request(payload)

        if payload.anomaly_status == AnomalyStatus.ATTACK.value:
            return Response(status=403)
        else:
            return self._response()

    @staticmethod
    def _use_analyzer(payload):
        if analyzer.analyze(payload):
            payload.anomaly_status = AnomalyStatus.ATTACK.value

    def _use_classifier(self, payload):
        if self.classifier.predict(payload):
            payload.anomaly_status = AnomalyStatus.ATTACK.value
