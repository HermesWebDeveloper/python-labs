
lista_compras = []

numero_de_vezes = int(input('Quantas compras você deseja fazer: '))

for contador in range(numero_de_vezes):
    item = input(f'Digite o item {contador + 1}: ')
    lista_compras.append(item)

print(f'Lista de compras atual: {lista_compras}')