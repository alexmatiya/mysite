### Отработка теоритических знаний полученных из книги Меле Django 4

Вдруг каким-то чудом :) кто-то захочет запустить данный проект и нет особого желания 
играться с Postgresql:
- можете в настройках раскоментить настройки для sqlite3,
- поставить зависимости
```
pip install -r requirements.txt
```
- прогнать миграции
```
python manage.py migrate
```
- и запускайте
```
python manage.py runserver
```

p.s.: этапы работы удобнее смотреть коммитами