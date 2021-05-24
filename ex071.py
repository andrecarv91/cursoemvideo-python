valor = int(input('Qual valor você quer sacar? R$'))
cedula = 200
totced = 0
while True:
    if valor >= cedula:
        valor -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totced = 0
        if valor == 0:
            break

'''
while valor != 0:
    if valor // 50:
        n50 = valor // 50
        valor %= 50
        print(f'Total de {n50} cédulas de R$50')
    elif valor // 20:
        n20 = valor // 20
        valor %= 20
        print(f'Total de {n20} cédulas de R$20')
    elif valor // 10:
        n10 = valor // 10
        valor %= 10
        print(f'Total de {n10} cédulas de R$10')
    elif valor // 1:
        n1 = valor // 1
        valor %= 1
        print(f'Total de {n1} cédulas de R$1')
'''