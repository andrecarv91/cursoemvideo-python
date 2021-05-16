loop = 1
print('Gerador de PA')
print('-='*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
while loop <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    loop += 1
print(' FIM')
