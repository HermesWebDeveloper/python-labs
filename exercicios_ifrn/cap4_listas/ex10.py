from funcoes_matriz import gerarMatrizAleatoria
from funcoes_matriz import matrizEsparsa
from funcoes_matriz import exibirMatriz

def exercicio10():
    nLinhas = int(input('Digite o número de linhas da matriz: '))
    nColunas = int(input('Digite o número de colunas da matriz: '))

    matriz = gerarMatrizAleatoria(nLinhas, nColunas)
    exibirMatriz(matriz)    

    if matrizEsparsa(matriz):
        print('A matriz é esparsa!')
    else:
        print('A matriz não é esparsa!')

exercicio10()