#Data para o alistamento militar

from datetime import date

x = int(input('Informe seu ano de nascimento '))
ano = date.today().year
alistamento = (ano - x) - 18

if alistamento < 0:
    print('Você deve se alistar daqui a {} anos'.format(alistamento * (-1)))
elif alistamento > 0:
    print('Você já deveria ter se alistado {} anos atrás'.format(alistamento))
else:
    print('Aliste-se imediatamente')
