# Recebe o peso das pessoas
# Analisa qual o maior e o menor

maior = 0
menor = 999

for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: ' .format(p)))
    if maior < peso:
        maior = peso
    if menor > peso:
        menor = peso
print('O maior peso lido foi de {}' .format(maior))
print('O menor peso lido foi de {}' .format(menor))
