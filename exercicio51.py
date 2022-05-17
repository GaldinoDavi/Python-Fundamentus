#10 termos de uma PA

n0 =  int(input('Primeiro termo: '))
r = int(input('Razão: '))
ultimo = n0 + 10 * r

for x in range(n0, ultimo, r):
    print('{}'.format(x), end=' -> ')
print('ACABOU!')