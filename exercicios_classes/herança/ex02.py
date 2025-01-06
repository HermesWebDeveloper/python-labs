# Exercício 2: Sistema de Pedidos
# Em uma loja de fast food, crie:

# Uma classe Pedido com os atributos numero_pedido e itens.
# Uma classe filha PedidoBebida, que adiciona o atributo tamanho (por exemplo: pequeno, médio, grande).
# Uma classe filha PedidoComida, que adiciona o atributo acompanhamentos (por exemplo: batata, salada).
# Simule a criação de pedidos de bebida e comida e exiba as informações de cada pedido.

class Pedido:
    def __init__(self, numero_pedido, itens):
        self.numero_pedido = numero_pedido
        self.itens = itens
    def __str__(self):
        return f'Nº do pedido: {self.numero_pedido}, itens: {self.itens}'
    
class PedidoBebida(Pedido):
    def __init__(self, numero_pedido, itens, tamanho):
        super().__init__(numero_pedido, itens)
        self.tamanho = tamanho
    def __str__(self):
        return f'{super().__str__()}, Tamanho: {self.tamanho}'
    
class PedidoComida(Pedido):
    def __init__(self, numero_pedido, itens, acompanhamentos):
        super().__init__(numero_pedido, itens)
        self.acompanhamentos = acompanhamentos
    def __str__(self):
        return f'{super().__str__()}, Acompanhamentos: {self.acompanhamentos}'

pedidoBebida1 = PedidoBebida(1, ['Suco de Laranja', 'Guaraná'], 'Pequeno')
pedidoComida1 = PedidoComida(2, ['Arroz', 'Feijão'], ['Ovo Frito', 'Salada', 'Batatinha'])

print(pedidoBebida1)
print(pedidoComida1)