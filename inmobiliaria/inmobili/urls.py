from django.conf.urls import patterns, include, url
from inmobili.views import *
from inmobili.models import *


urlpatterns = patterns('',
   url(r'^mapa/', 'inmobili.views.mapa', name='mapa'),
   url(r"", "inmobili.views.index"),
)
