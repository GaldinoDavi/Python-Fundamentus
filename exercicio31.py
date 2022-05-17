#Custo de Viagem
# Até 200km 0.5 por kM
# Acima de 200km 0.45 por Km

x = float(input('Insira a distância em KM: '))
'''
if x <= 200:
    print('O valor total da sua viagem será R${}'.format(x * 0.5))
else:
    print('Você fará uma viagem muito longa, o custo será {}'.format(x * 0.45))'''

preço = x * 0.5 if x <= 200 else x * 0.45
print('Sua viagem custará {}'.format(preço))
