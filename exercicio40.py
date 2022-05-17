# Calcular a Média

n1 = float(input('Quanto você tirou na primeira prova? '))
n2 = float(input('Quanto você tirou na segunda prova? '))

media = (n1 + n2) / 2

if media >= 7:
    print('Você foi aprovado com média {:.2}'.format(media))
elif media <= 5:
    print('Você foi reprovado com média {:.2}'.format(media))
else:
    print('Voce está na recuperação devido sua média {:.2}'.format(media))