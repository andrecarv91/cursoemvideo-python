peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    avaliacao = 'ABAIXO DO PESO'
elif imc <= 25.0:
    avaliacao = 'PESO IDEAL'
elif imc < 30.0:
    avaliacao = 'SOBREPESO'
elif imc <= 40.0:
    avaliacao = 'OBESIDADE'
else:
    avaliacao = 'OBESIDADE MÓRBIDA'
print(f'O seu resultado é: {avaliacao}')
