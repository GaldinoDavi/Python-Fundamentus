# Dizer o maior e menor valor

n1 = int(input('Primeiro valor: '))
n2 = int(input('Primeiro valor: '))
n3 = int(input('Primeiro valor: '))

menor = n1
if n1 > n2:
    menor = n2
if n2 > n3:
    menor = n3

maior = n1
if n1 < n2:
    maior = n2
if n2 < n3:
    maior = n3

print('menor valor digitado foi {}'.format(menor))
print('Maior valor digitado foi {}'.format(maior))
