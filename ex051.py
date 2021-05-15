print('='*40)
print(f'10 TERMOS DE UMA PA'.center(40))
print('='*40)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(0, 10):
    print(termo, end=' → ')
    termo += razao
print('ACABOU')
