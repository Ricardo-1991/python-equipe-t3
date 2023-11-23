# Declarar uma variável com o nome completo
nome_completo = "Seu Nome Completo Aqui"

# Separar o nome do sobrenome usando funcionalidades de strings
nome, sobrenome = nome_completo.split(maxsplit=1)

# Verificar qual variável antecede a outra na ordem alfabética
if nome < sobrenome:
    print(f"{nome} antecede {sobrenome} na ordem alfabética.")
elif sobrenome < nome:
    print(f"{sobrenome} antecede {nome} na ordem alfabética.")
else:
    print("Os valores são iguais na ordem alfabética.")

# Verificar a quantidade de caracteres em cada variável
print(f"Quantidade de caracteres no nome: {len(nome)}")
print(f"Quantidade de caracteres no sobrenome: {len(sobrenome)}")

# Verificar se o nome é um palíndromo
if nome.lower() == nome[::-1].lower():
    print(f"{nome} é um palíndromo!")
else:
    print(f"{nome} não é um palíndromo.")
