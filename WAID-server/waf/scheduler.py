from apscheduler.schedulers.background import BackgroundScheduler

from waf.dal.rule_dao import read_all_rules_json, create_rule
from waf.layout.rule.rule_control import upload_db
from waf import config
import requests

sched = BackgroundScheduler()


##################################################
# TODO : arrange functions to server or client define the which functions needed according to the system's mode
#   -Add emailaing function After uploading the server DB file to s3
#   -Change the path on upload_db function to the correct db file.
#   -Notice there are other tasks on upload_db
##################################################


@sched.scheduled_job('cron', id='server_task', hour=2, minute=00)
def scheduled_upload_db():
    if config.get_value('is_client', 'True') == 'False':
        upload_db()
    # TODO : email Update to the admins after task is done


@sched.scheduled_job('cron', id='client_task_collect')  # every 00:00 clients will send their rules to the server
def scheduled_db_collection():
    if config.get_value('is_client', 'True') == 'True':
        SERVER_ADDRESS = config.get_value('server_ip', '') + '/rule/collect'
        response = requests.post(url=SERVER_ADDRESS, json=read_all_rules_json())


@sched.scheduled_job('cron', id='client_task_update')  # every 00:00 clients will send their rules to the server
def scheduled_db_update():
    if config.get_value('is_client', 'True') == 'True':
        # TODO: add method to download updated server.db file from s3
        # download_db()
        pass
