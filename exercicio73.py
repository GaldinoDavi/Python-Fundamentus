#Crie uma tupla com 20 times do brasileirão
# Quais os 4 primeiros colocados
# Os últimos 4 colocados
# Organize de forma alfabética
# Em que posição está o chapecoense

times = ('Internacional', 'Atlético MG', 'Flamengo', 'São Paulo', 'Fluminense', 'Palmeiras',
        'Santos', 'Grêmio', 'Esporte', 'Recife', 'Corinthians', 'Chapecoense', 'Ceará SC',
        'Atlético GO', 'Bahia', 'Coritiba', 'Bragantino', 'Botafogo', 'Vasco',
        'Atlético PR')
print(f'Os times do G4 são {times[0:4]}')
print(f'Os times do Z4 são {times[-4:]}')
print(f'Chapecoense está na posição {times.index("Chapecoense")+1}')
print(f'Os times em ordem alfabéticas são {sorted(times)}')
