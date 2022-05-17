#Dizer quantos dólares podem ser comprados

x = float(input('Quantos reais você tem na carteira? R$'))

print('Com {:.2f} você pode comprar {:.2f} dólares'.format(x, x/5))