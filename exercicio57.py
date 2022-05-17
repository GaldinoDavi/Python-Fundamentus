#Validar a entrada correta

sexo = str(input('Informe seu sexo: [M]/[F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados incorretos. Informe seu sexo: [M]/[F]')).strip().upper()[0]
print(sexo)