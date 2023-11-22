nome_completo = "Tiago Senger dos Santos"
nome, sobrenome = nome_completo.split(maxsplit=1)
ordem_alfabetica = sorted([nome, sobrenome])
tamanho_nome = len(nome)
tamanho_sobrenome = len(sobrenome)
eh_palindromo = nome.lower() == nome[::-1].lower()

print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Ordem alfabética: {ordem_alfabetica}")
print(f"Tamanho do Nome: {tamanho_nome} caracteres")
print(f"Tamanho do Sobrenome: {tamanho_sobrenome} caracteres")
print(f"Seu nome é um palíndromo? {eh_palindromo}")
