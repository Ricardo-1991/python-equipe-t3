for i in range(10):
    # Imprime o caractere e seu código numérico
    print(f"'{chr(ord('0') + i)}' - {ord('0') + i}")

#Modificação para retonar número octal e hexadecimal

for i in range(10):
    # Imprime o caractere e seus códigos numéricos
    print(f"'{chr(ord('0') + i)}' - Decimal: {ord('0') + i}, Octal: {oct(ord('0') + i)}, Hexadecimal: {hex(ord('0') + i)}")

#Solicitando dados ao usuário

caractere = input("Digite um caractere: ")

print(f"'{caractere}' - Decimal: {ord(caractere)}, Octal: {oct(ord(caractere))}, Hexadecimal: {hex(ord(caractere))}")

"""
Em Python, os caracteres especiais como 'ç' e 'ã' são tratados como caracteres Unicode. Você pode usar 
esses caracteres diretamente em strings e operações relacionadas a strings sem problemas.
Um exemplo incluindo os caracteres especiais no código anterior:
"""

caractere = input("Digite um caractere: ")

print(f"'{caractere}' - Decimal: {ord(caractere)}, Octal: {oct(ord(caractere))}, Hexadecimal: {hex(ord(caractere))}")

exemplo_especial = 'çã'
print(f"Exemplo com caracteres especiais: '{exemplo_especial}'")
