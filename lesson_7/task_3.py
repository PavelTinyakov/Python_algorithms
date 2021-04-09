"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from random import randint, choice
from statistics import median
from timeit import timeit


def shell_median(arr):
    inc = len(arr) // 2
    while inc:
        for i, el in enumerate(arr):
            while i >= inc and arr[i - inc] > el:
                arr[i] = arr[i - inc]
                i -= inc
            arr[i] = el
        inc //= 2
    return arr[len(arr) // 2]


def gnome_median(arr):
    i, j, size = 1, 2, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i, j = j, j + 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return arr[len(arr) // 2]


def quickselect_median(arr, pivot_fn=choice):
    assert len(arr) % 2 == 1
    return quickselect(arr, len(arr) // 2, pivot_fn)


def quickselect(arr, k, pivot_fn):
    if len(arr) == 1:
        assert k == 0
        return arr[0]
    pivot = pivot_fn(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


def lst_median(arr):
    left = []
    right = []
    for i in arr:
        for j in arr:
            if i > j:
                left.append(j)
            elif i < j:
                right.append(j)
        if len(left) == len(right):
            return i
        left.clear()
        right.clear()


lst = [randint(-100, 100) for i in range(199)]

func_list = ['shell_median',  'gnome_median', 'quickselect_median', 'lst_median']
for func in func_list:
    print(f'Функция {func}:', timeit(func + '(lst[:])', number=1000, globals=globals()))

# Функция shell_median: 1.8442521
# Функция gnome_median: 12.7341596
# Функция quickselect_median: 0.4509369000000003
# Функция lst_median: 10.608960100000001
# Все функции представленные в замере, включая quickselect_median (алгоритм quickselect, разработан Тони Хоаром)
# при худшем варианте имеют O(n ** 2). Вместе с тем пристуствует значительная разница во времени, что
# объясняется входящими данными, которые могут быть оптимальными или нет относительно применяего к ним алгоритма.
# Лучший результат по замеру показал алгоритм quickselect, который имеет "среднее" время выполнения О(n)
