from lib import register
from aiogram import Bot

@register.apps # Регистрируем функцию как предрегистрацию параметров для бота
async def webhooks(bot:Bot): # Обязательно иметь переменную bot
    
    # Здесь пример: Перед запуском удаляем накопленные сообщения
    await bot.delete_webhook(drop_pending_updates=True)