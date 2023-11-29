# main.py

def main():
    produtos = []

    while True:
        print("\n=== Menu ===")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_produto(produtos)
        elif opcao == "2":
            excluir_produto(produtos)
        elif opcao == "3":
            listar_produtos(produtos)
        elif opcao == "4":
            consultar_preco(produtos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def inserir_produto(produtos):
    codigo = input("Digite o código do produto (13 caracteres numéricos): ")
    nome = input("Digite o nome do produto (começando com letra maiúscula): ")
    preco = input("Digite o preço do produto (com duas casas decimais): ")

    produto = {"codigo": codigo, "nome": nome, "preco": preco}
    produtos.append(produto)
    print("Produto cadastrado com sucesso.")

def excluir_produto(produtos):
    codigo = input("Digite o código do produto a ser excluído: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso.")
            return

    print("Produto não encontrado.")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}")
            if i % 10 == 0 or i == len(produtos):
                input("Pressione Enter para continuar...")

def consultar_preco(produtos):
    codigo = input("Digite o código do produto para consultar o preço: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']}")
            return

    print("Produto não encontrado.")

if __name__ == "__main__":
    main()
