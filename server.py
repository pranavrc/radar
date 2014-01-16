#!/usr/bin/env python

from flask import Flask, request, Response, render_template
import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer

gevent.monkey.patch_all()
app = Flask(__name__)

def event_stream():
    while True:
        gevent.sleep(2)
        yield 'data: %s\n\n' % 'foo'

@app.route('/stream')
def sse_request():
    return Response(event_stream(), mimetype='text/event-stream')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        print request.form('position');

if __name__ == "__main__":
    #http_server = WSGIServer(('127.0.0.1', 8000), app)
    #http_server.serve_forever()
    app.debug = True
    app.run()
