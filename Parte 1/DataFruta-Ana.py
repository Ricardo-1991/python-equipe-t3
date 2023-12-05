
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
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        pass

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        pass    

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        pass

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        pass    

    def __str__(self):
        pass
	
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
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        pass

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        pass    

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        pass

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        pass
    
    def __str__(self):
        pass

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        pass
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        pass    
    
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        pass
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        pass

    def __str__(self):
        pass

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

if __name__ == "__main__":
    main()
