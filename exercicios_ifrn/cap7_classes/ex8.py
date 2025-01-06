from Classes import ContaInvestimento
import os

def criar_conta():
    numero = int(input('Digite o número da conta: '))
    saldo = float(input('Digite o saldo inicial da conta: '))
    cliente = input('Digite o cliente: ')
    taxaJuros = float(input('Digite a taxa de juros da conta de investimmento: '))
    conta = ContaInvestimento(numero, saldo, cliente, taxaJuros)

    return conta

def exibir_linha_divisória():
    print('-'*30)

def pausar_e_limpar_console():
    input('Digite Enter para continuar...')
    os.system('cls')

def exercicio8():
    conta = criar_conta()
    sair = False

    while (not sair):
        exibir_linha_divisória()
        print('1 - Exibir Saldo')
        print('2 - Sacar')
        print('3 - Depositar')
        print('4 - Exibir Extrato')
        print('5 - Adicionar Juros')
        print('6 - Sair')
        op = int(input('Digite a opção desejada: '))
        os.system('cls')
        exibir_linha_divisória()
        if op == 1:
            conta.exibirSaldo()
        elif op == 2:
            valor_saque = float(input('Digite o valor desejado para sacar: '))
            conta.sacar(valor_saque)
        elif op == 3:
            valor_deposito = float(input('Digite o valor desejado para depositar: '))
            conta.depositar(valor_deposito)
        elif op == 4:
            conta.exibirExtrato()
        elif op == 5:
            conta.adicionarJuros()
            print('Juros adicionados!!')
        elif op == 6:
            sair = True
            print('Até mais!!')
        else:
            print('Opção inválida!!')
        exibir_linha_divisória()
        pausar_e_limpar_console()

exercicio8()