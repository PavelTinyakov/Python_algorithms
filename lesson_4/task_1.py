"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for i, el in enumerate(nums):
        if el % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_3(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_4(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


def func_5(nums):
    return list(filter(lambda i: nums[i] % 2 == 0, range(len(nums))))


n = 10000
my_list = [randint(0, n) for _ in range(n)]

func_list = ['func_1', 'func_2', 'func_3', 'func_4', 'func_5']
for func in func_list:
    print(f'Функция {func}:', timeit(func + '(my_list)', number=10000, globals=globals()))
# -------------------------------------------------------------------------------------
# Результаты замеров
# Функция func_1: 37.3261058 - эталонный вариант
# Функция func_2: 41.547016400000004 - вместо индексов - enumerate
# Функция func_3: 31.579526300000012 - list comprehension
# Функция func_4: 34.45431049999999 - list comprehension + enumerate
# Функция func_5: 70.9919271 - filter
# То, что в данных замерах лучший результат покажет list comprehension было понятно.
# Однако для меня было неочевидно, что использование enumerate вместо range(len())
# будет давать результаты замеров на 10% хуже.
# Использование filter в func_5 - один из заведомо проигрышных вариантов, однако
# настолько большую разницу - практически в 2 раза, я не ожидал. С другой стороны,
# данный алгоритм должен быть O(n log n) в отличии от O(n) в других функциях.
