# Calcul3e a soma entre todos os números ímpares múltimos de 3 no intervalo entre 1 e 500
y = 0
cont = 0
for x in range(1,500,2):
    if x % 3 == 0:
        y += x
        cont = cont + 1
print('Exitem {} números e a soma dos valores é {}'.format(cont, y))