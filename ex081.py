lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    while c not in 'SN':
        c = str(input('Comando inválido. Digite S para continuar ou N para sair: ')).strip().upper()
    if c == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
print(f'O valor 5 faz parte da lista.') if 5 in lista else print('O valor 5 não faz parte da lista.')
  