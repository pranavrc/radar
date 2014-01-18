import os
from django.core.wsgi import get_wsgi_application

os.environ.update(DJANGO_SETTINGS_MODULE='radar.settings')
application = get_wsgi_application()
