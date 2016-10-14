from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.http import Http404
from django.views import generic
from inmobili.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
import time
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from calendar import month_name
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Perfil


def index(request):
    context = RequestContext(request)
    user = request.user
    casas = Casa.objects.all().order_by("address")[0:10]
    paginator = Paginator(casas, 5)
    try: page = int(request.GET.get("page", '5'))
    except ValueError: page = 1

    try:
        casas = paginator.page(page)
    except (InvalidPage, EmptyPage):
        casas = paginator.page(paginator.num_pages)

    context.update(dict(casas=casas, user=request.user,
                        casa_list=casas.object_list))
    if user.is_authenticated:
        return render_to_response("nav.html", context)
    else:
        return render_to_response("mapa.html", context)

def mapa(request):
    context = RequestContext(request)
    context['casas'] = Casa.objects.all()
    return render_to_response("mapa.html", context)

def log(request):
    context = RequestContext(request)
    if 'POST' in request.method:
        usern = request.POST['username']
        passw = request.POST['password']
        print usern + passw
        user = authenticate(username=usern, password=passw)
        if user is not None:
            login(request, user)
            return redirect ('/')
        else:
            messages.add_message(request, messages.INFO, 'The Passwords doesnt match')
            return redirect ('/')

   
        
        
def register(request):
    context = RequestContext(request)
    if 'POST' in request.method:
        name = request.POST['regfirst']
        lname = request.POST['reglast']
        userw = request.POST['reguser']
        email1 = request.POST['regmail']
        passw1 = request.POST['regpass']
        passw2 = request.POST['regpass2']
        print userw
        if passw1 == passw2:
            user = User.objects.create_user(userw, email1, passw1)
            user.first_name = name
            user.last_name = lname            
            user.save()
            userant = authenticate(username=userw, password=passw1)
            profile = Perfil(user=user, avatar=request.POST['avatar'])
            profile.save()
            if userant is not None:
                login(request, userant)
                return redirect ('/')
            else:
                messages.add_message(request, messages.INFO, 'The Passwords doesnt match')
                return redirect ('/')

def logout(request):
    context = RequestContext(request)
    auth.logout(request)
    return redirect ('/')

def bubblecontent(request, id_post):
    context = RequestContext(request)



