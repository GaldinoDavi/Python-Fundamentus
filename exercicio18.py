#Diga o SENO, Cosseno e Tangente
import math

x = float(input('Digite a angulação: '))
seno = math.sin(math.radians(x))
cons = math.cos(math.radians(x))
tan = math.tan(math.radians(x))

print('Valor seno {:.2f}º, \n'
      'Valor Cosseno {:.2f}º \n'
      'Valor Tangente {:.2f} \n'.format(seno, cons, tan))
