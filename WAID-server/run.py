from waf import app, config
import argparse


def argparser():
    parser = argparse.ArgumentParser(description='Determine if Client or Server mode')
    parser.add_argument('--server', action='store_true', default=False)
    parser.add_argument('--client', action='store_true', default=False)
    return parser


if __name__ == '__main__':
    parser = argparser()
    args = parser.parse_args()
    if args.client:
        threaded = False
        config.set_value("is_client", True)
    else:
        threaded = True
        config.set_value("is_client", False)

    app.run(debug=True, host='0.0.0.0', use_reloader=False, ssl_context=('cert.pem', 'key.pem'),
            threaded=threaded)

''''
LAYERS:

controller - pass http to the destination, pass http to service(Business logic)
Business logic - maps the http request to an object of the db
dal - commit Request entity to the db
db - save the entity


'''
