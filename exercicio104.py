#Função que lê um número inteiro
def leiaint(numero):
    while True:
        if numero.isnumeric():
            numero = int(numero)
            break
        else:

            numero = input('Error! Digite um número válido! Digite um número: ')
    return numero


n = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}')