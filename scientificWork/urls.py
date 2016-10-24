#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.conf.urls import patterns, url

from scientificWork import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^competitions$', views.competitions, name='competitions'),
    url(r'^publications$', views.publications, name='publications'),
    url(r'^rads$', views.rad, name='rad'),
)