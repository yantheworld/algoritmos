#Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente
from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))


print('Valor seno: {:.2f}\nValor cosseno: {:.2f}\nValor tangente: {:.2f}'.format(seno, cosseno, tangente))