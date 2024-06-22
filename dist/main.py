import asyncio
import apps

try:
    print('Бот запущен...')
    asyncio.run(apps.bot) # Запускаем бота
except KeyboardInterrupt:
    print('Завершение...')
    apps.bot.close() # Завершаем бота