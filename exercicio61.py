#10 termos de uma PA usando While

n0 =  int(input('Primeiro termo: '))
y = n0
r = int(input('Razão: '))
ultimo = n0 + 10 * r
x = 1
while x < 11:
    print('{}'.format(y), end=' -> ')
    y += r
    x +=1
print('ACABOU!')