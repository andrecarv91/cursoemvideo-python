# Python exercise 106: 
# Make a mini-system that utilizes Python Interactive Help. 
# The user is going to type the command and the manual will show up. 
# When the user types the word 'FIM' ('END'), the program will close. 
# Important: Use colors.

from time import sleep

cores = {
    'default': '\033[m',        
    'red':     '\033[0;30;41m', 
    'green':   '\033[0;30;42m', 
    'yellow':  '\033[0;30;43m',
    'blue':    '\033[0;30;46m', 
    'purple':  '\033[0;30;45m', 
    'white':   '\033[0;30;47m'     
}

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{func}\'', 'yellow')
    print(cores['white'], end='')
    help(comando)
    print(cores['default'], end='')
    sleep(1)

def titulo(msg, cor='default'):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores['default'], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'blue')
    func = input('Função ou Biblioteca > ').strip()
    if func.upper() == 'FIM':
        break
    else:
        ajuda(func)
titulo('Até logo!', 'red')
        