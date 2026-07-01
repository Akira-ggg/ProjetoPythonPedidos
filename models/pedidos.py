class Pedidos:
    def __init__(self,nome,quantidade,preco):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self,quantidade):
        self.__quantidade = quantidade

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,preco):
        self.__preco = preco

