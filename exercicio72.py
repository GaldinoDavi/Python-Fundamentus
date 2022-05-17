#Escrever um número por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    x = int(input('Digite um número entre 0 e 20: '))
    if 0 <= x <= 20:
        break
print(f'O número {x} por extenso é {numeros[x]}')