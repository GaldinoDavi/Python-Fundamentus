#Uma Lista geram e outras duas com valores pares, ímpares
valores = []
par = []
impar = []

while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    x = input('Continuar [S/N] ').upper()
    if x == 'N':
        break
print(f'Lista {valores}\n'
      f'Pares {par}\n'
      f'Ímpares {impar}')