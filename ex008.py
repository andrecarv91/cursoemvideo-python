# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros
d = float(input('Uma distância em metros: '))
print(f'A medida de {d:.1f}m corresponde a \n {(d/1000)}km \n {(d/100)}hm \n {(d/10)}dam '
      f'\n {(d*10)}dm \n {(d*100)}cm \n {(d*1000)}mm')
