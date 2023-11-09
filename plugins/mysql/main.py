from mysqldb import MYSQL

# Подключаем Базу Данных
sql = MYSQL('localhost','user','12345','dbbot','3306') # Подключаемся к серверу, здесь описан пример
sql.connect() # Подключаемся к базе данных
sql.cursor(True) # Объявляем курсор. True - автоматический commit | False - обязателен sql.commit()

# Пример запроса
sql.query('SELECT name FROM users WHERE id=%s',(20,))
user = sql.fetchone()
print(user[0])