# Exercício Python 095
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.

jogadores = []
jogador = {}
gols = []

while True:
    resp = ' '
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0,partidas):
        gols.append(int(input(f'  Quantos gols na partida {c+1}? ')))
        jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp not in 'SN':
            print(f'Comando inválido. Tente novamente.')
    if resp == 'N':
        break
print(f'\n{"cod":<3} {"Nome":<15} {"Gols":<15} {"Total":>3}')
print('-'*45)
for i, v in enumerate(jogadores):
    print(f'{i+1:>3} {v["Nome"]:<15} {str(v["Gols"]):<15} {v["Total"]:<3}')
print('-'*45)

while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp == 999:
        print('Volte sempre!')
        break
    elif resp < 1 or resp > len(jogadores):
        print(f'Erro! Não existe jogador com código {resp}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[resp - 1]["Nome"]}')
        for i, v in enumerate(jogadores[resp - 1]["Gols"]):
            print(f'  => Na partida {i+1}, fez {v} gols.')
