from datetime import date
anonasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
print(f'Quem nasceu em {anonasc} tem {idade} anos em {anoatual}')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.\n'
          f'Seu alistamento será em {anonasc + 18}')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos. \n'
          f'Seu alistamento foi em {anoatual - (idade - 18)}')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')