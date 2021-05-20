win = 0
from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    jogada = ' '
    jogador = -1
    while jogador < 0 or jogador > 10:
        jogador = int(input('Diga um valor: '))
    while jogada != 'P' and jogada != 'I':
        jogada = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    cpu = randint(0,10)
    if (jogador + cpu) % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {cpu}. Total de {jogador + cpu} deu {resultado}')
    print('-'*30)
    if resultado == 'PAR' and jogada == 'P' or resultado == 'ÍMPAR' and jogada == 'I':
        print('Você venceu\nVamos jogar novamente...')
        win += 1
        print('=-'*15)
    else:
        print('Você perdeu!')
        break
print('=-'*15)
print(f'GAME OVER! Você venceu {win} vezes.')
