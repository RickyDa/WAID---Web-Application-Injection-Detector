from waf import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=False, ssl_context=('cert.pem', 'key.pem'), threaded=True)

''''
LAYERS:

controller - pass http to the destination, pass http to service(Business logic)
Business logic - maps the http request to an object of the db
dal - commit Request entity to the db
db - save the entity


'''
