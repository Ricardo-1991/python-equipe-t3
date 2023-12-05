
from abc import ABC, abstractmethod

class Data: #Alan feature
    def __init__(self, dia = 1, mes = 1, ano = 2000):
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

class ListaNomes(AnaliseDados): #Ricardo feature
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        try:
            num_elementos = int(input("Quantos elementos na lista? "))
            for _ in range(num_elementos):
                nome = input("Digite um nome: ")
                self.__lista.append(nome)
        except ValueError:
            print("Por favor, insira um número válido.")


    def mostraMediana(self):
        if not self.__lista:
            print("A lista está vazia.")
            return

        lista_ordenada = sorted(self.__lista)
        tamanho_lista = len(lista_ordenada)

        if tamanho_lista % 2 == 0:
            meio1 = tamanho_lista // 2
            meio2 = meio1 - 1
            mediana = lista_ordenada[meio1], lista_ordenada[meio2]
        else:
            meio = tamanho_lista // 2
            mediana = lista_ordenada[meio]

        print("Mediana da lista de nomes:", mediana)
    def mostraMenor(self):
        if not self.__lista:
            print("A lista está vazia.")
            return

        menor_elemento = min(self.__lista)
        print("Menor elemento da lista de nomes:", menor_elemento)  

    def mostraMaior(self):
        if not self.__lista:
            print("A lista está vazia.")
            return

        menor_elemento = max(self.__lista)
        print("Maior elemento da lista de nomes:", menor_elemento)     

    def __str__(self):
        return f"Lista de Nomes: {self.__lista}"
    pass
	
class ListaDatas(AnaliseDados): #Ana feature
        
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

class ListaSalarios(AnaliseDados): #Tiago feature

    def __init__(self):
        super().__init__(float)
        self.__lista = []        

    def entradaDeDados(self):
        while True:
            try:
                n = int(input("Quantos elementos na lista de salários? "))
                for _ in range(n):
                    salario = float(input("Digite um salário: "))
                    self.__lista.append(salario)
                break
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir valores numéricos.")
    pass

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        tamanho = len(sorted_lista)
        
        if tamanho % 2 == 0:
            mediana = (sorted_lista[tamanho // 2 - 1] + sorted_lista[tamanho // 2]) / 2
        else:
            mediana = sorted_lista[tamanho // 2]

        print(f"Mediana: {mediana}")
    pass

    def mostraMenor(self):
        if not self.__lista:
            print("A lista está vazia.")
            return
        menor = min(self.__lista)
        print(f"Menor elemento: {menor}")
    pass

    def mostraMaior(self):
        if not self.__lista:
            print("A lista está vazia.")
            return
        maior = max(self.__lista)
        print(f"Maior elemento: {maior}")
    pass    
    
    def __str__(self):
        return f"Lista de Salários: {self.__lista}"
    pass

class ListaIdades(AnaliseDados): #Rafaela feature
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        while True:
            try:
                n = int(input("Quantos elementos existem na lista de idades? "))
                for _ in range(n):
                    idade = int(input("Digite uma idade: "))
                    self.__lista.append(idade)
                break
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir valores inteiros.")
    
    def mostraMediana(self):
        if not self.__lista:
            print("A lista está vazia.")
            return
        
        lista_ordenada = sorted(self.__lista)
        tamanho_lista = len(lista_ordenada)

        if tamanho_lista % 2 == 0:
            mediana = (lista_ordenada[tamanho_lista // 2 - 1] + lista_ordenada[tamanho_lista // 2]) / 2
        else:
            mediana = lista_ordenada[tamanho_lista // 2]

        print(f"Mediana das idades: {mediana}")   
    
    def mostraMenor(self):
        if not self.__lista:
            print("A lista está vazia.")
            return
        menor_idade = min(self.__lista)
        print(f"Menor idade: {menor_idade}")
    
    def mostraMaior(self):
        if not self.__lista:
            print("A lista está vazia.")
            return
        maior_idade = max(self.__lista)
        print(f"Maior idade: {maior_idade}")

    def __str__(self):
        return f"Lista de Idades: {self.__lista}"

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

if __name__ == "__main__":
    main()
    print("Fim do teste!!!")