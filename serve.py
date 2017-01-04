#!/usr/bin/env python3

import argparse

from gevent.wsgi import WSGIServer
from zoom import app

parser = argparse.ArgumentParser(
            description='Run the Zoom link shortener webserver.')
parser.add_argument('--port', default=80, type=int,
                    help='The port to serve on.')
args = parser.parse_args()

http_server = WSGIServer(('', args.port), app)
http_server.serve_forever()
