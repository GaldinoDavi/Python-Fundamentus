# Ler Nome, sexo e idade
# Média de Idade
# Mulheres cadastradas
# QUem ta acima da Média
# Validar os dados digitados

pessoa = dict()
galera = list()
media = 0

while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('[M/F] ').upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    while True:
        continua = input('Deseja continuar [S/N]: ').upper()[0]
        if continua in 'SN':
            break
        print('Error 404! Informe um campo exato S ou N')
    if continua == 'N':
        break
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'C) As mulheres cadastradas foram: ',end='')
for x in galera:
    media += x['idade']
    if x['sexo'] == 'F':
        print(f' {x["nome"]}',end='')
media = media/len(galera)
print(f'\nB) A média de idade é de {media} anos')
# print(f'C) As mulheres cadastradas foram {x["sexo"]}')
print(f'D) Lista de pessoas que estão acima da média:')
for x in galera:
    if x['idade'] > media:
        print(f'Nome = {x["nome"]}; Sexo = {x["sexo"]}; Idade = {x["idade"]}')

print('<< ENCERRADO >>')