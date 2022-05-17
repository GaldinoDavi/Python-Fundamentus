#Informe um número
#O programa deve responder com o dobro, tripo e raiz quadrada do valor

x = int(input('informe um número: '))
print('O dobro de {} vale {}.'.format(x, x * 2))
print('O triplo de {} vale {}.'.format(x, x * 3))
print('A raiz quadrada de  \n'
      '{} vale {:.2f}.'.format(x, x ** (1/2)))
