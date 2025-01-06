from exercicios_ifrn.cap4.funcoes_matriz import exibirMatriz
import random

def exercicio9():
    nLinhas = int(input('Digite o número de linhas da matriz: '))
    nColunas = int(input('Digite o número de colunas da matriz: '))

    matriz = []

    for i in range(nLinhas):
        linha = []
        for j in range(nColunas):
            numero_aleatorio = random.randint(1, 10)
            linha.append(numero_aleatorio)
        matriz.append(linha)

    exibirMatriz(matriz)
    matriz_diagonal = matrizDiagonal(matriz)
    if matriz_diagonal:
        print('A matriz é diagonal!')
    else:
        print('A matriz não é diagonal!')


def matrizDiagonal(matriz):

    nLinhas = len(matriz)
    nColunas = len(matriz[0])
    matriz_diagonal = True

    for i in range(nLinhas):
        for j in range(nColunas):
            if (j != i) and (matriz[i] != 0 or matriz[j] != 0):
                matriz_diagonal = False
    
    return matriz_diagonal

exercicio9()