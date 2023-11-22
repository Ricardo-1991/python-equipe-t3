from task_manager import TaskManager

def print_menu():
    print("\n===== ToDoList App =====")
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar tarefa como realizada")
    print("4. Editar tarefa")
    print("0. Sair")

def main():
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            task_manager.list_tasks()
        elif choice == "2":
            description = input("Digite a descrição da tarefa: ")
            task_manager.add_task(description)
        elif choice == "3":
            task_id = input("Digite o identificador da tarefa: ")
            task_manager.mark_task_done(task_id)
        elif choice == "4":
            task_id = input("Digite o identificador da tarefa: ")
            new_description = input("Digite a nova descrição da tarefa: ")
            task_manager.edit_task(task_id, new_description)
        elif choice == "0":
            print("Saindo do aplicativo. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
