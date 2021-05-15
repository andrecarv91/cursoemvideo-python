# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode
# comprar. Considere US$ 1,00 = R$ 3,27

c = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${c:.2f} você pode comprar US${c/3.27:.2f}')