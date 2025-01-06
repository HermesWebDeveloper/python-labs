def exibir_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(f"{chave}: {valor}")

def obter_dados_funcionarios():
    return {
        1: ["Ana", "F", "TI", 7, 3200.00],
        2: ["Beatriz", "F", "TI", 4, 3720.00],
        3: ["Carla", "F", "TI", 1, 2100.00],
        4: ["Daniela", "F", "RH", 2, 3920.00],
        5: ["Emílio", "M", "RH", 7, 4235.12],
        6: ["Fernando", "M", "Marketing", 7, 1200.00],
        7: ["Gabriela", "F", "Marketing", 8, 7234.89],
        8: ["Hernandes", "M", "TI", 6, 4234.12],
        9: ["Ítalo", "M", "RH", 13, 13934.23],
        10: ["Janaína", "F", "RH", 7, 9341.89],
    }

def filtrar_funcionarios(funcionarios):
    return {
        chave: valor
        for chave, valor in funcionarios.items()
        if valor[3] > 5
    }

exibir_dicionario(filtrar_funcionarios(obter_dados_funcionarios()))