# Exercício 1: Sistema de Transporte
# Em uma cidade, diferentes meios de transporte têm formas distintas de calcular a tarifa. Crie:

# Uma classe Transporte com o método calcular_tarifa.
# Classes filhas Onibus, Trem e Uber que sobrescrevem o método para calcular tarifas com base em regras fictícias:
# Ônibus: tarifa fixa de R$5.
# Trem: R$3 por estação.
# Uber: R$2 por quilômetro.
# Simule o cálculo de tarifas para cada tipo de transporte.

class Transporte:
    def calcular_tarifa(self):
        pass

class Onibus(Transporte):
    def calcular_tarifa(self):
        return 'Tarifa fixa de R$ 5,00'

class Trem(Transporte):
    def calcular_tarifa(self):
        return 'R$ 3,00 por estação'

class Uber(Transporte):
    def calcular_tarifa(self):
        return 'R$ 2,00 por quilômetro'
    
transportes = [Uber(), Onibus(), Trem()]

for transporte in transportes:
    print(transporte.calcular_tarifa())