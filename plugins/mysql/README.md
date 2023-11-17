# Mysql

## Установка
Перед работой загрузите:
```console
> pip install mysql-connector-python
```

## Подключение

Папку ```mysql``` можно положить в папку ```plugins/``` Подключение можно сделать в ```app/__init__.py``` следующим образом:



```python
from plugins.mysql.db import MYSQL

# Подключаем Базу Данных
sql = MYSQL('localhost','user','12345','dbbot','3306') # Подключаемся к серверу, здесь описан пример
sql.connect() # Подключаемся к базе данных
sql.cursor(True) # Объявляем курсор. True - автоматический commit | False - обязателен sql.commit()

# Пример запроса
sql.query('SELECT name FROM users WHERE id=%s',(20,))
user = sql.fetchone()
print(user[0])
```

## Возможности

### Версия v1.0: 
* Добавлен класс MYSQL
* В классе описаны ```fetchone```, ```fetchall``` и ```fetchmany```.
* Добавлены ```connect```, ```cursor```, ```commit```, ```query```, и ```close```