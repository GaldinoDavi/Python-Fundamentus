# Recebe 4 nomes e embaralha eles

from random import shuffle

n1 = input('Nome do aluno 1: ')
n2 = input('Nome do aluno 2: ')
n3 = input('Nome do aluno 3: ')
n4 = input('Nome do aluno 4: ')

lista = [n1, n2, n3, n4]

shuffle(lista)

print(lista)