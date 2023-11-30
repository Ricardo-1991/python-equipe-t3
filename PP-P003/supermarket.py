from product import Produto

class Supermercado:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def excluir_produto(self, codigo):
        self.produtos = [p for p in self.produtos if p.codigo != codigo]

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)

    def consultar_preco(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto.preco
        return None

    def listar_produtos_paginados(self, pagina, itens_por_pagina=10):
        inicio = (pagina - 1) * itens_por_pagina
        fim = inicio + itens_por_pagina
        produtos_pagina = self.produtos[inicio:fim]
        for produto in produtos_pagina:
            print(produto)
