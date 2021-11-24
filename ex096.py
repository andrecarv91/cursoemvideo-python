# Exercício Python 096
# Faça um programa que tenha uma função chamada área(), que receba
# as dimensões de um terreno retangular (largura e comprimento) e mostre
# a área do terreno.

def área(l,c):
    área = l * c
    print(f'A área de um terreno {l}x{c} é de {área}m²')


l = float(input('Informe a largura (m): '))
c = float(input('Informe o comprimento (m): '))
área(l,c)
