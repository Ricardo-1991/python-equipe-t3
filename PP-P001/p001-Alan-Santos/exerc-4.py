nome_completo = "Alan Carlos dos Santos Pereira"

nome, sobrenome = nome_completo.split()

if nome < sobrenome:
    print(f"{nome} antecede {sobrenome} na ordem alfabética.")
else:
    print(f"{sobrenome} antecede {nome} na ordem alfabética.")

print(f"Quantidade de caracteres em '{nome}': {len(nome)}")
print(f"Quantidade de caracteres em '{sobrenome}': {len(sobrenome)}")

nome_invertido = nome[::-1]
if nome.lower() == nome_invertido.lower():
    print(f"{nome} é um palíndromo.")
else:
    print(f"{nome} não é um palíndromo.")
