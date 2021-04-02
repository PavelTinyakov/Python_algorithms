"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {i: i for i in range(100000)}
my_ordered = OrderedDict(my_dict)

print(f'my_dict.keys() - {timeit("my_dict.keys()", globals=globals(), number=10000)}')
print(f'my_ordered.keys() - {timeit("my_ordered.keys()", globals=globals(), number=10000)}')

print(f'\nmy_dict.values() - {timeit("my_dict.values()", globals=globals(), number=10000)}')
print(f'my_ordered.values() - {timeit("my_ordered.values()", globals=globals(), number=10000)}')

print(f'\nmy_dict.get(27589) - {timeit("my_dict.get(27589)", globals=globals(), number=10000)}')
print(f'my_ordered.get(27589) - {timeit("my_ordered.get(27589)", globals=globals(), number=10000)}')

print(f'\nmy_dict.popitem() - {timeit("my_dict.popitem()", globals=globals(), number=10000)}')
print(f'my_ordered.popitem() - {timeit("my_ordered.popitem()", globals=globals(), number=10000)}')
# -----------------------------------------------------------------------------------------------------
# my_dict.keys() - 0.004169500000000048
# my_ordered.keys() - 0.004288099999999906
#
# my_dict.values() - 0.0040135999999999505
# my_ordered.values() - 0.003985799999999928
#
# my_dict.get(27589) - 0.006478800000000007
# my_ordered.get(27589) - 0.00446089999999999
#
# my_dict.popitem() - 0.005242100000000027
# my_ordered.popitem() - 0.012188199999999982
#
# Cмысла в использовании OrderedDict нет.
# В Python 3.6  -  словарь упорядоенный.
# По основным методам взаимодействия выигрыша по скорости нет.
