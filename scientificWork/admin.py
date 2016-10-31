#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.contrib import admin

# Подключаем наши модели в админку сайта

# Указываем, что из scientificWork.models импортируем конкретную модель Test_collection
from scientificWork.models import sw_publication, sw_participation, sw_rand, UserProfile
# Регистрируем импортированную модель в админку
admin.site.register(sw_publication)
admin.site.register(sw_rand)
admin.site.register(sw_participation)
admin.site.register(UserProfile)


# Create your models here.
