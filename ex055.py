lista = []
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    lista.append(peso)
lista.sort()
maiorpeso = lista[-1]
menorpeso = lista[0]
print(f'O maior peso lido foi de {maiorpeso:.1f}Kg\n'
      f'O menor peso lido foi de {menorpeso:.1f}Kg')
