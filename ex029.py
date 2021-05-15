v = int(input('Qual é a velocidade atual do carro? '))
if v > 80:
    multa = float((v - 80) * 7)
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h \n'
          f'Você deve pagar uma multa de R${multa:.2f}!')
print(f'Tenha um bom dia! Dirija com segurança!')