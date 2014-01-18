import os
import gevent
import redis.connection

redis.connection.socket = gevent.socket
os.environ.update(DJANGO_SETTINGS_MODULE = 'radar.settings')
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()
