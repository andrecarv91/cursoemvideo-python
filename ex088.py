# Exercício Python 088
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
listajogos = []
jogo = []
num = 0
qtdejogos = int(input('Quantos jogos serão jogados? '))
for c in range(0, qtdejogos):
    for c in range(0,6):
        while True:
            num = randint(1,60)
            if num not in jogo:
                jogo.append(num)
                break
    jogo.sort()
    listajogos.append(jogo[:])
    jogo.clear()
for i, jogo in enumerate(listajogos):
    print(f'Jogo {i+1}: {jogo}')
    sleep(0.5)
