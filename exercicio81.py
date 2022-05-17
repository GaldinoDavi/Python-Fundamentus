#Ler valores e organizar em forma decrescente
valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    x = input('Quer continuar? [S/N]').upper()
    if x == 'N':
        break
valores.sort(reverse=True)

print(f'Você digitiou {len(valores)} elementos.\n'
      f'Os valores em ordem decrescente são {valores}')
