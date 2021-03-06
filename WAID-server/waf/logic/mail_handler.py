from flask_mail import Message
from waf import mail, config
import datetime

from waf.dal.user_dao import get_users_mails
from waf.database.models import Rule


def __send_mail(subject, recipients, text):
    recp = parse_recipients(recipients)
    msg = Message(subject,
                  sender=str(config.get_value("mail", "waidwaf@gmail.com")),
                  recipients=recp)
    msg.body = text
    mail.send(msg)


def parse_recipients(recipients):
    return [str(r.mail) for r in recipients]


def __prepare_rules(rules: Rule):
    text = ''
    counter = 1
    for rule in rules:
        text += f"{counter}. Rule -'{rule.rule}' Type-'{rule.type}' Action-'{rule.action}\n"
        counter += 1
    return text


def update_rules_mail(rules):
    date = datetime.date.today() - datetime.timedelta(days=1)
    subject = f"New Rules for {str(date)}"
    recipients = get_users_mails()

    text = "New rules - \n" + __prepare_rules(rules)
    __send_mail(subject, recipients, text)
