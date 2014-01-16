from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from ws4redis import settings as redis_settings
import redis

class Base(TemplateView):
    def __init__(self):
        self.connection = redis.StrictRedis(**redis_settings.WS4REDIS_CONNECTION)
        print self.connection

    def get_context_data(self, **kwargs):
        context = super(Base, self).get_context_data(**kwargs)
        print context
        context.update(ws_url = 'ws://{SERVER_NAME}:{SERVER_PORT}/ws/stream'.format(**self.request.META))
        print context
        return context

class Broadcast(Base):
    template_name = 'index.html'

    def __init__(self):
        super(Broadcast, self).__init__()
        self.connection.set('_broadcast_:stream', 'Init')
