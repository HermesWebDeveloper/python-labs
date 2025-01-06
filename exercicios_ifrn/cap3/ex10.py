medias_alunos = []

for aluno in range(1, 6):
    nota1 = float(input(f'Digite a 1º nota do {aluno}º aluno: '))
    nota2 = float(input(f'Digite a 2º nota do {aluno}º aluno: '))
    media = (nota1+nota2)/2
    medias_alunos.append(media)

medias_prova_final = [media for media in medias_alunos if (media >= 2 and media < 6)]

print(f'Quantidade de alunos em prova final: {len(medias_prova_final)}')