# Aprovar valor do empréstimo
# Valor do Empréstimo, Salário e em Quantos Anos será pago
# A prestação não pode exceder 30% do salário

emprestimo = int(input('De quanto você precisa? R$ '))
salario = int(input('Qual o seu salário em reais? R$ '))
prazo = int(input('Quantos anos você deseja financiar? ')) * 12
prestacao = emprestimo / prazo

if prestacao >= salario * 0.3:
    print('Infelizmente seu empréstimo no valor de {} foi negado'.format(emprestimo))
else:
    print('Seu empréstimo no valor de {} foi aprovado, sua prestação será de {:.2f} por {} meses'.format(emprestimo,
                                                                                                        prestacao,
                                                                                                        prazo))
