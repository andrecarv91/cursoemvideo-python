from random import randint
from time import sleep
cont = 0
flag = False
computador = randint(0, 10)
print('-='*30)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-='*30)
while flag == False:
    jogador = int(input('Em que número eu pensei? '))
    cont += 1
    print('Processando...')
    sleep(0.5)
    if jogador == computador:
        flag = True
    else:
        if jogador < computador:
            print('Mais... tente outra vez.', end=' ')
        else:
            print('Menos... tente outra vez.', end=' ')
print(f'ACERTOU após {cont} tentativas! O número que pensei era {computador}!')


'''if computador == jogador:
    print('PROCESSANDO...')
    sleep(0.5)
else:
    while computador != jogador:
        cont += 1
        print('PROCESSANDO...')
        sleep(0.5)
        jogador = int(input(f'ERROU! Tente novamente: '))
print(f'ACERTOU após {cont} tentativas! O número que pensei era {computador}!')'''
