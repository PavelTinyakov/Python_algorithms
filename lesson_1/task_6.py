"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class ToDo:
    def __init__(self):
        self.base_tasks = []
        self.rework_tasks = []
        self.completed_tasks = []

    def __str__(self):
        base = list(map(str, self.base_tasks))
        rework = list(map(str, self.rework_tasks))
        completed = list(map(str, self.completed_tasks))
        return f'Список задач :{base}\nДоделать: {rework}\nВыполненные задачи: {completed}'

    def add_base(self, name):
        self.base_tasks.append(name)

    def add_rework(self):
        self.rework_tasks.append(self.base_tasks.pop(0))

    def add_complete_base(self):
        self.completed_tasks.append(self.base_tasks.pop(0))

    def add_complete_rework(self):
        self.completed_tasks.append(self.rework_tasks.pop(0))


tasks = ToDo()
tasks.add_base('task1')
tasks.add_base('task2')
tasks.add_base('task3')
tasks.add_base('task4')
tasks.add_base('task5')
tasks.add_base('task6')
tasks.add_base('task7')

tasks.add_complete_base()
tasks.add_rework()
tasks.add_complete_base()
tasks.add_rework()
tasks.add_complete_rework()
print(tasks)
