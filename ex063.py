cont = 0
n1 = 0
n2 = 1
t = int(input('Quantos termos você quer mostrar? '))
while cont < t:
    print(f'{n1} -> ', end='')
    n3 = n1 + n2 
    n1 = n2
    n2 = n3
    cont += 1
print('FIM')
  