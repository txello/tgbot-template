from .enums import WebMethod
from aiogram import Bot
from settings import dirs, webserver
from importlib import import_module
from aiohttp import web
from pydantic import ValidationError

async def handle_wrapper(func, bot: Bot, request: web.Request, data_model): # Функция для запуска функций из файла webhook
    if data_model: # Если data_model определен
        body = await request.json() # Получаем body в виде json
        try:
            model_instance = data_model(**body) # Пробуем объявить pydantic модель
        except ValidationError as e:
            return web.Response(body=e.json(), status=400) # В случае ошибки возвращаем результат ошибки
        return await func(bot, request, model_instance) # Возвращаемся в функцию запроса с параметром pydantic
    
    return await func(bot, request) # Возвращаемся в функцию запроса

async def init_webserver(bot: Bot): # Функция веб-сервера
    import_module(f'{dirs.webhook}') # Подкючаем файл webhook, который указан в settings.py
    
    app = web.Application() # Объявляем веб-приложение
    
    for func, method, url, data_model in getattr(import_module(f'{dirs.lib}'), 'register').data_webhook: # Получаем функции из файла webhook
        if isinstance(method, WebMethod): # Если метод записан как core.enums.WebMethod
            method = method.value # Получаем метод
        getattr(app.router, f"add_{method}")(url, lambda request, bot=bot, func=func, data_model=data_model: handle_wrapper(func, bot, request, data_model)) # Записываем новый метод в веб-приложение
    
    runner = web.AppRunner(app) # Объявляем запуск Веб-приложения
    await runner.setup() # Запускаем Веб-приложение
    site = web.TCPSite(runner, webserver.host, webserver.port) # Объявляем Веб-сервер для Веб-приложения
    await site.start() # Запускаем Веб-сервер
    print(f"======= Сервер запущен на {webserver.host}:{webserver.port}/ ======")
    return runner