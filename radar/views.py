from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from ws4redis import settings as redis_settings
import redis

class Broadcast(TemplateView):
    template_name = 'index.html'

    def __init__(self):
        self.connection = redis.StrictRedis(**redis_settings.WS4REDIS_CONNECTION)

    def get_context_data(self, **kwargs):
        context = super(Base, self).get_context_data(**kwargs)
        context.update(ws_url = 'ws://{SERVER_NAME}:{SERVER_PORT}/ws/stream'.format(**self.request.META))
        return context
