flag = 'S'
menor = maior = soma = cont = 0
while flag == 'S':
    n1 = int(input('Digite um número: '))
    cont += 1
    soma += n1
    if cont == 1:
        maior = menor = n1
    elif n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1
    flag = str(input('Quer continuar? [S/N] ')).upper()
print(f'Você digitou {cont} números e a média foi {soma / cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
        