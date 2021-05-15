val = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = val / (anos * 12)
print(f'Para pagar uma casa de R${val:.2f} em {anos} anos a '
      f'prestação será de R${parcela:.2f}')

if parcela > (sal * 0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo pode ser concedido!')
