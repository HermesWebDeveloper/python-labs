#  8. Construa um programa que receba do usuário o valor do salário mínimo atual. Na sequência, o programa deve solicitar que o usuário informe o valor do seu salário mensal. Ao fim, o programa deve calcular a quantidade de salários mínimos recebidos pelo usuário.

salario_minimo = float(input('Digite o valor do salário mínimo atual: R$ '))
salario_mensal = float(input('Digite o valor do salario mensal: R$ '))

qtd_salarios = salario_mensal / salario_minimo

print(f'A quantidade de salários é: {qtd_salarios:.2f}')