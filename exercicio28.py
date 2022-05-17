#Adivinhar um numero entre 0 e 5
print('\033[0;30;46mVamos adivinhar!\033[m')

from time import sleep
from random import randint
n = randint(0,5)
x = int(input('Em que número estou pensando? '))

print('Processando.')
sleep(0.5)
print('Processando..')
sleep(0.5)
print('Processando...')
sleep(0.5)

if x == n:
    print('\033[0;32;40mVocê acertou, eu estou pensando no número {} \033[m'.format(n))

else:
    print('\033[7;30;41mQue pena, você errou... Eu pensei no número {} não no {} \033[m'.format(n,x))