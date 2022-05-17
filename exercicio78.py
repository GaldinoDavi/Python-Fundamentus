# Ler 5 valores e informar o maior/menor valor e a posição que eles se encontram.
valores = list()
maior = menor = 0
for x in range (0,5):
    valores.append(int(input(f'Digite um valor pra posição {x} ')))

maior = max(valores)
menor = min(valores)

print(f'O maior valor foi {maior} e você o digitou na posição ',end='')
for y, z in enumerate(valores):
    if z == maior:
        print(f'... {y}',end='')
print(f'\nO menor valor foi {menor} e você o digitou na posição',end='')

for y, z in enumerate(valores):
    if z == menor:
        print(f'... {y}',end='')

