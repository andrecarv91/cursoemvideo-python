p = h = m = 0
while True:
    print(f'{"-"*30}\n{"CADASTRE UMA PESSOA": ^30}\n{"-"*30}')
    sexo = c = ' '
    idade = -1
    while idade < 0 or idade > 110:
        idade = int(input('Idade: '))
        if idade < 0 or idade > 110:
            print('Digite um valor válido.')
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo != 'M' and sexo != 'F':
            print('Digite um valor válido.')
    if idade > 18:
        p += 1
    if sexo == 'M':
        h += 1
    elif sexo == 'F' and idade < 20:
        m += 1
    while c != 'S' and c != 'N':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()
        if c != 'S' and sexo != 'N':
            print('Digite um valor válido.')
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {p}\nAo todo temos {h} homens cadastrados\n'
f'E temos {m} mulheres com menos de 20 anos')
