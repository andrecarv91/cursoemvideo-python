# Exercício Python 089
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
# em uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
boletim = []
num = 0
while True:
    boletim.append(str(input('Nome: ')))
    boletim.append(float(input('Nota 1: ')))
    boletim.append(float(input('Nota 2: ')))
    alunos.append(boletim[:])
    boletim.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{(aluno[1]+aluno[2])/2:>8}')
while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num >= 0 and num < len(alunos):
        print(f'Notas de {alunos[num][0]} são {alunos[num][1]}, {alunos[num][2]} ')
    elif num == 999:
        break
    else:
        print(f'Aluno não encontrado!')         
