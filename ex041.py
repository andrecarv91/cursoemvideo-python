from datetime import date
anonasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    classificacao = 'MIRIM'
elif idade <= 14:
    classificacao = 'INFANTIL'
elif idade <= 19:
    classificacao = 'JUNIOR'
elif idade <= 25:
    classificacao = 'SÊNIOR'
else:
    classificacao = 'MASTER'
print(f'Classificação: {classificacao}')

