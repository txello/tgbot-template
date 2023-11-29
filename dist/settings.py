class globales:
    TOKEN = 'TOKEN' # Токен бота из BotFather
    BOT_NAME = 'Bot name' # Имя бота
    BOT_PARSE_MODE = 'Markdown' # Парсер-мод
    
class apps:
    # data - здесь записаны файлы, которые пойдут в диспетчер бота.
    # Важно! Диспетчер подключает их поочерёдно, поэтому такие как echo лучше подключать последними для корректной работы бота.
    data = [
        'start',
        'echo'
    ]
    # middleware - здесь записаны названия внутренних миддлварей, которые находятся в libs.middleware
    # 'Название класса':['Название функции диспетчера, к которому будет привязываться миддлварь','функций диспетчера может быть несколько']
    middleware = {
        'TestMiddleware':['message','callback_query']
    }
    
    # middleware - здесь записаны названия внешних миддлварей, которые находятся в libs.middleware
    # 'Название класса':['Название функции диспетчера, к которому будет привязываться миддлварь','функций диспетчера может быть несколько']
    outer_middleware = {
        
    }
    
class SQL:
    sqlite_file = 'files/db/test.db'

class dirs:
    # Для продвинутых разработчиков
    
    middleware = 'libs.middleware' # Папка со внешними миддлварями
    app = 'app' # Папка со скриптами
    app_router = 'router' # Переменная роутера для подключения к диспетчеру
    
class debug:
    traceback = True # True - показать Tracaback при ошибках | False - скрыть Traceback при ошибках