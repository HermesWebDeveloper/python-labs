def aplicar_desconto(tabela, desconto):
    nova_tabela = {}    
    for chave, valor in tabela.items():
        valor[1] *= (1-desconto)
        valor[1] = round(valor[1], 2) 
        nova_tabela[chave] = valor

    return nova_tabela

def exibir_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(f"{chave}: {valor}")

def exercicio8():
    tabela = {1: ['Monitor LED 25"', 599.99],
            2: ['Teclado weriless', 49.26],
            3: ['Mouse wireless', 19.90],
            4: ['Cartucho colorido', 54.00] 
            }

    tabela_com_desconto = aplicar_desconto(tabela, 0.10)
    exibir_dicionario(tabela_com_desconto)

exercicio8()