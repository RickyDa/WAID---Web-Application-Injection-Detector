import waf.dal.rule_dao as dao


def create(rule):
    return dao.create_rule(rule)


def get_all_rules():
    return dao.read_all_rules_json()



def delete_rule_by_id(rule_id):
    return dao.delete_rule_by_id(rule_id)


def update_rule_by_id(rule_id, new_rule):
    return dao.update_rule_by_id(rule_id, new_rule)