#Desenvolva um programa que leita seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o

soma = 0
for x in range(1,7):
    n = int(input('Digite o {}ª número: '.format(x)))
    if n % 2 == 0:
        soma += n
print(soma)