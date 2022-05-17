#Sortear Números para mega sena

from random import randint
from time import sleep
jogo = [0,0,0,0,0,0]
n = int(input('Quandos jogos você deseja sortear? '))
print(f'=' * 3, 'Boa Sorte', '=' * 3)
for qtd in range (0,n):
    for x in range (0,6):
        numero = randint(0,60)
        while numero in jogo:
            numero = randint(0, 60)
        jogo[x] = numero
    jogo.sort()
    print(f' jogo nº{qtd+1}: {jogo}')
    sleep(0.5)