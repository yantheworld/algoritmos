# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

#Nesse exercio estou treinando como importar biliotecas então vou testar com duas soluções porém vou deixar a segunda comentada.
#Caso queira rodar a segunda opção, basta descomentar e comentar a primeira opção utilizando #.

from math import trunc
num = float(input('Digite um número: ' ))
print('O número digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

#n = float(input('Digite um número: '))
#print('O número digitado foi {} e sua porção inteira é {}'.format(n, int(n)))
