# X termos de uma PA usando While

n0 =  int(input('Primeiro termo: '))
r = int(input('Razão: '))
ultimo = n0 + 10 * r
x = 1
termo = 11
count = 0
z = 0
while x < termo:
    print('{}'.format(n0), end=' -> ')
    n0 += r
    x +=1

    if x == termo:
        z = int(input('Quantos temos a mais você quer? '))
        termo += z
    count += 1
print('ACABOU, com {} termos!'.format(count))