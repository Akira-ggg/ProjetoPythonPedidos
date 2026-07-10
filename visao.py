from models.pedidos import Pedidos
from repository.pedido_repository import repository

def main():
    id = int(input("Informe o id: \n"))
    nome = input("Qual o nome do produto: ")
    print()

    quantidade = int(input("Digite a quantidade: "))
    print()

    preco = float(input("Qual o preço: "))

    pedido = Pedidos(id, nome, quantidade, preco)

    rp = repository()
    rp.adicionarSql(pedido)

if __name__ == "__main__":
    main()