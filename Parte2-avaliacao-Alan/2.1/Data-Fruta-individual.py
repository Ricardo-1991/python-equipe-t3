from abc import ABC, abstractmethod

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 1900 or ano > 2100:
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

    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        print("Quantos elementos irá existir na lista nomes? ")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite o nome {i+1}:")
            valor = input()
            self.__lista.append(valor)

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if len(listaOrdenada) % 2 == 0:
            pos = (len(listaOrdenada) // 2) - 1
        else:
            pos = len(listaOrdenada) // 2
        print(f"Mediana dos nomes: {listaOrdenada[pos]}")    

    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Primeiro nome: {listaOrdenada[0]}")

    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Último nome: {listaOrdenada[len(listaOrdenada) - 1]}")   

    def listarEmOrdem(self):
        return sorted(self.__lista)

    def __str__(self):
        separador = ", "
        string = separador.join(self.__lista)
        return string

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        print("Quantos elementos irá existir na lista data? ")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite a data {i + 1} no seguinte formato: DD/MM/YYYY")
            valor = input()
            dia = int(valor.split(("/"))[0])
            mes = int(valor.split(("/"))[1])
            ano = int(valor.split(("/"))[2])
            data = Data(dia, mes, ano)
            self.__lista.append(data)
    
    def mostraMediana(self):
        listaOrdenada = self.ordena()
        if len(listaOrdenada) % 2 == 0:
            pos = (len(listaOrdenada) // 2) - 1
        else:
            pos = len(listaOrdenada) // 2
        print(f"Mediana das datas: {listaOrdenada[pos]}")     

    def mostraMenor(self):
        listaOrdenada = self.ordena()
        print(f"Primeira data: {listaOrdenada[0]}")
    
    def mostraMaior(self):
        listaOrdenada = self.ordena()
        print(f"Última data: {listaOrdenada[len(listaOrdenada) - 1]}")
    
    def listarEmOrdem(self):
        return self.ordena()

    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string

    def ordena(self):
        listaOrdenada = self.__lista.copy()
        for i in range(len(listaOrdenada)):
            for j in range(len(listaOrdenada) - i - 1):
                if listaOrdenada[j] > listaOrdenada[j + 1]:
                    aux = listaOrdenada[j]
                    listaOrdenada[j] = listaOrdenada[j + 1]
                    listaOrdenada[j + 1] = aux
        return listaOrdenada

class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        print("Quantos elementos irá existir na lista salário? ")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite o salário {i+1}:")
            valor = float(input())
            self.__lista.append(valor)

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if len(listaOrdenada) % 2 == 0:
            resultado = ListaSalarios.calculaMedia(listaOrdenada[(len(listaOrdenada)//2)-1], listaOrdenada[(len(listaOrdenada)//2)])
        else:
            resultado = listaOrdenada[len(listaOrdenada) // 2]
        print(f"Mediana dos salários: {resultado}")     

    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Menor salário: {listaOrdenada[0]}")

    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Maior salário: {listaOrdenada[len(listaOrdenada) - 1]}") 
    
    def listarEmOrdem(self):
        return sorted(self.__lista)

    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string
    
    @staticmethod
    def calculaMedia(a, b):
        media = (a + b) / 2
        return media

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        print("Quantos elementos irá existir na lista idade: ?")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite a idade {i+1}:")
            valor = int(input())
            self.__lista.append(valor)
    
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if len(listaOrdenada) % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(len(listaOrdenada)//2)-1], listaOrdenada[(len(listaOrdenada)//2)])
        else:
            resultado = listaOrdenada[len(listaOrdenada) // 2]
        print(f"Mediana das idades: {resultado}")     
    
    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Menor idade: {listaOrdenada[0]}")
    
    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Maior idade: {listaOrdenada[len(listaOrdenada) - 1]}") 

    def listarEmOrdem(self):
        return sorted(self.__lista)
    
    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string
    
    @staticmethod
    def calculaMedia(a, b):
        media = (a + b) / 2
        return media

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
        print("Lista em Ordem:")
        print(lista.listarEmOrdem())
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
