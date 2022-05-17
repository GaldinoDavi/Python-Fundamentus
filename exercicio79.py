#Ler valores e listar em ordem crescente, dizer o maior e o menor valor
valores = []
valores.append(int(input(f'Digite um valor: ')))
print('Valor adicionado com sucesso!')
while True:
    x = input('Continuar [S/N]? ')
    if x.upper() == 'N':
        break
    if x.upper() == 'S':
        valor = (int(input('Digite um valor: ')))
        if valores.__contains__(valor):
            print('Valor já digitado, digite outro número.')
        else:
            valores.append(valor)
            print('Valor adicionaddo com sucesso!')
print(f'Os valores digitados foram {sorted(valores)},'
      f'O maior valor foi {max(valores)} e o menor foi {min(valores)}.')