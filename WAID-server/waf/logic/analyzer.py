import re
import urllib
from urllib.parse import urlparse
from waf import log
import waf.logic.rule_service as rs
from waf.database.enums import RuleType, Action
from waf.database.models import Rule


def analyze(payload):
    if validate_host(payload):
        return True
    elif validate_payload(payload):
        rs.create(Rule(rule=payload.srcIP, type=RuleType.BLOCKED_HOST.value, action=Action.BLOCK.value))
        return True
    return False


def validate_host(payload):
    hosts = rs.get_all_rules_by_type(RuleType.BLOCKED_HOST.value)
    srcIP = payload.srcIP
    flag = False

    for host in hosts:
        flag = True if host.rule == srcIP and host.action == Action.BLOCK.value else False
        if flag:
            break

    log.info(f"Analyzer result for payload [srcIP] - '{payload.srcIP}' is {flag}")
    return flag


def validate_payload(payload):
    rules = rs.get_all_rules_by_type(RuleType.INJECTION_ATTACK.value)
    flag = False
    for key, val in payload.inspected_value.items():
        if key == 'url':
            flag = inspect_payload_values(parse(val), rules)
        else:
            flag = inspect_payload_values(val, rules)
        if flag:
            break
    log.info(f"Analyzer result for payload [values]- '{payload.inspected_value.items()}' is {flag}")
    return flag


def inspect_payload_values(value, rules):
    for rule in rules:
        r = re.compile(rule.rule)
        if r.search(value):
            return True
    return False


def parse(url):
    return urllib.parse.urlparse(urllib.parse.unquote(url)).query.replace(" ", "")
