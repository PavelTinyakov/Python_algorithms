"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from hashlib import sha256
from uuid import uuid4


class Caching:
    def __init__(self):
        self.__cache = {}
        self.__salt = uuid4().hex

    def __gen_hash(self, url):
        return sha256(self.__salt.encode() + url.encode()).hexdigest()

    def add_cache(self, url):
        url_hash = self.__gen_hash(url)
        if self.__cache.get(url_hash) is None:
            self.__cache[url_hash] = url


cache_url = Caching()
cache_url.add_cache('https://geekbrains.ru/')
cache_url.add_cache('https://geekbrains.ru/education')

# print(cache_url._Caching__cache)
