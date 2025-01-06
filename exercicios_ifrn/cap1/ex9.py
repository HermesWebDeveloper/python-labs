# 9. Construa um programa que solicite que o usuário informe 2 números inteiros positivos. O programa deve calcular:
# a) O cubo do segundo número
# b) A média geométrica entre o primeiro e o segundo número, isto é,

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

cubo = num2**2
media_geometrica = (num1*num2)**(1/2)

print(f'O cubo do segundo número é: {cubo}')
print(f'A média geométrica entre os números é: {media_geometrica:.2f}')