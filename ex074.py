from random import randint
sort = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os números sorteados foram: ',end='')
for numero in sort:
    print(f'{numero} ',end='')
print(f'\nO maior valor sorteado foi {max(sort)}')
print(f'O menor valor sorteado foi {min(sort)}')
