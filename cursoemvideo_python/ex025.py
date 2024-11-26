#Faça um programa que leia o nome de uma pessoa e diga se ela tem o nome "SILVA" no nome

nome = str(input('Digite seu nome completo: ')).strip()
nomer = 'SILVA' in nome.upper().split()

print(nomer)