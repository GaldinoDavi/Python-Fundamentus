#Preencher uma matriz 3x3
#Informar a Soma dos valores Pares
#Informar o maior valor da segunda linha
#informar a soma dos valres da terceira coluna

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = segunda = coluna = 0

for x in range(0,3):
    for y in range (0,3):
        n = int(input(f'Digite um valor para a posição [{x,y}]'))
        matriz[x][y] = n
        if n % 2 == 0:
            par += n
        if x == 1 and n > segunda:
            segunda = n
        if y == 2:
            coluna += n
print('='*30)

print(f'Soma dos números pares é: {par}\n'
      f'A soma dos valores da terceira coluna é {coluna}\n'
      f'O maior número da segunda linha é: {segunda}\n'
      f'Matriz = {matriz}')