"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from timeit import default_timer
from memory_profiler import memory_usage
from hashlib import sha256
from uuid import uuid4
from pympler.asizeof import asizeof
from collections import namedtuple
from recordclass import recordclass


def measuring(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        start_memory = memory_usage()
        func(*args, **kwargs)
        end_memory = memory_usage()
        end_time = default_timer()
        return f'Функция {func.__name__}\n' \
               f'Замер времени: {end_time - start_time}\n' \
               f'Замер памяти: {end_memory[0] - start_memory[0]}'
    return wrapper


# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например,
# число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
@measuring
def my_func1():
    basic_list = [el ** 3 for el in range(1, 1000001, 2)]
    total = 0
    for number in basic_list:
        number_sum = 0
        temp_num = number
        while temp_num > 0:
            number_sum += temp_num % 10
            temp_num = temp_num // 10
        if number_sum % 7 == 0:
            total += number
    return total


@measuring
def my_func1_opt():
    basic_list = (el ** 3 for el in range(1, 1000001, 2))
    return sum(el for el in basic_list if sum(map(int, str(el))) % 7 == 0)


print(my_func1())
print(my_func1_opt())


# Функция my_func1
# Замер времени: 6.03737
# Замер памяти: 1.03125
# Функция my_func1_opt
# Замер времени: 6.590669200000001
# Замер памяти: 0.00390625
# Пример оптимизации по памяти с использованием генератора. За счет механики работы генераторов -
# обработка по необходимости.
# Во втором варианте также использованы встроенные функции для сокращения кода.
# Как видно из произведенного замера скорости, не всегда данный вариант будет оптимальным.
# -------------------------------------------------------------------------------------------------

# Реализуйте скрипт "Кэширование веб-страниц"
# Функция должна принимать url-адрес и проверять
# есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш
# Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
# Можете условжнить задачу, реализовав ее через ООП

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
print(f'Размер экземпляра: {asizeof(cache_url)}')


class CachingOpt:
    __slots__ = ('__cache', '__salt')

    def __init__(self):
        self.__cache = {}
        self.__salt = uuid4().hex

    def __gen_hash(self, url):
        return sha256(self.__salt.encode() + url.encode()).hexdigest()

    def add_cache(self, url):
        url_hash = self.__gen_hash(url)
        if self.__cache.get(url_hash) is None:
            self.__cache[url_hash] = url


cache_url_opt = CachingOpt()
cache_url_opt.add_cache('https://geekbrains.ru/')
print(f'Размер экземпляра: {asizeof(cache_url_opt)}')

# Размер экземпляра Caching: 792
# Размер экземпляра CachingOpt: 560
# Пример использования слотов для оптимизации по памяти в основе которой лежит
# использование менее памятизатратных структур чем хеш таблицы.
# -------------------------------------------------------------------------------------------------

# Программа должна определить среднюю прибыль (за год для всех предприятий)


@measuring
def my_func2(n):
    companies_count = n
    company = namedtuple('company', 'name profit')
    companies_lst = []
    for i in range(companies_count):
        name = f'Firm_{i}'
        profit = '326516 2216577 65659889 321321321'
        companies_lst.append(company(name, sum(map(int, profit.split()))))
    return sum(el.profit for el in companies_lst) / companies_count


@measuring
def my_func2_opt(n):
    companies_count = n
    company = recordclass('company', 'name profit')
    companies_lst = []
    for i in range(companies_count):
        name = f'Firm_{i}'
        profit = '326516 2216577 65659889 321321321'
        companies_lst.append(company(name, sum(map(int, profit.split()))))
    return sum(el.profit for el in companies_lst) / companies_count


print(my_func2(3000))
print(my_func2_opt(3000))


# Функция func2
# Замер времени: 0.24003600000000014
# Замер памяти: 0.38671875
# Функция func2_opt
# Замер времени: 0.23910549999999997
# Замер памяти: 0.14453125
# Пример оптимизации по памяти с использованием recordclass.
# В данном примере разница по сравнению с применением namedtuple более чем 2 раза.

