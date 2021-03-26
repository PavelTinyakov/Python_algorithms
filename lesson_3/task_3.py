"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
a
"""


def unique_substring(word, is_hash=True):
    result = set()
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            if is_hash:
                element = hash(word[i:j])
            else:
                element = word[i:j]
            result.add(element)
    result.discard(hash(word)) if is_hash else result.discard(word)
    return f'{word} - {len(result)} уникальных подстрок\n' \
           f'{"hash:" if is_hash else "Подстроки"}\n' \
           f'{", ".join(map(str, result)) if is_hash else ", ".join(result)}'


print(unique_substring('papa'))





