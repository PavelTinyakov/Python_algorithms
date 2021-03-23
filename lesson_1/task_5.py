"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class Plates:
    def __init__(self, size):
        self.stack = [[]]
        self.size = size

    def is_empty(self):
        return self.stack == [[]]

    def push_in(self, plate):
        if len(self.stack[-1]) < self.size:
            self.stack[-1].append(plate)
        else:
            self.stack.append([])
            self.stack[-1].append(plate)

    def pop_out(self):
        if len(self.stack[-1]) == 1:
            last_el = self.stack[-1].pop()
            self.stack.pop()
            return last_el
        return self.stack[-1].pop()

    def show_stacks(self):
        return self.stack

    def get_val(self):
        return self.stack[-1][-1]

    def stacks_count(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = Plates(3)
    stack.push_in(1)
    stack.push_in(2)
    stack.push_in(3)
    stack.push_in(4)
    stack.push_in(5)
    stack.push_in(6)
    stack.push_in(7)
    stack.push_in(8)
    print(stack.get_val())
    print(stack.show_stacks())
    print(stack.stacks_count())
    stack.pop_out()
    print(stack.show_stacks())
    stack.pop_out()
    print(stack.show_stacks())
    print(stack.get_val())
    stack.pop_out()
    print(stack.show_stacks())