"""
 Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas.
 B) Uma listagem com as pessoas mais pesadas.
 C) Uma listagem com as pessoas mais leves.
"""
dados = []
pessoas = []
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maiorpeso:
        print(f'{pessoa[0]} ', end='')
print(f'\nO menor peso foi de {menorpeso}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menorpeso:
        print(f'{pessoa[0]} ', end='')
