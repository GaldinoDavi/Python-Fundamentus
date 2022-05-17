#Sequência de Fibonacci

n = int(input('Calculando Fibonacci, quantos termos você quer mostrar? '))
x = 3

t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
while x <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{} -> '.format(t3), end='')

    x +=1
    if x > n:
        mais = int(input('Quantos termos a mais? '))
        n += mais
print('ACABOU!!')