# Ler o nome de um aluno e sua nota em duas disciplinas
# Fazer a média das notas
# Poder acessar as notas individuais

boletim = [[],[],[]]
media = qtd = 0
while True:
    boletim[0].append(input('Nome: '))
    boletim[1].append(float(input('Nota 1: ')))
    boletim[2].append(float(input('Nota 2: ')))

    if input('Deseja continuar [S/N]? ').upper() == 'N':
        break

qtd = len(boletim[1])
for x in range(0,qtd):
    media = (boletim[1][x] + boletim[2][x]) / 2
    print(f'{x} Aluno {boletim[0][x]}, a média foi {media:.2f}')
while True:
    n = int(input('Deseja acessar as notas individuais de qual aluno? ([999] para encerrar)'))
    if n == 999:
        break
    print(boletim[0][n], boletim[1][n], boletim[2][n])
