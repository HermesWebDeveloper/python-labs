valor_venda = float(input(f'Digite o valor total da venda: '))
forma_pagamento = int(input('Digite o número da forma de pagamento:\n 1 - À vista (em espécie)\n 2 - Cartão de débito \n 3 - Cartão de crédito (vencimento)\n'))

if forma_pagamento == 1:
    desconto = 0.15
elif forma_pagamento == 2:
    desconto = 0.10
elif forma_pagamento == 3:
    desconto = 0.05

valor_final = valor_venda - (desconto) * valor_venda

print(f'O valor final, aplicando desconto, é de: R$ {valor_final}')