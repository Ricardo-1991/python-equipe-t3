L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Lista ao contrário - {L[::-1]}")
print(f"Último elemento - {L[-1::]}")
print(f"Todos, menos o último elemento - {L[:-1:]}")
print(f"Lista ao contrário, 2 em 2 elementos - {L[::-2]}")
print(f"Lista do penúltimo até o final - {L[-2::]}")
print(f"Todos, exceto os dois últimos - {L[:-2:]}")

L2 = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]

userInput = input("Ano de nascimento, Escolha de 0 a 11: ")

index = int(userInput)
sign = L2[index]
print(f"Signo: {sign}")