# Escreva um programa que leia uma frase pelo teclado e mostre:
#   Quantas vezes aparece a letra "A"
#   Em que posição ela aparece a primeira vez
#   Em que posição ela aparece a ultima vez

frase = str(input('Digite a uma frase: '))
fraser = frase.upper().replace(" ", "")

print('Quantidades de vezes que a letra A aparece: {}'.format(fraser.count('A')))
print('Ela aparece pela primeira vez na posição: {}'.format(fraser.find('A')+1))
print('Ela apareece pela ultima vez na posição: {}'.format(fraser.rfind('A')+1))