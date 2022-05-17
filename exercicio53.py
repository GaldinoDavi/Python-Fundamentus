# Digitar uma frase
# Transcrever o inverso
# Identificar se ela é um palíndromo

frase = input('Digite uma frase: ').upper().replace(' ','')
inverso = frase [::-1]

if inverso == frase:
    print('O inverso de {} é {}, ela é um palíndromo'.format(frase, inverso))
else:
    print('O inverso de {} é {}, ela NÃO É um palíndromo'.format(frase, inverso))
