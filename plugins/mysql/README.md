В main описан пример работы.

Перед работой загрузите:
```
pip install mysql-connector-python
```

Файл ```mysqldb.py``` можно положить в папку libs/
Подключение можно сделать в app/__init__.py следующим образом:
```python
from libs.mysqldb import MYSQL

# Далее по примеру в файле main
```