# Exercício Python 098
# Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        fim += 1
    else:
        fim -= 1
        passo *= -1
    for c in range(inicio, fim, passo):
        print(f'{c}',end=' ')
        sleep(0.1)
    print('Fim!')
        

contador(1, 10, 1)
contador(10, 0, -2)
print(f'\nAgora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

