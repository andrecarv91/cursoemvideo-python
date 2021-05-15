n = int(input('Digite um número para calcular seu fatorial: '))
cont = n
fat = n
print(f'Calculando {n}! = {n} ', end='')
while cont > 1:
    cont -= 1
    fat *= cont
    print(f'x {cont} ', end='')
print(f'= {fat}')

'''from math import factorial
n = int(input('número:)
f = factorial(n)
print(f)'''