def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def subtract(x,y):
    return x-y

def divide(x,y):
    # БЫЛО:
    #     if y!=0:
    #         return x / y
    #
    # Если y равен нулю, до return дело не доходило, и функция
    # возвращала None: в Python функция без return всегда отдаёт None.
    # Программа печатала "None" как результат деления.
    #
    # Хуже того: ZeroDivisionError при этом не возникал НИКОГДА, потому
    # что деления просто не происходило. Значит except ZeroDivisionError
    # в main.py был мёртвым и не сработал бы ни при каком вводе.
    #
    # СТАЛО: делим всегда. На нуле Python сам бросит ZeroDivisionError,
    # а поймает его except в main(). Проверка ошибки переехала туда, где
    # с ошибкой умеют разговаривать.
    return x / y

