#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    casas = Casa.objects.all().order_by("-created")[0:4]
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
        return render_to_response("index.html", context)

def mapa(request):
    context = RequestContext(request)
    arry = []
    ca = Casa.objects.all()
    for a in ca:
        arry.append(a.district)
    foo = set(arry)
    print ca
    context.update(dict(casas=ca, foo=foo))
    context.update(csrf(request))
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
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.add_message(request, messages.INFO, 'Usuario o contraseña incorrecta!')
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
        u = User.objects.filter(username=userw)
        print u
        if u is not None:
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
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.add_message(request, messages.INFO, 'Algo salio mal')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.add_message(request, messages.INFO, 'Contraseñas no coinciden')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.add_message(request, messages.INFO, 'Ese usuario ya esta en uso')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            

def logout(request):
    context = RequestContext(request)
    auth.logout(request)
    print request.META.get('HTTP_REFERER')
    if request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/showfav/":
            return redirect ('/')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def casa(request, id_casa):
    context = RequestContext(request)
    casa = Casa.objects.get(pk=id_casa)
    img = Image.objects.filter(casa=casa)
    f = Fav.objects.filter(casa=casa).filter(author=request.user)
    context.update(dict(casa=casa, user=request.user, img=img, favorite=f))
    context.update(csrf(request))
    return render_to_response("casa.html", context)

def comentarios(request, id_casa):
    context = RequestContext(request)
    u = User.objects.all()
    casa = Casa.objects.get(pk=id_casa)
    context['comments'] = Comment.objects.filter(casa=casa)
    context.update(dict(casa=casa, users=u))
    context.update(csrf(request))
    return render_to_response("coments.html", context)

def comment(request, id_casa):
    context = RequestContext(request)
    casa = Casa.objects.get(pk=id_casa)
    if 'POST' in request.method:
        author = request.user
        content = request.POST['coment']
        comentario = Comment(author=author, 
                             body=content,
                             casa=casa)
        comentario.save()
    comments = Comment.objects.filter(casa=casa)
    context.update(dict(user=request.user, comments=comments))
    context.update(csrf(request))
    return redirect('/casa/'+id_casa)

def favorite(request, id_casa):
    context = RequestContext(request)
    casa = Casa.objects.get(pk=id_casa)
    author=request.user
    f = Fav.objects.filter(casa=casa).filter(author=author)
    print f 
    if not f:
        fav = Fav(author=author, casa=casa)
        fav.save()
        print "gurde"
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        f.delete()
        print "bore"
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def showfav(request):
    context = RequestContext(request)
    user = request.user
    context['favorites'] = Fav.objects.filter(author=user)
    return render_to_response("favorites.html", context)

def busqueda(request):
    context = RequestContext(request)
    allcasas = Casa.objects.all()
    arry = []
    arry2 = []
    if 'POST' in request.method:
        cas = request.POST.get('tipo1', '')
        dep = request.POST.get('tipo2', '')
        ofi = request.POST.get('tipo3', '')
        opera = request.POST.get('operacion', '')
        premin = request.POST.get('premin', '0')
        premax = request.POST.get('premax', '')
        barr = request.POST.get('barrio', '')
        room = request.POST.get('rooms', '')

        for c in allcasas:
            if c.tipo in {cas, dep, ofi}:
                if opera != '':
                    if premax != '':
                        if  barr != '':
                            if room != '':
                                amax = room[1:]
                                amin = room[:1]
                                amin = int(amin)
                                amax = int(amax)
                                if (c.price >= premin and c.price <= premax and c.rooms >= amin and c.rooms <= amax and c.district == barr and c.Operation == opera):
                                    arry2.append(c)
                            else:
                                if (c.price >= premin and c.price <= premax and c.district == barr and c.Operation == opera):
                                    arry2.append(c)
                        else:
                            if room != '':
                                amax = room[1:]
                                amin = room[:1]
                                amin = int(amin)
                                amax = int(amax)
                                if (c.price >= premin and c.price <= premax and c.rooms >= amin and c.rooms <= amax and c.Operation == opera):
                                    arry2.append(c)
                            else:
                                if (c.price >= premin and c.price <= premax and c.Operation == opera):
                                    arry2.append(c)
                    else:
                        if  barr != '':
                            if room != '':
                                amax = room[1:]
                                amin = room[:1]
                                amin = int(amin)
                                amax = int(amax)
                                if (c.rooms >= amin and c.rooms <= amax and c.district == barr and c.Operation == opera):
                                    arry2.append(c)
                            else:
                                if (c.district == barr and c.Operation == opera):
                                    arry2.append(c)
                        else:
                            if room != '':
                                amax = room[1:]
                                amin = room[:1]
                                amin = int(amin)
                                amax = int(amax)
                                if (c.rooms >= amin and c.rooms <= amax and c.Operation == opera):
                                    arry2.append(c)
                            else:
                                if (c.Operation == opera):
                                    arry2.append(c)
                else:
                    if premax != '':
                        if  barr != '':
                            if room != '':
                                amax = room[1:]
                                amin = room[:1]
                                amin = int(amin)
                                amax = int(amax)
                                if (c.price >= premin and c.price <= premax and c.rooms >= amin and c.rooms <= amax and c.district == barr):
                                    arry2.append(c)
                            else:
                                if (c.price >= premin and c.price <= premax and c.district == barr):
                                    arry2.append(c)
                        else:
                            if room != '':
                                amax = room[1:]
                                amin = room[:1]
                                amin = int(amin)
                                amax = int(amax)
                                if (c.price >= premin and c.price <= premax and c.rooms >= amin and c.rooms <= amax):
                                    arry2.append(c)
                            else:
                                if (c.price >= premin and c.price <= premax):
                                    arry2.append(c)
                    else:
                        if  barr != '':
                            if room != '':
                                amax = room[1:]
                                amin = room[:1]
                                amin = int(amin)
                                amax = int(amax)
                                if (c.rooms >= amin and c.rooms <= amax and c.district == barr):
                                    arry2.append(c)
                            else:
                                if (c.district == barr):
                                    arry2.append(c)
                        else:
                            if room != '':
                                amax = room[1:]
                                amin = room[:1]
                                amin = int(amin)
                                amax = int(amax)
                                if (c.rooms >= amin and c.rooms <= amax):
                                    arry2.append(c)
                            else:
                                arry2.append(c)
        foo2 = set(arry2)
        for a in allcasas:
            arry.append(a.district)
        foo = set(arry)
        context.update(dict(casas=foo2, foo=foo))
        context.update(csrf(request))
        return render_to_response("mapa.html", context)
