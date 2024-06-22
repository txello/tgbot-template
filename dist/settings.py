class globales:
    # Важно! Название параметров и их значения в точности копируют параметры Bot()
    token = 'TOKEN' # Токен бота из BotFather
    parse_mode = 'Markdown' # Парсер-мод

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

class dirs:
    # Для продвинутых разработчиков
    
    middleware = 'libs.middleware' # Файл со внешними миддлварями
    webhook = 'libs.webhooks'
    app = 'app' # Папка со скриптами
    app_router = 'router' # Переменная роутера для подключения к диспетчеру
    lib = 'lib' # Файл с внутренними библиотеками
    globalbot = 'libs.globalbot' # Файл с глобальными командами
    
class webserver:
    enable = False
    
    protocol = 'http'
    host = 'localhost'
    port = 8080
    
class debug:
    traceback = True # True - показать Tracaback при ошибках | False - скрыть Traceback при ошибках