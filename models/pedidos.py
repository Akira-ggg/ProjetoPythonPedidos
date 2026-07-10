class Pedidos:
    def __init__(self,id ,nome,quantidade,preco):
        self.__id = id
        self.__nome = nome
        self.__quantidade = quantidade
        self.__preco = preco

    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id
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

