## Manipulação de Variáveis de Ponto Flutuante em Python
Python possui um tipo de dado para representar números de ponto flutuante, chamado float. Vamos explorar suas características, operadores, limites e a imutabilidade das variáveis.

Operadores Aritméticos em Variáveis de Ponto Flutuante

```python
# Exemplo de operações aritméticas com números de ponto flutuante em Python
num1 = 3.5
num2 = 2.0

# Adição, subtração, multiplicação e divisão
resultado_soma = num1 + num2
resultado_subtracao = num1 - num2
resultado_multiplicacao = num1 * num2
resultado_divisao = num1 / num2

# Operadores aritméticos compostos
num1 += 1
num2 -= 0.5
```
Python permite realizar operações aritméticas com variáveis de ponto flutuante da mesma maneira que com números inteiros.

Limites das Potências de 2 em Variáveis de Ponto Flutuante
O operador de exponenciação (**) pode ser utilizado para encontrar a maior e a menor potência de 2 que podem ser representadas por variáveis de ponto flutuante:
```python
# Maior potência de 2 representável
max_potencia = 2.0 ** 1023
print("Maior potência de 2 representável:", max_potencia)

# Menor potência de 2 representável
min_potencia = 2.0 ** -1022
print("Menor potência de 2 representável:", min_potencia)

```
Esses valores representam o limite superior e inferior para as potências de 2 que podem ser representadas com precisão em variáveis de ponto flutuante.

Imutabilidade das Variáveis Numéricas de Ponto Flutuante em Python
As variáveis de ponto flutuante em Python são imutáveis, o que significa que, uma vez atribuído um valor, este não pode ser modificado:

```python
x = 3.14
x += 1.0  # Cria uma nova variável com novo valor
print("Novo valor de x:", x)  # x é uma nova variável, não o mesmo objeto x original

```
Métodos Disponíveis para Variáveis de Ponto Flutuante
Python fornece alguns métodos embutidos para variáveis de ponto flutuante, incluindo:

`as_integer_ratio()`: retorna a representação do número como uma fração.  
`is_integer()`: verifica se o número é um inteiro.  
`hex()`: retorna a representação hexadecimal do número.  

Por exemplo:

```python
num = 3.75
print("Representação como fração:", num.as_integer_ratio())
print("É um inteiro?", num.is_integer())
print("Representação hexadecimal:", float.hex(num))

```