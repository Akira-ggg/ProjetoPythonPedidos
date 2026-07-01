from models.pedidos import Pedidos


class repository:
    dados = "dataBase/Pedidos.txt"

    def lista(self):
        lista_pedidos = []
        with open(self.dados, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:
                vetor = linha.strip().split(";")
                nome = vetor[0]
                quantidade = int(vetor[1])
                preco = float(vetor[2])
                base = Pedidos(nome, quantidade, preco)
                lista_pedidos.append(base)
        return lista_pedidos

    def adicionar(self, pedidos):
        lista = self.lista()
        with open(self.dados, "a", encoding="utf-8") as arquivo:
            linha = pedidos.nome + ";" + pedidos.quantidade + ";" + pedidos.preco + "\n"
            arquivo.write(linha)
