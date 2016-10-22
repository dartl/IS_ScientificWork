#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,'scientificWork/index.html')

def competitions(request):
    return render(request,'scientificWork/competitions.html')

def publications(request):
    return render(request,'scientificWork/publications.html')

def rad(request):
    return render(request,'scientificWork/rads.html')