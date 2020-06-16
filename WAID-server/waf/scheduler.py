from apscheduler.schedulers.background import BackgroundScheduler

from waf.dal.rule_dao import read_all_rules_json, get_all_rules_by_time_delta
from waf.layout.rule.rule_control import upload_db, download_db
from waf import config
from waf.logic.mail_handler import update_rules_mail
import requests

sched = BackgroundScheduler()


@sched.scheduled_job('cron', id='server_task', hour=2, minute=00)
def scheduled_upload_db():
    if config.get_value('is_client', 'True') == 'False':
        upload_db()
        update_rules_mail(get_all_rules_by_time_delta(dt=2))


@sched.scheduled_job('cron', id='client_task_collect', hour=0)  # every 00:00 clients will send their rules to the server
def scheduled_db_collection():
    if config.get_value('is_client', 'True') == 'True':
        SERVER_ADDRESS = config.get_value('server_ip', '') + '/rule/collect'
        response = requests.post(url=SERVER_ADDRESS, json=read_all_rules_json())


@sched.scheduled_job('cron', id='client_task_update', hour=4,
                     minute=00)  # every 04:00 clients will download the updated db
def scheduled_db_update():
    if config.get_value('is_client', 'True') == 'True':
        download_db()
