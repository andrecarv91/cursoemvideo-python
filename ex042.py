color = {'black' : '\033[30m',
        'red' : '\033[31m',
        'green' : '\033[32m',
        'yellow' : '\033[33m',
        'blue' : '\033[34m',
        'purple' : '\033[35m',
        'cyan' : '\033[36m',
        'gray' : '\033[37m',
        'white' : '\033[97m',
        'clean' : '\033[m'}

print('-='*15)
print('{}Analisador de Triângulos{}'.format(color['blue'], color['clean']))
print('-='*15)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))


if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 == s3:
        classificacao = 'equilátero'
    elif s1 == s2 or s1 == s3 or s2 == s3:
        classificacao = 'isósceles'
    else:
        classificacao = 'escaleno'
    print(f'Os segmentos acima podem formar um triângulo {classificacao}!')
else:
    print('Os segmentos acima não podem formar triângulo!')