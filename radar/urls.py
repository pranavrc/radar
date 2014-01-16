from django.conf.urls import patterns, include, url

from django.contrib import admin
from gpserve.views import Broadcast
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'radar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Broadcast.as_view())
)