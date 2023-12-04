from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        num_elementos = int(input("Quantos elementos deseja adicionar? "))
        for _ in range(num_elementos):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de nomes está vazia.")
        else:
            lista_ordenada = sorted(self.__lista)
            tamanho_lista = len(lista_ordenada)
            if tamanho_lista % 2 == 0:
                mediana = (lista_ordenada[tamanho_lista // 2 - 1] + lista_ordenada[tamanho_lista // 2]) / 2
            else:
                mediana = lista_ordenada[tamanho_lista // 2]
            print(f"A mediana dos nomes é: {mediana}")

    def mostraMenor(self):
        if not self.__lista:
            print("A lista de nomes está vazia.")
        else:
            menor_nome = min(self.__lista)
            print(f"O menor nome é: {menor_nome}")

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de nomes está vazia.")
        else:
            maior_nome = max(self.__lista)
            print(f"O maior nome é: {maior_nome}")

    def __str__(self):
        if not self.__lista:
            return "Lista de nomes vazia."
        else:
            return "\n".join(str(nome) for nome in self.__lista)

class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        while True:
            try:
                num_elementos = int(input("Quantos elementos deseja adicionar? "))
                break
            except ValueError:
                print("Por favor, insira um número válido.")

        for _ in range(num_elementos):
            while True:
                try:
                    dia = int(input("Digite o dia: "))
                    mes = int(input("Digite o mês: "))
                    ano = int(input("Digite o ano: "))
                    nova_data = Data(dia, mes, ano)
                    self.__lista.append(nova_data)
                    break
                except ValueError:
                    print("Data inválida. Por favor, insira novamente.")
    
    def mostraMediana(self):
        if not self.__lista:
            print("A lista de datas está vazia.")
        else:
            lista_ordenada = sorted(self.__lista)
            tamanho_lista = len(lista_ordenada)
            if tamanho_lista % 2 == 0:
                mediana = (lista_ordenada[tamanho_lista // 2 - 1] + lista_ordenada[tamanho_lista // 2]) / 2
            else:
                mediana = lista_ordenada[tamanho_lista // 2]
            print(f"A mediana das datas é: {mediana}")
    
    def mostraMenor(self):
        if not self.__lista:
            print("A lista de datas está vazia.")
        else:
            menor_data = min(self.__lista)
            print(f"A menor data é: {menor_data}")
    
    def mostraMaior(self):
        if not self.__lista:
            print("A lista de datas está vazia.")
        else:
            maior_data = max(self.__lista)
            print(f"A maior data é: {maior_data}")
    
    def __str__(self):
        if not self.__lista:
            return "Lista de datas vazia."
        else:
            return "\n".join(str(data) for data in self.__lista)
        

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        num_elementos = int(input("Quantos elementos deseja adicionar? "))
        for _ in range(num_elementos):
            salario = float(input("Digite um salário: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de salários está vazia.")
        else:
            lista_ordenada = sorted(self.__lista)
            tamanho_lista = len(lista_ordenada)
            if tamanho_lista % 2 == 0:
                mediana = (lista_ordenada[tamanho_lista // 2 - 1] + lista_ordenada[tamanho_lista // 2]) / 2
            else:
                mediana = lista_ordenada[tamanho_lista // 2]
            print(f"A mediana dos salários é: {mediana}")

    def mostraMenor(self):
        if not self.__lista:
            print("A lista de salários está vazia.")
        else:
            menor_salario = min(self.__lista)
            print(f"O menor salário é: {menor_salario}")

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de salários está vazia.")
        else:
            maior_salario = max(self.__lista)
            print(f"O maior salário é: {maior_salario}")

    def __str__(self):
        if not self.__lista:
            return "Lista de salários vazia."
        else:
            return "\n".join(str(salario) for salario in self.__lista)

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        num_elementos = int(input("Quantos elementos deseja adicionar? "))
        for _ in range(num_elementos):
            idade = int(input("Digite uma idade: "))
            self.__lista.append(idade)

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de idades está vazia.")
        else:
            lista_ordenada = sorted(self.__lista)
            tamanho_lista = len(lista_ordenada)
            if tamanho_lista % 2 == 0:
                mediana = (lista_ordenada[tamanho_lista // 2 - 1] + lista_ordenada[tamanho_lista // 2]) / 2
            else:
                mediana = lista_ordenada[tamanho_lista // 2]
            print(f"A mediana das idades é: {mediana}")

    def mostraMenor(self):
        if not self.__lista:
            print("A lista de idades está vazia.")
        else:
            menor_idade = min(self.__lista)
            print(f"A menor idade é: {menor_idade}")

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de idades está vazia.")
        else:
            maior_idade = max(self.__lista)
            print(f"A maior idade é: {maior_idade}")

    def __str__(self):
        if not self.__lista:
            return "Lista de idades vazia."
        else:
            return "\n".join(str(idade) for idade in self.__lista)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    print("Fim do teste!!!")

def menu_listas():
    while True:
        print("\nEscolha o tipo de lista:")
        print("1 - Lista de Nomes")
        print("2 - Lista de Datas")
        print("3 - Lista de Salários")
        print("4 - Lista de Idades")
        print("0 - Sair")

        escolha_lista = input("Digite o número da opção desejada: ")

        if escolha_lista == "1":
            menu_opcoes(ListaNomes())
        elif escolha_lista == "2":
            menu_opcoes(ListaDatas())
        elif escolha_lista == "3":
            menu_opcoes(ListaSalarios())
        elif escolha_lista == "4":
            menu_opcoes(ListaIdades())
        elif escolha_lista == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_opcoes(lista):
    while True:
        
        print("\nOpções para Lista:")
        print("1 - Adicionar elemento")
        print("2 - Mostrar mediana")
        print("3 - Mostrar menor elemento")
        print("4 - Mostrar maior elemento")
        print("0 - Voltar ao menu anterior")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            lista.entradaDeDados()
        elif escolha == "2":
            lista.mostraMediana()
        elif escolha == "3":
            lista.mostraMenor()
        elif escolha == "4":
            lista.mostraMaior()
        elif escolha == "0":
        
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_listas()
