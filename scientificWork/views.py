#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from scientificWork.models import Publication

def index(request):
	return render(request,'scientificWork/index.html')

def competitions(request):
    return render(request,'scientificWork/competitions.html')

#def publications(request):
 #   return render(request,'scientificWork/publications.html')

def publications(request):
    s = Publication.objects.all()
    count = 3
    if request.GET:
        pH = request.GET['publishingHouseName']
        pl = request.GET['place']
        tp = request.GET['typePublication']
        dt = request.GET['date']
        vl = request.GET['volume']
        uvl = request.GET['unitVolume']
        ed = request.GET['edition']
        nm = request.GET['bookName']
        type = request.GET['type']
        ISBN = request.GET['isbn']
        number = request.GET['number']
        editor = request.GET['editor']
        nameSbornik = request.GET['nameSbornik']
        reiteration = request.GET['reiteration']
        if(pH != ''): s = s.filter(publishingHouseName=pH)
        if(pl != ''): s = s.filter(place=pl)
        if(tp != ''): s = s.filter(typePublication=tp)
        if(dt != ''): s = s.filter(date=dt)
        if(vl != ''): s = s.filter(volume=vl)
        if(uvl != ''): s = s.filter(unitVolume=uvl)
        if(ed != ''): s = s.filter(edition=ed)
        if(nm != ''): s = s.filter(bookName=nm)
        if(type != ''): s = s.filter(type=type)
        if(ISBN != ''): s = s.filter(isbn=ISBN)
        if(number != ''): s = s.filter(number=number)
        if(editor != ''): s = s.filter(editor=editor)
        if(nameSbornik != ''): s = s.filter(nameSbornik=nameSbornik)
        if(reiteration != ''): s = s.filter(reiteration=reiteration)
        return render(request,'scientificWork/publications.html',
             {'notes': s[0:count]})
    else:
        return render(request, 'scientificWork/publications.html',
                      {'notes': s})

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