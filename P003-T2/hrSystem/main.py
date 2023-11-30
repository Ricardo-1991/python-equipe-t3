from functionalities import *
from utils import *

def main():
    employees = read_employees_from_file("./employees.txt")

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Empregado")
        print("2. Remover Empregado")
        print("3. Listar Todos os Empregados")
        print("4. Reajustar Salários")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            remove_employee(employees)
        elif choice == "3":
            list_all_employees(employees)
        elif choice == "4":
            adjust_salaries(employees)
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()