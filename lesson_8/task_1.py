"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
import collections


class Node:

    def __init__(self, frequency=None, letter=None):
        self.frequency = frequency
        self.letter = letter
        self.left = None
        self.right = None

    def add_left(self, new_node):
        self.left = new_node

    def add_right(self, new_node):
        self.right = new_node

    def is_leaf(self):
        return (not self.right) & (not self.left)


def build_nodes_deque(str_):
    freq_table = collections.Counter(str_)
    return collections.deque(
        sorted([Node(frequency=elem[1], letter=elem[0])
                for elem in freq_table.items()], key=lambda item: item.frequency))


def build_haffman_tree(deque_):
    if len(deque_) != 1:
        while len(deque_) > 1:
            new_node = Node()
            elem = deque_.popleft()
            new_node.add_left(elem)
            elem = deque_.popleft()
            new_node.add_right(elem)
            new_node.frequency = new_node.left.frequency + new_node.right.frequency
            for i in range(len(deque_)):
                if deque_[i].frequency < new_node.frequency:
                    continue
                else:
                    deque_.insert(i, new_node)
                    break
            else:
                deque_.append(new_node)
    return deque_[0]


def build_haffman_code(haffman_tree, letter_code=''):
    if haffman_tree.is_leaf():
        code.update({haffman_tree.letter: letter_code})
    else:
        build_haffman_code(haffman_tree.left, letter_code=letter_code + '0')
        build_haffman_code(haffman_tree.right, letter_code=letter_code + '1')
    return code


code = dict()
s = "beep boop beer!"

haffman_tree = build_haffman_tree(build_nodes_deque(s))
haffman_code = build_haffman_code(haffman_tree)
print(haffman_code)
print(*[haffman_code[i] for i in s])
