
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))

    def remove_task(self, task):
        new_stack = Stack()
        while not self.tasks.is_empty():
            current_task = self.tasks.pop()
            if current_task[0] != task:
                new_stack.push(current_task)

        while not new_stack.is_empty():
            self.tasks.push(new_stack.pop())

    def __str__(self):
        sorted_tasks = sorted(self.tasks.stack, key=lambda x: x[1])
        result = ""
        for task in sorted_tasks:
            result += str(task[1]) + " " + task[0] + "; "
        return result.rstrip("; ")


manager = TaskManager()
manager.new_task("Сесть за работу", 3)
manager.new_task("Устать", 4)
manager.new_task("Подготовить рабочее место", 1)
manager.new_task("Включить чайник", 2)
manager.new_task("Сделать кофе", 3)
print(manager)