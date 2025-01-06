import math

class ContaInvestimento :
    def __init__(self, numero, saldo, cliente, taxaJuros):
        self.numero = numero
        self.saldo = saldo
        self.saldoInicial = saldo
        self.cliente = cliente
        self.operacoes = {}
        self.qtd_operacoes = 0
        self.taxaJuros = taxaJuros
    def exibirSaldo(self):
        print('EXIBINDO SALDO:')
        print(f'Conta de nº: {self.numero}')
        print(f'Cliente: {self.cliente}')
        print(f'Saldo: {self.saldo}')
        print(f'Taxa de Juros: {self.taxaJuros}')
    def sacar(self, valor):
        if valor > self.saldo:
            print('Valor indisponível na conta!')
        else:
            self.saldo -= valor
            self.operacoes.update({self.qtd_operacoes: ['Saque', valor]})
            self.qtd_operacoes += 1
    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.update({self.qtd_operacoes: ['Depósito', valor]})
        self.qtd_operacoes += 1
    def exibirExtrato(self):
        print('EXIBINDO EXTRATO:')
        print(f'+ R$ {self.saldoInicial:.2f} (Saldo inicial)')
        for valor, chave in self.operacoes.items():
            if chave[0] == 'Saque':
                print(f'- R$ {chave[1]:.2f} ({chave[0]})')
            elif chave[0] in ('Depósito', 'Juros'):
                print(f'+ R$ {chave[1]:.2f} ({chave[0]})')
        print(f'+ R$ {self.saldo} (Saldo Atual)')
    def adicionarJuros(self):
        valor_com_juros = self.saldo * self.taxaJuros
        self.saldo += valor_com_juros
        self.operacoes.update({self.qtd_operacoes: ['Juros', valor_com_juros]})
        self.qtd_operacoes += 1

class Trigonometria:
    def __init__(self, angulo):
        self.angulo_em_graus = angulo
        self.angulo_em_radianos = (angulo * math.pi)/180
        self.cosseno = math.cos(angulo)
        self.seno = math.sin(angulo)
        self.tangente = math.tan(angulo)
    def __str__(self):
        return (f'Angulo em graus: {self.angulo_em_graus:.2f}º\n'
                f'Angulo em radianos: {self.angulo_em_radianos:.2f}\n'
                f'Cosseno do angulo: {self.cosseno:.2f}\n'
                f'Seno do angulo: {self.seno:.2f}\n'
                f'Tangente do angulo: {self.tangente:.2f}\n')