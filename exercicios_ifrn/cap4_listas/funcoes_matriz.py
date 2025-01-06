import random

def exibirMatriz(matriz):
    nLinhas = len(matriz)
    nColunas = len(matriz[0])

    print('-'*20)
    for i in range(nLinhas):
        for j in range(nColunas):
            print(f'{matriz[i][j]:3}', end=' ')
        print()
    print('-'*20)

def gerarMatrizAleatoria(nLinhas, nColunas):
    matriz = []
    
    for i in range(nLinhas):
        linha = []
        for j in range(nColunas):
            linha.append(random.randint(0, 4))
        matriz.append(linha)

    return matriz

def matrizEsparsa(matriz):
    nLinhas = len(matriz)
    nColunas = len(matriz[0])
    qtd_elementos = nLinhas * nColunas
    elementos_nulos = 0

    for i in range(nLinhas):
        for j in range(nColunas):
            if matriz[i][j] == 0: 
                elementos_nulos += 1

    if elementos_nulos > (qtd_elementos - elementos_nulos):
        return True
    else:
        return False