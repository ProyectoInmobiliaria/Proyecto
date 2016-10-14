from django.conf.urls import patterns, include, url
from inmobili.views import *
from inmobili.models import *


urlpatterns = patterns('',
    url(r'^logout/', 'inmobili.views.logout', name='logout'),
    url(r'^register/', 'inmobili.views.register', name='register'),
    url(r'^bubblecontent/(?P<id_post>\d+)', 'inmobili.views.bubblecontent', name='bubblecontent'),
    url(r'^login/', 'inmobili.views.log', name='log'),
    url(r'^mapa/', 'inmobili.views.mapa', name='mapa'),
    url(r"", "inmobili.views.index"),
)
