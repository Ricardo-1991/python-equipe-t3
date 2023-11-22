print('Manipulação de lista:')
L = [1,2,3,4,5,6,7,8,9]
print(L[::-1]) # lista invertida
print(L[-1::]) # apenas o último elemento
print(L[:-1:]) # exclui o último elemento
print(L[::-2]) # lista invertida pulando de 2 em 2
print(L[-2::]) # últimos dois elementos
print(L[:-2:]) # exlclui os dois últimos elementos
print(' ')

print('Animal do Calendário Chinês:')
def calcular_animal_calendario_chines(ano_nascimento):
    animais = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]
    ano_calendario_chines = ano_nascimento % 12
    return animais[ano_calendario_chines]

ano_nascimento = int(input("Digite o ano de nascimento: "))
animal_calendario_chines = calcular_animal_calendario_chines(ano_nascimento)
print(f"Seu animal no calendário chinês é: {animal_calendario_chines}")
