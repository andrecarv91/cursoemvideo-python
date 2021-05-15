import time
import random

print(f'Suas opções:\n'
      f'[ 0 ] PEDRA\n'
      f'[ 1 ] PAPEL\n'
      f'[ 2 ] TESOURA')

jogada = int(input('Qual é a sua jogada? '))

if jogada > 2 or jogada < 0:
    print('Jogada inválida!')
    exit()
else:
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!')
    cpu = random.choice(['Pedra', 'Papel', 'Tesoura'])

if jogada == 0:
    jogador = 'Pedra'
elif jogada == 1:
    jogador = 'Papel'
elif jogada == 2:
    jogador = 'Tesoura'
print('-=' * 12)
print(f'Computador jogou {cpu}\n'
      f'André jogou {jogador}')
print('-=' * 12)

if cpu == jogador:
    resultado = 'Empate!'
elif jogador == 'Pedra' and cpu == 'Papel' or jogador == 'Papel' and\
        cpu == 'Tesoura' or jogador == 'Tesoura' and cpu == 'Pedra':
    resultado = 'Você perdeu!'
else:
    resultado = 'Você venceu!'
print(f'{resultado}')
