lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        print('Adicionado ao final da lista.')
        lista.append(num)
    else:
        for pos in range(0, len(lista)):
            if num < lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
print(lista)