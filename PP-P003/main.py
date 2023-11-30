from supermarket import Supermercado
from product import Produto
from employee import Empregado

def carregar_dados_empregados(filename):
    with open(filename, 'r') as file:
        linhas = file.readlines()

    empregados = []
    for linha in linhas:
        dados = linha.strip().split(',')
        nome, sobrenome, ano_nascimento, rg, ano_admissao, salario = dados
        empregado = Empregado(nome, sobrenome, int(ano_nascimento), rg, int(ano_admissao), float(salario))
        empregados.append(empregado)

    return empregados

def Reajusta_dez_porcento(empregados):
    for empregado in empregados:
        empregado.salario *= 1.1

def menu():
    print("1. Inserir novo produto")
    print("2. Excluir produto cadastrado")
    print("3. Listar todos os produtos")
    print("4. Consultar preço de um produto")
    print("5. Listar todos os empregados")
    print("6. Reajustar salários")
    print("7. Sair")

def main():
    supermercado = Supermercado()
    empregados = carregar_dados_empregados('dados_empregados.txt')

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            produto = Produto(codigo, nome, preco)
            supermercado.inserir_produto(produto)
            print("Produto inserido com sucesso!")

        elif opcao == "2":
            codigo = input("Digite o código do produto a ser excluído: ")
            supermercado.excluir_produto(codigo)
            print("Produto excluído com sucesso!")

        elif opcao == "3":
            pagina = int(input("Digite o número da página: "))
            supermercado.listar_produtos_paginados(pagina)

        elif opcao == "4":
            codigo = input("Digite o código do produto: ")
            preco = supermercado.consultar_preco(codigo)
            if preco is not None:
                print(f"Preço do produto: {preco:.2f}")
            else:
                print("Produto não encontrado.")

        elif opcao == "5":
            print("Lista de Empregados:")
            for empregado in empregados:
                print(empregado)

        elif opcao == "6":
            Reajusta_dez_porcento(empregados)
            print("Salários reajustados em 10%.")

        elif opcao == "7":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
