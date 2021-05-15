d = int(input('Qual é a distância da sua viagem? '))
if d <= 200:
    preco = float(d * 0.50)
else:
    preco = float(d * 0.45)
print(f'Você está prestes a completar uma viagem de {d:.1f}Km\n'
      f'E o preço da sua passagem será de R${preco:.2f}')