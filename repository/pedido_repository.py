from models.pedidos import Pedidos
from pathlib import Path
import sqlite3 


class repository:

    def __init__(self):
        self.pasta = Path("dataBase")
        self.arquivo = self.pasta / "Pedidos"
        self.arquivoSQL = self.pasta / "Pedidos.db"
        if not self.pasta.exists():
            self.pasta.mkdir()

        if not self.arquivo.exists():
            self.arquivo.touch()
        self.connection = sqlite3.connect(self.arquivoSQL)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
           CREATE TABLE IF NOT EXISTS pedidos(
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            quantidade INTEGER NOT NULL,
                            preco REAL NOT NULL 
                            
                            
                            
                            
                            );



         """)
        self.connection.commit()

    def lista(self):
        lista_pedidos = []
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:
                vetor = linha.strip().split(";")
                nome = vetor[0]
                quantidade = int(vetor[1])
                preco = float(vetor[2])
                base = Pedidos(nome, quantidade, preco)
                lista_pedidos.append(base)
        return lista_pedidos

    def adicionar(self, pedido):
        lista = self.lista()
        for pedido_existe in lista:
            if pedido_existe.nome == pedido.nome:
                raise Exception("Pedido ja existe")
        with open(self.arquivo, "a", encoding="utf-8") as arquivo:
            linha = pedido.nome + ";" + str(pedido.quantidade) + ";" + str(pedido.preco )+ "\n"
            arquivo.write(linha)


    def adicionarSql(self,pedido):
        lista = self.filtro()
        for pediso_existe in lista:
            if pediso_existe.id == pedido.id:
                raise Exception("Pedido ja existe")
        self.cursor.execute("""
           INSERT INTO pedidos(nome, quantidade, preco)
                            VALUES (?,?,?)
 



         """, (pedido.nome, pedido.quantidade, pedido.preco))
        self.connection.commit()

    def filtro(self):
        lista = []
        self.cursor.execute("""SELECT id, nome, quantidade, preco FROM Pedidos""")
        for linha in self.cursor.fetchall():
            pedidos = Pedidos(
                linha[0],
                linha[1],
                linha[2],
                linha[3]


            )
            lista.append(pedidos)
        return lista
        


        

        
        
        
