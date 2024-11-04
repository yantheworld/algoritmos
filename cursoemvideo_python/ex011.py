#Faça um programa que leia a largura ea altura de uma parede em metros. Calcule sua area e a quantidade de tinta necessaria
#para pinta-la sabendo wue cada litro de tinta pinta uma área de 2 metros quadrado.

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura*altura

print('Sua parede tema dimensão {}x{} e sua área é de {}m^2'.format(largura, altura, area))

tinta = area/2

print('Paara você pintar essa parede você precisará de {}l de tinta'.format(tinta))