# from flask import Flask, request, redirect, Response
# import requests
#
# app = Flask(__name__)
# SITE_NAME = 'http://www.ynet.co.il'
#
#
# @app.route('/', methods=['GET', 'POST', 'DELETE'])
# def proxy():
#     global SITE_NAME
#     excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
#
#      if request.method == 'GET':
#         resp = requests.get(f'{SITE_NAME}')
#     elif request.method == 'POST':
#         resp = requests.post(f'{SITE_NAME}', json=request.get_json())
#
#     headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
#     response = Response(resp.content, resp.status_code, headers)
#     return response
#
#
# if __name__ == '__main__':
#     app.run(debug=False, port=3000)
