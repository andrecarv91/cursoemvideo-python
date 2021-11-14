# Exercício Python 093
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
# ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []

jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0,partidas):
    gols.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)

print('=='*15)
print(jogador)

print('=='*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=='*15)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
