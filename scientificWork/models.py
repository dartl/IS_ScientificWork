#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.db import models

# Описание моделей приложения scientificWork


# Тестовая модель, для примера
class Test_collection(models.Model):
    text = models.TextField()

class sw_publications(models.Model):
 #   _id = models.IntegerField()  #  Идентификатор публикации
    typePublication = models.TextField("Тип публикации")  # тип публикации
    publishingHouseName = models.TextField("Название издательства")  # название издательства
    place = models.TextField("Место издания")  #  место издания
    date = models.DateField("Дата издания")  #  дата издания
    volume = models.IntegerField("Объем")  #  объем
    unitVolume = models.TextField("Единицы объёма")  #  еденицы объема
    edition = models.IntegerField("Тираж")  #  тираж
    user = models.IntegerField("Идентификатор пользователя")  #  идентификатор пользователя

    type = models.TextField("Вид методического указания")  #  вид методического издания / книги
    isbn = models.TextField("ISBN")  #  ISBN
    number = models.IntegerField("Номер издания")  #  номер издания
    editor = models.TextField("Редактор сборника")  #  редакто сборника
    reiteration = models.TextField("Вид повторения сборника")  #  вид повторения сборника

class sw_participations(models.Model):
 #   _id = models.IntegerField()  # идентифиатор
    type = models.TextField("Тип (конференция - conference| семинар - seminar)")  #  тип: конференция - conference, семинар - seminar
    name = models.TextField("Название")  # название
    date = models.DateField("Дата проведения")  # дата проведения
    place = models.TextField("Место проведения")  # дата проведения
    reiteration = models.TextField("Вид проведения (одноразовый - disposable| повторяющийся - repeating")  # вид проведения: одноразовый - disposable, повторяющийся - repeating
    rank = models.TextField("Ранг") # ранг

class sw_RandD(models.Model):
  #  id = models.TextField() # идентификатор
    name = models.TextField("Название НИОКР")  # Название НИОКР
    cipher = models.TextField("Шифр")  #Шифр
# Create your models here.