num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: \n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
opt = int(input('Sua opção: '))
if opt == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opt == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opt == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Programa encerrado.')