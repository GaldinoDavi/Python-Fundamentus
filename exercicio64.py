# Crie um programa que somas os números exceto o 999 de parar

y = 0
while True:
    print('Digite 999 para parar')
    x = int(input('Insira um número: '))
    if x == 999:
        break
    y += x
print(f'A soma dos números digitados é {y}')