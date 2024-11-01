#Leia um programa que leia duas notas de um aluno, calcule e mostre sua média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

print('A media entre {:.1f}, e {:.1f} é igual a : {}'.format(n1,n2,media))