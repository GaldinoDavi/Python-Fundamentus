# Calcular o fatorial de um número
# Incluir as informações no Help da função
# Se true mostrar o calculo

def fatorial (numero, detalhe = 0):
    """
    :param numero: Digite um número para calcular o fatorial
    :param detalhe: Se True irá mostrar a memória de calculo
    :return: retorna o resultado da fatorial
    """
    fat = 1
    if detalhe == False:
        for x in range(1,numero + 1):
            fat *= x
    else:
        for x in range(numero, 1,-1):
            fat *= x
            print(f'{x} x ',end='')

            if x == 2:
                print(f'1 =')

    return fat


resultado = fatorial(5,True)
print(f' Resultado {resultado}')
help(fatorial)