#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.contrib import admin

# Подключаем наши модели в админку сайта

# Указываем, что из scientificWork.models импортируем конкретную модель Test_collection
from scientificWork.models import sw_publications, sw_participations, sw_RandD, Test_collection
# Регистрируем импортированную модель в админку
admin.site.register(Test_collection)
admin.site.register(sw_publications)
admin.site.register(sw_RandD)
admin.site.register(sw_participations)


# Create your models here.
