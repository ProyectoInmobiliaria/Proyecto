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
    if request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/perfil/":
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
    con = Comment.objects.filter(casa=casa)
    context.update(dict(casa=casa, users=u, comments=con, unu=request.user))
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

def perfil(request):
    context = RequestContext(request)
    user = request.user
    ava = [1, 2, 3, 4, 5]
    favorites = Fav.objects.filter(author=user)
    context.update(dict(user=user, favorites=favorites, ava=ava))
    context.update(csrf(request))
    return render_to_response("perfil.html", context)

def busqueda(request):
    context = RequestContext(request)
    allcasas = Casa.objects.all()
    barrio = []
    attributosIngresados = {}
    casa = []
    if 'POST' in request.method:
        attributosIngresados['tipo__in'] = []
        attributosIngresados['tipo__in'].append(request.POST.get('tipo1', None))
        attributosIngresados['tipo__in'].append(request.POST.get('tipo2', None))
        attributosIngresados['tipo__in'].append(request.POST.get('tipo3', None))
        
        if request.POST.get('operacion', False):
            attributosIngresados['Operation'] = request.POST.get('operacion', None)
        if not request.POST.get('premin', 0) == '':
            attributosIngresados['price__gte'] = request.POST.get('premin', 0)
        if not request.POST.get('premax', 0) == '':
            attributosIngresados['price__lte'] = request.POST.get('premax', 0)
        
        
        if request.POST.get('barrio', False):
            attributosIngresados['district'] = request.POST.get('barrio', None)
        if request.POST.get('rooms', False):
            rooms = request.POST.get('rooms', None).split('-')
            attributosIngresados['rooms__gte'] = rooms[0]
            attributosIngresados['rooms__lte'] = rooms[1]
        
        print(dict(attributosIngresados))
        
        casas = Casa.objects.filter(**attributosIngresados)
        
        
        for a in allcasas:
            barrio.append(a.district)
        barrios = set(barrio)
        context.update(dict(casas=casas, foo=barrios))
        context.update(csrf(request))
        return render_to_response("mapa.html", context)
    
def answer(request, id_comment):
    context = RequestContext(request)
    coment = Comment.objects.get(pk=id_comment)
    if 'POST' in request.method:
        author = request.user
        content = request.POST['body']
        respuesta = Respuesta(comment=coment,
                             author=author,
                             body=content)
        respuesta.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cambiai(request,id_perfil):
    context = RequestContext(request)
    ims = []
    arr = []
    if 'POST' in request.method:
        ims.append(request.POST.get('img1', None))
        ims.append(request.POST.get('img2', None))
        ims.append(request.POST.get('img3', None))
        ims.append(request.POST.get('img4', None))
        ims.append(request.POST.get('img5', None))

        for i in ims:
            if i != None:
				#guardar img
                arr.append(i)
        print arr
        Perfil.objects.filter(pk=id_perfil).update(avatar=arr[0])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
