#Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - O nome com todas as letras maiusculas
# 2 - O nome com todas minusculas
# 3 - Quantas letras ao todo (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))

semEsp = nome.replace(" ", "")
primNome = nome.split()

print('Nome com letras todas as letras maiusculas: {}'.format(nome.upper()))
print('Nome com todas as letras minusculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(semEsp)))
print('Quantas letras tem o primeiro nome: {}'.format(len(primNome[0])))