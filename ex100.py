# Exercício Python 100
# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares
# sorteados pela função anterior.
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando os valores da lista:',end=' ')
    for c in range(0,5):
        lista.append(randint(1,10))
        print(lista[c],end=' ')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}.')

numeros = []
sorteia(numeros)
somaPar(numeros)
