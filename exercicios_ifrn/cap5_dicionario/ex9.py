def exibir_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(f"{chave}: {valor}")

funcionarios = {
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

tabela_funcionarios_filtrada = {
    chave: valor
    for chave, valor in funcionarios.items()
    if (valor[2] == "TI") and (valor[1] == "F" ) and (valor[4] > 3000)
}

exibir_dicionario(tabela_funcionarios_filtrada)