#Programa que lê um valor e diz a porcentagem de desconto

valor = float(input('Qual o valor do produto: R$'))
desconto = float(input('Qual a porcentagem de desconto: '))

valor = valor - valor/100 * desconto

print('O valor do produto após o desconto é {}'.format(valor))