print('Caracteres numéricos e correspondentes códigos númericos decimais:')
for i in range(10):
    print(f"'{chr(ord('0') + i)}' - {ord('0') + i}")
print(' ')

print('Caracteres numéricos e correspondentes códigos númericos dec, octa, hexa:')
for i in range(10):
    print(f"'{chr(ord('0') + i)}' - Decimal: {ord('0') + i}, Octal: {oct(ord('0') + i)}, Hexadecimal: {hex(ord('0') + i)}")
print(' ')

print('Caracteres numéricos e correspondentes códigos númericos dec, octa, hexa:')
caractere = input("Digite um caractere: ")
print(f"'{caractere}' - Decimal: {ord(caractere)}, Octal: {oct(ord(caractere))}, Hexadecimal: {hex(ord(caractere))}")
print(' ')

print('Caracteres especiais e correspondentes códigos númericos dec, octa, hexa:')
caractere = input("Digite um caractere especial: ")
print(f"'{caractere}' - Decimal: {ord(caractere)}, Octal: {oct(ord(caractere))}, Hexadecimal: {hex(ord(caractere))}")
