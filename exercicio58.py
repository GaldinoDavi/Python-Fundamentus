# Melhorando o jogo do exercicio 28
# Adivinhar um número de 0 a 10
# O computador da dicas se está maior ou menor

from random import randint
from time import sleep

numero = randint(0,10)
n = -1
c = 0

print('Vou pensar em um número entre 0 e 10')
for x in range (0,4):
    print('.', end='')
    sleep(0.3)

print('Tente adivinhar que número estou pensando', end='\n')

while n != numero:
    n = int(input('Adivinhe um número: '))
    while n not in range(0,11):
        n = int(input('Somente números entre 0 e 10... Adivinhe um número: '))
    if n > numero:
        print('Tente um número menor.')
    if n < numero:
        print('Tente um número maior.')
    c += 1
print('Parabéns, você acertou o número {} na {}ª tentativa'.format(numero, c))
