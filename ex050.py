soma = 0
for c in range(1, 7):
    num = int(input(f'Informe o número inteiro {c}: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos números pares é {soma}')