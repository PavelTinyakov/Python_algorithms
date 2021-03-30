"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from random import randint
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def my_reversed(enter_num):
    return reversed(str(enter_num))


def main(count_iter, number):
    for i in range(count_iter):
        revers_1(number)
        revers_2(number)
        revers_3(number)
        my_reversed(number)


print('Замеры Timeit:')
numb = randint(1000000, 1000000000)
func_list = ['revers_1', 'revers_2', 'revers_3', 'my_reversed']
for func in func_list:
    print(f'Функция {func}:', timeit(func + '(numb)', number=1000000, globals=globals()))

print('\nЗамеры cProfile:')
run('main(1000000, numb)')

# -------------------------------------------------------------------------------------
# Замеры Timeit:
# Функция revers_1: 10.9921236
# Функция revers_2: 7.674190500000002
# Функция revers_3: 1.6396937999999999
# Функция my_reversed: 1.680406399999999
#
# Замеры cProfile:
# 13000004 function calls (4000004 primitive calls) in 39.803 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   39.802   39.802 <string>:1(<module>)
# 10000000/1000000   21.938    0.000   21.938    0.000 task_3.py:20(revers_1)
#   1000000    8.000    0.000    8.000    0.000 task_3.py:30(revers_2)
#   1000000    2.656    0.000    2.656    0.000 task_3.py:38(revers_3)
#   1000000    2.255    0.000    2.255    0.000 task_3.py:44(my_reversed)

# По первым трем функциям получаем закономерные результаты:
# Рекурсия - фактическое кол-во вызовов функции 10 000 000 говорит само за себя.
# revers_2 - цикл O(n). За счет доп. вычислений в теле цикла завышеное время выполнения
# revers_3 - оптимальный вариант O(n). Работа с индексами списка. Самы быстрый вариант.
# my_reversed - неоднозначные результаты. cProfile - самая быстрая реализация. Timeit -
# всегда проигрывает срезам.
