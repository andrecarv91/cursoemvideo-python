times = ('Bragantino', 'Bahia', 'Ceará SC', 'Fortaleza', 'Athletico-PR', 'Flamengo', 
'Atlético-GO', 'Sport Recife', 'Juventude', 'Cuiabá', 'Internacional', 'São Paulo', 
'Fluminense', 'Grêmio', 'Atlético-MG', 'América-MG', 'Palmeiras', 'Corinthians', 
'Chapecoense', 'Santos')

print(f'{"="*100}\n'
f'Lista de times do Brasileirão 2021 após a primeira rodada: \n{times}\n'
f'{"="*100}\n'
f'Os 5 primeiros são {times[0:5]}\n'
f'{"="*100}\n'
f'Os 4 últimos são {times[-4:]}\n'
f'{"="*100}\n'
f'Times em ordem alfabética: \n{sorted(times)}\n'
f'{"="*100}\n'
f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição\n'
f'{"="*100}')
