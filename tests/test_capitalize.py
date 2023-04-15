import main

if main.capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if main.capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')