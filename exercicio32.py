# Dizer se um ano é bissexto ou não
from datetime import date

ano = int(input('Qual ano você quer analisar? Digite 0 para o ano atual. '))

if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))