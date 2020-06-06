from waf import ma
from waf.database.models import Payload, Rule, User


class PayloadSchema(ma.Schema):
    class Meta:
        fields = ("id", "srcIP", "headers", "url", "body", "inspected_value", "anomaly_status", "payload_type")


class RuleSchema(ma.Schema):
    class Meta:
        fields = ("id", "rule", "type", "action", "date_created")


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "password", "action", "role")
