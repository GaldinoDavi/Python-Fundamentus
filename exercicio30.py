#Dizer se um número é par ou ímpar

x = int(input('Escolha um número inteiro: '))
resultado = x % 2

if resultado == 0:
    print('Seu número é par')
else:
    print('O número é ímpar.')
