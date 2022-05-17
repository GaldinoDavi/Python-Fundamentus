# Dizer se um número é primo e sinalizar por quais números ele é divisível

z = 0
n = int(input('Insira um número '))
for x in range(1,n + 1):
    if n % x == 0:
        print('\033[36m', end='')
        z += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(x), end='')
print('\n\033[mO número {} foi divisível {}x'.format(n, z))

if z == 2:
    print('O número {} É PRIMO'.format(n))
else:
    print('O número {} NÃO É PRIMO'.format(n))
    