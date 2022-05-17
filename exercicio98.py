#Contar de 1 a 10
#Contar de 10 a 1
#Contar de um valor até
from time import sleep

def contador (inicio, final, passo):
    if passo == 0:
        passo = 1
    if passo > 0:
        print(f'Contando de {inicio} até {final} de {passo} em {passo}')
    if inicio < final:
        c = inicio
        while c <= final:
            print(f'- {c}', end=' ')
            while True:
                if passo <0:
                    passo = int(input('Digite um valor positivo. Passo: '))
                else:
                    break
            c += passo
            sleep(0.2)
    else:
        print(f'\nContando de {inicio} até {final} de {passo} em {passo}')
        c = inicio
        while c >= final:
            print(f'- {c}',end='')
            while True:
                if passo > 0:
                    passo = int(input('Digite um valor negativo. Passo: '))
                else:
                    break
            c += passo
        print(end='\n')


contador(0,10,1)
contador(10,0,-2)
contador(int(input('Inicio: ')), int(input('Final: ')), int(input('Passo: ')))
