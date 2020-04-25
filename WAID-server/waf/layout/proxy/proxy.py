############################################################
from flask import request
############################################################
from waf import app, log
from waf.logic import classi
from waf.logic.proxy_flows import Flows

############################################################
flows = Flows(classi)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def send_receive(path):
    log.info(f"Getting request - {request}")
    return flows.main_flow(request, path)
