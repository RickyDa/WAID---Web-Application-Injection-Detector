from waf import ma
from waf.database.models import Payload, Rule,User


class PayloadSchema(ma.ModelSchema):
    class Meta:
        model = Payload


class RuleSchema(ma.ModelSchema):
    class Meta:
        model = Rule


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
