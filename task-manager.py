#Менеджер задач
#Задача: Создай класс `Task`, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Неверный индекс задачи")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def __str__(self):
        return "\n".join(str(task) for task in self.tasks)

# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Купить продукты", "2024-07-25")
    manager.add_task("Сделать домашнее задание", "2024-07-26")

    print("Все задачи:")
    print(manager)

    manager.mark_task_as_completed(0)

    print("\nЗадачи после отметки первой задачи как выполненной:")
    print(manager)

    print("\nТекущие (не выполненные) задачи:")
    for task in manager.get_pending_tasks():
        print(task)


