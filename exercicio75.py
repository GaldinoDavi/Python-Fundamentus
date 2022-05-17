# Ler o valor de 4 números
# Informar o valor 9 apareceu
# O valor que apareceu na segunda posição
# Os valores pares

pares = 0
x = (int(input('Digite um número: ')), int(input('Digite mais um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite o último número: ')))


print(f'O número 9 apareceu {x.count(9)}x')
print(f'O número {x[1]}, está na 2ª posição')

for n in x:
    if n % 2 == 0:
        pares += 1
print(f'Vocês digitou {pares} números pares')