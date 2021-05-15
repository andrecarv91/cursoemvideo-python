totidade = 0
velho = 0
menor = 0
nomevelho = ''
contf = 0
print()
for c in range(1, 5):
    print('-'*5, f'{c}ª PESSOA', '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    totidade += idade
    if idade > velho and sexo == 'M':
        velho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        contf += 1
print(f'A média de idade do grupo é de {totidade/4:.1f} anos\n'
      f'O homem mais velho tem {velho} anos e se chama {nomevelho}\n'
      f'Ao todo são {contf} mulheres com menos de 20 anos')
