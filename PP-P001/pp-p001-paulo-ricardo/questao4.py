#QUESTÃO 4.1
#Declare uma variável nome atribuindo a ela seu nome completo;
completeName = "Paulo Ricardo Santos Nascimento"

#QUESTÃO 4.2
""" Pesquise por funcionalidades já implementadas nas strings e separe 
em duas variáveis novas seu nome do seu sobrenome; """

partsOfTheName = completeName.split()
print(partsOfTheName)

firstName = partsOfTheName[0]
surname = partsOfTheName[len(partsOfTheName) - 1]

if firstName > surname:
    print(f"O primeiro nome {firstName} antecede em ordem alfabética o sobrenome {surname}.")
elif(firstName < surname):
    print(f"O sobrenome {surname} antecede em ordem alfabética o primeiro nome {firstName}.")
else:
    print("Os nomes são iguais em ordem alfabética.") 

#QUESTÃO 4.3
# Verifique a quantidade de caracteres de cada uma das novas variáveis;
print(f"A quantidade de caracteres no primeiro nome: {len(firstName)}")
print(f"A quantidade de caracteres no sobrenome: {len(surname)}")

#QUESTÃO 4.4
#Verifique se seu nome é uma palíndromo;

if firstName == firstName[::-1]:
    print(f"O nome {firstName} é palindromo")
else:
    print(f"O nome {firstName} não é palindromo")


