frase = str(input('Digite uma frase: ')).replace(' ','').upper()
invertida = frase[::-1].replace(' ','').upper()
print(f'O inverso de {frase} é {invertida}')

if frase == invertida:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')