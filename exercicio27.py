#DIzer o último e o primeiro nome da pessoa
nome = input('Digite seu nome').strip()
ndivisao = nome.split()

print('Seu primeiro nome é {} e seu último nome é {}'.format(ndivisao[0], ndivisao[-1]))
