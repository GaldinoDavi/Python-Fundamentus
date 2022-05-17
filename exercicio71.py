#Contar quais cédulas de real serão necessárias para realizar o saque

n100 = n50 = n20 = n10 = n5 = n1 = 0

print(f'=========== \n'
      f'BANCO CEV \n'
      f'===========')
valor = int(input('Quanto você deseja sacar? '))
if valor // 100 != 0:
    n100 = valor // 100
    valor = valor % 100
if valor // 50 != 0:
    n50 = valor // 50
    valor = valor % 50
if valor // 20 != 0:
    n20 = valor // 20
    valor = valor % 20
if valor // 10 != 0:
    n10 = valor //10
    valor = valor % 10
if valor // 5 != 0:
    n5 = valor //5
    valor = valor % 5
n1 = valor


print(f'Notas de R$100 = {n100}\n'
      f'Notas de R$50 = {n50} \n'
      f'Notas de R$20 = {n20}\n'
      f'Notas de R$10 = {n10}\n'
      f'Notas de R$5 = {n5}\n'
      f'Notas de R$1 = {n1}')
