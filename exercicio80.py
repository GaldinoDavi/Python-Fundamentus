#Adicionar 5 valores em ordem crescente na lista
valores = []
pos = 0

for y in range(0,5):
    valor = int(input('Digite um número: '))
    if  y == 0:
        valores.insert(0,valor)
        print(f'{valor} adicionado no início')
    elif valor >= max(valores):
        valores.append(valor)
        print(f'{valor} adicionado na última posição')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos,valor)
                print(f'Valor inserido na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valores}')

