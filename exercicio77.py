# Listar quais vogais aparecem em cada palavra de uma Tupla

lista = ('aprender','elogiar','aluno','italia','trabalho', 'arcanjo','cerimonia', 'visita', 'palpebra')
vogais = ('a','e','i','o','u')

for palavra in lista:
    print(f'Na palavra {palavra.upper()} as vogais são ',end='')
    for x in vogais:
        if x.lower() in palavra:
            print(f'{x.upper()} ',end='')
    print('',end='\n')
