# Cadastrar Trabalhador (Nome, Nascimento, Carteira de Trabalho)
# Se tiver carteira de trabalhar (Ano de contratação, Salário)
# Print na tela com as informações organizadas e com quantos ela vai se aposentar

pessoa = dict()

pessoa['nome'] = input('Nome: ')
pessoa['nascimento'] = int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Cardeira de trabalho (0) não tem: '))

if pessoa['ctps'] == 0:
    print('=' * 30)
    for x, y in pessoa.items():
        print(f'- {x} tem o valor {y}')
else:
    pessoa['ano'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['ano'] + 35 - pessoa['nascimento']
    for x, y in pessoa.items():
        print(f'- {x} tem o valor {y}')