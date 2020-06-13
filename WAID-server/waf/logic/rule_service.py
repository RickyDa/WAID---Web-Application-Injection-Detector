from typing import List, Dict

import waf.dal.rule_dao as dao
from waf import log
from waf.database.enums import RuleType
import datetime
from waf.database.models import Rule


def create(rule):
    log.info(
        f"Created Rule {rule.rule} as "
        f"{'BLOCKED_HOST' if rule.type == RuleType.BLOCKED_HOST.value else 'INJECTION_ATTACK'}"
        f" on Rule Table")
    return dao.create_rule([rule])[0]


def get_all_rules():
    return dao.read_all_rules_json()


def delete_rule_by_id(rule_id):
    return dao.delete_rule_by_id(rule_id)


def update_rule_by_id(rule_id, new_rule):
    return dao.update_rule_by_id(rule_id, new_rule)


def get_all_rules_by_type(type_):
    return dao.read_rules_by_type(type_)


def add_rules(new_rules):
    rules = dao.read_all_rules()
    new_rules = rules_to_obj(new_rules)
    rules = [item for item in new_rules if item not in rules]
    return dao.create_rule(rules)


def rules_to_obj(j_rules):
    rules = []
    for rule in j_rules:
        rules.append(Rule(rule=rule['rule'], type=rule['type'], action=rule['action'],
                          date_created=datetime.datetime.strptime(rule['date_created'], '%Y-%m-%dT%H:%M:%S.%f')))
    return rules


def get_rules_of_today():
    return dao.get_all_rules_by_time_delta(dt=2)
