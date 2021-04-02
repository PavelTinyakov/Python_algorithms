"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))
# -------------------------------------------------------------------------------------
# В первом случае функция производит рассчет 10000 раз.
# Во втором случае функция производит рассчет 1 раз,
# а последующие 9999 раз данные берутся из кэша.
# Т.е. мы фактически сохраняем результат работы функции.
# Соответственно, проводить замеры этих двух функций некорректно.

# Мемоизация положительно влияет на оптимазацию функции, если внутри функции
# происходят одинаковые расчеты. В нашем случае таковые отсутсвуют.
# Поэтому применение мемоизации тут не имеет смысла.

# Оптимизировать, безусловно, можно задействовав встроенную функцию reversed


def my_reversed(number):
    return reversed(str(number))


print('Использование reversed')
print(
    timeit(
        'my_reversed(num_100)',
        setup='from __main__ import my_reversed, num_100',
        number=10000))
print(
    timeit(
        'my_reversed(num_1000)',
        setup='from __main__ import my_reversed, num_1000',
        number=10000))
print(
    timeit(
        'my_reversed(num_10000)',
        setup='from __main__ import my_reversed, num_10000',
        number=10000))

# Не оптимизированная функция recursive_reverse
# 0.10472860000000006
# 0.1109758999999999
# 0.2113908

# Использование reversed
# 0.016332800000000036
# 0.01576069999999996
# 0.01724340000000013
