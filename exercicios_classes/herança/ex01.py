# Exercício 1: Cadastro de Funcionários
# Imagine um sistema para gerenciar uma empresa. Crie:

# Uma classe Funcionario com os atributos nome, cpf e salario.
# Uma classe filha Gerente, que herda de Funcionario e adiciona o atributo departamento.
# Uma classe filha Vendedor, que herda de Funcionario e adiciona o atributo meta_vendas.
# Crie instâncias de cada classe e simule ações, como calcular o salário com base em bônus específicos para gerentes e vendedores.

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf} e salario: {self.salario}'

class Gerente(Funcionario):
    bonus = 0.10

    def __init__(self, nome, cpf, salario, departamento):
        super().__init__(nome, cpf, salario)
        self.departamento = departamento

    def calcular_salario(self):
        self.salario = self.salario + (self.salario * Gerente.bonus)

    def __str__(self):
        return f'{super().__str__()}, Hierarquia: Gerente, Departamento: {self.departamento}'

class Vendedor(Funcionario):

    bonus = 0.5

    def __init__(self, nome, cpf, salario, meta_vendas):
        super().__init__(nome, cpf, salario)
        self.meta_vendas = meta_vendas
    
    def calcular_salario(self):
        self.salario = self.salario + (self.salario * Vendedor.bonus)

    def __str__(self):
        return f'{super().__str__()}, Hierarquia: Vendedor, Meta de Vendas: {self.meta_vendas}'

vendedor1 = Vendedor('Hermes', '63130775390', 1500, 12)
gerente1 = Gerente('Rubens', '12345635293', 2500, 'geral')

print(vendedor1)
print(gerente1)

print('Calculando novo salário...')
vendedor1.calcular_salario()
gerente1.calcular_salario()

print(vendedor1)
print(gerente1)