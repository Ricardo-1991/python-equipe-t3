# main.py

def main():
    # Lê as informações dos funcionários do arquivo
    funcionarios = ler_arquivo("funcionarios.txt")

    while True:
        print("\n=== Menu ===")
        print("1. Listar funcionários")
        print("2. Reajustar salários em 10%")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_funcionarios(funcionarios)
        elif opcao == "2":
            reajustar_salarios(funcionarios)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Salva as informações atualizadas no arquivo
    salvar_arquivo("funcionarios_atualizados.txt", funcionarios)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()

        funcionarios = []
        for linha in linhas:
            dados = linha.strip().split(", ")
            funcionario = {
                "nome": dados[0],
                "sobrenome": dados[1],
                "ano_nascimento": int(dados[2]),
                "RG": dados[3],
                "ano_admissao": int(dados[4]),
                "salario": float(dados[5])
            }
            funcionarios.append(funcionario)

        return funcionarios

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []

def listar_funcionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        for i, funcionario in enumerate(funcionarios, start=1):
            print(f"{i}. Nome: {funcionario['nome']} {funcionario['sobrenome']}, "
                  f"Ano Nascimento: {funcionario['ano_nascimento']}, "
                  f"RG: {funcionario['RG']}, "
                  f"Ano Admissão: {funcionario['ano_admissao']}, "
                  f"Salário: R${funcionario['salario']:.2f}")

def reajustar_salarios(funcionarios):
    for funcionario in funcionarios:
        funcionario["salario"] *= 1.10  # Aumento de 10%

    print("Salários reajustados em 10%.")

def salvar_arquivo(nome_arquivo, funcionarios):
    with open(nome_arquivo, "w") as arquivo:
        for funcionario in funcionarios:
            linha = (f"{funcionario['nome']}, {funcionario['sobrenome']}, "
                     f"{funcionario['ano_nascimento']}, {funcionario['RG']}, "
                     f"{funcionario['ano_admissao']}, {funcionario['salario']:.2f}\n")
            arquivo.write(linha)

if __name__ == "__main__":
    main()
