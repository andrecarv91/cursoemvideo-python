nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print(f'Muito prazer em te conhecer! \n'
      f'Seu primeiro nome é {lista[0]} \n'
      f'Seu último nome é {lista[-1]}')

