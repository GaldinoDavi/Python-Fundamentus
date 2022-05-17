#Ler o nome e a média de um aluno
#SE >7 aprovado, <5 reprovado
aluno = dict()

aluno['nome'] = input('nome: ')
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    print(f'Aprovado com média {aluno["media"]}')
elif 7 > aluno['media'] >=5:
    print(f'Em recuperação com média {aluno["media"]}')
else:
    print(f'Reprovado com média {aluno["media"]}')
