#Faça um programa que leia algo no teclado e mostre na tela o seu tipo primitivo e todos as informações possíveis sobre
# ela

x = input('Digite algo: ')
print(f'O tipo primitivo desse valor é ', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético:', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está em maiúsculas?', x.isupper())
print('Está em minúscula?', x.islower())
print('Está capitalizada?', x.istitle())

