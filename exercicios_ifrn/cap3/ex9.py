salarios_nutricionistas = []
salarios_medicos = []
valid_codes = [1, 2, 3]

while True:
    print('-'*30)
    cod = int(input('Digite o código: '))
    
    if cod == 0:
        break
    if cod not in valid_codes:
        print('Código inválido')
        continue

    salario = float(input('Digite o salário: R$ '))

    if cod == 2:
        salarios_nutricionistas.append(salario)
    elif cod == 3:
        salarios_medicos.append(salario)

media_salarial = sum(salarios_nutricionistas) / len(salarios_nutricionistas)
salarios_medicos_acima_4500 = [salario for salario in salarios_medicos if salario > 4500]

print('-'*30)
print(f'A média salarial dos nutricionistas é: R$ {media_salarial:.2f}')
print(f'Quantidade de médicos com salário acima de R$ 4.500,00: {len(salarios_medicos_acima_4500)}')