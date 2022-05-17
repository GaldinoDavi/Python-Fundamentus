# Leia informação de Nome e Peso
# Dizer qual foi o maior e o menor peso e a quem eles pertencem
imaior = []
nome = []
peso = []
maior = menor = 0
while True:
	nome.append(input('Nome: '))
	peso.append(int((input('Peso: '))))
	if input('Continue[S/N]: ') .upper() == 'N':
		break
maior = max(peso)
menor = min(peso)
print(f'O maior peso foi {maior}. Peso de ',end='')

for x in range (0,len(peso)):
	if peso[x] == maior:
		print(f'{nome[x]} ', end='')
print(f'\nO menor peso foi {menor}. Peso de ',end='')
for x in range (0,len(peso)):
	if peso[x] == menor:
		print(f'{nome[x]} ', end='')