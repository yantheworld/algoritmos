#Faça um programa que leia o comprimento de um cateto oposto e o cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Digite o número do cateto oposto: '))
ca = float(input('Digite o número do cateto adjacente: '))
hi = hypot(ca, co)

print('Valor da hipotenusa: {:.2}'.format(hi))