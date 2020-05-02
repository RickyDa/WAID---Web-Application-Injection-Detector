from flask import jsonify

from waf import db
from waf.database.models import Rule
from waf.database.schemas import RuleSchema


def create_rule(rule):
    db.session.add(rule)
    db.session.commit()
    return rule


def read_all_rules_json():
    rule_schema = RuleSchema(many=True)
    return rule_schema.dump(obj=Rule.query.all())


def read_all_rules():
    return Rule.query.all()


def read_rule_by_id(identifier):
    return Rule.query.filter_by(id=identifier).first()


def delete_rule_by_id(rule_id):
    rule = read_rule_by_id(rule_id)
    if rule:
        db.session.delete(rule)
        db.session.commit()
        return True
    else:
        return False


def update_rule_by_id(rule_id, new_rule):
    rule = read_rule_by_id(rule_id)
    update_rule(rule, new_rule)
    db.session.commit()
    return rule


def update_rule(rule, new_rule):
    if rule.rule != new_rule.get("rule"):
        rule.rule = new_rule.get("rule")
    if rule.action != new_rule.get("action"):
        rule.action = new_rule.get("action")
    if rule.type != new_rule.get("type"):
        rule.type = new_rule.get("type")


def read_rules_by_type(type_):
    return Rule.query.filter_by(type=type_).all()
