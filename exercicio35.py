# Informar se as medidas formam ou não um triangulo

x = float(input('Informe o valor 1:'))
y = float(input('Informe o valor 2:'))
z = float(input('Informe o valor 3'))

print( '=' * 20)
if x < y + z and y < z + x and z < x + y:
    print('Os segumentos geram um triângulo')
else:
    print('Os segmentos não geram um triângulo')
print( '=' * 20)