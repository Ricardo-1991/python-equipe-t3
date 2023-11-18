#Questão 6.1
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Imprime a lista ao contrárioª - {L[::-1]}")
print(f"Imprime apenas o último elementoª - {L[-1::]}")
print(f"Imprime todos, menos o último elemento - {L[:-1:]}")
print(f"Imprime a lista ao contrário, pulando de 2 em 2 elementos - {L[::-2]}")
print(f"Imprime a lista do penultimo até o finalª - {L[-2::]}")
print(f"imprime todos, exceto os dois últimos - {L[:-2:]}")

#Questão 6.2

L2 = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]

userInput = input("Qual o ano do seu nascimento? Escolha de 0 a 11: ")

try:
    index = int(userInput)
    sign = L2[index]
    print(f"Signo: {sign}")
except (ValueError, IndexError):
    print("Ano de nascimento inválido.")

            

