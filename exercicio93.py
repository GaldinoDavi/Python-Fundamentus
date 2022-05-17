# Cadastrar 1 Jogador
# Quantas Partidas foram jogadas
# Gols por cada partida

gols = list()
dados = dict()
dados['nome'] = input('Nome do jogador: ')
jogos = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

x = 0
for x in range(0,jogos):
    gols.append(int(input(f'Quantos gols fez na partida {x+1}? ')))
dados['partida'] = gols[:]
dados['total'] = sum(gols)

print('=' * 30)
print(dados)
print('=' * 30)

for x, y in dados.items():
    print(f'O campo {x} tem o valor {y}')
print('=' * 30)
print(f'O jogador {dados["nome"]}, jogou {jogos} partidas.')
for x,y in enumerate(gols):
    print(f'    => Na partida {x+1}, fez {y} gols')
print(f'Foi um total de {dados["total"]} gols.')