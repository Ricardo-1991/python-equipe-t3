class ToDoList:
    def __init__(self):
            self.tasks = {}

    def isEmpty_task(self):
        return not bool(self.tasks)
            
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
    
def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Escolha uma opção: ")

        if choice == '0':
            break
        elif choice == '1':
            todo_list.show_tasks()
        elif choice == '2':
            new_task_description = input("Digite a descrição da nova tarefa: ")
            todo_list.register_task(new_task_description)
        elif choice == '3':
            todo_list.mark_task_done()
        elif choice == '4':
            try:
                task_id = int(input("Digite o identificador da tarefa a ser editada: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue
            new_description = input("Digite a nova descrição da tarefa: ")
            todo_list.edit_task(task_id, new_description)
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()