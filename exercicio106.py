#Sistema de Ajuda PyHelp
def ajuda(comando):
    x = help(comando)
    return x
while True:
    x = input('Função ou biblioteca: ')
    if x == 'fim':
        break
    x = ajuda(x)
    print(x)
print('FIM')