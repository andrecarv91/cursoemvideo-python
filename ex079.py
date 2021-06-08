num = []
while True:
    n = int(input('Digite um valor: '))
    if n in num:
        print(f'Valor duplicado! Não vou adicionar...')
    else:
        num.append(n)
        print(f'Valor adicionado com sucesso...')
    c = str(input('Quer continuar? [S/N] ')).upper().strip()
    while c not in 'SN':
        c = str(input('Valor inválido, digite S para continuar ou N para parar: ')).upper().strip()
    if c == 'N':
        break
print(f'Você digitou os valores {sorted(num)}')
