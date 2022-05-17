# Cadastrar Jogadores
# Quantas Partidas foram jogadas
# Gols por cada partida

jogador = dict()
jogadores = list()
gol = list()
while True:
    jogador['nome'] = input('Nome: ')
    partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for x in range(0,partida):
        gol.append(int(input(f'Quantos gols na partida {x+1}? ')))
    jogador['jogos'] = gol[:]
    jogadores.append(jogador.copy())

    jogador.clear()
    gol.clear()

    if input('Continuar [S/N]?' ).upper()[0] in 'Nn':
        break
print('-=' * 50)
print('Cod  nome            gols          total')
print('-'*120)
for x,y in enumerate(jogadores):
    print(f'{str(x):>3} {str(y["nome"]):<15} {str(y["jogos"]):<15} {str(sum(y["jogos"])):>5}')
print('-'*120)

while True:
    z = int(input(f'Mostrar detalhes qual jogador ([999] parar): '))
    if z == 999:
        break
    if z > len(jogadores):
        print(f'Informe um número entre 0 e {len(jogadores)}')
    else:
        print(f'=== {jogadores[z]["nome"]} ===')
        partida = len(jogadores[z]["jogos"])
        for x in range(0,partida):
            print(f'No jogo {x+1} fez {jogadores[z]["jogos"][x]} gols.')

print(f'=== FIM ===')
