class TaskManager:
    def __init__(self):
        self.tasks = []

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def add_task(self, description):
        description = capitalize_first_letter(description)
        task = f"{len(self.tasks) + 1}.{description} [ ]"
        self.tasks.append(task)
        print("Tarefa registrada!!!")

    def mark_task_done(self, task_id):
        try:
            index = int(task_id) - 1
            task = self.tasks.pop(index)
            task = task.replace("[ ]", "[x]")
            self.tasks.insert(0, task)
            print("Tarefa realizada!!!")
        except (ValueError, IndexError):
            print("Identificador de tarefa inválido ou tarefa já realizada.")

    def edit_task(self, task_id, new_description):
        try:
            index = int(task_id) - 1
            current_task = self.tasks[index]
            new_description = capitalize_first_letter(new_description)
            new_task = f"{task_id}.{new_description} {current_task.split(maxsplit=2)[-1]}"
            self.tasks[index] = new_task
            print("Tarefa editada!!!")
        except (ValueError, IndexError):
            print("Identificador de tarefa inválido.")

from utils import capitalize_first_letter
