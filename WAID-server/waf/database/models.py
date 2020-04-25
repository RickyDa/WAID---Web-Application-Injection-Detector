from datetime import datetime

from waf import db
from waf.database.enums import AnomalyStatus, Action

'''
By creating a class that inherits from the db.model 
it will create a table of this class
with the fields as the cols.
'''

'''
Payload Table:
this table stores all of the http traffic activity in the proxy
'''


class Payload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headers = db.Column(db.Text(), nullable=False)
    url = db.Column(db.Text(), nullable=True)
    body = db.Column(db.Text(), nullable=True)
    inspected_value = db.Column(db.JSON, nullable=True)
    anomaly_status = db.Column(db.Integer, nullable=False, default=AnomalyStatus.UNCHECKED.value)
    payload_type = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"Payload('{self.id}', Headers - {self.headers}, Type - {self.anomaly_status} , Body - {self.body}" \
               f"' Payload type - {self.payload_type})"


class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule = db.Column(db.Text(), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    action = db.Column(db.Integer, nullable=False, default=Action.ALLOW.value)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"Rule(Rule ID:{self.id}'," \
               f"Rule - {self.rule}'," \
               f"Type - '{self.type}'," \
               f"Action - {self.action}'," \
               f"Created : - {self.date_created})"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    salt = db.Column(db.LargeBinary, nullable=False)
    mail = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"User(User ID:{self.id}'," \
               f"Username - {self.username}'," \
               f"Password - '{self.password}'," \
               f"Role - {self.role}'," \
               f"Created : - {self.date_created})"
