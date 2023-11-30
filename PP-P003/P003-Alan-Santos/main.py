import json

class GerenciadorProdutos:
    def __init__(self):
        self.produtos = {}
        self.arquivo = "produtos.txt"
        self.carregar_produtos()

    def validar_codigo(self, codigo):
        return len(codigo) == 13 and codigo.isdigit()

    def validar_nome(self, nome):
        return nome and nome[0].isalpha()

    def validar_preco(self, preco):
        try:
            preco = float(preco)
            return preco >= 0
        except ValueError:
            return False

    def carregar_produtos(self):
        try:
            with open(self.arquivo, 'r') as file:
                self.produtos = json.load(file)
        except FileNotFoundError:
            print("Arquivo de produtos não encontrado. Criando um novo.")

    def salvar_produtos(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.produtos, file)

    def inserir_produto(self, codigo, nome, preco):
        if not self.validar_codigo(codigo):
            print("Código inválido. Deve ser uma string numérica de 13 caracteres.")
            return

        if not self.validar_nome(nome):
            print("Nome inválido. Deve começar com uma letra maiúscula.")
            return

        if not self.validar_preco(preco):
            print("Preço inválido. Deve ser um número não negativo.")
            return

        if codigo not in self.produtos:
            self.produtos[codigo] = {'nome': nome, 'preco': preco}
            print(f"Produto {nome} inserido com sucesso!")
            self.salvar_produtos()
        else:
            print("Código de produto já existe. Use outro código.")

    def excluir_produto(self, codigo):
        if codigo in self.produtos:
            del self.produtos[codigo]
            print(f"Produto com código {codigo} excluído com sucesso!")
            self.salvar_produtos()
        else:
            print("Código de produto não encontrado.")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("Lista de produtos:")
            produtos_ordenados = sorted(self.produtos.items(), key=lambda x: float(x[1]['preco']))
            for i, (codigo, produto) in enumerate(produtos_ordenados, start=1):
                print(f"{i} - Código: {codigo}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

    def consultar_preco(self, codigo):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            print(f"O preço do produto {produto['nome']} (Código {codigo}) é R${produto['preco']:.2f}.")
        else:
            print("Código de produto não encontrado.")

# Exemplo de uso do programa
gerenciador = GerenciadorProdutos()

while True:
    print("\nOpções:")
    print("1 - Inserir novo produto")
    print("2 - Excluir produto cadastrado")
    print("3 - Listar todos os produtos")
    print("4 - Consultar preço de um produto")
    print("0 - Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")
        gerenciador.inserir_produto(codigo, nome, preco)

    elif escolha == "2":
        codigo = input("Digite o código do produto a ser excluído: ")
        gerenciador.excluir_produto(codigo)

    elif escolha == "3":
        gerenciador.listar_produtos()

    elif escolha == "4":
        codigo = input("Digite o código do produto para consultar o preço: ")
        gerenciador.consultar_preco(codigo)

    elif escolha == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
