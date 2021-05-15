nome = input('Digite seu nome completo: ')
nomecompleto = len(nome) - nome.count(' ')
nomeseparado = nome.split()

print(f'Tudo maiúsculo: {nome.upper()}\n'
      f'Tudo minúsculo: {nome.lower()}\n'
      f'Quantas letras ao todo: {nomecompleto}\n'
      f'Quantas letras tem o primeiro nome: {len(nomeseparado[0])}')


