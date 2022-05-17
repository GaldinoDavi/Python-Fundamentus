# Programa Recebe um Dicionário
# Situação opcional, se True então mostra nota
# Colocar a documentação do help

def notas(*n, sit=False):
    maior = max(n)
    menor = min(n)
    count = len(n)
    media = sum(n) / count
    print(f'Maior = {maior}, Manor = {menor}, Quantidade = {count}, Média = {media:.2f}')
    if sit == True:
        if media >= 6 and media < 8:
            print('Situação Razoável')
        elif media <6:
            print('Situação ruim')
        else:
            print('Muito bom!')

resposta = notas(5.6,9,8,10,5,6,9,8,7,4)