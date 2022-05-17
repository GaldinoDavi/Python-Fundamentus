#Trabalhando com função
# Receber Largura e Comprimento e dizer a área

def calc_area (largura, comprimento):
    x = largura * comprimento
    return x


print('Controle de Terreno')
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

area = calc_area(largura, comprimento)
print(area)