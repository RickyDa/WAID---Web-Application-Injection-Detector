import waf.dal.rule_dao as dao
from waf import log
from waf.database.enums import RuleType


def create(rule):
    log.info(
        f"Created Rule {rule.rule} as "
        f"{'BLOCKED_HOST' if rule.type == RuleType.BLOCKED_HOST.value else 'INJECTION_ATTACK'}"
        f" on Rule Table")
    return dao.create_rule(rule)


def get_all_rules():
    return dao.read_all_rules_json()


def delete_rule_by_id(rule_id):
    return dao.delete_rule_by_id(rule_id)


def update_rule_by_id(rule_id, new_rule):
    return dao.update_rule_by_id(rule_id, new_rule)


def get_all_rules_by_type(type_):
    return dao.read_rules_by_type(type_)
