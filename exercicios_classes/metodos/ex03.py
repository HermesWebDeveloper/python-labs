# Método Especial: Crie uma classe chamada Retangulo que aceita largura e altura no construtor (__init__). Implemente o método especial __str__ para retornar uma representação como "Retângulo: largura x altura" e o método especial __eq__ para verificar se dois retângulos são iguais (mesmas dimensões).

class Retangulo:

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def __str__(self):
        return f'Retângulo: {self.altura} x {self.largura}'

    def __eq__(self, other):
        if not isinstance(other, Retangulo):
            return False
        return other.altura == self.altura and self.largura == other.largura

def exercicio03():
    retangulo1 = Retangulo(10, 3)
    retangulo2 = Retangulo(10, 3)
    retangulo3 = Retangulo(8, 4)

    print(retangulo1)
    print(retangulo2)
    print(retangulo3)

    print(retangulo1 == retangulo2)
    print(retangulo1 == retangulo3)

exercicio03()