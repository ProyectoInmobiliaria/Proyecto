from django.conf.urls import patterns, include, url
from inmobili.views import *
from inmobili.models import *


urlpatterns = patterns('',
    url(r'^logout/', 'inmobili.views.logout', name='logout'),
    url(r'^register/', 'inmobili.views.register', name='register'),
    url(r'^favorite/(?P<id_casa>\d+)', 'inmobili.views.favorite', name='favorite'),
    url(r'^perfil/', 'inmobili.views.perfil', name='perfil'),
    url(r'^busqueda/', 'inmobili.views.busqueda', name='busqueda'),
    url(r'^comentarios/(?P<id_casa>\d+)', 'inmobili.views.comentarios', name='comentarios'),
    url(r'^comment/(?P<id_casa>\d+)', 'inmobili.views.comment', name='comment'),
    url(r'^answer/(?P<id_comment>\d+)', 'inmobili.views.answer', name='answer'),
    url(r'^casa/(?P<id_casa>\d+)', 'inmobili.views.casa', name='casa'),
    url(r'^login/', 'inmobili.views.log', name='log'),
    url(r'^mapa/', 'inmobili.views.mapa', name='mapa'),
	url(r'^cambiai/(?P<id_perfil>\d+)', 'inmobili.views.cambiai', name='cambiai'),
    url(r'^$', "inmobili.views.index"),
)
