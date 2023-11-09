from libs.sql import SQLITE
from settings import SQL
sql = SQLITE(SQL.sqlite_file) # Подлючаемся к файлу SQLITE
sql.connect() # Подключаемся к БД
sql.cursor(True) # Объявляем курсор. True - автоматический commit | False - обязателен sql.commit()