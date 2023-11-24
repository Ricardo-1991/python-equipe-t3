import math

#QUESTÃO 2.2
factorial = math.factorial(30)
    
print(factorial) 

#Saída da variável factorial = 265252859812191058636308480000000
#valor máximo de um tipo inteiro em C/C++ = 2147483647

#------------------------------------------------------#

#QUESTÃO 2.3
""" As variáveis numéricas são imutáveis. Demonstre com exemplos as
implicações desta afirmação; """

number1 = 5
# Apontando a variável number2 para o number1. Neste momento, ambas as variáveis apontaram para o mesmo endereço de memória.
number2 = number1
print("Imprimindo a variável number1: ", number1)
print("Imprimindo a variável number2: ", number2)

# Ambas as variáveis são identicas.
print(number1 is number2)

# Agora, a variavel number1 recebe o valor 2
number1 = 2

""" Todas as variáveis em Python são Objetos, todas as variáveis são na realidade “referências” a objetos
Quando atribuímos novos valores, na verdade se cria uma nova variável onde vai apontar para o endereço de memória
De um novo valor """

# Ao imprimir, percebemos que a variável number2 continua apontando para o antigo valor (5)
 
print("Imprimindo a variável number1: ", number1)
print("Imprimindo a variável number2: ", number2)

#------------------------------------------------------#
#QUESTÃO 2.4
# Verifique quais métodos estão disponíveis para as variáveis inteiras;

#Métodos Embutidos:
""" 
bit_length(): Retorna o número mínimo de bits necessários para representar o valor em binário, 
excluindo o sinal e os zeros à esquerda. """
myInt = 5
print(myInt.bit_length()) #Saída: 3

# to_bytes(length, byteorder): Retorna uma representação de bytes do número. Exemplo:
print(myInt.to_bytes(2, byteorder='big')) #Saída: b'\x00\x05'




