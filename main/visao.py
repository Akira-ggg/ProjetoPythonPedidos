from models.pedidos import Pedidos
from repository.pedido_repository import repository
nome = input("Qual o nome do produto: ")
print()
quantidade = int(input("Digite a quantidade"))
print()
preco = float(input("Qual o preco "))

pedido = Pedidos(nome,quantidade,preco)
rp = repository()
rp.adicionarSql(pedido)

