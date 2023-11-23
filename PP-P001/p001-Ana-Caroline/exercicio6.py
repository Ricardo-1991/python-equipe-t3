print('Manipulação de listas:')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[::-1])  # Lista invertida
print(lista[-1:])  # Apenas o último elemento
print(lista[:-1:])  # Exclui o último elemento
print(lista[::-2])  # Lista invertida pulando de 2 em 2
print(lista[-2:])  # Últimos dois elementos
print(lista[:-2:])  # Exclui os dois últimos elementos
print(' ')

print('Animal do Calendário Chinês:')
def determinar_animal_calendario_chines(ano_nascimento):
    animais = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]
    ano_no_calendario_chines = ano_nascimento % 12
    return animais[ano_no_calendario_chines]

ano_nascimento = int(input("Digite o ano de nascimento: "))
signo_chines = determinar_animal_calendario_chines(ano_nascimento)
print(f"O signo chinês associado ao ano é: {signo_chines}")
