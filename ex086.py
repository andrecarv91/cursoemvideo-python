'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 
e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta.
'''
matriz = [[], [], []]
for linha in range(0,3): 
    for coluna in range(0,3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha}][{coluna}]: ')))
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
