loop = 1
termos = 10
total = 0
print('Gerador de PA')
print('-='*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
while termos != 0:
    total += termos
    while loop <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        loop += 1
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')