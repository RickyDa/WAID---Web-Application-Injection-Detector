import hashlib
import os

from flask import jsonify

from waf import db, log
from waf.database.models import User
from waf.database.schemas import UserSchema


def create_user(user):
    user.salt, user.password = hash_password(user)
    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_by_mail(user_mail):
    return User.query.filter_by(mail=user_mail).first()


def get_all():
    user_schema = UserSchema(many=True)
    return user_schema.dump(obj=User.query.with_entities(User.id, User.username, User.mail, User.role).all())


def delete_user_by_id(user_id):
    user = get_user_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    else:
        return False


def hash_password(user):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', user.password.encode('utf-8'), salt, 100000)
    return salt, key


def update_user_by_id(user_id, new_user):
    user = get_user_by_id(user_id)
    update_user(user, new_user)
    db.session.commit()
    return user


def update_user(user, new_user):
    if user.username != new_user.get("username"):
        user.username = new_user.get("username")
    if user.mail != new_user.get("email"):
        user.mail = new_user.get("email")
    if user.role != new_user.get("role"):
        user.role = new_user.get("role")


def login(user):
    db_user = get_user_by_mail(user.get("email"))
    if db_user:
        key = hashlib.pbkdf2_hmac('sha256', user.get("password").encode('utf-8'), db_user.salt, 100000)
        is_same_key = key == db_user.password
        if is_same_key:
            return True, db_user
        else:
            log.info(f"Password didnt match DB password for user - `{user.get('email')}`")
            return False
    log.info(f"No user with the mail `{user.get('email')}` in the DB ")
    return False
