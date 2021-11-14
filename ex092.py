# Exercício Python 092
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
# de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
trabalhador = {}
trabalhador['Nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = datetime.now().year - anonasc
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Admissão'] = int(input('Ano de Admissão: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] = ((trabalhador['Admissão'] + 35) - datetime.now().year) + trabalhador['Idade']
for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')
    