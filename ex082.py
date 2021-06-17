valores = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    pares.append(num) if num % 2 == 0 else impares.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
