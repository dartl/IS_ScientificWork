# IS_ScientificWork
ИС Кафедры: Научная работа

rootSite - основной каталог сайта (настройки и т.д.) <br>
scientificWork - приложение ИС "Научная работа"<br>
manage.py - системный файл Django для запуска/работы с сайтом

Для корректной работы необходимо изменить подключение к БД на ваше - в файле rootSite/settings.py
```python
DATABASES = {
       'default' : {
       'ENGINE' : 'django_mongodb_engine',
       'NAME' : 'db_sw',  # Замените на ваше название БД
       'TEST': {
            'NAME': 'mytestdatabase',
            'CREATE_DB' : "False"
        },
   }
}
```

Для загрузки fixtures (тестовых данных) в БД необходимо выполнить команду "manage.py loaddata data.json", после чего будет загружено 20 различных элементов.

Доступ к приложению: http://127.0.0.1:8000/scientificWork/
Административная панель: http://127.0.0.1:8000/admin/
