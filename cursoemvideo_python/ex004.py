#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaço?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Esta em maiusculo?', a.isupper())
print('Esta em minusculo?', a.islower())
print('Esta capitalizada?', a.istitle())