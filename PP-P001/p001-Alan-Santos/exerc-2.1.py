#fatorial de 30 em python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado_python = fatorial(30)
print(f"Fatorial de 30 em Python: {resultado_python}")

"""
Em C/C++, o maior valor que um inteiro de 32 bits pode representar é 2 elevado a 31, exemplo:

#include <stdio.h>
#include <limits.h>

int main() {
    printf("Maior valor inteiro em C/C++ (int): %d\n", INT_MAX);
    return 0;
}
"""

#variáveis em python são imutáveis

"""
A afirmação de que as variáveis numéricas são imutáveis em Python significa que, uma vez que um valor é
atribuído a uma variável numérica, esse valor não pode ser alterado diretamente. 
 
 Alguns exemplos:
"""

# Exemplo com inteiros
a = 5
b = a  # b recebe o mesmo valor que a

# Tentativa de modificação direta
a = a + 2

print("a:", a)  # O valor de 'a' é alterado para 7
print("b:", b)  # O valor de 'b' permanece 5

# Exemplo com floats
x = 3.14
y = x  # y recebe o mesmo valor que x

# Tentativa de modificação direta
x = x * 2

print("x:", x)  # O valor de 'x' é alterado para 6.28
print("y:", y)  # O valor de 'y' permanece 3.14


# bit_length(): Retorna o número mínimo de bits necessários para representar o valor binário do número (excluindo o sinal e zeros à esquerda).

num = 42
print(num.bit_length())  # Saída: 6

#to_bytes(length, byteorder, signed=False): Retorna a representação do inteiro como uma sequência de bytes. Útil para manipulação de dados binários.

num = 1234
byte_representation = num.to_bytes(2, byteorder='big')
print(byte_representation)  # Saída: b'\x04\xd2'

#from_bytes(bytes, byteorder, signed=False): Converte uma sequência de bytes de volta para um inteiro.

byte_representation = b'\x04\xd2'
num = int.from_bytes(byte_representation, byteorder='big')
print(num)  # Saída: 1234

#conjugate(): Retorna o conjugado do número complexo (não tem efeito em números inteiros reais).

num = 42
print(num.conjugate())  # Saída: 42






