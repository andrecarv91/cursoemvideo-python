from time import sleep
opcao = '0'
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opcao != '5':
    print('[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa')
    sleep(0.5)
    opcao = input('>>>>> Qual é a sua opção? ')
    if opcao == '1':
        result = n1 + n2
        print(f'{n1} + {n2} = {result}')
    elif opcao == '2':
        result = n1 * n2
        print(f'{n1} X {n2} = {result}')
    elif opcao == '3':
        if n1 > n2:
            print(f'{n1} > {n2}')
        elif n1 < n2:
            print(f'{n1} < {n2}')
        else:
            print(f'{n1} = {n2}')
    elif opcao == '4':
        n1 = int(input('Informe o primeiro novo valor: '))
        n2 = int(input('Informe o segundo novo valor: '))
    elif opcao == '5':
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa. Volte sempre!')
