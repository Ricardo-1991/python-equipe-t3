"""
Em Python, os operadores aritméticos realizam operações básicas em números. 
Aqui estão os operadores aritméticos básicos em Python e alguns exemplos:
"""

# Operadores aritméticos
a = 10
b = 3

soma = a + b        # Soma
subtracao = a - b   # Subtração
multiplicacao = a * b   # Multiplicação
divisao = a / b     # Divisão
resto = a % b       # Resto da divisão
exponenciacao = a ** b  # Exponenciação

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto: {resto}")
print(f"Exponenciação: {exponenciacao}")

#Os operadores compostos em Python são uma forma compacta de realizar uma operação e atribuir o resultado à variável. Por exemplo:

# Operadores compostos
x = 5
x += 3  # Equivalente a x = x + 3
print(x)  # Saída: 8

y = 10
y *= 2  # Equivalente a y = y * 2
print(y)  # Saída: 20

#Principais diferenças em relação ao conjunto de operadores com inteiros disponíveis em C/C++:

"""
1 - Divisão Padrão (Python): Em Python, a operação de divisão entre dois inteiros resulta em um número de ponto
flutuante, mesmo que o resultado seja um número inteiro. Isso é diferente de C/C++, 
onde a divisão de dois inteiros resulta em uma divisão de piso, truncando a parte decimal
"""

# Em Python
resultado = 10 / 3  # Resultado é 3.3333...

"""
2- Operador de Exponenciação (**): Em Python, o operador ** é usado para exponenciação
enquanto em C/C++, geralmente você usaria a função pow ou operadores bit a bit.
"""

# Em Python
resultado = 2 ** 3  # Resultado é 8

"""
3 - Não há operadores de incremento/decremento unários (++/--): Python não possui operadores de incremento (++) ou decremento (--)
como em C/C++. Em vez disso, você usa os operadores += e -= para alcançar o mesmo resultado
"""

# Em Python
x = 5
x += 1  # Incremento, x é atualizado para 6

