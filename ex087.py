# Exercício Python 087
# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
somapares = somacoluna = maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha].append(int(input(f'Digite um valor para a posição [{linha}][{coluna}]: ')))
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
        if coluna == 2:
            somacoluna += matriz[linha][coluna]        
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares digitados é {somapares}.')
print(f'A soma dos valores da terceira coluna é {somacoluna}.')
print(f'O maior valor da segunda linha é {maior}.')