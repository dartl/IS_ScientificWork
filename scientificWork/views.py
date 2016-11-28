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
from scientificWork.models import Participation

from scientificWork.models import Rand
def index(request):
	return render(request,'scientificWork/index.html')

def competitions(request):

    return render(request,'scientificWork/competitions.html')
def competitions(request):
    comp_list=Participation.objects.all()
    t=''
    n = ''
    dt = ''
    p = ''    
    r=''
    rk=''
    if request.POST:
        t=request.POST.get('type')
        n = request.POST.get('name')
        p = request.POST.get('place')
        dt = request.POST.get('date')        
        r = request.POST.get('reiteration')
        rk = request.POST.get('rank')       
        if (t != ''): comp_list = comp_list.filter(type=t)
        if (n != ''): comp_list = comp_list.filter(name=n)
        if (p != ''): comp_list = comp_list.filter(place=p)
        if (dt != ''): comp_list = comp_list.filter(date=dt)
        if (r != ''): s = s.filter(reiteration=r)        
        if (rk != ''): comp_list = comp_list.filter(rank=rk)       
    paginator = Paginator(comp_list, 10)
    page = request.POST.get('page')
    try:
        comp_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comp_list = paginator.page(1)
    except EmptyPage:
        comp_list = paginator.page(paginator.num_pages)

    return render(request, 'scientificWork/competitions.html',
                      {'comps': comp_list,
                       't': t,
                       'p': p,
                       'n': n,
                       'dt': dt,
                       
                       'rk': rk,
                       
                       'r': r
                       })

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
    rand_list=Rand.objects.all()
    n=''
    c=''
    if request.POST:
        n=request.POST.get('name')
        c=request.POST.get('cipher')
        if(n!=''):rand_list=rand_list.filter(name=n)
        if(c!=''):rand_list=rand_list.filter(cipher=c)
    
    paginator=Paginator(rand_list,5)
    page=request.POST.get('page')
    try:
        rand_list=paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rand_list=paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rands=paginator.page(paginator.num_pages)

    return render(request,'scientificWork/rads.html',{"rands": rand_list,'n':n,'c':c})
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