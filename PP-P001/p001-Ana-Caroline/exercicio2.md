### Operadores Aritméticos em Python

Python possui operadores aritméticos similares ao C/C++:

- Adição: `+`
- Subtração: `-`
- Multiplicação: `*`
- Divisão: `/`
- Divisão inteira: `//` (resultado sem a parte decimal)
- Módulo: `%` (resto da divisão)
- Exponenciação: `**` (por exemplo, `2 ** 3` é 2 elevado à 3, resultando em 8)

### Operadores Aritméticos Compostos em Python

Python oferece operadores compostos que combinam operação com atribuição:

- `+=`, `-=` para adição/subtração
- `*=`, `/=` para multiplicação/divisão
- `//=`, `%=` para divisão inteira/módulo
- `**=` para exponenciação

### Números Inteiros Grandes em Python

Python tem o tipo de dado `int` que permite representar inteiros de tamanho arbitrário, sem limite prático para o tamanho.

```python
# Exemplo: Fatorial de 30 em Python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado_python = fatorial(30)
print("Fatorial de 30 em Python:", resultado_python)
# Não há limite prático para o tamanho dos inteiros em Python
```
### Imutabilidade das Variáveis Numéricas em Python

Variáveis numéricas em Python são imutáveis. Uma vez atribuído um valor, não pode ser modificado:

```python
x = 5
x += 3  # Cria uma nova variável com novo valor
print("Novo valor de x:", x)  # x é uma nova variável, não o mesmo objeto x original
 
```

### Métodos Disponíveis para Inteiros em Python

Os inteiros em Python têm métodos embutidos, incluindo:

`bit_length()`: retorna o número de bits necessários para representar o número.
`to_bytes(length, byteorder)`: converte o inteiro em uma sequência de bytes.
`from_bytes(bytes, byteorder)`: converte uma sequência de bytes em um inteiro.
Exemplo:

```python
num = 12345
print("Número de bits:", num.bit_length())  # Retorna 14 para o número 12345

```