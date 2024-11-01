#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um numero inteiro: '))
antecessor = num-1
sucessor = num+1

print('O valor é {}, seu sucessor é {} e antecessor é {}'.format(num, sucessor, antecessor))