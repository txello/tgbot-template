from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from settings import globales,apps,dirs, webserver
from importlib import import_module
from .errors import middlewareError, appRegisterError
from inspect import getmembers, isroutine
from aiohttp import web
from .web import init_webserver

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
    
    bot = Bot(token=globales.token, default=DefaultBotProperties(**{i[0]:i[1] for i in [a for a in getmembers(globales, lambda a:not(isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))] if i[0] != 'token'})) # Объявляем бота с токеном и парсер-модом, настройки которых записаны в settings.globales
    if webserver.enable: # Если в настройках включен веб-сервер
        await init_webserver(bot) # То запускаем функцию веб-сервера
    glb = import_module(f'{dirs.globalbot}') # Импортируем файл с глобальными командами, настройки которых записаны в settings.dirs
    [await i(bot) for i in getattr(import_module(f'{dirs.lib}'),'register').data] # Подключаем все функции, которые были зарегистрированы через @register.apps
    return await dp.start_polling(bot) # Запускаем бота как poll

bot = start()