#Informe o nome de 4 alunos e sortei um
from random import choice

n1 = input('Nome do aluno 1: ')
n2 = input('Nome do aluno 2: ')
n3 = input('Nome do aluno 3: ')
n4 = input('Nome do aluno 4: ')

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('O escolhido foi {}'.format(escolhido))