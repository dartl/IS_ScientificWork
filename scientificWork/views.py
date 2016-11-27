#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from scientificWork.models import Publication
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
    if request.GET:
        pH = request.GET.get('publishingHouseName')
        pl = request.GET.get('place')
        tp = request.GET.get('typePublication')
        dt = request.GET.get('date')
        vl = request.GET.get('volume')
        uvl = request.GET.get('unitVolume')
        ed = request.GET.get('edition')
        nm = request.GET.get('bookName')
        type = request.GET.get('type')
        ISBN = request.GET.get('isbn')
        number = request.GET.get('number')
        editor = request.GET.get('editor')
        nameSbornik = request.GET.get('nameSbornik')
        reiteration = request.GET.get('reiteration')
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
    page = request.GET.get('page')

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
    # Перенаправляем пользователя обратно на главную страницу.
    return HttpResponseRedirect('/scientificWork/')