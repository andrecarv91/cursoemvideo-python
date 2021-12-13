# Exercício Python 103
# Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum 
# dado não tenha sido informado corretamente.

def ficha(nomeJogador=0, qtdeGols=0):
    if nomeJogador == '':
        nomeJogador = '<desconhecido>'
    if qtdeGols.isdecimal() == False:
        qtdeGols = 0
    return f'O jogador {nomeJogador} fez {qtdeGols} gol(s) no campeonato.'


print(ficha(str(input('Nome do jogador: ')),str(input('Número de gols: '))))