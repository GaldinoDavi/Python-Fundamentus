#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math

x = float(input('Digite um número: '))
print('O valor é {}'.format(math.trunc(x)))

