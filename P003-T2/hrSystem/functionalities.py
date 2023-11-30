def add_employee(employees):
    try:
        print("\n=== Adicionar Empregado ===")
        name = input("Nome: ")
        last_name = input("Sobrenome: ")
        birth_year = int(input("Ano de Nascimento: "))
        rg = input("RG: ")
        admission_year = int(input("Ano de Admissão: "))
        salary = int(input("Salário: "))

        employee = {
            "nome": name,
            "sobrenome": last_name,
            "ano_nascimento": birth_year,
            "RG": rg,
            "ano_admissao": admission_year,
            "salario": salary,
        }

        employees.append(employee)
        
        write_employees_to_file(employees, "employees.txt")
        
        print("Empregado adicionado com sucesso.")
        
    except ValueError as e:
        print(f"Erro ao adicionar funcionário: {e}")
    
def write_employees_to_file(employees, file_path):
    try:
        with open(file_path, 'w') as file:
            for employee in employees:
                file.write(f"{employee['nome']} {employee['sobrenome']} "
                           f"{employee['nascimento']} {employee['rg']} "
                           f"{employee['admissao']} {employee['salario']:.2f}\n")

    except Exception as e:
        print(f"Erro ao escrever no arquivo {file_path}: {e}")

def remove_employee(employees):
    print("\n=== Remover Empregado ===")
    rg_to_remove = input("Digite o RG do empregado a ser removido: ")

    for employee in employees:
        if employee["RG"] == rg_to_remove:
            employees.remove(employee)
            write_employees_to_file(employees, "employees.txt")
            print("Empregado removido com sucesso.")
            return

    print("Empregado com RG {} não encontrado.".format(rg_to_remove))

def list_all_employees(employees):
    print("\n=== Lista de Empregados ===")
    
    if not employees:
        print("Não há empregados cadastrados.")
        return

    sorted_employees = sorted(employees, key=lambda x: x["salario"])
    for employee in sorted_employees:
        print(f"Nome: {employee['nome']} {employee['sobrenome']}")
        print(f"Ano de Nascimento: {employee['ano_nascimento']}")
        print(f"RG: {employee['RG']}")
        print(f"Ano de Admissão: {employee['ano_admissao']}")
        print(f"Salário: R${employee['salario']:.2f}")
        print("------------------------")

def adjust_salaries(employees):
    for employee in employees:
        employee['salario'] *= 1.1