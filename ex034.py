sal = float(input('Qual o salário do funcionário? R$'))
if sal > 1250.00:
    novosal = sal + (sal * 0.10)
else:
    novosal = sal + (sal * 0.15)
print(f'Quem ganhava R${sal:.2f} passa a ganhar R${novosal:.2f}')