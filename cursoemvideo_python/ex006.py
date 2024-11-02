#Crie um algoritmo que leia um numero e mostre seu dobro, seu triplo e raiz quadrada.

num = int(input('Digite um numero: '))
dobro = num*2
triplo = num*3
raizQ = num ** (1/2)

print('O dobro vale {}, seu triplo vale {} e sua raiz quadrada é igual a: {:.2f}'.format(dobro, triplo, raizQ))