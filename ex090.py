# Exercício Python 090
# Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['Nome'] = str(input('Digite o nome: '))
aluno['Média'] = float(input(f'A média do {aluno["Nome"]} foi: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Recuperação'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')