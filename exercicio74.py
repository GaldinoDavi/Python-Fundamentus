#Sortear 5 números e armazenar numa tupla
#Informar o maior e o menor valor

from random import randint

x = (randint(0,20), randint(0,20), randint(0,20),
     randint(0,20), randint(0,20),)

print(f'Os números sorteados foram: {x}')
print(f'O maior valor é {max(x)}')
print(f'O menor valor é {min(x)}')
