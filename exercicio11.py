#Diga a Largura e Altura da Parede
#Obtenha a área da parede
#E quantos litros de tinta será necessário para pintá-la

x = float(input('Digite a largura da parede: '))
y = float(input('Digite a altura da parede: '))
area = x * y

print('Sua parede de {:.1f}x{:.1f} possui uma área de {:.1f}m².'.format(x, y, area))
print('Para pintar a parede você precisará de {:.1f}lt de tinta.'.format(area/2))