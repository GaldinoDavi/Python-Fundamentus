# Recebe o nome do jogador se nome for em branco = <desconhecido>
# Recebe quantos gols foram feito, se gol is not numeric então 0


def validador(nome=0, gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome}, marcou {gols} gols.')

validador(input('Jogador: '), input('Gols: '))
