from waf.database.models import Rule


class RulePayload:

    def __init__(self, id=None, rule=None, type_=None, action=None):
        self.id = id
        self.rule = rule
        self.type_ = type_
        self.action = action

    def serialize(self):
        return {"id": self.id,
                "rule": self.rule,
                "type_": self.type_,
                "action": self.action}


def parse_rule(payload):
    rule, type_, action = payload.get_json().values()
    return Rule(rule=rule, type=type_, action=action)
