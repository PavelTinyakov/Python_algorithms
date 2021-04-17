"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform
from timeit import timeit


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if len(left) > i:
        result += left[i:]
    elif len(right) > j:
        result += right[j:]
    return result


lst_10 = [uniform(0, 50) for _ in range(10)]
print(timeit('merge_sort(lst_10[:])', number=1000, globals=globals()))  # 0.0591767

lst_100 = [uniform(0, 50) for _ in range(100)]
print(timeit('merge_sort(lst_100[:])', number=1000, globals=globals()))  # 0.961586

lst_1000 = [uniform(0, 50) for _ in range(1000)]
print(timeit('merge_sort(lst_1000[:])', number=1000, globals=globals()))  # 13.119929800000001
