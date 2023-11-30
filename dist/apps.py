from aiogram import Dispatcher,Bot
from settings import globales,apps,dirs
from importlib import import_module
from errors import middlewareError, appRegisterError
dp = Dispatcher() # Объявляем диспетчер

try:
    [[getattr(dp,j).middleware(getattr(import_module(dirs.middleware),i[0])()) for j in i[1]] for i in apps.middleware.items()] # Подключаем внутренние миддлвари
    [[getattr(dp,j).outer_middleware(getattr(import_module(dirs.middleware),i[0])()) for j in i[1]] for i in apps.outer_middleware.items()] # Подключаем внешние миддлвари
except Exception as e:
    raise middlewareError(e.__class__)
try:
    dp.include_routers(*[getattr(import_module(f'{dirs.app}.{i}'),dirs.app_router) for i in apps.data]) # Получаем роутеры из папки app определённых файлов, которые записаны в settings.apps и подключаем роутеры к диспетчеру
except Exception as e:
    print(e.__class__)
    raise appRegisterError(e.__class__)


async def start():
    bot = Bot(globales.TOKEN,parse_mode=globales.BOT_PARSE_MODE) # Объявляем бота с токеном и парсер-модом, настройки которых записаны в settings.globales
    glb = import_module(f'{dirs.globalbot}') # Импортируем файл с глобальными командами, настройки которых записаны в settings.dirs
    [await getattr(glb,i)(bot) for i in getattr(import_module(f'{dirs.lib}'),'register').data] # Подключаем все функции, которые были зарегистрированы через @register.apps
    return await dp.start_polling(bot) # Запускаем бота как poll

bot = start()