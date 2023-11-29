# SQLITE

## Установка
Не требует установки.

## Подключение

Папку ```sqlite``` можно положить в папку ```plugins/``` Подключение можно сделать в ```app/__init__.py``` следующим образом:



```python
from plugins.sqlite.db import SQLITE

# Подключаем Базу Данных
sql = SQLITE('plugins/sqlite/test.db') # Подключаемся к файлу базы данных, здесь описан пример
sql.connect() # Подключаемся к базе данных
sql.cursor(True) # Объявляем курсор. True - автоматический commit | False - обязателен sql.commit()

# Пример запроса
user = sql.query('SELECT name FROM users WHERE id=?',(20,)).fetchone()
print(user[0])
```

## Возможности

### Версия v1.0: 
* Добавлен класс SQLITE
* Добавлены ```connect```, ```cursor```, ```commit```, ```query```, и ```close```