#Pegar os dados de 5 pessoas Nome, Idade, Sexo
#Dizer a média de idade o maior e o menor

idadetotal = 0
maior = 0
menor = 9999
nomevelho = ''
cont = 0
for x in range(1,5):
    print('==== {} Pessoa ===='.format(x))
    nome = input('Nome: '.format(x)).strip()
    idade = int(input('Idade: '))
    sexo = input('[M] ou [F]: ').strip()
    idadetotal += idade
    if idade > maior and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if idade < menor:
        menor = idade
        pessoam = nome
    if idade < 21 and sexo in 'Ff':
        cont += 1
media = idadetotal / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O nome do homem mais velho é {} e sua idade é {}'.format(nomevelho, maior))
print('Há {} mulheres menor de 21 anos'.format(cont))
