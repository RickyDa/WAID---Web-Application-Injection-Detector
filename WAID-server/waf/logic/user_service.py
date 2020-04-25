import waf.dal.user_dao as dao
import re


def create(user):
    is_exist = get_by_mail(user.mail)
    if not is_exist:
        return dao.create_user(user)
    return None


def get(user_id):
    return dao.get_user_by_id(user_id)


def get_all():
    return dao.get_all()


def get_by_mail(user_mail):
    return dao.get_user_by_mail(user_mail)


def delete_user_by_id(user_id):
    return dao.delete_user_by_id(user_id)


def update_user_by_id(user_id, new_user):
    return dao.update_user_by_id(user_id, new_user)


def login(user):
    return dao.login(user)
