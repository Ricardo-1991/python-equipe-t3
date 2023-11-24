import sys

# Maior potência de 2 representável
maior_potencia = sys.float_info.max_10_exp

# Menor potência de 2 representável (considerando o epsilon da máquina)
menor_potencia = sys.float_info.min_10_exp

print(f"Maior potência de 2 representável: 2^{maior_potencia}")
print(f"Menor potência de 2 representável: 2^{menor_potencia}")


# Imutabilidade de inteiros
x = 5
print("Valor original de x:", x)

# Tentativa de modificação (isso resultará em um erro)
# x += 2
# print("Novo valor de x:", x)  # Isso causará um 


# Criando uma variável de ponto flutuante
x = 3.14

# Listando os métodos disponíveis para a variável de ponto flutuante
metodos_float = dir(x)

# Exibindo alguns dos métodos disponíveis
print("Métodos disponíveis para variáveis de ponto flutuante:")
for metodo in metodos_float:
    print(metodo)

