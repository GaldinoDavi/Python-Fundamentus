#Sortear 5 valores e colocar dentro de uma lista
#somar os valores pares
numeros = list()
from random import randint

def sorteador(lista):
    for x in range(0,5):
        lista.append(randint(0,100))
    print(lista)

def soma_pares(valores):
    par = 0
    for x in valores:
        if x % 2 == 0:
            par += x
    print(par)


sorteador(numeros)
soma_pares(numeros)
