#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.db import models
from django.contrib.auth.models import User

# Общие модели
PERSON_TYPE_CHOICES = (
    ('s', 'Студент'),
    ('h', 'Староста'),
    ('t', 'Преподаватель'),
    ('a', 'Администратор'),
)
ACADEMIC_STATUS_CHOICES  = (
  ('a','Ассистент'),
  ('s','Старший преподаватель'),
  ('d','Доцент'),
  ('p','Профессор'),
)

ACADEMIC_DEGREE_CHOICES = (
  ('n','Без степени'),
  ('t','Кандидат наук'),
  ('d','Доктор наук'),
)


class Person(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=20)
  user = models.ForeignKey(
    User,
    null=True
  )
  type = models.CharField(
    max_length=2,
    choices=PERSON_TYPE_CHOICES,
    default='s'
  )
  studyGroup = models.CharField(
    max_length=5,
    null=True
  )
  birstDate = models.DateField(null=True)
  #Дата текущего избрания или зачисления на преподавательскую должность
  electionDate = models.DateField(null=True)
  #Должность
  position = models.CharField(max_length=40,null=True)
  #Срок окончания трудового договора
  contractDate = models.DateField(null=True) # Возможн поменяю
  #Ученая степень
  academicDegree = models.CharField(
    max_length=1,
    choices=ACADEMIC_DEGREE_CHOICES,
    null=True
  )
  #Год присвоения ученой степени
  yearOfAcademicDegree = models.DateField(null=True)
  #Учебное звание
  academicStatus = models.CharField(
    max_length=1,
    choices=ACADEMIC_STATUS_CHOICES,
    null=True,
  )
  yearOfAcademicStatus = models.DateField(null=True)


  def __str__(self):
    return self.firstName + " " + self.lastName
# Описание моделей приложения scientificWork


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
    user = models.ForeignKey(Person, default="")
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
    user = models.ForeignKey(Person, default="")
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
    user = models.ForeignKey(Person, default="")
    name = models.CharField("Название НИОКР", max_length="100")  # Название НИОКР
    cipher = models.CharField("Шифр", max_length="100")  #Шифр

