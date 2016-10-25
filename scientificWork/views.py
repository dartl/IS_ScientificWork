#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

def index(request):
	return render(request,'scientificWork/index.html')

def competitions(request):
    return render(request,'scientificWork/competitions.html')

def publications(request):
    return render(request,'scientificWork/publications.html')

def rad(request):
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
