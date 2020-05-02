from flask_jwt_extended import create_access_token, create_refresh_token

from waf.database.models import User


class UserPayload:

    def __init__(self, id=None, username=None, mail=None, role=None):
        self.id = id
        self.username = username
        self.mail = mail
        self.role = role

    def serialize(self):
        return {"id": self.id,
                "email": self.mail,
                "username": self.username,
                "role": self.role,
                "access_token": create_access_token(identity=self.username),
                "refresh_token": create_refresh_token(identity=self.username)
                }


def parse_user(payload):
    username, password, mail, role = payload.get_json().values()
    return User(username=username, password=password, mail=mail, role=role)
