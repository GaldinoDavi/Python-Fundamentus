#Calculo do Fatorial
x = int(input('Digite um número: '))
x2 = x
f= 1
for x in range(x,0,-1):
    print('{}'.format(x), end='')
    print(' x ' if x > 1 else ' = ', end='')
    f *= x
print(end='\n''O fatorial de {} é {}'.format(x2, f))