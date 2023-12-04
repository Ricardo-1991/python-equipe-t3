
from abc import ABC, abstractmethod

class Data:
    
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
    
	
	
	Data (int _dia, int _mes, int _ano) {
		dia = _dia;
		mes = _mes;
		ano = _ano;
	}
	string toString() {
		string ret = "";
		ret.append(to_string(dia));
		ret.append("/");
		ret.append(to_string(mes));
		ret.append("/");
		ret.append(to_string(ano));
		return ret;
	}

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

class ListaSalarios(AnaliseDados): # featureTiago

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

class ListaIdades(AnaliseDados):
    
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
            # Média dos dois valores no meio
            mediana = (lista_ordenada[tamanho_lista // 2 - 1] + lista_ordenada[tamanho_lista // 2]) / 2
        else:
            # Valor no meio para lista ímpar
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

    print("Fim do teste!!!")

    if __name__ == "__main__":
        main()
