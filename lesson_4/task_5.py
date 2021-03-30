"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def eratosthenes(i, n=10000):
    sieve = set(range(2, n + 1))
    res = []
    while sieve:
        prime = min(sieve)
        if len(res) < i:
            res.append(prime)
            sieve -= set(range(prime, n + 1, prime))
        else:
            return res[-1]


# print(simple(1000))
# print(eratosthenes(1000))

# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))

num_10 = 10
num_100 = 100
num_1000 = 1000


print(f'Функция simple:', timeit('simple(num_10)', number=10, globals=globals()))
print(f'Функция simple:', timeit('simple(num_100)', number=10, globals=globals()))
print(f'Функция simple:', timeit('simple(num_1000)', number=10, globals=globals()))
print(f'Функция eratosthenes:', timeit('eratosthenes(num_10)', number=10, globals=globals()))
print(f'Функция eratosthenes:', timeit('eratosthenes(num_100)', number=10, globals=globals()))
print(f'Функция eratosthenes:', timeit('eratosthenes(num_1000)', number=10, globals=globals()))
# -------------------------------------------------------------------------------------
# Функция simple: 0.0007547000000000248
# Функция simple: 0.30378780000000005
# Функция simple: 15.0001785
# Функция eratosthenes: 0.13918949999999874
# Функция eratosthenes: 0.30651720000000005
# Функция eratosthenes: 1.4196753999999991
# Сложность решета Эратосфена O(n log log n). Сложность наивного алгоритма O(n ** 2).
# При не больших n наивный алгоритм выполняется быстрее. С ростом n алгоритм решета
# Эратосфена будет выигрывать по скрости и чем больше будет n тем значительнее будет разница.
