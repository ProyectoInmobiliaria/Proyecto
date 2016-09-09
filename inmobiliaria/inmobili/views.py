from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.http import Http404
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
import time
from calendar import month_name
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.template import RequestContext





def index(request):
    return render_to_response("index.html")

def mapa(request):
    return render_to_response("mapa.html")