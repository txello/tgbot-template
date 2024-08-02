from core.lib import register
from core.enums import WebMethod
from aiogram import Bot
from aiohttp import web
from pydantic import BaseModel

@register.webhooks('/send','post') # Регистрируем функцию как запрос webhook. Параметры: URL, метод запроса
async def send(bot:Bot, request:web.Request):
    # Здесь пример: Отправляем сообщение
    ###{
    ### "key": "123",
    ### "id": "ID пользователя",
    ### "msg": "Привет!"
    ###}
    data = await request.json()
    if 'key' not in data or data['key'] != "123":
        return web.Response(body={"status":False}, status=200)
    msg = await bot.send_message(chat_id=data["id"], text=data["msg"])
    body = msg.model_dump_json()
    return web.Response(body=body, status=200)

class Item(BaseModel):
    name:str
    price:float
    is_offer:bool=False

@register.webhooks('/test', WebMethod.POST, data_model=Item) # Другой способ работы с веб-сервером: pydantic
async def test(bot: Bot, request:web.Request, model:Item):
    # Здесь пример работы с pydantic
    ###{
    ### "name": "Test",
    ### "price": 1050
    ###}
    print(model.name, model.price, model.is_offer) # Test 1050.0 False
    return web.Response(text="OK!", status=200)