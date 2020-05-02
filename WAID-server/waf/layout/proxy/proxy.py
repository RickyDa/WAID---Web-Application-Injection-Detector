############################################################
from flask import request
############################################################
from waf import app, log
from waf.logic import waidAI
from waf.logic.proxy_flows import Flows

############################################################
flows = Flows(waidAI)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def send_receive(path):
    log.info(f"Getting request - {request} from - {request.remote_addr}")
    return flows.main_flow(request, path)
