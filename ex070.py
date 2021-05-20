p = total = precobarato = c = 0
prodbarato = ' '
while True:
    r = ' '
    preco = -1
    produto = str(input('Nome do produto: '))
    while preco < 0:
        preco = float(input('Preço: R$'))
        if preco < 0:
            print('Digite um valor válido.')
    c += 1
    if preco > 1000:
        p += 1
    if c == 1 or preco < precobarato:
        prodbarato = produto
        precobarato = preco
    total += preco
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
        if r not in 'SN':
            print('Informe um valor válido.')
    if r == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^50}\n'
f'O total da compra foi R${total:.2f}\nTemos {p} produtos custando mais de R$1000.00\n'
f'O produto mais barato foi {prodbarato} que custa R${precobarato:.2f}')