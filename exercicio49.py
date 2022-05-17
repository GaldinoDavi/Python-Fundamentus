#Voltando ao exercício 9 (Calculando tabuada)

x = int(input('Digite um número para a tabuada: '))

for t in range(1,11):
    print('{} x {} = {}'.format(t, x, t * x))