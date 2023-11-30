from supermarket import Supermercado
from product import Produto

def menu():
    print("1. Inserir novo produto")
    print("2. Excluir produto cadastrado")
    print("3. Listar todos os produtos")
    print("4. Consultar preço de um produto")
    print("5. Sair")

def main():
    supermercado = Supermercado()

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
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
