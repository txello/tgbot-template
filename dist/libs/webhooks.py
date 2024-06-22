from core.lib import register
from aiogram import Bot
from aiohttp import web


@register.webhooks('/webhook','post') # Регистрируем функцию как запрос webhook. Параметры: URL, метод запроса
async def test1(bot:Bot, request:web.Request):
    # Здесь пример: Получаем информацию о боте
    
    data = await request.json()
    if 'key' in data and data['key'] == "123":
        data_bot = await bot.get_me()
        body = data_bot.model_dump_json()
    else:
        body = {"status":False}
    
    return web.Response(body=body, status=200)