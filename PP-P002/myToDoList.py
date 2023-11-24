class ToDoList:
    def __init__(self):
            self.tasks = {}
            
    def show_tasks(self):
        if self.isEmpty_task():
            print("Não há tarefas cadastradas.")
        else:
            print("\nTarefas:")
            for task_id, (description, status) in self.tasks.items():
                print(f"{task_id}.{description} [{status}]")
            
    def register_task(self, description):
        if not description[0].isupper():
            description = description.capitalize()

        task_id = len(self.tasks) + 1
        self.tasks[task_id] = (description, ' ')

        print("Tarefa registrada!!!")



todo_list = ToDoList()

def print_menu():
    
    print("\nMenu:")
    print("1. Mostrar Tarefas")
    print("2. Registrar Nova Tarefa")
    print("3. Marcar Tarefa como Realizada")
    print("4. Editar Tarefa")
    print("0. Sair")
    
print_menu()