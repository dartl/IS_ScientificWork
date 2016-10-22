#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.contrib import admin

# Подключаем наши модели в админку сайта

# Указываем, что из scientificWork.models импортируем конкретную модель Test_collection
from scientificWork.models import Test_collection

# Регистрируем импортированную модель в админку
admin.site.register(Test_collection)


# Create your models here.
