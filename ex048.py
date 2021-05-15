soma = 0
cont = 0
for n in range(3, 501, 3):
    if n % 2 == 1:
        cont += 1
        soma += n
print(f'A soma de todos os {cont} valores solicitados é {soma}')
