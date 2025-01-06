# Método de Classe Crie uma classe chamada Funcionario com os atributos nome e salario_base. Inclua um método de classe chamado ajustar_taxa_aumento que altera a taxa de aumento salarial (um atributo de classe). Em seguida, crie dois funcionários e simule o ajuste da taxa para aplicar o aumento.

class Funcionario:
    taxa_aumento_salarial = 0.1

    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def __str__(self):
        return (
            f'Nome: {self.nome}, salario: {self.salario_base} e taxa: {Funcionario.taxa_aumento_salarial}'
        )
    
    @classmethod
    def ajustar_taxa_aumento(cls, novaTaxa):
        cls.taxa_aumento_salarial = novaTaxa

def simulacao():
    funcionario1 = Funcionario('Hermes', 5000)
    funcionario2 = Funcionario('Keyse', 6500)

    print(f'{funcionario1}')
    print(f'{funcionario2}')

    nova_taxa = float(input('Digite o valor decimal da nova taxa: '))

    Funcionario.ajustar_taxa_aumento(nova_taxa)
    print(f'{funcionario1}')
    print(f'{funcionario2}')

simulacao()