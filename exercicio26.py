
nome = input('Digite seu nome completo:').lower().strip()
print('Contando a letra "a" {} '.format(nome.count('a')))
print('Aparece pela primeira vez na posição {}'.format(nome.find('a') + 1))
print('Aparece pela primeira vez na posição {}'.format(nome.rfind('a') + 1))