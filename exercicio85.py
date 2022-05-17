#Criar uma lista composta que divida os números em pares ou ímpares.
lista = [[], []]
for x in range(0,7):
    n = int(input(f'Digite {x+1}ª valor: '))
    if n % 2 ==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são {lista[0]}\n'
      f'Os valores ímpares são {lista[1]}\n'
      f'Todos os valores {lista.sort}')
