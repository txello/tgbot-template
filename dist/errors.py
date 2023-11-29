import sys
from settings import debug
if not debug.traceback:
    sys.tracebacklimit = 0

class middlewareError(Exception):
    def __init__(self, *args: object) -> None:
        for err in args:
            if err == AttributeError:
                print(f'{self.__class__.__name__}: Ошибка загрузки миддлвари. Параметра не существует')
            elif err == ModuleNotFoundError:
                print(f'{self.__class__.__name__}: Ошибка загрузки миддлвари. Пути к миддлварям не существует')

class appRegisterError(Exception):
    def __init__(self, *args: object) -> None:
        for err in args:
            if err == ModuleNotFoundError:
                print(f'{self.__class__.__name__}: Ошибка загрузки файла app. Файла/папки не существует')
            if err == AttributeError:
                print(f'{self.__class__.__name__}: Ошибка загрузки файла app. Переменной роутера не существует')