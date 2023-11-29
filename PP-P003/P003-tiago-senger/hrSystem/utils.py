def read_employees_from_file(file_path):
    employees = []

    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                data = line.strip().split()
                if len(data) == 5: 
                    nome, sobrenome, nascimento, rg, admissao = data
                    salario = float(data[-1]) 
                    try:
                        employee = {
                            'nome': nome,
                            'sobrenome': sobrenome,
                            'nascimento': int(nascimento),
                            'rg': rg,
                            'admissao': int(admissao),
                            'salario': salario,
                        }
                        employees.append(employee)
                    except ValueError as e:
                        print(f"Erro ao converter dados na linha {line_number}: {e}")
                else:
                    print(f"Formato inválido na linha {line_number}: {line}")

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")

    return employees

def write_employees_to_file(file_path, employees):
    with open(file_path, 'w') as file:
        for employee in employees:
            line = f"{employee['name']} {employee['surname']} {employee['birth_year']} {employee['rg']} {employee['admission_year']} {employee['salary']:.2f}\n"
            file.write(line)
