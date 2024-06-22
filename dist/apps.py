from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from settings import globales,apps,dirs, webserver
from importlib import import_module
from errors import middlewareError, appRegisterError
from inspect import getmembers, isroutine
from aiohttp import web

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

async def handle_wrapper(func_name, bot: Bot, dirname, request: web.Request): # Функция для запуска функций из файла webhook
    return await getattr(dirname,func_name)(bot, request)

async def init_webserver(bot:Bot): # Функция веб-сервера
    dirname = import_module(f'{dirs.webhook}') # Подкючаем файл webhook, который указан в settings.py
    app = web.Application() # Объявляем веб-приложение
    for func_name, method, url in getattr(import_module(f'{dirs.lib}'),'register').data_webhook: # Получаем функции из файла webhook
        getattr(app.router,f"add_{method}")(url, lambda request, bot=bot, dirname=dirname, func_name=func_name: handle_wrapper(func_name, bot, dirname, request)) # Записываем новый метод в веб-приложение
    runner = web.AppRunner(app) # Объявляем запуск Веб-приложения
    await runner.setup() # Запускаем Веб-приложение
    site = web.TCPSite(runner, webserver.host, webserver.port) # Объявляем Веб-сервер для Веб-приложения
    await site.start() # Запускаем Веб-сервер
    print(f"======= Сервер запущен на {webserver.protocol}://{webserver.host}:{webserver.port}/ ======")
    return runner


async def start():
    
    bot = Bot(token=globales.token, default=DefaultBotProperties(**{i[0]:i[1] for i in [a for a in getmembers(globales, lambda a:not(isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))] if i[0] != 'token'})) # Объявляем бота с токеном и парсер-модом, настройки которых записаны в settings.globales
    if webserver.enable: # Если в настройках включен веб-сервер
        await init_webserver(bot) # То запускаем функцию веб-сервера
    glb = import_module(f'{dirs.globalbot}') # Импортируем файл с глобальными командами, настройки которых записаны в settings.dirs
    [await getattr(glb,i)(bot) for i in getattr(import_module(f'{dirs.lib}'),'register').data] # Подключаем все функции, которые были зарегистрированы через @register.apps
    return await dp.start_polling(bot) # Запускаем бота как poll

bot = start()