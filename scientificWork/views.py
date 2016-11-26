#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from scientificWork.models import Rand
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from scientificWork.models import Participation
def index(request):
	return render(request,'scientificWork/index.html')

def competitions(request):
    comp_list=Participation.objects.all()
    paginator=Paginator(comp_list,5)
    page=request.GET.get('page')
    try:
        comps=paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comps=paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comps=paginator.page(paginator.num_pages)

    return render_to_response('scientificWork/competitions.html',{"comps": comps})

def publications(request):
    return render(request,'scientificWork/publications.html')


     
    



def rads(request):
    
    rand_list=Rand.objects.all()
    paginator=Paginator(rand_list,5)
    page=request.GET.get('page')
    try:
        rands=paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rands=paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rands=paginator.page(paginator.num_pages)

    return render_to_response('scientificWork/rads.html',{"rands": rands})

'''def rads(request):
    if request.GET:
     point=Rand.objects.all()
     
   
     n=request.GET['name']
     cip=request.GET['cipher']
     if (n!= ''): point = point.filter(name=n)
     if (cip!= ''): point = point.filter(cipher=cip)
     context_dict={'rands':point}
     return render(request,'scientificWork/rads.html', context_dict)
    else:
        point=Rand.objects.order_by('user')[:5]
        context_dict={'rands':point}
        return render(request, 'scientificWork/rads.html',context_dict)'''

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