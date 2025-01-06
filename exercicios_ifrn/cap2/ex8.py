print('Expressão da equação de 2º grau: ax² + bx + c')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 + 4*a*c

if delta > 0: 
    x1 = -b + delta**(1/2)
    x2 = -b - delta**(1/2)
    print(f'O valor de x1 e x2, respectivamente, são: {x1:.2f} e {x2:.2f}')
else:
    print(f'Não existem raízes reais')