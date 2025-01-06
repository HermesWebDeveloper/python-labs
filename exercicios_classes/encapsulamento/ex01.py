# Exercício 1: Controle de Acesso em uma Conta Bancária
# Crie uma classe ContaBancaria com:

# Atributos: __titular, __saldo.
# Métodos:
# depositar(valor): Adiciona um valor ao saldo, desde que seja positivo.
# sacar(valor): Diminui o saldo se o valor for menor ou igual ao saldo disponível.
# exibir_saldo(): Exibe o saldo atual.
# Simule a criação de uma conta, faça depósitos e saques, e tente acessar diretamente o atributo __saldo para observar a restrição.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f'Valor de R$ {valor:.2f} depositado com sucesso!!')
    
    def sacar(self, valor):
        if valor > self.__saldo:
            print('Valor inválido para saque!')
        else:
            self.__saldo -= valor
            print(f'Valor de R$ {valor:.2f} sacado com sucesso!!')
    
    def exibir_saldo(self):
        print(f'O saldo bancário é de R$ {self.__saldo:.2f}')

    def __str__(self):
        return f'Titular: {self.__titular}, Saldo: {self.__saldo}'

conta1 = ContaBancaria('Hermes', 1000)
conta1.depositar(100)
conta1.sacar(50)
conta1.sacar(1050)
conta1.depositar(550)
print(f'Conta 1: {conta1}')
conta1.exibir_saldo