'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
Deve ser utilizado uma lista composta para resolver o exercício
'''
valores = [[], []]
for c in range(0,7):
    numero = int(input(f'Digite o {c+1}o. valor: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)
print(f'Valores pares: {sorted(valores[0])}')
print(f'Valores ímpares: {sorted(valores[1])}')
