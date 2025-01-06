nLinhas = int(input('Digite o número de linhas da matriz: '))
nColunas = int(input('Digite o número de colunas da matriz: '))

matriz = []

for i in range(nLinhas):
    novaLinha = []
    for j in range(nColunas):
        elemento = int(input(f'Digite o elemento (número inteiro) da linha {i} e coluna {j}: '))
        novaLinha.append(elemento)
    matriz.append(novaLinha)

if nLinhas == nColunas:
    qtd_1 = 0

    print('-'*20)
    for i in range(nLinhas):
        for j in range(nColunas):
            print(f'{matriz[i][j]:3}', end=' ')
            if matriz[i][j] == 1:
                qtd_1 += 1
        print()
    print('-'*20)

    if qtd_1 == nLinhas:
        print('A matriz é identidade!')
    else:
        print('A matriz não é identidade!')
else:
    print('A matriz não é identidade!')