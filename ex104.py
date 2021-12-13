# Exercício Python 104
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante 'a função input() do Python, só que fazendo a validação para
# aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg):
    while True:
        numero = input(msg)
        if numero.isdecimal() == False:
            print('\033[1;31;40mERRO! Digite um número inteiro válido.\033[0;0m')
        else: 
            break
    return numero


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')