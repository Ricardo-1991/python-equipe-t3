### Manipulação de Variáveis do Tipo String e Uso do Print em Python

As strings em Python são formadas por conjuntos de caracteres que podem ser tratadas também como valores numéricos. Vamos explorar como imprimir os caracteres numéricos e seus códigos correspondentes, além de modificar o comportamento do `print`.

#### Imprimindo Caracteres Numéricos e Seus Códigos

```python
# Imprime os caracteres numéricos e seus códigos ASCII
for i in range(10):
    print(f"'{chr(48 + i)}' - {48 + i}")  # Imprime o caractere e seu código numérico
```
Isso imprimirá os caracteres numéricos '0' a '9' e seus códigos numéricos correspondentes.

# Adicionando Formatos Octal e Hexadecimal

```python
# Imprime os caracteres numéricos e seus códigos em octal e hexadecimal
for i in range(10):
    print(f"'{chr(48 + i)}' - {48 + i} - Octal: {oct(48 + i)} - Hexadecimal: {hex(48 + i)}")
```
Agora, além dos códigos numéricos, serão exibidos em octal e hexadecimal.

Lendo um Caractere e Imprimindo no Mesmo Formato

```python
# Lê um caractere da entrada padrão e imprime suas representações
caractere = input("Digite um caractere: ")
print(f"'{caractere}' - {ord(caractere)} - Octal: {oct(ord(caractere))} - Hexadecimal: {hex(ord(caractere))}")
```

Isso permite ao usuário inserir um caractere e exibir suas representações numéricas, octal e hexadecimal.

Caracteres Especiais em Python
Python trabalha com caracteres especiais, como 'ç' e 'ã'. Vejamos como eles são tratados:

```python
# Imprime caracteres especiais e seus códigos
print("'ç' -", ord('ç'))  # Imprime código numérico de 'ç'
print("'ã' -", ord('ã'))  # Imprime código numérico de 'ã'
```

