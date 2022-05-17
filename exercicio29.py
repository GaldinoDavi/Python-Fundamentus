#Verificar a velocidade e cobrar multa por KM

vel = int(input('Qual a velocidade do carro? '))
if vel <= 40:
    print('Você está dentro do limite de segurança, dirija com cuidado.')
else:
    multa = (vel-40) *7
    print('Você foi multado! Você deve pagar uma multa no valor de {:.2f}'.format(multa))