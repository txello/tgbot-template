from aiogram import Dispatcher,Bot
from settings import globales,apps,dirs
from importlib import import_module

dp = Dispatcher() # Объявляем диспетчер

[[getattr(dp,j).middleware(getattr(import_module(dirs.middleware),i[0])()) for j in i[1]] for i in apps.middleware.items()] # Подключаем внутренние миддлвари
[[getattr(dp,j).outer_middleware(getattr(import_module(dirs.middleware),i[0])()) for j in i[1]] for i in apps.outer_middleware.items()] # Подключаем внешние миддлвари

dp.include_routers(*[getattr(import_module(f'{dirs.app}.{i}'),dirs.app_router) for i in apps.data]) # Получаем роутеры из папки app определённых файлов, которые записаны в settings.apps и подключаем роутеры к диспетчеру

bot = dp.start_polling(Bot(globales.TOKEN,parse_mode=globales.BOT_PARSE_MODE)) # Объявляем бота с токеном и парсер-модом, настройки которых записаны в settings.globales и запускаем бота как poll