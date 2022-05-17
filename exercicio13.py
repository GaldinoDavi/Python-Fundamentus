#Lê o salário de um funcionário e calcular o reajuste após uma porcentagem de aumento
x = float(input('Qual o seu salário? R$'))
y = float(input('qual a inflação anual?'))

print('O seu salário atual é R$ {}, após o reajuste inflacionário ele passará para R$ {:.2f}'.format(x, x*(1+y/100)))