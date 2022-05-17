#DIgitar o nome completo
#Retornar o nome em maiúsculo, minúsculo, contar a quantidade de letras total e do primeiro nome.

nome = input('Digite seu nome completo: ').strip()
qtdLetra = nome.count(' ')
lista = nome.split()

print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome possui {} letras.'.format(len(nome) - qtdLetra))
print('Seu primeiro nome possui {} letras'.format(len(lista[0])))
