import asyncio
import apps
import app

try:
    print('Бот запущен...')
    asyncio.run(apps.bot) # Запускаем бота
except KeyboardInterrupt:
    print('Завершение...')
    apps.bot.close() # Завершаем бота
    app.sql.close() # Завершаем подключение к БД