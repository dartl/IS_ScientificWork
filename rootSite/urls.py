#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^scientificWork/', include('scientificWork.urls')),
    # Examples:
    # url(r'^$', 'rootSite.views.home', name='home'),
    # url(r'^rootSite/', include('rootSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)