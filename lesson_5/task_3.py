"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from collections import deque
from timeit import timeit

my_list = list(range(1000))
my_deque = deque(range(1000))

print(f'list.append(100) - {timeit("my_list.append(100)", number=10000, globals=globals())}')
print(f'deque.append(100) - {timeit("my_deque.append(100)", number=10000, globals=globals())}')

print(f'\nlist.insert(0, 100) - {timeit("my_list.insert(0, 100)", number=10000, globals=globals())}')
print(f'deque.insert(0, 100) - {timeit("my_deque.insert(0, 100)", number=10000, globals=globals())}')
print(f'deque.appendleft(100) - {timeit("my_deque.appendleft(100)", number=10000, globals=globals())}')
print(f'my_list.insert(433, 100) - {timeit("my_list.insert(433, 100)", number=10000, globals=globals())}')
print(f'deque.insert(433, 100) - {timeit("my_deque.insert(433, 100)", number=10000, globals=globals())}')

print(f'\nlist.index(500) - {timeit("my_list.index(500)", number=10000, globals=globals())}')
print(f'deque.index(500) - {timeit("my_deque.index(500)", number=10000, globals=globals())}')

print(f'\nlist.pop() - {timeit("my_list.pop()", number=10000, globals=globals())}')
print(f'deque.pop() - {timeit("my_deque.pop()", number=10000, globals=globals())}')

print(f'\nlist.pop(0) - {timeit("my_list.pop(0)", number=10000, globals=globals())}')
print(f'deque.popleft() - {timeit("my_deque.popleft()", number=10000, globals=globals())}')

# --------------------------------------------------------------------------------------
# list.append(100) - 0.0024875999999999787
# deque.append(100) - 0.0024772000000000127
#
# list.insert(0, 100) - 1.0043406000000001
# deque.insert(0, 100) - 0.004526699999999995
# deque.appendleft(100) - 0.0024860999999998246
# my_list.insert(433, 100) - 0.7923713000000001
# deque.insert(433, 100) - 0.03623030000000016
#
# list.index(500) - 11.514395
# deque.index(500) - 17.021405
#
# list.pop() - 0.002214599999998512
# deque.pop() - 0.002180599999999089
#
# list.pop(0) - 0.2276756000000013
# deque.popleft() - 0.0023143999999994946
#
# Основное правильно по работе с deque подтвердилось. Если нужно работать
# c началом или концом списка используем deque.
# Если нужен быстрый случайный доступ - используем list.
