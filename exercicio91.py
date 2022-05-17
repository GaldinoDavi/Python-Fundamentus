# 4 Jogadores jogarão um dado
# Guarde os resultado em um dicionário
# Rankeie do maior para o menor

from random import randint
from time import sleep
from operator import itemgetter


jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('Sorteando Valores:')

for x,y in jogo.items():
    print(f'{x}, tirou {y} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True)
print(f'=-' * 40)
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}.')
    sleep(0.5)