from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    p = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = date.today().year - p
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade \n'
      f'E também tivemos {menor} pessoas menores de idade')