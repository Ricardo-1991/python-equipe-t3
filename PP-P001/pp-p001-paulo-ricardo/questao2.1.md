## Demonstre como funcionam os operadores aritméticos e aritméticos compostos em Python e destaque as principais novidades e diferenças em relação ao conjunto de operadores com inteiros disponíveis em C/C++.

```python
Adição (+):

Soma dois números.
Subtração (-):

Subtrai o segundo número do primeiro.
Multiplicação (*):

Multiplica dois números.
Divisão (/):

Divide o primeiro número pelo segundo. O resultado é sempre um número de ponto flutuante.
Divisão Inteira (//):

Divide o primeiro número pelo segundo, retornando a parte inteira do resultado.
Módulo (%):

Retorna o resto da divisão do primeiro número pelo segundo.
Potência (**)

Eleva o primeiro número à potência do segundo.
Operadores Aritméticos Compostos:
Operadores compostos combinam uma operação aritmética com uma atribuição.

Adição e Atribuição (+=):

a += b é equivalente a a = a + b.
Subtração e Atribuição (-=):

a -= b é equivalente a a = a - b.
Multiplicação e Atribuição (*=):

a *= b é equivalente a a = a * b.
Divisão e Atribuição (/=):

a /= b é equivalente a a = a / b.
Divisão Inteira e Atribuição (//=):

a //= b é equivalente a a = a // b.
Módulo e Atribuição (%=):

a %= b é equivalente a a = a % b.
Potência e Atribuição (=):**

a **= b é equivalente a a = a ** b.

```

## As principais novidades e diferenças em relação ao C/C++:

Divisão Padrão (Ponto Flutuante):

A divisão padrão em Python (/) retorna um número de ponto flutuante mesmo se os operandos forem inteiros.
```python
print(2 / 5) # saída: 0.4

```

Divisão truncada(Ponto Flutuante):

Já o operador de divisão truncada preserva o comportamento do operador de divisão tradicional
de outras linguagens, como C/C++.

```python
print(6 // 3) # saída: 2
``````