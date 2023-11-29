# tgbot-template by [@txello](https://github.com/txello)

### Шаблон для профессиональной работы с aiogram
## Версия: v1.2.1

### Установка
1. Переместите бота из ```dist/``` в Вашу рабочую среду
2. Установите pip
3. Установите aiogram:
```console
pip install aiogram
```

### Настройка бота
В файле ```settings.py``` в классе ```globales``` укажите свои настройки.
Более подробнее описано в комментариях этого файла

### Запуск
Достаточно запустить файл ```main.py```:
```console
python main.py
```


### Плагины
Вы можете загружать в шаблон свои библиотеки.
Также в папке ```plugins/``` выкладываем наши библиотеки для удобства использования


## Версии

### v1.0
* Добавлен шаблон
* Добавлены функции, папки
* Добавлены настройки

### v1.1
* Добавлено разделение на внешние и внутренние миддлвари
* Изменены настройки для миддлварей

### v1.2
* Добавлены обработчики ошибок
* Изменены настройки дял debug

### v1.2.1
* Функция ```SQLITE``` была вырезана из основного шаблона и перемещена в ```plugins/```
* Из настройки был вырезан класс ```SQL```

### v1.3
* Добавлена предрегистрация для бота
* Изменены настройки для dirs