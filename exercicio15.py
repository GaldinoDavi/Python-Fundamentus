#Aluguel de Carros
#Pega a quantidade de KM percorridos por um carro alugado
#A quantidade de dias que foi alugado
# Calcule o preço sabendo que  o custo diário é R$60 e o KM rodado custa R$0,15

dias = int(input('Por quantos dias deseja alugar o veículo? '))
km = float(input('Qual a KM média esperada? '))

valor = dias * 60 + km * 0.15

print('O valor esperado para pagamento será de R${}'.format(valor))