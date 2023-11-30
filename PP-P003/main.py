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

if __name__ == "__main__":
    main()
