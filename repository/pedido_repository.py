from models.pedidos import Pedidos
from pathlib import Path


class repository:

    def __init__(self):
        self.pasta = Path("dataBase")
        self.arquivo = self.pasta / "Pedidos"
        if not self.pasta.exists():
            self.pasta.mkdir()

        if not self.arquivo.exists():
            self.arquivo.touch()

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
