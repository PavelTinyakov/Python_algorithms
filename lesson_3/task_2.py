"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
from hashlib import pbkdf2_hmac
from binascii import hexlify


def gen_hash_passwd(login, email):
    obj = pbkdf2_hmac(hash_name='sha256', password=login.encode(), salt=email.encode(), iterations=10000)
    return hexlify(obj)


def validation():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    with open('password.txt', 'w') as wf:
        wf.write(gen_hash_passwd(password, login).decode("utf-8"))
    with open('password.txt') as rf:
        passwd_file = rf.read().encode('utf-8')
    password = input('Введите пароль еще раз для проверки: ')
    if gen_hash_passwd(password, login) == passwd_file:
        return f'Вы ввели правильный пароль'
    return f'Вы ввели неверный пароль'


print(validation())
