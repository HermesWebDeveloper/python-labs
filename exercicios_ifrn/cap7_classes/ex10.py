class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calcularDistancia(self, outro_ponto):
        dist = ((outro_ponto.x - self.x)**2 + (outro_ponto.y - self.y)**2)**(1/2)
        return dist

def exercicio10():
    ponto1_x = float(input('Digite o ponto 1 em x: '))
    ponto1_y = float(input('Digite o ponto 1 em y: '))
    ponto2_x = float(input('Digite o ponto 2 em x: '))
    ponto2_y = float(input('Digite o ponto 2 em y: '))

    ponto1 = Ponto(ponto1_x, ponto1_y)
    ponto2 = Ponto(ponto2_x, ponto2_y)

    print(f'Distância entre os pontos: {ponto1.calcularDistancia(ponto2):.2f}')

exercicio10()