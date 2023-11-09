import functools

def TestDecorator(func): # Шаблон для написания декоратора
    
    @functools.wraps(func) # Подключаем к обёртке functools для работы с параметрами    
    async def wrapper(*args,**kwargs): # Создаём обёртку с параметрами
        # Код здесь...
        return await func(*args,**kwargs) # Возвращаем в функцию все параметры
    return wrapper