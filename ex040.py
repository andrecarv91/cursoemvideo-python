n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print(f'Tirando {n1} e {n2}, a média do aluno é {media}')
if media >= 7.0:
    print(f'O aluno está aprovado.')
elif media < 5.0:
    print(f'O aluno está reprovado.')
else:
    print(f'O aluno está em recuperação.')