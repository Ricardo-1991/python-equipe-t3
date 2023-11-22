print('Operador de Exponenciação:')
maior_potencia = 2.0 ** 1023
menor_potencia = 2.0 ** -1022
print(f"Maior Potência de 2: {maior_potencia}")
print(f"Menor Potência de 2: {menor_potencia}\n")

print('Variáveis Numéricas Imutáveis:')
x = 3.0
print(id(x)) 
x += 2.0 
print(id(x))
print(' ')

print('Métodos Disponíveis para Variáveis de Ponto Flutuante:')
num = 3.14
print(num.is_integer())
print(num.as_integer_ratio()) 
print(num.hex())
