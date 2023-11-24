#QUESTÃO 5.2
""" Utilizando o operador de exponenciação mostre qual a maior e a
menor potência de 2 que pode ser representada com variáveis de
ponto flutuante. """

import sys

try:
    maior_expoente = sys.float_info.max_exp
    maior_potencia_de_2 = 2.0 ** maior_expoente
    print("Maior potência de 2 representável:", maior_expoente)
    print("Maior valor representável:", maior_potencia_de_2)
except OverflowError:
    print("Maior potência de 2 está fora do intervalo representável para ponto flutuante.")

# Encontrar a menor potência de 2 representável
menor_expoente = sys.float_info.min_exp
menor_potencia_de_2 = 2.0 ** menor_expoente

print("Menor potência de 2 representável:", menor_expoente)
print("Menor valor representável:", menor_potencia_de_2)


#QUESTÃO 5.3
""" As variáveis numéricas são imutáveis. Demonstre com exemplos as
implicações desta afirmação; """

number1 = 5.2
# Apontando a variável number2 para o number1. Neste momento, ambas as variáveis apontaram para o mesmo endereço de memória.
number2 = number1
print("Imprimindo a variável number1: ", number1)
print("Imprimindo a variável number2: ", number2)

# Ambas as variáveis são identicas.
print(number1 is number2)

# Agora, a variavel number1 recebe o valor 2
number1 = 2.3

""" Todas as variáveis em Python são Objetos, todas as variáveis são na realidade “referências” a objetos
Quando atribuímos novos valores, na verdade se cria uma nova variável onde vai apontar para o endereço de memória
De um novo valor """

# Ao imprimir, percebemos que a variável number2 continua apontando para o antigo valor (5.2)
 
print("Imprimindo a variável number1: ", number1)
print("Imprimindo a variável number2: ", number2)

#QUESTÃO 5.4
""" Verifique quais métodos estão disponíveis para as variáveis de ponto
flutuante; """

myFloat = 4.5
# Retorna a representação de ponto flutuante como uma razão de dois inteiros, uma fração.
print(myFloat.as_integer_ratio()) #Saída: (9,2)

# Retorna True se o número de ponto flutuante for um número inteiro.
print(myFloat.is_integer()) #Saída: False. No caso, se fosse 4.0, que pode ser representado apenas por 4, seria um inteiro.


