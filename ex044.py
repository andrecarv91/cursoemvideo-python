import sys
print(f'{" Lojas Carvalho ":=^40}')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] à vista dinheiro/cheque\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão')
opcao = input('Qual é a opção? ')
if opcao == '1':
    valorfinal = preco - (preco * 0.10)
elif opcao == '2':
    valorfinal = preco - (preco * 0.05)
elif opcao == '3':
    valorfinal = preco
    print(f'Sua compra será parcelada em 2x de R${valorfinal / 2:.2f} sem juros.')
elif opcao == '4':
    valorfinal = preco + (preco * 0.20)
    parcelas = int(input('Quantas parcelas? '))
    if 0 <= parcelas <= 2:
        print(f'Quantidade de parcelas inválida para esta forma de pagamento.')
        sys.exit()
    else:
        valorparcelado = valorfinal / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${valorparcelado:.2f} com juros.')
else:
    print(f'Opção inválida. Tente novamente.')
    sys.exit()
print(f'Sua compra de R${preco:.2f} vai custar R${valorfinal:.2f} no final.')
