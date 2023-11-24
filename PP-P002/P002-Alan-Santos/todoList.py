import os

def show_menu():
    print("======= ToDo List =======")
    print("1. Adicionar Tarefa")
    print("2. Exibir Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Editar Tarefa")
    print("5. Excluir Tarefa")
    print("6. Sair")

def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Tarefa adicionada com sucesso.")

def show_tasks(tasks):
    print("======= Tarefas =======")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {task['task']} {status}")

def mark_task_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        save_tasks(tasks)
        print("Tarefa marcada como concluída.")
    else:
        print("Índice de tarefa inválido.")

def edit_task(tasks, task_index, new_task):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["task"] = new_task
        save_tasks(tasks)
        print("Tarefa editada com sucesso.")
    else:
        print("Índice de tarefa inválido.")

def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Tarefa '{deleted_task['task']}' excluída com sucesso.")
    else:
        print("Índice de tarefa inválido.")

def save_tasks(tasks):
    with open("todolist.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['completed']}\n")

def load_tasks():
    tasks = []
    if os.path.exists("todolist.txt"):
        with open("todolist.txt", "r") as file:
            for line in file.readlines():
                task, completed = line.strip().split(',')
                tasks.append({"task": task, "completed": completed.lower() == 'true'})
    return tasks

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Escolha uma opção (1-6): ")

        if choice == "1":
            task = input("Digite a tarefa: ")
            add_task(tasks, task)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            task_index = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            mark_task_completed(tasks, task_index)
        elif choice == "4":
            task_index = int(input("Digite o número da tarefa a ser editada: "))
            new_task = input("Digite a nova descrição da tarefa: ")
            edit_task(tasks, task_index, new_task)
        elif choice == "5":
            task_index = int(input("Digite o número da tarefa a ser excluída: "))
            delete_task(tasks, task_index)
        elif choice == "6":
            print("Saindo da aplicação. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
