#Crie um programa que leia uanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. 02/11/2024
real = float(input("Digite o valor do seu dinheiro em R$: "))
dolar = real / 5.70

print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))