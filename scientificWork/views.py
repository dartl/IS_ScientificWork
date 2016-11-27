#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from scientificWork.models import Publication, UserProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	return render(request,'scientificWork/index.html')

def competitions(request):
    return render(request,'scientificWork/competitions.html')


def publications(request):
    s = Publication.objects.all()
    pH = ''
    pl = ''
    tp = ''
    dt = ''
    vl = ''
    uvl = ''
    ed = ''
    nm = ''
    type = ''
    ISBN = ''
    number = ''
    editor = ''
    nameSbornik = ''
    reiteration = ''
    if request.POST:
        pH = request.POST.get('publishingHouseName')
        pl = request.POST.get('place')
        tp = request.POST.get('typePublication')
        dt = request.POST.get('date')
        vl = request.POST.get('volume')
        uvl = request.POST.get('unitVolume')
        ed = request.POST.get('edition')
        nm = request.POST.get('bookName')
        type = request.POST.get('type')
        ISBN = request.POST.get('isbn')
        number = request.POST.get('number')
        editor = request.POST.get('editor')
        nameSbornik = request.POST.get('nameSbornik')
        reiteration = request.POST.get('reiteration')
        if (pH != ''): s = s.filter(publishingHouseName=pH)
        if (pl != ''): s = s.filter(place=pl)
        if (tp != ''): s = s.filter(typePublication=tp)
        if (dt != ''): s = s.filter(date=dt)
        if (vl != ''): s = s.filter(volume=vl)
        if (uvl != ''): s = s.filter(unitVolume=uvl)
        if (ed != ''): s = s.filter(edition=ed)
        if (nm != ''): s = s.filter(bookName=nm)
        if (type != ''): s = s.filter(type=type)
        if (ISBN != ''): s = s.filter(isbn=ISBN)
        if (number != ''): s = s.filter(number=number)
        if (editor != ''): s = s.filter(editor=editor)
        if (nameSbornik != ''): s = s.filter(nameSbornik=nameSbornik)
        if (reiteration != ''): s = s.filter(reiteration=reiteration)
    paginator = Paginator(s, 10)
    page = request.POST.get('page')

    try:
        s = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        s = paginator.page(1)
    except EmptyPage:
        s = paginator.page(paginator.num_pages)

    return render(request, 'scientificWork/publications.html',
                      {'notes': s,
                       'pH': pH,
                       'pl': pl,
                       'tp': tp,
                       'dt': dt,
                       'vl': vl,
                       'uvl': uvl,
                       'ed': ed,
                       'nm': nm,
                       'type': type,
                       'ISBN': ISBN,
                       'number': number,
                       'editor': editor,
                       'nameSbornik': nameSbornik,
                       'reiteration': reiteration
                       })

def rads(request):
    return render(request,'scientificWork/rads.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/scientificWork/')
            else:
                return HttpResponse("Your  account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'scientificWork/login.html', {})


# Используйте декоратор login_required(), чтобы гарантировать, что только авторизированные пользователи смогут получить доступ к этому представлению.
@login_required
def user_logout(request):
    # Поскольку мы знаем, что только вошедшие в систему пользователи имеют доступ к этому представлению, можно осуществить выход из системы
    logout(request)
    return HttpResponseRedirect('/scientificWork/')

def strength(request):
    aspirant = UserProfile.objects.filter(academic_state='a').count();
    doctorant = UserProfile.objects.filter(academic_state='d').count();
    soiskatel = UserProfile.objects.filter(academic_state='s').count();
    stajer = UserProfile.objects.filter(academic_state='st').count();
    return render(request,'scientificWork/strength.html', {
        'aspirant' : aspirant,
        'doctorant' : doctorant,
        'soiskatel' : soiskatel,
        'stajer' : stajer
        })