
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Preço: {self.preco:.2f}"
