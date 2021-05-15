class Fg:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'


class Style:
    BRIGHT = '\033[1m'
    DIM = '\033[2m'
    NORMAL = '\033[22m'
    RESET_ALL = '\033[0m'


cont = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print(Style.BRIGHT, Fg.BLUE, f'{c}', Fg.RESET, Style.RESET_ALL, end='')
    else:
        print(Style.BRIGHT, Fg.RED, f'{c}', Fg.RESET, Style.RESET_ALL, end='')
print(f'\nO número {num} foi divisível {cont} vezes', end=' ')
if cont == 2:
    print('e por isso ele é primo.')
else:
    print('e por isso ele não é primo.')
