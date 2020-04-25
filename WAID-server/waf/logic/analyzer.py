import re
import urllib
from urllib.parse import urlparse
from waf import log
import waf.dal.rule_dao as rd


def analyze(payload):
    rules = rd.read_all_rules()
    flag = False
    for key, val in payload.inspected_value.items():
        if key == 'url':
            flag = inspect(preprocess(val), rules)
        else:
            flag = inspect(val, rules)
        if flag:
            return flag
    log.info(f"Analyzer result for payload - '{payload.inspected_value.items()}' is {flag}")
    return flag


def inspect(value, rules):
    for rule in rules:
        r = re.compile(rule.rule)
        if r.search(value):
            return True
    return False


def preprocess(url):
    return urllib.parse.urlparse(urllib.parse.unquote(url)).query.replace(" ", "")
