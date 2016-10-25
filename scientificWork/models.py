#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.db import models

# Описание моделей приложения scientificWork


# Тестовая модель, для примера
class Test_collection(models.Model):
    text = models.TextField()

class User(models.Model):
    Identifier = models.IntegerField("Идентификатор пользователя")
    def __str__(self):
        return str(self.Identifier)

class sw_publication(models.Model):
    tpPubl = (
        ('guidelines', 'Методическое указание'),
        ('book', 'Книга'),
        ('journal', 'Статья в журнале'),
        ('compilation', 'Конспект лекции/сборник докладов'),
        ('collection ', 'Сборник трудов')
    )
    reIter = (
        ('disposable', 'одноразовый'),
        ('repeating','повторяющийся')
    )
    user = models.ForeignKey(User, default="")
    typePublication = models.CharField("Тип публикации",
                                       max_length="20",
                                       choices=tpPubl,
                                       default="book")

    publishingHouseName = models.CharField("Название издательства", max_length="100")  # название издательства
    place = models.CharField("Место издания", max_length="100")  #  место издания
    date = models.DateField("Дата издания")  #  дата издания
    volume = models.IntegerField("Объем")  #  объем
    unitVolume = models.CharField("Единицы объёма", max_length="100")  #  еденицы объема
    edition = models.IntegerField("Тираж")  #  тираж

    type = models.CharField("Вид", max_length="100",
                            help_text="Поле заполняется, если тип вашей публикации"
                                      " \"Книга\" или \"Методическое указание\"")  #  вид методического издания / книги
    isbn = models.CharField("ISBN", max_length="100",
                            help_text="Поле заполняется, если тип вашей публткации"
                                      "\"Книга\" или \"Методическое указание\"")  #  ISBN
    number = models.IntegerField("Номер издания")  #  номер издания
    editor = models.CharField("Редактор сборника", max_length="100")  #  редакто сборника
    reiteration = models.CharField("Вид повторения сборника",
                                   choices=reIter,
                                   max_length="10",
                                   default="disposable"
                                   )  #  вид повторения сборника

class sw_participation(models.Model):
    tp = (
        ('conference', 'конференция'),
        ('seminar', 'семинар')
    )
    type = models.CharField("Тип", choices=tp, max_length="10", default="conference")  #  тип: конференция - conference, семинар - seminar
    name = models.CharField("Название", max_length="100")  # название
    date = models.DateField("Дата проведения")  # дата проведения
    place = models.CharField("Место проведения", max_length="100")  # дата проведения
    reIter = (
        ('disposable', 'одноразовый'),
        ('repeating', 'повторяющийся')
    )
    reiteration = models.CharField("Вид повторения сборника",
                                    choices=reIter,
                                    max_length="10",
                                    default="disposable"
                                   )  # вид повторения сборника

    rank = models.CharField("Ранг", max_length="100") # ранг


class sw_rand(models.Model):
    user = models.ForeignKey(User, default="")
    name = models.CharField("Название НИОКР", max_length="100")  # Название НИОКР
    cipher = models.CharField("Шифр", max_length="100")  #Шифр

