#Calcule a Hipotenusa
import math

oposto = float(input('Qual o valor do cateto oposto? '))
adjacente = float(input('Qual o valor do cateto adjacente? '))
h = (oposto ** 2 + adjacente ** 2) ** (1/2)
h2 = math.hypot(oposto, adjacente)

print('A hipotenusa é {:.2f} / outro método {:.2f}'.format(h, h2))

