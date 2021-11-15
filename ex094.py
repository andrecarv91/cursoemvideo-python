# Exercício Python 094
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = {}
pessoas = []
somaidade = 0

while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoa['Sexo'] in 'MF':
            break    
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=='*15)

print(f'A) Quantidade de pessoas cadastradas: {len(pessoas)}')

for c in range(0, len(pessoas)):
    somaidade += pessoas[c]['Idade']
média = somaidade / len(pessoas)
print(f'B) Média de idade: {média} anos.')

print(f'C) Mulheres cadastradas: ', end='')
for c in range(0,len(pessoas)):
    if pessoas[c]['Sexo'] == 'F':
        print(f'{pessoas[c]["Nome"]}', end=' ')

print('\nD) Pessoas acima da idade média:')
for c in range(0,len(pessoas)):
    if pessoas[c]['Idade'] > média:
        for k, v in pessoas[c].items():
            print(f'{k} = {v}; ', end='')
        print()
