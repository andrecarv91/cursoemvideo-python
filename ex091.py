# Exercício Python 091
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
jogos = {}
for c in range(0,4):
    jogos[f'Jogador {c+1}'] = randint(1,6)
for k,v in jogos.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogos.items(), key=lambda x:x[1], reverse=True)
print(f'\n{"RANKING:":^25}')
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
