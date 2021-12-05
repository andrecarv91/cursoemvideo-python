# Exercício Python 101
# Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.

def voto(anonasc):
    """
    -> Informa se a pessoa tem voto negado, opcional ou obrigatório nas eleições.
    - Parâmetro anonasc: Ano de nascimento do cidadão.
    """
    from datetime import date
    idade = date.today().year - anonasc
    if idade < 16:
        return f'Com {idade} anos, o voto é NEGADO!'
    elif idade >= 18 and idade < 70:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO!'
    else:
        return f'Com {idade} anos, o voto é OPCIONAL!'
    

print(voto(int(input('Digite o ano de nascimento: '))))