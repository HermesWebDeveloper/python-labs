peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso / (altura**2)
print(f'IMC: {IMC:.2f}')

if IMC < 18.5:
    print('Situação: Abaixo do peso')
elif IMC < 25:
    print('Situação: Peso normal')
elif IMC < 30:
    print('Situação: Sobrepeso')
elif IMC < 35:
    print('Situação: Obesidade grau 1')
elif IMC < 40:
    print('Situação: Obesidade grau 2')
else:
    print('Situação: Obesidade grau 3')