#Aumento de Salário de acordo com a faixa salarial
# <= 1250 aumento de 15%
# > 1250 aumento de 10%

salario = float(input('Informe o salário: R$'))

if salario <= 1250:
    print('O seu salário reajustado será de R$ {}'.format(salario * 1.15))
else:
    print('Seu salário reajustado será de R$ {}'.format(salario * 1.1))
