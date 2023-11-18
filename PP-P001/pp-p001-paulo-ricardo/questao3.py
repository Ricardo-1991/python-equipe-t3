#QUESTÃO 3.1 e 3.2

""" Imprima na tela, utilizando print, cada um dos caracteres numéricos e
seu correspondente código numérico. Pesquise como modificar o
comportamento do print para imprimir como caractere e como
número. 

Modifique o exercício anterior para que a saída imprima também o
código numérico em octal e em hexadecimal.
"""
list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for char in list:
    print(char, '-', ord(char), oct(ord(char)), hex(ord(char)))

#QUESTÃO 3.3

""" Acrescente ao código do exercício anterior a possibilidade de ler um
caractere qualquer e imprima no mesmo formato do inciso anterior.
Pesquise como ler um valor da entrada padrão. """
myString = input("Digite um caractere qualquer: ")
if(len(myString) == 1):
    print(myString, '-', ord(myString), oct(ord(myString)), hex(ord(myString)))
else:
    print("Por favor, digite apenas um caractere.")
    
#QUESTÃO 3.4

""" Pesquise como trabalha Python os caracteres especiais, ‘ç’ e ‘ã’
por exemplo. Acrescente no código do exercício anterior um exemplo
que demonstra como usar este recurso """


""" Em Python, os caracteres especiais como 'ç' e 'ã' são tratados como qualquer outro caractere. 
Python suporta Unicode, o que significa que você pode trabalhar 
com caracteres de diferentes idiomas e conjuntos de caracteres. """

myEspecialChar = input("Digite um caractere especial qualquer: ")
if(len(myEspecialChar) == 1):
    print(myEspecialChar, '-', ord(myEspecialChar), oct(ord(myEspecialChar)), hex(ord(myEspecialChar)))
else:
    print("Por favor, digite apenas um caractere.")    



